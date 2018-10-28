import sys
import re
import boto3

# Helper function for printing confidence details
def format_confidence(confidence):
    return 'Confidence: ' + "{:.2f}".format(text['Confidence']) + "%"

if __name__ == "__main__":
    # Check for correct number of parameters
    if(len(sys.argv) != 2): # 2 parameters: This file and image name: Ex. "python detect-taxes.py testrcpt.jpg"
        print('Invalid parameters:')
        print(str(sys.argv))
        exit(1)

    bucket="timtam-img"
    image=str(sys.argv[1]) # Ex: "testrcpt.jpg"

    # Call AWS Rekognition API 
    client=boto3.client('rekognition')
    # TODO: Need to handle invalid object exceptions
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':image}})
    textDetections=response['TextDetections']

    # Initialize variables
    regex_tax = re.compile(r'tax', re.IGNORECASE)
    regex_amount = re.compile(r'\d+\.\d+(?!\%)', re.IGNORECASE) # Dollar amount. Ex: "5.12".
    regex_tax_amount = re.compile(r'tax.*\d+\.\d+(?!\%)', re.IGNORECASE) # Tax string with dollar amount. Ex: "Spirits Sales Tax(20.5%) 5.12"
    tax_found = False # Flag used in below logic to indicate a "tax" string has been found, now find corresponding dollar amount

    print('\nSearching for all taxes...')
    # TODO: Update to write detected strings into proper KVP output
    for text in textDetections:
        detected_text = text['DetectedText']
        confidence = text['Confidence']
        if(tax_found): # Found corresponding amount for most recent "tax" occurence
            match_amount = regex_amount.search(detected_text)
            if(match_amount):
                print('\t\tDetected amount: ' + detected_text)
                print('\t\t' + format_confidence(confidence))
                print()
                # Switch logic to search for next "tax"/amount pair
                tax_found = False 
        else:
            match_tax_amount = regex_tax_amount.search(detected_text)
            match_tax = regex_tax.search(detected_text)
            if(match_tax_amount): # Found line with "tax"/amount pair       
                print('\tDetected tax with amount: ' + detected_text)
                print('\t' + format_confidence(confidence))
                print()
            elif(match_tax): # Found "tax"
                print('\tDetected tax: ' + detected_text)
                print('\t' + format_confidence(confidence))
                print('\tSearching for amount...')
                # Switch logic to search for corresponding amount
                tax_found = True 

    print('Search completed!\n')

import sys
import re
import boto3

def format_confidence(confidence):
    return 'Confidence: ' + "{:.2f}".format(text['Confidence']) + "%"

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print('Invalid parameters:')
        print(str(sys.argv))
        exit(1)

    bucket="timtam-img"
    image=str(sys.argv[1])

    client=boto3.client('rekognition')
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':image}})
    textDetections=response['TextDetections']

    regex_tax = re.compile(r'tax', re.IGNORECASE)
    regex_amount = re.compile(r'\d+\.\d+(?!\%)', re.IGNORECASE)
    regex_tax_amount = re.compile(r'tax.*\d+\.\d+(?!\%)', re.IGNORECASE)
    tax_found = False

    print('\nSearching for all taxes...')
    for text in textDetections:
        detected_text = text['DetectedText']
        confidence = text['Confidence']
        if(tax_found):
            match_amount = regex_amount.search(detected_text)
            if(match_amount):
                print('\t\tDetected amount: ' + detected_text)
                print('\t\t' + format_confidence(confidence))
                print()
                tax_found = False
        else:
            match_tax_amount = regex_tax_amount.search(detected_text)
            match_tax = regex_tax.search(detected_text)
            if(match_tax_amount):                
                print('\tDetected tax with amount: ' + detected_text)
                print('\t' + format_confidence(confidence))
                print()
            elif(match_tax):     
                print('\tDetected tax: ' + detected_text)
                print('\t' + format_confidence(confidence))
                print('\tSearching for amount...')
                tax_found = True

    print('Search completed!\n')

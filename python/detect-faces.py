import boto3

BUCKET = "timtam-img"
KEY = "ScreenShot.png"

def detect_labels(bucket, key, max_labels=30, min_confidence=50, region="us-east-1"):
	rekognition = boto3.client("rekognition", region)
	response = rekognition.detect_labels(
		Image={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
		MaxLabels=max_labels,
		MinConfidence=min_confidence,
	)
	return response['Labels']


for label in detect_labels(BUCKET, KEY):
	print("{Name} - {Confidence}%".format(**label))

"""
	Expected output:
	People - 99.2436447144%
	Person - 99.2436447144%
	Human - 99.2351226807%
	Clothing - 96.7797698975%
	Suit - 96.7797698975%
"""
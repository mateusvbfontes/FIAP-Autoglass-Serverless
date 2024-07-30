import json
import boto3
from sqsHandler import SqsHandler


def api(event, context):
    print(json.dumps(event))
    
    payload=json.loads(event["body"])
    
    sqs = SqsHandler("https://sqs.us-east-1.amazonaws.com/041854577888/feedback")
    sqs.send(json.dumps(payload))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Feedback recebido. Obrigado')
    }

def sqs(event, context):
    print(json.dumps(event))
    
    for record in event["Records"]:
        payload = record["body"]

    

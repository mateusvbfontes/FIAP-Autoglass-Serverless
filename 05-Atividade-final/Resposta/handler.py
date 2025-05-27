import json
import boto3
from sqsHandler import SqsHandler
from baseDAO import BaseDAO


def api(event, context):
    print(json.dumps(event))
    
    payload=json.loads(event["body"])
    
    sqs = SqsHandler("https://sqs.us-east-1.amazonaws.com/185837994267/feedback-queue")
    sqs.send(json.dumps(payload))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Feedback recebido. Obrigado')
    }

def sqs(event, context):
    print(json.dumps(event))
    
    dao = BaseDAO("Feedback") # Instancia o DAO (ajuste se precisar de parâmetros)
    for record in event["Records"]:
        payload = json.loads(record["body"])
        dao.put_item(payload)

        sns = boto3.client('sns')
        sns.publish(
            TopicArn='arn:aws:sns:us-east-1:185837994267:feedback-notification',
            Message=json.dumps(payload),
            Subject='Novo Feedback Recebido'
        )

    

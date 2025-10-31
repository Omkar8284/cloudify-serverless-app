import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employeedata')  # your table name

def lambda_handler(event, context):
    response = table.scan()
    data = response['Items']

    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }

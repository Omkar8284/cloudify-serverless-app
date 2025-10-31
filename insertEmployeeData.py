import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employeedata')  # Replace with your table name

def lambda_handler(event, context):
    # Handle both cases — API Gateway proxy or direct test event
    try:
        if 'body' in event:
            body = json.loads(event['body'])
        else:
            body = event
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }

    employeeid = body.get('employeeid')
    name = body.get('name')
    department = body.get('department')
    salary = body.get('salary')

    # Insert into DynamoDB
    table.put_item(Item={
        'employeeid': employeeid,
        'name': name,
        'department': department,
        'salary': salary
    })

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Employee data inserted successfully'})
    }

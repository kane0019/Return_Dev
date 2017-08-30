import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ID_Count')
response = table.update_item(
        Key={'Server_ID':'Test_Server' },
        UpdateExpression = 'ADD Ship_Count :val',
        ExpressionAttributeValues = {':val': 1}
)
'''dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ID_Count')
response = table.get_item(
    Key={
        'Server_ID': 'Test_Server'
        },
    AttributesToGet=['Ship_Count'],
    ConsistentRead=True
    )
print(response['Item']['Ship_Count'])
'''
'''dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')
response = client.describe_table(
            TableName='ship_info'
        )
shipcount=response['Table']['ItemCount']
ship_id=str(int(shipcount+1)).zfill(7)
print(ship_id)'''

import boto3 
import time




def db_initial():
    dynamo_client = boto3.client('dynamodb')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName='ship_info',
        KeySchema=[{
            'AttributeName': 'ship_id',
            'KeyType': 'HASH'
            }     
        ],
        AttributeDefinitions=[
            {
            'AttributeName': 'ship_id',
            'AttributeType': 'S'
            }
            ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
            }
        )
    
    table = dynamodb.create_table(
        TableName='ID_Count',
        KeySchema=[{
            'AttributeName': 'Server_ID',
            'KeyType': 'HASH'
            }     
        ],
        AttributeDefinitions=[
            {
            'AttributeName': 'Server_ID',
            'AttributeType': 'S'
            }
            ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
            }
        )
    while True:
        table_initial=dynamo_client.describe_table(TableName='ship_info')
        if table_initial['Table']['TableStatus'] == 'CREATING':
            time.sleep(5)
        elif table_initial['Table']['TableStatus'] == 'ACTIVE':
            break
        else:
            time.sleep(5)
            print("Invaliad TableName or Table Status Error!")
            
    while True:
        table_initial=dynamo_client.describe_table(TableName='ID_Count')
        if table_initial['Table']['TableStatus'] == 'CREATING':
            time.sleep(5)
        elif table_initial['Table']['TableStatus'] == 'ACTIVE':
            break
        else:
            time.sleep(5)
            print("Invaliad TableName or Table Status Error!")
    
    table = dynamodb.Table('ID_Count')
    table.put_item(
        Item={
            'Server_ID': 'Test_Server',
            'Ship_Count': 0
            }
        )
db_initial()


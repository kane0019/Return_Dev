import pymysql

import boto3 

def db_initial():
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


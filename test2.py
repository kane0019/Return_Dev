import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ID_Count')
table.put_item(
        Item={
            'ID_Count': 0
            }
        )
'''
dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')
response = client.describe_table(
            TableName='ship_info'
        )
shipcount=response['Table']['ItemCount']
ship_id=str(int(shipcount+1)).zfill(7)
print(ship_id)'''
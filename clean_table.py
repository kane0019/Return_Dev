import boto3
client = boto3.client('dynamodb')
response = client.delete_table(
    TableName='ship_info'
)
response = client.delete_table(
    TableName='ID_Count'
)
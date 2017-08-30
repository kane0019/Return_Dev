import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ship_info')
response = table.update_item(
        Key={'ship_id': '0000001'},
        UpdateExpression='SET #map.#module_name = :val1',
        ExpressionAttributeNames={'#map':'module','#module_name':selection},
        ExpressionAttributeValues= {':val1': 'true'}
    )
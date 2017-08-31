import boto3 
def get_ship_status(ship_id):
    ship_id = ship_id
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ship_info')
    response = table.get_item(
        Key={'ship_id': '0000001'},
        AttributesToGet=['ship_id','ship_name','ship_class','ship_energy','ship_power','ship_resourceA','ship_resourceB','ship_resourceA_income','ship_resourceB_income'],
        ConsistentRead=True
        )
    output_key=['ship_id','ship_name','ship_class','ship_energy','ship_power','ship_resourceA','ship_resourceB','ship_resourceA_income','ship_resourceB_income']
    output = {keys: response['Item'][keys] for keys in output_key}
    return output
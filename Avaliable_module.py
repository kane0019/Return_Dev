
import boto3
from module_dic import module_dictionary
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ship_info')
def module_list(ship_id):
    ship_id=ship_id
    response = table.get_item(
        Key={
            'ship_id': ship_id
        }
        )
    item = response['Item']
    output=[]
    for key,item in item['module'].items():
        if item == False:
            output.append(key)
    print("Avalible Modules are: ",output)
    return output
    
def module_detail(module):
    details = module_dictionary(module)
    print(details)

def build_module(selection,ship_id):
    ship_id = ship_id
    module_name=selection
    response = table.update_item(
        Key={'ship_id': ship_id},
        UpdateExpression='SET #map.#module_name = :val1',
        ExpressionAttributeNames={'#map':'module','#module_name':selection},
        ExpressionAttributeValues= {':val1': 'true'}
    )
    

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
    print("{}{}\n".format("Module Name: ", details["Description"]))
    print("{}{}\n".format("Energy: ", details["energy_change"]))
    print("{}{}\n".format("Resource_A: ", details["resourceA_change"]))
    print("{}{}\n".format("Resource_B: ", details["resourceB_change"]))
    print("{}{}\n".format("Power: ", details["power_change"]))
    print("{}{}\n".format("ResourceA_Income: ", details["resourceA_income"]))
    print("{}{}\n".format("ResourceB_Income: ", details["resourceB_income"]))


def build_module(selection,ship_id):
    ship_id = ship_id
    details = module_dictionary(selection)
    response = table.update_item(
        Key={'ship_id': ship_id},
        UpdateExpression='SET #map.#module_name = :val1',
        ExpressionAttributeNames={'#map':'module','#module_name':selection},
        ExpressionAttributeValues= {':val1': 'true'}
    )
    response = table.update_item(
        Key={'ship_id': ship_id},
        UpdateExpression='ADD ship_energy :val1,ship_resourceA :val2,ship_resourceB :val3,ship_power :val4,ship_resourceA_income :val5,ship_resourceB_income :val6',
        ExpressionAttributeValues= {':val1': details['energy_change'],':val2': details['resourceA_change'],':val3': details['resourceB_change'],':val4': details['power_change'],':val5':details["resourceA_income"],':val6':details["resourceB_income"]}
    )
    
    
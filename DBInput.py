import boto3

def new_ship(ship_id,ship_name,ship_class,energy,power,resourceA,resourceB,ship_resourceA_income,ship_resourceB_income):
    ship_id=ship_id
    ship_name=ship_name
    ship_class=ship_class
    ship_energy=energy
    ship_power=power
    ship_resourceA=resourceA
    ship_resourceB=resourceB
    ship_resourceA_income=ship_resourceA_income
    ship_resourceB_income=ship_resourceB_income
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ship_info')
    table.put_item(
        Item={
            'ship_id': ship_id,
            'ship_name': ship_name,
            'ship_class': ship_class,
            'ship_power': ship_power,
            'ship_resourceA': ship_resourceA,
            'ship_resourceB': ship_resourceB,
            'module': {
                'RESOURCE_A_MINER': False,
                'GENERATOR': False,
                'REFLECT_SHEILD': False
                }
            }
        )
    
    
    table = dynamodb.Table('ID_Count')
    response = table.update_item(
            Key={'Server_ID':'Test_Server' },
            UpdateExpression = 'ADD Ship_Count :val',
            ExpressionAttributeValues = {':val': 1}
    )

    
    
def ship_status_update(ship_id,name,ship_class,energy,power,resourceA,resourceB):
    ship_id=ship_id
    ship_name=name
    ship_class=ship_class
    ship_energy=energy
    ship_power=power
    ship_resourceA=resourceA
    ship_resourceB=resourceB
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ship_info')
    
    
    table.update_item(
        Key={
            'ship_id': ship_id
            },
        UpdateExpression='SET ship_energy= :energy,ship_power= :power,ship_resourceA= :resourceA, ship_resourceB= :resourceB',
        ExpressionAttributeValues={
            ':energy': ship_energy,
            ':power': ship_power,
            ':resourceA': ship_resourceA,
            ':resourceB': ship_resourceB
        }
    )







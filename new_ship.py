import boto3
import time
from DBInput import new_ship,ship_status_update
from get_ship_status import get_ship_status

class ship:
    shipname=""
    shipclass=""
    energy=0
    resourceA=0
    resourceB=0
    ship_resourceA_income=0
    ship_resourceB_income=0
    power=0
    def __init__(self,shipname,shipclass):
        
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('ID_Count')
        response = table.get_item(
            Key={
                'Server_ID': 'Test_Server'
                },
            AttributesToGet=['Ship_Count'],
            ConsistentRead=True
            )
        shipcount=response['Item']['Ship_Count']
        self.ship_id=str(int(shipcount+1)).zfill(7)
        self.shipname = shipname
        self.shipclass = shipclass
        self.energy= 5
        self.resourceA=100
        self.resourceB=100
        self.power=0
        self.ship_resourceA_income=0
        self.ship_resourceB_income=0
        
    def create_new_ship(self):
        new_ship(self.ship_id,self.shipname,self.shipclass,self.energy,self.power,self.resourceA,self.resourceB,self.ship_resourceA_income,
        self.ship_resourceB_income)

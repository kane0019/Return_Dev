from Roll_Dice import dice
import boto3
import time
from event import event
from turn import turn_out_come
from DBInput import new_ship,ship_status_update
from Avaliable_module import module_list,module_detail,build_module

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

ship_a=ship("test","testclass")
ship_a.create_new_ship()




# start of the turn
eventnumber=dice(2).rolldice()
turn_event=event(eventnumber).event_run()
turn_out_come(ship_a,turn_event)
print(ship_a.shipname,ship_a.shipclass,ship_a.energy,ship_a.resourceA,ship_a.resourceB,ship_a.power)    
ship_status_update(ship_a.ship_id,ship_a.shipname,ship_a.shipclass,ship_a.energy,ship_a.power,ship_a.resourceA,ship_a.resourceB,)

loopender = 0
while loopender != 1:
    avaliable_module_list=module_list(ship_a.ship_id)
    selection=input("Type in Module Name to check details:\n")
    module_detail(selection)
    build_confirm = input("Build this module?(Y/N)\n")
    while True:
        if build_confirm != "Y" and build_confirm != "N":
            build_confirm = input("Invalid option.Please use Y or N to choose\n")
        elif build_confirm == "Y":
            build_module(selection,ship_a.ship_id)
            loopender = 1
            print("Module Built!")
            break
        else:
            break
           



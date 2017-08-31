from Roll_Dice import dice
import boto3
import time
from new_ship import ship
from event import event
from turn import turn_out_come
from DBInput import ship_status_update
from Avaliable_module import module_list,module_detail,build_module
from get_ship_status import get_ship_status


def new_ship(ship_name,ship_class):
        newship = ship(ship_name,ship_class)
        newship.create_new_ship()
        return newship


def turn(ship_a):
    # start of the turn
    eventnumber=dice(2).rolldice()
    turn_event=event(eventnumber).event_run()
    turn_out_come(ship_a,turn_event)  
    ship_status_update(ship_a.ship_id,ship_a.shipname,ship_a.shipclass,ship_a.energy,ship_a.power,ship_a.resourceA,ship_a.resourceB,ship_a.ship_resourceA_income,ship_a.ship_resourceB_income)
    print(get_ship_status(ship_a.ship_id))
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

    print(get_ship_status(ship_a.ship_id))

ship_a = new_ship('test_ship','test_class')
time.sleep(2)
print(get_ship_status(ship_a.ship_id))
turn(ship_a)

           



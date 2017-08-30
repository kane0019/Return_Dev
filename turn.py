class turn_out_come:
    def __init__(self,ship,event):
        ship.energy+=event["energy_change"]
        ship.resourceA+=event["resourceA_change"]
        ship.resourceB+=event["resourceB_change"]
        ship.power+=event["power_change"]
    
from event_dic import events
class event:
    energy_change=0
    resourceA_change=0
    resourceB_change=0
    power_change=0
    def __init__(self,eventnumber):
        self.eventnumber=eventnumber
        print("event "+str(self.eventnumber))
    def event_run(self):
        event_result=events(self.eventnumber)
        self.energy_change=event_result["energy_change"]
        self.resourceA_change=event_result["resourceA_change"]
        self.resourceB_change=event_result["resourceB_change"]
        self.power_change=event_result["power_change"]
        return {"energy_change":self.energy_change,"resourceA_change":self.resourceA_change,"resourceB_change":self.resourceB_change,"power_change":self.energy_change}
    
# print(event(1).event_run())
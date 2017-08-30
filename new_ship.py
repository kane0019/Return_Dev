from DBInput import db_new
class ship:
    shipname=""
    shipclass=""
    energy=0
    resourceA=0
    resourceB=0
    power=0
    def __init__(self,shipname,shipclass):
        self.shipname = shipname
        self.shipclass = shipclass
        self.energy= 5
        self.resourceA=10
        self.resourceB=10
        self.power=0
    def create_new_ship(self):
        db_new(self.shipname,self.shipclass,self.energy,self.resourceA,self.resourceB,self.power)   

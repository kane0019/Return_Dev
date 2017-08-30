import random
class dice:
    def __init__(self,dicenumber):
        self.n=dicenumber
    def rolldice(self):
        total=0
        for i in range(self.n):
            total+=random.randrange(1,6)
        return total
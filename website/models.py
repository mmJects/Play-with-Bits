# to get user's inputs before the response
class Users_desires:
    def __init__(self,cal_types:list,numbers:int):
        self.cal_types = cal_types
        self.numbers = numbers
        self.numbers_changes = False
    
    def make_changes(self):
        self.numbers_changes = True

# to create own calculations 
class Calculations:
    def bitwise_and(self,x,y):
        return x & y
    def bitwise_nand(self,x,y):
        pass
    def bitwise_nor(self,x,y):
        pass
    def bitwise_not(self,x,y):
        pass
    def bitwise_or(self,x,y):
        return x | y
    def bitwise_xOR(self,x,y):
        return x  ^ y


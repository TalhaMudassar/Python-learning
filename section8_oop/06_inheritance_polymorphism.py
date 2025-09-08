class BaseChai:
    def __init__(self,type_):
        self.type = type_
        
    def prepare(self):
        print(f"preparing {self.type} chai ....")
        
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardmom,ginger, cloves")
        
class ChaiShop:
    chai_cls = BaseChai
    def __init__(self):
        self.chai = self.chai_cls("Regular")
        
    def serve(self):
        print(f"serving {self.chai.type} chai in shop")
        self.chai.prepare()
        
class FansyChaiShop(ChaiShop):
    chai_cls = MasalaChai
    
    
shop = ChaiShop()
fansy = FansyChaiShop()
shop.serve()
fansy.serve()
fansy.chai.add_spices()
        

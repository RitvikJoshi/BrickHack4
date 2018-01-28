class product:
 
   __slots__ = 'self','ItemNumber','Brand','Description','Price','StoreNumber'
   
   def __init__(self,ItemNumber=None,StoreNumber=None,Description=None,Brand=None,Price=None):
    self.Brand=Brand
    self.Description=Description
    self.Price = Price
    self.ItemNumber=ItemNumber
    self.StoreNumber=StoreNumber
    
    
   def __repr__(self):
    return     "ItemNumber :"+str(self.ItemNumber)+" Brand :"+self.Brand+" Descritpion :"+self.Description+" price :"+str(self.Price)+' storeNum :'+str(self.StoreNumber)

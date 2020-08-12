def getVAT(VAT_percantage, Taxamount):
   VAT = int(VAT_percantage * Taxamount)
   
   return VAT

def userinput():
   VAT_percantage = int(input("Enter VAT Percantage"))/100
   Taxamount = float(input("Enter your Tax amount"))
   VAT = getVAT(VAT_percantage,Taxamount)

#print("Your VAT amount is {:,.2f}".format(VAT))

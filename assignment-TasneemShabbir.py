def getVAT(VAT, amount):
   Tax= float(amount * VAT)

   return Tax

def userinput():
   VAT = float(input("Enter VAT"))
   amount = float(input("Enter Amount"))
   clientTaxAmount= getVAT(VAT, amount)

   print("KSH{:,.2f}".format(clientTaxAmount))
userinput()




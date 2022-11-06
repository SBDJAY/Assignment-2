import random
#INPUT
print('Welcome to the Product Sales Data Estimator')


#Product Code
while True:
    try:
        ProductCode = int(input('\nPlease enter the Product Code: '))
        break
    except:
        print('Please enter a INTEGER VALUE') 
#Product Name
ProductName = str(input('Please enter the Product Name: '))
#Current Stock
while True:
    try:
        CurrentStock = int(input('Please enter the Curent Stock: '))
        break
    except:
        print('Please Enter a INTEGER VALUE')
#Product Price
while True:
    try:
        ProductPrice = float(input('Please enter the Product Sale Price: '))
        break
    except:
        print('Please Enter a valid cost (float)')
#Manufacture Price
while True:
    try:
        ManufacturePrice = float(input('Please enter Product Manufacture Price: '))
        break
    except:
        print('Please Enter a valid cost (float)')
#Monthly Production
while True:
    try:
        MonthlyProduction = int(input('Please enter the Estimated Monthly Production: '))
        break
    except:
        print('Please Enter a INTEGER VALUE')

print('Product code: ', ProductCode)
print('Prodcut Name: ', ProductName)
print('-----------------------------')
print('Sale Price: ', ProductPrice)
print('Manufacture Price: ', ManufacturePrice)
print('Monthly Production: ', MonthlyProduction, '(approx)')

#CALCULATOR
for month in range (1,13):
    
    EstimatedProduction = [MonthlyProduction]
    for SoldProduction in EstimatedProduction:
        SoldProduction = MonthlyProduction + random.randrange(-10, 11)

        NewStock = (CurrentStock + MonthlyProduction - SoldProduction)
        CurrentStock = NewStock

        print('\nMonth', month,': \n-    Current Stock:', CurrentStock,'\n-    Manufactured Units: ',MonthlyProduction,'\n-    Sold: ',SoldProduction,'\n-    Stock: ', NewStock)

StockSold = MonthlyProduction + NewStock
netprofit = ((StockSold * ProductPrice) - (MonthlyProduction * ManufacturePrice))
print('\nNet Profit: ','%.2f' % netprofit)





        
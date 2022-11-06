import random
print('Welcome to the Product Sales Data Estimator')
        
ProductCode = int(input('\nPlease enter the Product Code: '))
ProductName = str(input('Please enter the Product Name: '))
CurrentStock = int(input('Please enter the Curent Stock: '))
ProductPrice = float(input('Please enter the Product Sale Price: '))
ManufacturePrice = float(input('Please enter Product Manufacture Price: '))
MonthlyProduction = int(input('Please enter the estimated monthly production: '))

EstimatedProduction = [MonthlyProduction]
for SoldProduction in EstimatedProduction:
    SoldProduction = MonthlyProduction + random.randrange(-10, 11)

NewStock = ((CurrentStock + MonthlyProduction) - SoldProduction)

print('Product code: ', ProductCode)
print('Prodcut Name: ', ProductName)
print('-----------------------------')
print('Sale Price: ', ProductPrice)
print('Manufacture Price: ', ManufacturePrice)
print('Monthly Production: ', MonthlyProduction, '(approx)')

for month in range (1,13):
    print('\nMonth', month,':')
    print('-    Manufactured Units: ', MonthlyProduction)
    print('-    Sold: ', SoldProduction)   
    print('-    Stock: ', NewStock)
    print('\nNet Profit: ', (SoldProduction * ProductPrice) - ((MonthlyProduction + CurrentStock) * ManufacturePrice)) 
#IGNORE THE NEGATIVE NET PROFIT FOR NOW, IT IS ONLT SHOWING NET PROFIT FOR 1 MONTH
#step 1: take net profit formula and put into one variable
#step 2: make formula add to a total variable and will acculmilate with time
#step 3: print variable total
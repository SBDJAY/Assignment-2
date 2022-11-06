#-----------------------------------------------------------
# Objected Oriented Analysus, Design, & Programming
# Daniel Pius
# Muhammad Asif
# Class: 1229_4013: Programming Principles
# November 3, 2022
#-----------------------------------------------------------
#IMPORTING MODULE AND CLASS
import ProductSaleCalculatorModule
completeProductEstimator = ProductSaleCalculatorModule.ProductSaleCalculator()
#-----------------------------------------------------------
#APPLICATION
#Product Code
while True:
    try:
        completeProductEstimator.ProductCode = int(input('\nPlease enter the Product Code: '))
        break
    except:
        print('Please enter a INTEGER VALUE') 
#Product Name
completeProductEstimator.ProductName = str(input('Please enter the Product Name: '))
#Current Stock
while True:
    try:
        completeProductEstimator.CurrentStock = int(input('Please enter the Curent Stock: '))
        break
    except:
        print('Please Enter a INTEGER VALUE')
#Product Price
while True:
    try:
        completeProductEstimator.ProductPrice = float(input('Please enter the Product Sale Price: '))
        break
    except:
        print('Please Enter a valid cost (float)')
#Manufacture Price
while True:
    try:
        completeProductEstimator.ManufacturePrice = float(input('Please enter Product Manufacture Price: '))
        break
    except:
        print('Please Enter a valid cost (float)')
#Monthly Production
while True:
    try:
        completeProductEstimator.MonthlyProduction = int(input('Please enter the Estimated Monthly Production: '))
        break
    except:
        print('Please Enter a INTEGER VALUE')

completeProductEstimator.displayOuputs()
    
        
import random

#CALCULATIONIONS CLASS
class ProductSaleCalculator:
    def __init__(self, ProductCode= 1, ProductName = "", CurrentStock = 1, ProductPrice = 1, ManufacturePrice = 1, MonthlyProduction = 1):
        self.ProductCode = ProductCode
        self.ProductName = ProductName
        self.CurrentStock = CurrentStock
        self.ProductPrice = ProductPrice
        self.ManufacturePrice = ManufacturePrice
        self.MonthlyProduction = MonthlyProduction


    def displayOuputs(self):
        print('\nProduct code: ', self.ProductCode,'\nProduct Name: ', self.ProductName,'\n-----------------------------\nSale Price: ',self.ProductPrice,
        '\nManufacture Price: ',self.ManufacturePrice,'\nMonthly Production: ',self.MonthlyProduction,'(Approx)')
        newStock = self.CurrentStock
        SoldProduction = 0
        for Month in range(1,13):
            StockReturns = random.randrange(-10,11)
            newStock -= StockReturns
            print('\nMonth', Month,': \n-    Current Stock:', self.CurrentStock,'\n-    Manufactured Units: ',self.MonthlyProduction,'\n-    Sold: ',self.CurrentStock + StockReturns,
            '\n-    Stock: ', newStock)
            SoldProduction += self.MonthlyProduction + StockReturns
        netProfit = ((SoldProduction * self.ProductPrice) - (self.MonthlyProduction+ self.ManufacturePrice))
        print('\nNet Profits: ','%.2f' % netProfit)





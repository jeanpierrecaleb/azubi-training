#Welcome to our tip calculator
charge = float(input('Enter the charge for the food: '))
tip = charge*18/100
tax_sales = charge*7/100
print('Charge for food: ', charge, '\n',
      'Charge tip', tip, '\n',
      'Sales tax:', tax_sales,'\n',
      'Grand Total', charge + tip + tax_sales)

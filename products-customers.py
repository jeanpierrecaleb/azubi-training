products = ["Sankofa Foods", "Jamestown Coffee",
            "Bioko Chocolate", "Blue Skies Ice Cream",
            "Fair Afric Chocolate", "Kowa Moka Coffee",
            "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

nb_cust = [2, 3, 5, 8, 4, 4, 6, 2, 9]

sum=0
index=0
for x in prices:
    #for y in nb_cust:
        #if index < len(prices):
            print(products[index], ':', prices[index], '*' , nb_cust[index], '=', prices[index]*nb_cust[index])
            sum = sum + prices[index] * nb_cust[index]
            index = index + 1
        
print("Total grand: ", sum)
print("Total average per product: ", sum/len(products))
#avg_total = sum/sum(nb_cust_lw, 0)
#print('Total price Average: ', avg_total)

new_price = list()
y=0
for x in prices:
    y = x - 5
    new_price.append(y)
    y=0

print('Old prices', prices)
print('New prices', new_price)

sum_new=0
index=0
for x in new_price:
    #for y in nb_cust:
        #if index < len(new_price):
            print(new_price[index], '*' , nb_cust[index], '=', new_price[index]*nb_cust[index])
            sum_new = sum_new + new_price[index] * nb_cust[index]
            index = index + 1


#product less than 30 dollars
prd_inf_30 = []
index = 0
for x in new_price:      
    if x < 30:
        prd_inf_30.append(products[index])
    index = index+1

print('Product with price less than 30:', prd_inf_30)
print("New Total grand (New prices): ", sum_new)
print("New Total average per product: ", sum_new/len(products))
print("Total revenue generated (Last week, this week)", sum+sum_new)
print("Daily revenue average if considered -5$ is for present week: ",
      (sum+sum_new)/14)

#print(sum)
    



 

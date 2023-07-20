products = ["Sankofa Foods", "Jamestown Coffee",
            "Bioko Chocolate"]

prices = [30, 25, 40]

nb_cust = [2, 3, 10]

sum=0
index=0
for x in prices:
    for y in nb_cust:
        if index < len(prices):
            print(products[index], ':', prices[index], '*' , nb_cust[index], '=', prices[index]*nb_cust[index])
            sum = sum + prices[index] * nb_cust[index]
            index = index + 1
        
print("Total grand: ", sum)
print("Total average: ", sum/len(products))
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
    for y in nb_cust:
        if index < len(new_price):
            print(new_price[index], '*' , nb_cust[index], '=', new_price[index]*nb_cust[index])
            sum_new = sum_new + new_price[index] * nb_cust[index]
            index = index + 1

print("New Total grand: ", sum_new)
print("New Total average: ", sum_new/len(products))

#print(sum)
    



 

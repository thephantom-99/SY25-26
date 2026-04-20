stock_count = int(input("How many items are in stock? "))
if stock_count > 5:
    print("Stock level: High")
elif 5 <= stock_count <= 5:
    print("Stock level: Low")
else:
    print("Out of stock")

int = 0 
for i in range(2,51,2):
    sum = sum + i 
    print("The sum of even numbers from 2 to 50 is:", sum)

from math import e

weight = float(input("Enter the weight of the potato in grams: "))
if weight < 100:
    grade = "small"
elif 100 <= weight <= 200:
    grade = "medium"
else:
    grade = "large"
print(f"This is a: {grade} potato.")

#---------------------------------

blemish_count = []
for i in range(5):
    count = int(input(f"Enter counts {i+1}: "))
    blemish_count.append(count)
total = sum(blemish_count)
print("Total blemishes recorded:", total)
print(f"average blemishes per day: {total / 5:.2f}")


#---------------------------------

all_potatoes = [0,2,5,1,0,8,3,0]
perfect_potatoes = []

for p in all_potatoes:
    if p == 0:
        perfect_potatoes.append(p)
num_total = len(all_potatoes)
num_perfect = len(perfect_potatoes)
percentage = (num_perfect / num_total) * 100

print(f"Perfect potatoes found:", perfect_potatoes)
print(f"Batch quality: {percentage}%")

rider_scores = [10, 45, 80, 25, 120, 60]

for i in range(len(rider_scores)):
    if rider_scores[i] >= 50:
        rider_scores[i] += 20

final_sum = sum(rider_scores)

print("Final sum of rider scores:", final_sum)



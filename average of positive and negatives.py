pos_sum = pos_count = neg_sum = neg_count = 0

while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    elif num > 0:
        pos_sum += num
        pos_count += 1
    elif num < 0:
        neg_sum += num
        neg_count += 1

if pos_count > 0:
    print("Average of positive numbers:", round(pos_sum / pos_count, 2))
else:
    print("No positive numbers entered.")

if neg_count > 0:
    print("Average of negative numbers:", round(neg_sum / neg_count, 2))
else:
    print("No negative numbers entered.")

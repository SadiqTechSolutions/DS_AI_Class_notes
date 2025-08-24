prev_num = 0

for i in range(10):
    num_sum = prev_num + i
    print("Current Number ", i, "Previous Number ", prev_num, "Sum: ", num_sum)
    prev_num = i
data = input().split(", ")
int_data = [int(ele) for ele in data]
data_even = [index for index in range(len(int_data)) if int_data[index] % 2 == 0]

print(data_even)

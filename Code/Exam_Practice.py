data_list = [1, 7, 3, 9, 2, 4]
temp = 0
loop = 0
n = len(data_list)
for i in range(n):
    for num in range (0, n - i - 1):
        if data_list[num] > data_list[num + 1]:
            data_list[num], data_list[num + 1] = data_list[num + 1], data_list[num]
n = len(data_list)
if n % 2 == 0:
    half = n // 2
    median = data_list[half - 1] 
elif n % 2 != 0:
    half = n // 2
    median1 = data_list[half - 1]
    median2 = data_list[half]
    median = (median1 + median2) / 2
print("The median =", median)

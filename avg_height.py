heights = input("Enter the different heights separated by a comma ")
delimiter = ","
height_list = heights.split(delimiter)

count=0
for i in height_list:
    count=count+1

sum = 0
for i in range(count):
    sum = sum+int(height_list[i])
average = round(sum/count)
print(f"Average is {average}")
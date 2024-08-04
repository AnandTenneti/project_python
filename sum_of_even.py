# Program to caluclate the sum of 100 numbers in the range 1..100

-- Program execution started -------
print("Approach 1")
sum_of_even_numbers=0
for i in range(2,101,2):
    sum_of_even_numbers +=i  
print("Approach 1",sum_of_even_numbers)

print("Approach 2")
sum_of_even_nos=0
for i in range(1,101):
    if i%2==0:
        sum_of_even_nos +=i  
print("Approach 2",sum_of_even_nos)

# WAP to find out how many days, weeks, months are left if we live until 90 years old
# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

max_age=90
current_age = int(input("Enter your age : "))
years_left=max_age-current_age
days_left= years_left*365
weeks_left=years_left*52
months_left= years_left*12

print(f"You have {days_left} days,{weeks_left} weeks and {months_left} months")

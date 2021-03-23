#1. Create a variable and initialize it with a
#    number 1-4.
#2. Create 4 conditions (if-elif) which will check
#the variable.
#3. print the season name accordingly:
#- 1 = summer
#- 2 = winter
#- 3 = fall
#- 4 = spring

num = "a"
if type(num) == str:
    num = num.isdigit()
    print("enter numbers only")
if num == 1:
    print("summer")
if num == 2:
    print("winter")
if num == 3:
    print("fall")
if num == 4:
    print("spring")
elif num >= 5 or num <= 0:
    print("wrong input")

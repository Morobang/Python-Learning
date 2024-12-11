# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆
new_height = float(height)
new_weight = float(weight)
# Write your code below this line 👇

BMI=int(new_weight/(new_height*new_height))
print(BMI)

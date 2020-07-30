# Write your height in meters
 
height = float(input("Enter your height : "))
print(height)

# Write your weight in kilograms

weight = float(input("Enter your weight : "))
print(weight)
bmi = round(weight / (height * height) , 2)

print("")
print("Your body mass index is : ", bmi)
print("")
if(bmi < 18.5):
    print("Oh no, you are under weight")

if(bmi > 18.5 and bmi <= 24.9):
    print("Perfect! you're just right. Normal weight")

if(bmi >= 25 and bmi <= 29.9):
    print(" Wake up call, it seems you're Over Weight")

if(bmi >= 30 and bmi <= 34.9):
    print("You are mildly obese or in other words Obese class 1")

if(bmi >= 35 and bmi <= 39.9):
    print("You are more than average obese or in simpler terms class 2)")

if(bmi >= 40):
    print("You are extremely obese or in other words class 3)")

#Keep pushing !
    #AkiraChix
    #CodeHive


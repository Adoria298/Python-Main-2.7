import time

weight = raw_input("What is your weight?(kg) ")
height = raw_input ("What is your height?(m) ")
squareHeight = float(height) * float(height)

bmi = float(weight)/float(squareHeight)
round (bmi)

print "BMI:" ,str(bmi) + "kg/sq m"
if bmi<18.5:
   print "You are underweight."
elif bmi>18.5 and bmi<25:
   print "You are in the normal range."
elif bmi>25 and bmi<30:
   print "You are overweight."
elif bmi>30:
   print "You are obese."
time.sleep(10)

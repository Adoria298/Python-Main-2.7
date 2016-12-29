import time

weight = raw_input("What is your weight?")
height = raw_input ("What is your height?")
squareHeight = float(height) * float(height)

bmi = float(weight)/float(squareHeight)
round (bmi)

print bmi
time.sleep(10)

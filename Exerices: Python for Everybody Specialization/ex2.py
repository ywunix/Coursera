number = input("Enter Score: ")
try:
    score = float(number)
except:
    print("Error: Invalid Input!!")
    exit(-1)

if score < 0.6:
    Letter = "F"
elif score < 0.7:
    Letter = "D"
elif score < 0.8:
    Letter = "C"
elif score < 0.9:
    Letter = "B"
else:
    Letter = "A"

print(Letter)
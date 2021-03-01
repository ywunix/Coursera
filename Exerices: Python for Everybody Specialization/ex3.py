def computepay(hrs, rate):
    pay = hrs * rate
    if hrs > 40:
        pay += 0.5 * (hrs - 40) * rate
    return pay

hours = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    hrs = float(hours)
    r = float(rate)
except:
    print("Error: Invalid Input")
    exit(-1)

print(computepay(hrs, r))
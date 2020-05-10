def computepay():
    hrs = input("Enter hours:")
    rate = input("Enter Rate:")
    h = float(hrs)
    r = float(rate)
    if h > 40:
        overtime = (h - 40) * (r * 1.5)
        pay = (40 * r) + overtime
    elif h <= 40 :
        pay = h * r
    return pay
    
print(computepay())
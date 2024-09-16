#function to solve each criteria
#area of a circle function
def circleArea(pi,radius):
    pi = 3.1415926
    area = 3.1415926 * radius ** 2
    return area
#calculate money and tax rate
def totalDue(money, taxRate):
    total = money + (money * (taxRate/100))
    return total
#covert farenheit to celcius
def celsiusConversion(farenheit):
    celsius = (farenheit - 32) * (5 / 9)
    return celsius

#input data
#circle data
print("Input data for circle.")
radius = float(input("Enter radius: "))
pi = 3.1415926
area = circleArea(pi, radius)
print("Circle area: {:.2f}".format(area))

#tax data
print("Input data for money and taxes.")
money = int(input("Input money: "))
taxRate = float(input("Input tax rate: "))
total = totalDue(money, taxRate)
print("Total due: {:.2f}".format(total))

#temperature data
print("Input data for temperature.")
farenheit = int(input("Input temperature in Farenheit: "))
celsius = celsiusConversion(farenheit)
print("Celsius temperature is: {:.4f}".format(celsius))
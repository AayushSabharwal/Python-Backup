#program to convert celsius to farenheit and vice versa

#temperature in celsius
c = int(input("Enter temperature in celsius"))
#converting to farenheit
f = ((9/5) * c) + 32
print(c, ' Celsius = ', f, ' Farenheit')

#vice versa
f = int(input("Enter temperature in farenheit"))
c = (5/9)*(f-32)
print(f, ' Farenheit = ', c, ' celsius')

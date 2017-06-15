# converting units of measurement using programs

# length - convert 25.5 inches to meters. Math formula?

length = (25.5 * 2.54)/100
print(length)

# convert miles to km. Math formula

mileTokm = 650 * 1.609
print(mileTokm)

# temperature conversion Fahrenheit to Celsius
'''
C =(F-32)*5/9
'''

# 98.6 degrees Fahrenheit is the normal human body temperature. Celsius? (37)

F= 98.6
C= (F-32)*(5/9)
print(C)

'''
Task: convert temperature from Celsius to Fahrenheit
F = (C* 9/5)+32

'''
C= 37
F = C*(9/5)+32

print(F)

#warmUp finished
#########################################
# Unit Converter: Miles to Kilometers

def print_menu():
    print('1.Kilometers to Miles')
    print('2.Miles to Kilometers')

def km_miles():
    km = float(input('Enter the distance in kilometers: '))
    miles = km/1.609
    print("Distance in miles: {0}".format(miles))
def miles_km():
    miles = float( input("Enter the distance in miles: "))
    km = miles* 1.609
    print("Distance in kilometers: {0:.2f}".format(km))

if __name__ == '__main__':
    print_menu()
    print('Which conversion would you like to do? : ')
    choice = input("Pick 1 for km to miles and 2 for miles to km: ")
    if choice == "1":
        km_miles()
          
    if choice == '2':
        miles_km()



    
        






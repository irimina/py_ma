'''
handle exceptions with try...except 
'''

while True:
    try:
        a = float(input('Enter  a number: '))
        if a%2==0:
            print(a, 'This is an even number')
        if a%2 !=0:
            print(a, 'You have an odd number')
    except ValueError:
        print('you entered an invalid number.Program terminated')
        break

        

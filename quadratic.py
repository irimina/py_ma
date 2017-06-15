# solve linear equation using Python

x= 10-500+79
print(x)

# for a second degree equation, use quadratic formula ax squared + bx+c = 0
# quadratic formula
#x1 and then x2 = -b + square root of b squared minus ac, everything divided by 2a

a = 1
b = 2
c = 1

D = ( b**2 - 4*a*c)**0.5

# now evaluate x1 and x2

x_1= (-b+D)/(2*a)
print(x_1)

x_2= (-b-D)/(2*a)
print(x_2)

# you can substitute the answer in the equation and see if it evaluates to 0

#warmup done
############################################

'''
Quadratic equation root calculator
'''

def roots(a,b,c):
    D= (b*b -4*a*c)**0.5
    x_1=(-b+D)/(2*a)
    x_2=(-b-D)/(2*a)

    print('x1:{0}'.format(x_1))
    print('x2:{0}'.format(x_2))

if __name__ == '__main__':
    a = input("Enter a: ")
    b = input("Enter b: ")
    c= input("Enter c: ")
    roots(float(a), float(b), float(c))
    
    
          




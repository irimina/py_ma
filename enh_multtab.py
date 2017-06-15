#generating multiplication tables

#a, b,n are integer numbers a X n = b

# WARMUP using the format() method

item1 = 'apples'
item2= 'bananas'
item3 = 'grapes'
#print("At the grocery store, I bought some {0} and {1}".format(5,10))

print("At the grocery store, I bought some {0} and {1}".format(item2,item3))

# finish warmup

'''
Multiplication table printer
'''

def multi_table(a):
    for i in range(1,11):
        print('{0} x {1} = {2}'.format(a,i,a*i))

if __name__ =='__main__':
    a = input("Enter a number: ")
    multi_table(float(a))
    

'''
further control how numbers are printed
by modifying the place holder {2:.2f}
meaning we want only 2 numbers after the decimal point
'''



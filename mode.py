'''
finding the mode and creating a frequency table 
mode is the number that happens the most frequently
'''

'''
use the Counter class from collections module which is part of the standard
library; most_common is a method of the Counter class

'''
# warmup

simpleList = [4,2,1,3,4]
from collections import Counter
c = Counter(simpleList)
print(c.most_common())

'''
Calculating the mode
'''

def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]
if __name__ =='__main__':
    scores = [7,8,9,2,10,9,9,9,9,4,5,6,1,5,6,7,8,6,1,10]
    mode = calculate_mode(scores)

    print('The mode of the list is {0}'.format(mode))


'''
dispersion - tells us how far away the numbers in a data set are from the
mean of the data set
'''
# three methods of dispersion: range, variance, standard deviation


'''
Finding the range of a set of numbers
The range shows the difference between the highest and the lowest number
'''

# find the range

def find_range(numbers):
    lowest= min(numbers)
    highest= max(numbers)

    # find the range
    r = highest-lowest
    return lowest, highest, r

if __name__ == '__main__':
    donations= [100,60,70,900,100,200,500,500,503,600,1000,1200]
    lowest, highest, r= find_range(donations)
    print('Lowest:{0} Highest:{1} Range: {2}'.format(lowest, highest, r))
    



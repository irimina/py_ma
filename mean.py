'''
Calculating the mean 

'''

def calculate_mean(numbers):
    s= sum(numbers)
    n = len(numbers)
    #calculate mean
    mean = s/n
    return mean

if __name__ == '__main__':
    donations= [100,60.50,70.25,900,100,200,500,500,503,600,1000,1200]
    mean= calculate_mean(donations)
    total_n = len(donations)
    print('The average donation over the last {0} days is {1}'.format(total_n,mean))







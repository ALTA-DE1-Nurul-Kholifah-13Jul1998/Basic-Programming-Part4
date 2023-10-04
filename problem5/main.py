def mean_median(array_input):
    mean = 0
    median = 0
    n = len(array_input)

    if n!=0:
        for i in (array_input):
            mean+=i
        mean/=n
    
        if n%2==0:
            a1=int(n/2)   
            median=array_input[a1-1] + array_input[a1]
            median/=2
        else:
            a1=round(n/2)
            median=array_input[a1]
    if n==0:
        return None
        
    return (mean,median)

if __name__ == '__main__':
    print(mean_median([1, 2, 3, 4])) # (2.5, 2.5)
    print(mean_median([1, 2, 3, 4, 5])) # (3.0, 3)
    print(mean_median([7, 8, 9, 13, 15])) # (10.4, 9)
    print(mean_median([10, 20, 30, 40, 50])) # (30.0, 30)
    print(mean_median([15, 20, 30, 60, 120])) # (49.0, 30)
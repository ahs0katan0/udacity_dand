import pandas as pd

def variable_correlation(a, b):

    num_same_direction = None   # Replace this with your code
    
    num_different_direction = None   # Replace this with your code
    
    acomp_same =(a > a.mean())
    bcomp_same =(b > b.mean())
    #print (acomp_same) 
    #print (bcomp_same)
    num_same_direction = (len(acomp_same[acomp_same == bcomp_same]))
    #print (num_same_direction)
    num_different_direction = len(~acomp_same[~acomp_same == bcomp_same])
    print (num_same_direction, num_different_direction)
    return (num_same_direction,num_different_direction);
    
    
a = pd.Series([1, 2, 3, 4])
b = pd.Series([10, 11, 12, 13])

variable_correlation(a,b)

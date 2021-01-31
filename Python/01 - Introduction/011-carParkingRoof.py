!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'carParkingRoof' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY cars
#  2. INTEGER k
#

def carParkingRoof(cars, k):
    # Write your code here
    cars.sort()
    result = float('inf')
    n = len(cars)
    for i in range(n-k+1):
        result = min(result,cars[i+k-1] - cars[i])
    return result + 1
if __name__ == '__main__':
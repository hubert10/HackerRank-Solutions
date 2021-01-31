#
# Complete the 'segment' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER_ARRAY space
#

def segment(x, space):
    # Write your code here
    res = []
    n = len(space)
    for i in range(0,n-x+1):
        temp = []
        temp = space[i:i+x]
        res.append(min(temp))
    return max(res)
print(segment(1, [1,3,2,1,2]))
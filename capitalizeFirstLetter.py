import os
def solve(s):
    
    st = s.split(' ')
    s1=""
    for i in st:
        s1 = s1 + i.capitalize() + " "
    
    return s1

    # return " ".join([name.capitalize() for name in s.split(" ")])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

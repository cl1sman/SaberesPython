"""
    The included code stub will read an integer,n , from STDIN.
    Without using any string methods, try to print the following:
    
    123 ... n

    Note that "..." represents the consecutive values in between.


    Example
    n = 5
    Print the string 12345
"""

if __name__ == '__main__':
    n = int(input())
    vetor = []
    for i in range(n):
        vetor.append(i+1)

    str1 = ''

    for element in vetor:
        str1 += str(element)
print(str1)
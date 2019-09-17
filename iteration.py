import os

def line_asterlisks(n):
    str1 = ''
    for i in range(n, 0, -1):
        for j in range(n - i):
            str1 = str1 + ''
        for j in range(2 * i - 1):
            str1 = str1 + '*'
        print(str1)

def mod(n):
    result = 0
    while n > 0:
        n = n // 10
        result += 1
    return result

def fibo(n):
    a = 1
    b = 1
    while b < n:
        c = a + b
        a = b
        b = c
        if c < 1000:
            print(c)

def iterdictionary():
    days = {'mon': 'Monday', 'tue': 'Tuesday',\
    'wed': 'Wednesday','thu': 'Thursday', 'fri':\
     'Friday', 'sat': 'Saturday','sun': 'Sunday'}
    for day in days:
         print (day, 'stands for', days[day])


if __name__ =='__main__':
    #line_asterlisks(5)
    iterdictionary()
import time
start_time=time.time()

digits={
-1:"and",
0:"",
1:"one",
2:"two",
3:"three",
4:"four",
5:"five",
6:"six",
7:"seven",
8:"eight",
9:"nine",
10:"ten",
11:"eleven",
12:"twelve",
13:"thirteen",
14:"fourteen",
15:"fifteen",
16:"sixteen",
17:"seventeen",
18:"eighteen",
19:"nineteen",
20:"twenty",
30:"thirty",
40:"forty",
50:"fifty",
60:"sixty",
70:"seventy",
80:"eighty",
90:"ninety",
100:"hundred",
1000:"thousand"
}

n=1000

def tell_1_99(n):
    if n <= 20:
        return digits[n]
    elif n<= 99:
        return digits[n//10*10]+digits[n%10]

def tell_1_999(n):
    if n <= 99: return tell_1_99(n)
    word=tell_1_99(n//100)+digits[100]
    if n%100 != 0 :
        word+=digits[-1]+tell_1_99(n%100)
    return word
     
def tell_1_999999(n):
    if n <= 999: return tell_1_999(n)
    word=tell_1_999(n//1000)+digits[1000]
    if n%1000 != 0 :
        word+=tell_1_999(n%1000)
    return word  

words=''

for i in range(1,n+1):
    word=tell_1_999999(i)
    words+=word

answ=len(words)
print("Answ:",answ)
print("Time:",time.time()-start_time)

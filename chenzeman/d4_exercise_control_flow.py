#!/bin/usr/env python3

for i in range(1,10):
    for n in range(1,10):
        if i >= n:
            s = i * n
            print(i, '*', n, '=', s,' ',end='\t')

x = 1
while x < 10:
    if x % 2 != 0:
        for n in range(1,1+x):
            s = x * n               
            print(x,'*',n,'=',s,' ',end='\t')
    x = x + 1

    
# file imports
from __future__ import print_function #Only for Python2
# python program without fast I/O
from time import perf_counter

#integer input from user, 2 input in single line
n,m = map(int,input().split()) 

t1_start = perf_counter()
for i in range(n):
    t=int(input()) # user gave input n times
    if t%m == 0:
        print(t) #print the output if condition satisfied



# file openings which to be compared
# outfile is to store the result of difference

with open('sample.txt') as f1, open('sample2.txt') as f2, open('result.txt', 'w') as outfile:
    for line1, line2 in zip(f1, f2):
        if line1 == line2:
            print(line1, end='', file=outfile)
            

# Stop the stopwatch/counter
t1_stop = perf_counter()

print("Elapsed time:", t1_stop-t1_start) # Report results


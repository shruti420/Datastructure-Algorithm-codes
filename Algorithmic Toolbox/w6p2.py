import sys
import pdb
from itertools import product
import random

def naive_partition(A):
    n = len(A)
    for partition in product([1,2,3], repeat=n):
        # for each option we can compute the sum of weights for each part
        sums = [sum([a[0] if a[1] == i else 0 for a in zip(A, partition)])for i in range(1,4)]
        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1
    return 0

def partition3(A):
    sum, number_of_values = 0, 0
    for value in A:
        sum += value
        number_of_values += 1
    if sum % 3 != 0 or number_of_values < 3:
        return 0
    sum = sum // 3

    def form_groups(group_target):
        dp = []
        for row in range(len(A)+1):
            dp.append([])
            for col in range(group_target+1):
                dp[row].append([0])
        target_reached, row, col = 0, 0, 0

        '''
        in dp, the 1st row is for a value of 0, although value 0 will never be present, it is needed as a starting value
        therefore we are starting the row from an index of 1, and dp will have len(A)+1 rows
        similarly there will be group_target + 1 columns
   each index in dp or item in dp, will be a list of length 3:
        0th item being the sum at that index,
        1st being "0" (indication of value at that row not being added at this column to get sum entered in 0th index)
               or "1" (indication of value at that row being added at this column)
        2nd item is a list, which contains row and column of the previous index from which current sum is formed as per logic in inner for loop (so a pointer)
        '''
        #pdb.set_trace()
        for row in range(1,len(A)+1):
            value = A[row-1]
            if value > group_target:
                return 0
            for col in range(1,group_target+1):
                if value > col:
                    dp[row][col] = [dp[row-1][col][0],0,[row-1,col]]
                else:
                    new_value = value + dp[row-1][col - value][0]
                    if new_value > col:
                        new_value = 0
                    if dp[row-1][col][0] > new_value:
                        dp[row][col] = [dp[row-1][col][0], 0, [row-1,col]]
                    else:
                        dp[row][col] = [new_value, 1, [row-1,col-value]]
                    if new_value == group_target:
                        target_reached = 1
                        break
            if target_reached:
                break
        #pdb.set_trace()
        added = dp[row][col][1]
        if target_reached:
            while row > 0:
                if added:
                    del A[row-1]
                try:
                    row, col = dp[row][col][2]
                    added = dp[row][col][1]
                except IndexError:
                    break
            return 1
        else:
            return 0

    for _ in range(3):
        if not form_groups(sum):
            return 0
    if A == []:
        return 1

if __name__ == '__main__':
    num = random.randint(1,40)
    for iteration in range(num):
        print ("Iteration: ",iteration)
        number_of_values = random.randint(3,9)
        A = []
        for _ in range(number_of_values):
            A.append(random.randint(1,15))
        naive = naive_partition(A)
        better = partition3(A)
        
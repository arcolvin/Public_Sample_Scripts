#!/usr/bin/env python

def solution(data, n):
    final = []
    final.extend(data)
    unique = set(data)
    for ele in unique:
        if data.count(ele) > n:
            for i in range(data.count(ele)):
                final.remove(ele)

    return final


testCases = (([1, 2, 3], 0),([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))

for case in testCases:
    print(solution(case[0], case[1]))

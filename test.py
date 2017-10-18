with open("/Users/jensen/Documents/Jensen_C/Case_Study_05/Class_Task_10/randomletters_wnumbers.txt", "r") as f:
    line = f.readline()

nums = [x for x in line if x in "0123456789"]

print(nums)
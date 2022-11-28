from imports import *

with open('Data/wheat.txt', 'r') as f:
    lines = f.readlines()

print(lines[:5])
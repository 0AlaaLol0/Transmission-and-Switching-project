import math
import numpy as np
from math import factorial

Na = [3,4,7,9,12,4]
n60 =  [2,1,1,1,1,1]
n120 = [3,2,2,2,2,2]
n180 = [4,3,3,3,3,3]

def erlang(A, m):
    L = (A ** m) / factorial(m)
    sum_ = 0
    for n in range(m + 1): sum_ += (A ** n) / factorial(n)
    block=(L / sum_)
    return block 
    
    
def getacell(block_prob, trunks):
    left = 0
    right = 1000

    # Perform binary search to find the minimum offered load with the desired blocking probability
    while True:
        mid = (left + right) / 2
        b = erlang(mid, trunks)
        if abs(b - block_prob) < 0.0001:
            return mid
        elif b > block_prob:
            right = mid
        else:
            left = mid
            
def aaa(blockingprobability,totalnoofslots,slotsperuser,numberofchannelspercluster, noofsubscribers, avgcallperuser, avgcallduration, interferenceRatio):
    N = (interferenceRatio * 6 )/ 3
    Auser = (avgcallperuser / (24 * 60)) * avgcallduration
    Trunk = math.floor((numberofchannelspercluster / N) * (totalnoofslots / slotsperuser))
    Acell = getacell(blockingprobability, Trunk)
    NoOfSubPerCell = math.floor(Acell / Auser)
    TotalNumOfCells = math.ceil(noofsubscribers / NoOfSubPerCell)
    
    print("Number of cells without sectoring",TotalNumOfCells)
    
    WorkingN = []
    
    ay7aga = N/6
    
    i = 0
    while i<len(Na):
        
        if (Na[i] / n60[i]) > ay7aga:
            WorkingN.append(Na[i])
            break
        else:
            i += 1
    Trunk60 = math.floor(((numberofchannelspercluster / WorkingN[0]) * (totalnoofslots / slotsperuser)) / 6)    
    Acell60 = getacell(blockingprobability, Trunk60)
    NoOfSubPerCell60 = math.floor(Acell60 * 6 / Auser)
    
    i = 0
    while i<len(Na):
        
        if (Na[i] / n120[i]) > ay7aga:
            WorkingN.append(Na[i])
            break
        else:
            i += 1
    Trunk120 = math.floor(((numberofchannelspercluster / WorkingN[1]) * (totalnoofslots / slotsperuser)) / 3)
    Acell120 = getacell(blockingprobability, Trunk120)
    NoOfSubPerCell120 = math.floor(Acell120 * 3 / Auser)
    
    i = 0
    while i<len(Na):
        
        if (Na[i] / n180[i]) > ay7aga:
            WorkingN.append(Na[i])
            break
        else:
            i += 1
    Trunk180 = math.floor(((numberofchannelspercluster / WorkingN[2]) * (totalnoofslots / slotsperuser)) / 2)     
    Acell180 = getacell(blockingprobability, Trunk180)
    NoOfSubPerCell180 = math.floor(Acell180 * 2 / Auser)
    
    if NoOfSubPerCell60 > NoOfSubPerCell120 and NoOfSubPerCell180 :
        print("60 is the best sectoring")
        TotalNumOfCells = math.ceil(noofsubscribers / NoOfSubPerCell60)
    elif NoOfSubPerCell120 > NoOfSubPerCell60 and NoOfSubPerCell180 :
        print("120 is the best sectoring")
        TotalNumOfCells = math.ceil(noofsubscribers / NoOfSubPerCell120)
    else :
        print("180 is the best sectoring")
        TotalNumOfCells = math.ceil(noofsubscribers / NoOfSubPerCell180)
        
    return TotalNumOfCells

blockingprobability=0.001
totalnoofslots=8
slotsperuser=2
numberofchannelspercluster = 125
citysize = 450  # in Km2
noofsubscribers=1000000#number of subscribers per city
avgcallperuser = 10 #calls per day
avgcallduration = 1  # in minutes
interferenceRatio = 6.25

TotalNumOfCells = aaa(blockingprobability,totalnoofslots,slotsperuser,numberofchannelspercluster, noofsubscribers, avgcallperuser, avgcallduration, interferenceRatio)
print("Number of cells", TotalNumOfCells)
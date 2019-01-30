import random

print("Starting Claire's Tracker Generator")

def generateAngleObservations(n):
    
    p = 42
    x = []
    for i in range(n):
        x.append(2 * p * random.uniform(0,1) - p)
    return x

def getRandomAngleCoulombScatter():

    p = 10
    return 2 * p * random.uniform(0,1) - p


def generateAngle(n):
    print("Making prediction")
    x=[]
    for i in range(n):
        x.append(random.triangular(0,10,6))
    return x
    


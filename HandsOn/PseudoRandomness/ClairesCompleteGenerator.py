import random
import DoubleTriangularGenerator as doubleTriPDF

#==================================================
# 
# Library for tracker simulator
#
#==================================================
# 
# Parameter not in argument on purpose (hidden)
#
# Coulomb scatter: uniform theta distrib, from -p to p
# 
# Hard scatter: double triangle, limit p (peak: +/- p/2) 
#
#               using Accept/Reject method
#
# 
#==================================================

def generateRandomAngleObservations(n):
    
    p = 42
    x = []
    for i in range(n):
        x.append(2 * p * random.uniform(0,1) - p)
    return x


#==================================================


def getRandomAngleCoulombScatterModel1():

    p = 10
    return 2 * p * random.uniform(0,1) - p


#==================================================


def getPRandomAngleHardScatterModel1():   
    
    # Model: doubleTriangular with theta max = 50 degrees
    
    param_a = 50

    return doubleTriPDF.generateDoubleTriangular(param_a)


#==================================================

"""
def generateAngleModel1(n): # triangular
    print("Making prediction")
    x=[]
    for i in range(n):
        x.append(random.triangular(0,10,6))
    return x
"""
    




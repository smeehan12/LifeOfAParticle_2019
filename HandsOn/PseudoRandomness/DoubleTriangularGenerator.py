import random


def doubleTriangularFunction(xval, a):
    
    # Double triangle, each centered in -a/2 and +a/2, from -a ; a total spread.
    # Peaks at 1/a

    if a < 0:
        print("Can't take negative parameter. Function is centered at zero.")
        return -99
    
    if xval < -a:
        return 0
    
    elif xval >= -a  and xval < -a/2.:
        return 2/(a)**2 * xval + 2/a
    
    elif xval >= -a/2. and xval < 0:
        return -2/(a)**2 * xval 
    
    elif xval >= 0.  and xval < a/2.:
        return 2/(a)**2 * xval 
    
    elif xval >= a/2. and xval < a:
        return -2/(a)**2 * xval + 2/a
   
    elif xval >= a:
        return 0.
    
    else:
        print("Issue with doubleTriangularFunction.")
        return -1.



def getPRandomDoubleTriangular(a, debug=False):

    # Paramater a is the limit of the distribution
    # Thus the PDF goes from -a to a
    # Triangles peak at +/- a/2

    #-----------------------
    # Splash points
    #-----------------------
    # X axis: uniform from -a to a
    # Y axis: uniform from 0  to 1/a

    x_val = 2 * a * random.uniform(0,1) - a
    y_val = random.uniform(0, 1/float(a))

    #-----------------------
    # Check!
    #-----------------------
    #
    #        /\  /\
    #_______/  \/  \________
    #
    #
    # is the random doublet (x_val, y_val) under 
    # the curve f(x_val, a) = doubleTriangularFunction(x_val, a) ?
    
    if debug:
        print("x_val = %.3f\ty_val = %.3f\tf(x_val) = %.3f"%(x_val,y_val,doubleTriangularFunction(x_val, a)))
    
    if y_val <= doubleTriangularFunction(x_val, a):
        return x_val
    else:
        # Call function again:
        return getPRandomDoubleTriangular(a)


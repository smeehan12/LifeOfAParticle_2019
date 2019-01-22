#!/usr/bin/python3

import sys
from pylab import *
import matplotlib.pyplot as plt
import numpy as np

#_________________________________________________________________

# Our little guy:
import toyTracker 

# Color palette to differentiate tracks
colors = cm.Blues(np.linspace(0, 1, 5)) 

#_________________________________________________________________

def getDeflectionWithAngle(angleInDegrees, distanceLayers=1):

    deflection = np.tan(np.deg2rad(angleInDegrees)) * distanceLayers

    return deflection
    
#_________________________________________________________________

def shootTracks(fig, ax, N_layers, n_tracks, param1, param2):

    finalDevs  = []        # storing the track positions on the last layer for all tracks
    
    for t in range(n_tracks):
    
        trackXvals = []   # storing the current track X coordinates
        trackYvals = []   # storing the current track Y corrdinates
        
        # source of particle hits first layer at detector origin
        x0 = 0
        y0 = 0
        
        trackXvals.append(x0)
        trackYvals.append(y0)
        
        for l in range(N_layers - 1):
        
            x_layer = trackXvals[-1]
            y_layer = trackYvals[-1]
            
            deviation = getDeflectionWithAngle(param1) # distance between two layers is set to 1.
            
            # Coordinates on next layer
            y_next = y_layer * (l + 1)
            x_next = x_layer + deviation
            trackYvals.append( y_next )
            trackXvals.append( x_next )
            
            # If on the last layer, store the final deviation
            if l == N_layers - 2:
                finalDevs.append( trackXvals[-1] )
                
        # Done with track, let's plot it!
        ax[0].plot( trackXvals, trackYvals, color=colors[t%len(colors)])
        
        fig.show()
        
        
    return finalDevs
 
#_________________________________________________________________         

def main():
        
    #=======================================
    #            T R A C K E R
    #======================================= 
    
    N_layers     =  15
    minx        = -10.
    maxx        = +10.
    
    #=======================================
    
    if len(sys.argv[1:]) < 3:
    
        print("Need three arguments: \npython " + sys.argv[0] + " NB_TRACKS PARAM1 PARAM2")
        print("Examples:\npython " + sys.argv[0] + "100 5 0")
        sys.exit(2)

    N_tracks =   int(sys.argv[1])    # choose a small number for debugging
    param1   = float(sys.argv[1])    # for now this is the angle (in degree) of deflection
    param2   = float(sys.argv[2])    # boolean to randomize the sign of the deflection (left/right)
    
    print("\nT R A C K E R    S I M U L A T O R")
    print("\nArchitecture:")
    print("\t\tNumber of layers:\t%d layers" % N_layers)
    print("\t\tWidth  of layers:\t%.2f to %.2f" % ( minx, maxx )) 
    
    print("\nYour parameters:")
    print("\t\tNumber of tracks:\t%d" % N_tracks)
    print("\t\tParameter 1:     \t%.2f" % param1)
    print("\t\tParameter 2:     \t%.2f" % param2)
    
    #=========== build the tracker
    
    fig, axarr = toyTracker.buildDetector(N_layers, minx, maxx)
    
    fig.show()  # Comment this line if you want to skip the plotting part
    
    #=========== add tracks
    
    answer  = input("\nReady to shoot particles? [y/n]: \t")
    
    if answer != "y": print("\nNo? Okay, bye.") ; sys.exit(0)
    # 'y' entered:
    
    print("\n=========> releasing particles!")
    
    devValues = shootTracks(fig, axarr, N_layers, N_tracks, param1, param2)
    
    print(devValues)
    
    """
    if fraction != 0:
        shoot(fig, axarr, N_layer, number, fraction)
    else:
        shoot(fig, axarr, N_layer, number)
    """
    
    #plt.show()
    #fig.canvas.draw()

if __name__ == '__main__':

    main()

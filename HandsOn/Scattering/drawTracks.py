#!/usr/bin/python3

import sys
from pylab import *
import matplotlib.pyplot as plt
import numpy as np

#_________________________________________________________________

# Our little guy:
import toyTracker 

# Color palette to differentiate tracks
colors = ['navy', 'blue', 'royalblue', 'deepskyblue', 'skyblue']
font = {'color':  'grey', 'weight': 'normal', 'size': 12}

splitter = "-" * 50

#_________________________________________________________________

def getDeflectionWithAngle(angleInDegrees, distanceLayers=1):

    # Note: distance between two layers is set to 1. 

    deflection = np.tan(np.deg2rad(angleInDegrees)) * distanceLayers

    return deflection
    
#_________________________________________________________________

def shootTracks(fig, ax, N_layers, n_tracks, param1, param2, drawTracks=True):

    finalDevs  = []        # storing the track positions on the last layer for all tracks
    
    for t in range(n_tracks):
    
        trackXvals = []   # storing the current track X coordinates
        trackYvals = []   # storing the current track Y corrdinates
        thetaIvals = []   # storing the incident angle
        
        # source of particle hits first layer at detector origin with incident angle 0
        x0      = 0
        y0      = 0
        theta0  = 0
        
        trackXvals.append(x0)
        trackYvals.append(y0)
        thetaIvals.append(theta0)
        
        for l in range(N_layers):
            
            # Get track coordinate at current layer l
            x_layer = trackXvals[-1]
            y_layer = trackYvals[-1]
            i_theta = thetaIvals[-1]
                       
            # Compute scattering angle to get the deflection at layer 'l + 1'
            
            #===================================================
            #   Dummy case: a zigzag track
            #===================================================  
            
            # Vary the angle by +/- param2 (in percent)
            coeffAngle = 1 - param2/100. * (0.5*(t%5) - 1 ) # you can verify 
            # Get a zigzag:
            new_angle = (-1)**(l%2) * param1 * coeffAngle
            
            if l == 0: # get half the deviation to center our track. Just Claire being picky.
                 new_angle = np.rad2deg(np.arctan(0.5 * np.tan(np.deg2rad(param1*coeffAngle))))

            #===================================================  
            #   Your computation here (and comment above)
            #===================================================  
            
            
            
            #===================================================
            
            # Get the horizontal deviation (deltaX) on next layer:           
            deviation = getDeflectionWithAngle(new_angle)    
                     
            # Store coordinates on next layer
            y_next = y_layer + 1
            x_next = x_layer + deviation
            trackYvals.append( y_next )
            trackXvals.append( x_next )
            thetaIvals.append( new_angle )
            
            # If on the last layer, store the final deviation (for histogramming later)
            if l == N_layers - 1:
                finalDevs.append( x_next )
                
        #----------------------------------------------
        # Done with track, let's plot it!
        #----------------------------------------------
        ax[0].plot( trackXvals, trackYvals, color=colors[t%len(colors)])
        
        #----------------------------------------------
        # Draw and or print info /!\ comment this to speed up
        #----------------------------------------------
        # You don't have to print info on all tracks
        # You can skip some for speeding up the execution of your program
        # See below: if you set skimTrack to 50, you will print info only every 50 tracks
        # For now it is set to 1: we print all track info.
        skimTrack = 1
        if(t%skimTrack==0): 
            print("   Track i = %d\tFinal angle = %.1f\tDefletion = %.3f" %(t, new_angle, x_next))        
        
        if drawTracks:
            fig.canvas.draw()
            plt.pause(1) 
                    

    return finalDevs
 
#_________________________________________________________________         

def main():
        
    #=======================================
    #            T R A C K E R
    #======================================= 
    # Architecture of our tracker: (fixed)
    
    N_layers    =  15
    minx        = -10.
    maxx        = +10.
    
    #=======================================
    #      D E F L E C T I O N   P A D
    #======================================= 
    # Setting graphic properties of distribution
    
    nBins       = 10 
    
    #======================================= 
    
    if len(sys.argv[1:]) < 3:
    
        print("Need three arguments: \npython " + sys.argv[0] + " NB_TRACKS PARAM1 PARAM2")
        print("Examples:\npython " + sys.argv[0] + " 100 5 0")
        sys.exit(2)

    N_tracks =   int(sys.argv[1])    # choose a small number for debugging
    param1   = float(sys.argv[2])    # for now this is the angle (in degree) of deflection
    param2   = float(sys.argv[3])    # boolean to randomize the sign of the deflection (left/right)
    
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
    fig.canvas.draw()
    
    #=========== get the user to check   
    answer  = input("\nReady to shoot particles? [y/n]: \t")   
    if answer != "y": print("\nNo? Okay, bye.") ; sys.exit(0)
        
    #=========== 'y' entered let's shoot all tracks
    print("\n%s\n\t\treleasing particles!\n%s\n" %(splitter, splitter))    
    devValues = shootTracks(fig, axarr, N_layers, N_tracks, param1, param2)
    
    #=========== Plot distribution on deflection plot
    n, binArray, patches = axarr[1].hist(devValues, nBins, histtype='bar', color='royalblue', alpha=0.75)
    maxHist = axarr[1].get_ylim()[1]
    axarr[1].text(-0.95*maxx, maxHist*0.85, '%d tracks'%(N_tracks), fontdict=font)
    fig.canvas.draw()
    
    #============ Done, now print info 
    # Exercise:
    # Add another text info on this plot 
    # that shows the average and standard deviation 
    # of the list devValues (try to compute yourself
    # or look up functions doing it)
    
    #===================================
    
    quit = input("\nQuit tracker simulator [press any key] ")
    

if __name__ == '__main__':

    main()

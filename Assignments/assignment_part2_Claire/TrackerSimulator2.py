import numpy as np
import random
import DoubleTriangularGenerator as DTG

#==================================================================
# Function to get the deflection for a given angle:
# Just trigonometry here.

def getDeflectionWithAngle(angleInDegrees, distanceLayers=1):

    deflection = np.tan(np.deg2rad(angleInDegrees)) * distanceLayers

    return deflection

#==================================================================

def getDeflectionsAllTracks( nLayersTK, N_tracks, p1, p2, p3 ):

    finalDevs     = []
    finalDevsCS   = []
    finalDevsHC   = []
    
    # Loop over tracks:
    for t in range(N_tracks):
                
        # For current track:
        track_xVals = []   # storing the current track X coordinates
        track_yVals = []   # storing the current track Y corrdinates
        
        # source of particle hits first layer at detector origin with incident angle 0
        x0      = 0
        y0      = 0

        track_xVals.append(x0)
        track_yVals.append(y0)
        
        isHS = False # by default tracks are small-angle scattering        
        
        # Looping of layers:
        for l in range(nLayersTK):

            # Get track coordinate at current layer l
            x_layer = track_xVals[-1]
            y_layer = track_yVals[-1]

            #------------------------------------
            # Hard scattering process
            #------------------------------------
            # let's get a random number from 0 and 1 and see if it falls below p3:
            if random.uniform(0,1) < p3:
                # Hard scattering:
                new_angle = DTG.getPRandomDoubleTriangular(p2)
                isHS = True

            #------------------------------------
            # Coulomb multiple scattering
            #------------------------------------
            else: # Coulomb
                new_angle = 2 * p1 * random.uniform(0 , 1) - p1
            
            #------------------------------------
            
            # Compute the horizontal deviation (deltaX) on next layer: 
            deviation = getDeflectionWithAngle(new_angle)

            # Store coordinates on next layer
            y_next = y_layer + 1
            x_next = x_layer + deviation
            track_yVals.append( y_next )
            track_xVals.append( x_next )

            # If on the last layer, store the final deviation (for histogramming later)
            if l == nLayersTK - 1:
                if isHS:
                    finalDevsHS.append( x_next)
                else:
                    finalDevsCS.append( x_next)
                finalDevs.append( x_next )
        
        # Done with the current track in all layers!
        
    # Done with all tracks!

    # Returning the total, CS and HS deflections:
    return finalDevs, finalDevsCS, finalDevsHS

#==================================================================


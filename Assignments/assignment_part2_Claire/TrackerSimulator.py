import numpy as np
import random


#==================================================================
# Function to get the deflection for a given angle:
# Just trigonometry here.

def getDeflectionWithAngle(angleInDegrees, distanceLayers=1):

    deflection = np.tan(np.deg2rad(angleInDegrees)) * distanceLayers

    return deflection

#==================================================================

def getDeflectionsAllTracksCoulomb( nLayersTK, N_tracks, theta_max ):

    finalDevs   = []
    
    # Loop over tracks:
    for t in range(N_tracks):
                
        # For current track:
        track_xVals = []   # storing the current track X coordinates
        track_yVals = []   # storing the current track Y corrdinates
        track_tVals = []   # storing the incident angle
        
        # source of particle hits first layer at detector origin with incident angle 0
        x0      = 0
        y0      = 0
        theta0  = 0

        track_xVals.append(x0)
        track_yVals.append(y0)
        track_tVals.append(theta0)
        
        # Looping of layers:
        for l in range(nLayersTK):

            # Get track coordinate at current layer l
            x_layer = track_xVals[-1]
            y_layer = track_yVals[-1]
            i_theta = track_tVals[-1]

            # Compute scattering angle to get the deflection at layer 'l + 1' 
            new_angle = 2 * theta_max * random.uniform(0 , 1) - theta_max
            
            # Compute the horizontal deviation (deltaX) on next layer: 
            deviation = getDeflectionWithAngle(new_angle)

            # Store coordinates on next layer
            y_next = y_layer + 1
            x_next = x_layer + deviation
            track_yVals.append( y_next )
            track_xVals.append( x_next )
            track_tVals.append( new_angle )

            # If on the last layer, store the final deviation (for histogramming later)
            if l == nLayersTK - 1:
                finalDevs.append( x_next )
        
        # Done with the current track in all layers!
        
    # Done with all tracks!
    
    # Returning the deflections:
    return finalDevs

#==================================================================


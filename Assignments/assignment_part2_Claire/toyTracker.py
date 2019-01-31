from pylab import *
import matplotlib.pyplot as plt
import matplotlib.pyplot as mpl
import numpy as np

mpl.rcParams['lines.linewidth'] = 1


#==============================================================

def buildDetector(n_layers, minx, maxx):

    if n_layers < 1:
        print("Our tracker cannot have less than 1 layer! Exiting program.")
        sys.exit(0)

    # Defining a figure with two axis arrays (axarr) 
    fig, axarr = plt.subplots(nrows=2, ncols=1, sharex=True,
        gridspec_kw = {'height_ratios':[3, 1]}, figsize=(12, 10))

    # Background color is white
    fig.set_facecolor('w')

    # Title of the canvas
    axarr[0].set_title('Toy Tracker')

    # Define x and y axis, the latter starts from top left
    axarr[0].set_ylabel('Layers')
    axarr[0].axis([minx, maxx, -0.7, n_layers])
    axarr[0].invert_yaxis()
    axarr[0].yaxis.set_major_locator(MaxNLocator(integer=True))
    axarr[1].set_ylabel('Number of tracks')
    axarr[1].set_xlabel('Deflection on the last layer')

    # Drawing the horizontal pixel layers from top (layer 0) to bottom:
    for iline in range(n_layers):
        axarr[0].axhline(y=iline, xmin=0, xmax=1, color='darkgrey', linestyle='dashed', lw=2)

    # Drawing the vertical middle line
    axarr[0].axvline(x=0, ymin=0,ymax=1, color='grey', linestyle='dotted')
    axarr[1].axvline(x=0, ymin=0,ymax=1, color='grey', linestyle='dotted')

    # Drawing incident track: vertical and hitting first layer at (0,0)
    initTrackX = [0,0]
    initTrackY = [-1,0]
    
    axarr[0].plot(initTrackX, initTrackY, c='dodgerblue')

    fig.tight_layout()
    
    return fig, axarr

#==============================================================

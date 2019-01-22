#!/usr/bin/python3

from pylab import *
import matplotlib.pyplot as plt
import matplotlib.pyplot as mpl

mpl.rcParams['lines.linewidth'] = 1

def buildDetector(n_layers, minx, maxx):
    
    # Defining a figure with two axis arrays (axarr) 
    fig, axarr = plt.subplots(nrows=2, ncols=1, sharex=True, gridspec_kw = {'height_ratios':[3, 1]}, figsize=(5,10))

    # Background color is white
    fig.set_facecolor('w')
    
    # Title of the canvas
    axarr[0].set_title('Toy Tracker')

    # Define x and y axis, the latter starts from top left
    axarr[0].set_ylabel('Layers')
    axarr[0].axis([minx, maxx, 0, n_layers])
    axarr[0].invert_yaxis()
    axarr[1].set_ylabel('Number of tracks')
    
    # Drawing the horizontal pixel layers from top (layer 0) to bottom:
    for iline in range(n_layers):
        axarr[0].axhline(y=iline, xmin=0, xmax=1, color='grey', linestyle='dotted')
        
    # Drawing the vertical middle line
    axarr[0].axvline(x=0, ymin=0,ymax=1, color='grey', linestyle='dotted')
    axarr[1].axvline(x=0, ymin=0,ymax=1, color='grey', linestyle='dotted')
    
    fig.tight_layout()
    
    return fig, axarr


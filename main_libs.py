from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import sys
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage
import glob
import moviepy.editor as mpy
from PIL import Image
import os
import random
globaltime = np.arange(0,30,0.01)     #  On donne un temps global pour ne pas se confondre dans les methodes. 
                                      #  On peut modifier les valeur si necessaire.





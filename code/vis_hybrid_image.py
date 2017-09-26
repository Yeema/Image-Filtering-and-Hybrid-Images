import numpy as np
from scipy.misc import imresize

def vis_hybrid_image(hybrid_image):
    #visualize a hybrid image by progressively downsampling the image and
    #concatenating all of the images together.

    scales = 5 #how many downsampled versions to create
    scale_factor = 0.5 #how much to downsample each time
    padding = 5 #how many pixels to pad.
    
    original_height = hybrid_image.shape[0]
    num_colors = hybrid_image.shape[2] #counting how many color channels the input has
    output = hybrid_image[:]
    cur_image = hybrid_image[:]
    
    for i in range(1,scales):
        #add padding
        output = np.concatenate((output, np.ones((original_height, padding, num_colors))), axis=1)
        
        #dowsample image;
        cur_image = imresize(cur_image, scale_factor, 'bilinear').astype(np.float)/255
        #pad the top and append to the output
        tmp = np.concatenate((np.ones((original_height-cur_image.shape[0],cur_image.shape[1],num_colors)), cur_image), axis=0)
        output = np.concatenate((output,tmp), axis=1)        
  
    return output

# Your Name <span style="color:red">(your cs id)</span>
賴怡惠 103011105
# Project 1 / Image Filtering and Hybrid Images

## Overview
The project is related to 
> The main idea of implementing my_filter.py is doing convolution for each pixel.
> Numpy provides many useful compuational functions which helps simplify my code and make it more readable.  

## Implementation
1. proj1.py
	* follow the steps in the comment:
	> Remove the high frequencies from image1 by blurring it. The amount of blur that works best will vary with different image pairs
	```
		low_frequencies = my_imfilter(image1, gaussian_filter)
	```
	> remove the low frequencies from image2. The easiest way to do this is to subtract a blurred version of image2 from the original version of image2. This will give you an image centered at zero with negative values.
	```
		high_frequencies = image2 - my_imfilter(image2, gaussian_filter)
	```
	> Combine the high frequencies and low frequencies
	```
		hybrid_image = low_frequencies+high_frequencies
	```
	* most tricky and easily forget:
	> use normalize function which has provided by TA in ../code
	```
		plt.imshow(normalize(low_frequencies))
		plt.imshow(normalize(high_frequencies+0.5))
		plt.imshow(normalize(vis))
		plt.imsave(main_path+'/results/low_frequencies_mouse_bear.png', normalize(low_frequencies), 'quality', 95)
		plt.imsave(main_path+'/results/high_frequencies_mouse_bear.png', normalize(high_frequencies+0.5), 'quality', 95)
		plt.imsave(main_path+'/results/hybrid_image_mouse_bear.png', normalize(hybrid_image), 'quality', 95)
		plt.imsave(main_path+'/results/hybrid_image_scales_mouse_bear.png', normalize(vis), 'quality', 95)
	```
2. my_filter.py

```
Code highlights
```

## Installation
* Other required packages.
import numpy as np in my_filter.py
* How to compile from source?
open a terminal in the folder homework1 and type "python proj1.py" in the command line 

### Results

<table border=1>
<col width="25%">
<col width="25%">
<col width="25%">
<col width="25%">
<tr>
    <th>low frequencies</th>
    <th>high frequencies</th> 
    <th>hybrid image</th>
    <th>hybrid image scales</th>
</tr>
<tr>
<td>
<img src="low_frequencies.png" width="100%"/>
</td>
<td>
<img src="high_frequencies.png"  width="100%"/>
</td>
<td>
<img src="hybrid_image.png" width="100%"/>
</td>
<td>
<img src="hybrid_image_scales.png" width="100%"/>
</td>
</tr>

<tr>
<td>
<img src="low_frequencies_einstein_marilyn.png" width="100%"/>
</td>
<td>
<img src="high_frequencies_einstein_marilyn.png"  width="100%"/>
</td>
<td>
<img src="hybrid_image_einstein_marilyn.png" width="100%"/>
</td>
<td>
<img src="hybrid_image_scales_einstein_marilyn.png" width="100%"/>
</td>
</tr>

<tr>
<td>
<img src="low_frequencies_submarine_fish.png" width="100%"/>
</td>
<td>
<img src="high_frequencies_submarine_fish.png"  width="100%"/>
</td>
<td>
<img src="hybrid_image_submarine_fish.png" width="100%"/>
</td>
<td>
<img src="hybrid_image_scales_submarine_fish.png" width="100%"/>
</td>
</tr>

<tr>
<td>
<img src="low_frequencies_bicycle_motorcycle.png" width="100%"/>
</td>
<td>
<img src="high_frequencies_bicycle_motorcycle.png"  width="100%"/>
</td>
<td>
<img src="hybrid_image_bicycle_motorcycle.png" width="100%"/>
</td>
<td>
<img src="hybrid_image_scales_bicycle_motorcycle.png" width="100%"/>
</td>
</tr>

<tr>
<td>
<img src="low_frequencies_plane_bird.png" width="100%"/>
</td>
<td>
<img src="high_frequencies_plane_bird.png"  width="100%"/>
</td>
<td>
<img src="hybrid_image_plane_bird.png" width="100%"/>
</td>
<td>
<img src="hybrid_image_scales_plane_bird.png" width="100%"/>
</td>
</tr>
</table>

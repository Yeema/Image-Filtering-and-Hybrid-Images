#this script has test cases to help you test my_imfilter() which you will
#write. You should verify that you get reasonable output here before using
#your filtering to construct a hybrid image in proj1.m. The outputs are
#all saved and you can include them in your writeup. You can add calls to
#imfilter() if you want to check that my_imfilter() is doing something
#similar.



from gauss2D import gauss2D
from my_imfilter import my_imfilter
from normalize import normalize
from scipy.misc import imresize
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os

''' set up '''
main_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
img_path = main_path + '/data/cat.bmp'
test_image = mpimg.imread(img_path)
test_image = imresize(test_image,0.7,'bilinear')
test_image = test_image.astype(np.single)/255
plt.figure('Image')
plt.imshow(test_image)


''' Identify filter '''
# This filter should do nothing regardless of the padding method you use.
identity_filter = np.array([[0,0,0], [0,1,0], [0,0,0]], dtype=np.single)
identity_image  = my_imfilter(test_image, identity_filter);
plt.figure('Identity')
plt.imshow(identity_image)


''' Small blur with a box filter '''
# This filter should remove some high frequencies
blur_filter = np.array([[1,1,1], [1,1,1], [1,1,1]])
blur_filter = blur_filter.astype(np.float) / np.sum(blur_filter);  # making the filter sum to 1
blur_image = my_imfilter(test_image, blur_filter)
plt.figure('Box filter')
plt.imshow(normalize(blur_image))
plt.imsave(main_path+'/results/blur_image.png', normalize(blur_image + 0.5), 'quality', 95);

''' Large blur '''
#This blur would be slow to do directly, so we instead use the fact that
#Gaussian blurs are separable and blur sequentially in each direction.
large_2d_blur_filter = gauss2D(shape=(25,25), sigma = 10)
large_blur_image = my_imfilter(test_image, large_2d_blur_filter);
plt.figure('Gauss filter')
plt.imshow(normalize(large_blur_image))
plt.imsave(main_path+'/results/large_blur_image.png', normalize(large_blur_image + 0.5), 'quality', 95);


''' Oriented filter (Sobel Operator) '''
sobel_filter = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
sobel_image = my_imfilter(test_image, sobel_filter);

#0.5 added because the output image is centered around zero otherwise and mostly black
plt.figure('Sobel filter')
plt.imshow(normalize(sobel_image+0.5))
plt.imsave(main_path+'/results/sobel_image.png', normalize(sobel_image + 0.5), 'quality', 95);


''' High pass filter (Discrete Laplacian) '''
laplacian_filter = np.array([[0,1,0], [1,-4,1], [0,1,0]])
laplacian_image = my_imfilter(test_image, laplacian_filter);

#0.5 added because the output image is centered around zero otherwise and mostly black
plt.figure('Laplacian filter')
plt.imshow(normalize(laplacian_image+0.5))
plt.imsave(main_path+'/results/laplacian_image.png', normalize(laplacian_image + 0.5), 'quality', 95);


''' High pass "filter" alternative '''
high_pass_image = test_image - blur_image; #simply subtract the low frequency content

plt.figure('High pass filter')
plt.imshow(normalize(high_pass_image+0.5))
plt.imsave(main_path+'/results/high_pass_image.png', normalize(high_pass_image + 0.5), 'quality', 95);
plt.show()

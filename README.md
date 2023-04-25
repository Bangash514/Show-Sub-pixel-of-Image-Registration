# Show-Sub-pixel-of-Image-Registration

Algorithm Description::
Sub-pixel image registration is a technique that enables the alignment of two or more images with high accuracy. It involves finding the precise alignment of the images at sub-pixel level. In C++, you can achieve sub-pixel image registration using the OpenCV library. Here is an example of how to perform sub-pixel image registration using OpenCV in C++:
In this example, we first load two images and convert them to grayscale. We then define a search range for sub-pixel registration and an initial guess for the registration. We perform sub-pixel registration using the phaseCorrelate function of OpenCV, which uses the phase correlation method. Finally, we add the sub-pixel offset to the initial guess to obtain the final registration result, which is displayed in the console.

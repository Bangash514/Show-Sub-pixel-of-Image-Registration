
//Created by; Bangash Software Engineer, SIAT CAS Shenzhen China
#include <opencv2/opencv.hpp>

using namespace cv;

int main()
{
    // Load the images to be registered
    Mat image1 = imread("image1.jpg");
    Mat image2 = imread("image2.jpg");

    // Convert the images to grayscale
    Mat gray1, gray2;
    cvtColor(image1, gray1, COLOR_BGR2GRAY);
    cvtColor(image2, gray2, COLOR_BGR2GRAY);

    // Define the search range for sub-pixel registration
    Rect searchRange(5, 5, gray1.cols - 10, gray1.rows - 10);

    // Define the initial guess for registration
    Point2f initialGuess(0, 0);

    // Perform sub-pixel registration using phase correlation method
    Point2f subPixelOffset = phaseCorrelate(gray1(searchRange), gray2(searchRange), noArray(), CV_HAL_BORDER_REFLECT101);

    // Add the sub-pixel offset to the initial guess to obtain the final registration result
    Point2f registrationResult = initialGuess + subPixelOffset;

    // Display the registration result
    std::cout << "Registration result: " << registrationResult << std::endl;

    return 0;
}

#include "opencv/highgui.h"
#include<iostream>
#include "opencv2/imgproc/imgproc.hpp"
//#include "Edges.hpp"
 
using namespace std;
using namespace cv;
 
int main(int, char**)
{
    VideoCapture cap(0); // open the default camera
    if (!cap.isOpened())  // check if we succeeded
        return -1;
    for (;;)
    {
        Mat frame,edges;
        cap >> frame; // get a new frame from camera
        cvtColor(frame,edges, COLOR_BGR2GRAY);
        GaussianBlur(edges, edges, Size(7, 7), 1.5, 1.5);
        Canny(edges, edges, 0, 30, 3);
        imshow("Webcam feed", frame);
        if (waitKey(30) >= 0) break;
    }
    // the camera will be deinitialized automatically in VideoCapture destructor

    return 0;
}

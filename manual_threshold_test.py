#importing OpevCV to be able to manipulte the images
import cv2 as cv

#Initializing HSV upper and lower range values
max_value = 255
max_value_H = 360//2
low_H = 0
low_S = 0
low_V = 0
high_H = max_value_H
high_S = max_value
high_V = max_value

#Initializing names to go on the track bars
low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'
high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'

#Initializing window names 
window_capture_name = 'HSV Image'
window_detection_name = 'HSV Image Filtered'

def on_low_H_thresh_trackbar(val):
    """_summary_
    Function created to be intputed into cv.createTrackbar(). Function is called everytime slider position changes on trackbar and 
    ensures the low_H value cannot be greater than or equal to the high_H value.
    Args:
        val (int): position of slider on trackbar
    """
    global low_H
    global high_H
    low_H = val
    low_H = min(high_H-1, low_H)
    cv.setTrackbarPos(low_H_name, window_detection_name, low_H)
    
def on_high_H_thresh_trackbar(val):
    """_summary_
    Function created to be intputed into cv.createTrackbar(). Function is called everytime slider position changes on trackbar and 
    ensures the high_H value cannot be less than or equal to the low_H value.
    Args:
        val (int): position of slider on trackbar
    """
    global low_H
    global high_H
    high_H = val
    high_H = max(high_H, low_H+1)
    cv.setTrackbarPos(high_H_name, window_detection_name, high_H)
    
def on_low_S_thresh_trackbar(val):
    """_summary_
    Function created to be intputed into cv.createTrackbar(). Function is called everytime slider position changes on trackbar and 
    ensures the low_S value cannot be greater than or equal to the high_S value.
    Args:
        val (int): position of slider on trackbar
    """    
    global low_S
    global high_S
    low_S = val
    low_S = min(high_S-1, low_S)
    cv.setTrackbarPos(low_S_name, window_detection_name, low_S)
    
def on_high_S_thresh_trackbar(val):
    """_summary_
    Function created to be intputed into cv.createTrackbar(). Function is called everytime slider position changes on trackbar and 
    ensures the high_S value cannot be less than or equal to the low_S value.
    Args:
        val (int): position of slider on trackbar
    """
    global low_S
    global high_S
    high_S = val
    high_S = max(high_S, low_S+1)
    cv.setTrackbarPos(high_S_name, window_detection_name, high_S)
    
def on_low_V_thresh_trackbar(val):
    """_summary_
    Function created to be intputed into cv.createTrackbar(). Function is called everytime slider position changes on trackbar and 
    ensures the low_V value cannot be greater than or equal to the high_V value. 
    Args:
        val (int): position of slider on trackbar
    """    
    global low_V
    global high_V
    low_V = val
    low_V = min(high_V-1, low_V)
    cv.setTrackbarPos(low_V_name, window_detection_name, low_V)
    
def on_high_V_thresh_trackbar(val):
    """_summary_
    Function created to be intputed into cv.createTrackbar(). Function is called everytime slider position changes on trackbar and 
    ensures the high_V value cannot be less than or equal to the low_V value.
    Args:
        val (int): position of slider on trackbar
    """
    global low_V
    global high_V
    high_V = val
    high_V = max(high_V, low_V+1)
    cv.setTrackbarPos(high_V_name, window_detection_name, high_V)
    
#Naming the 2 windows that will be used to observe the images
cv.namedWindow(window_capture_name)
cv.namedWindow(window_detection_name)


#Creating trackbar for upper and lower limit of HSV pixel thresholding
cv.createTrackbar(low_H_name, window_detection_name , low_H, max_value_H, on_low_H_thresh_trackbar)
cv.createTrackbar(high_H_name, window_detection_name , high_H, max_value_H, on_high_H_thresh_trackbar)
cv.createTrackbar(low_S_name, window_detection_name , low_S, max_value, on_low_S_thresh_trackbar)
cv.createTrackbar(high_S_name, window_detection_name , high_S, max_value, on_high_S_thresh_trackbar)
cv.createTrackbar(low_V_name, window_detection_name , low_V, max_value, on_low_V_thresh_trackbar)
cv.createTrackbar(high_V_name, window_detection_name , high_V, max_value, on_high_V_thresh_trackbar)

#Reading a specific image
image = cv.imread(r'C:\Users\alaah\OneDrive\Desktop\aUtoronto-Application\2018Proj1_train\7.2.png')

#converting image into HSV from BGR and manually moving slider to change value of upper 
# and lower HSV limit to observe which changes create the best mask for each barrel in each image
while True:
    hsvimage = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    thresholdimage = cv.inRange(hsvimage, (low_H, low_S, low_V), (high_H, high_S, high_V))
    cv.imshow(window_capture_name, hsvimage)
    cv.imshow(window_detection_name, thresholdimage)
    
    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break
    
#saving upper and lower ranges of HSV values to a txt file to be used later on
hsv_values = open(r"C:\Users\alaah\OneDrive\Desktop\aUtoronto-Application\hsv_values.txt","a")
hsv_text = "\n{},{},{},{},{},{}".format(low_H, low_S, low_V,high_H, high_S, high_V)
hsv_values.write(hsv_text)
hsv_values.close()
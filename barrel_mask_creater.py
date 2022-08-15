#importing OpevCV to be able to manipulte the images
import cv2 as cv
#importing os to know the names and root location for all the images
import os

#initializing HSV upper and lower limit 
low_H = 0
low_S = 0
low_V = 0
high_H = 0
high_S = 0
high_V = 0
lin_num = 0 

#Defining location of images and output
directory = r"C:\Users\alaah\OneDrive\Desktop\aUtoronto-Application\2018Proj1_train"
output = r"C:\Users\alaah\OneDrive\Desktop\aUtoronto-Application\output"

#iterates through txt file and sums all the values of each HSV upper and lower limit 
with open(r"C:\Users\alaah\OneDrive\Desktop\aUtoronto-Application\hsv_values.txt","r") as hsv_txt:
            for line in hsv_txt:
                currentline = line.split(",")
                low_H += int(currentline[0])
                low_S += int(currentline[1])
                low_V += int(currentline[2])
                high_H += int(currentline[3])
                high_S += int(currentline[4])
                high_V += int(currentline[5])
                lin_num+=1


#Finds the average value of each limit 
low_H = low_H/lin_num
low_S = low_S/lin_num
low_V = low_V/lin_num
high_H = high_H/lin_num
high_S = high_S/lin_num
high_V = high_V/lin_num

#iterates through folder and extracts image file name and root location
for root, subdirectories, files in os.walk(directory):
    for file in files:
        os.path.join(root, file)
        
        #image is converted to hsv 
        image = cv.imread(os.path.join(root, file))
        hsvimage = cv.cvtColor(image, cv.COLOR_BGR2HSV)
        
        #threshold limit placed on hsv based on average upper and lower limit for hue
        thresholdimage = cv.inRange(hsvimage, (low_H, 0, 0), (high_H, 255, 255))
        
        #extracts file name 
        file_name = os.path.splitext(file)[0]
        
        output_image_directory = "{}\{}_mask.png".format(output,file_name)
        #saves image mask as "imagename_mask" in the output folder
        output_image = cv.imwrite(output_image_directory,thresholdimage)
        

import numpy as np
import cv2
import json

img1 = input("Enter the location of your ID: ") 
image = cv2.imread(img1)
template0 = cv2.imread('C:/Users/rowelfacunla/Desktop/ID_sets/ID_Checker/nbi_left.png')
template1 = cv2.imread('C:/Users/rowelfacunla/Desktop/ID_sets/ID_Checker/nbi_center.png')
template2 = cv2.imread('C:/Users/rowelfacunla/Desktop/ID_sets/ID_Checker/nbi_right.png')
template3 = cv2.imread('C:/Users/rowelfacunla/Desktop/ID_sets/ID_Checker/pagibig_left.png')
template4 = cv2.imread('C:/Users/rowelfacunla/Desktop/ID_sets/ID_Checker/pagibig_center.png')
template5 = cv2.imread('C:/Users/rowelfacunla/Desktop/ID_sets/ID_Checker/pagibig_bottom.png')
template6 = cv2.imread('C:/Users/rowelfacunla/Desktop/ID_sets/ID_Checker/philhealth.png')
 
image = cv2.resize(image, (0,0), fx=0.5, fy=0.5)
template0 = cv2.resize(template0, (0,0), fx=0.5, fy=0.5)
template1 = cv2.resize(template1, (0,0), fx=0.5, fy=0.5)
template2 = cv2.resize(template2, (0,0), fx=0.5, fy=0.5)
template3 = cv2.resize(template3, (0,0), fx=0.5, fy=0.5)
template4 = cv2.resize(template4, (0,0), fx=0.5, fy=0.5)
template5 = cv2.resize(template5, (0,0), fx=0.5, fy=0.5)
template6 = cv2.resize(template6, (0,0), fx=0.5, fy=0.5) 
 
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray0 = cv2.cvtColor(template0, cv2.COLOR_BGR2GRAY)
templateGray1 = cv2.cvtColor(template1, cv2.COLOR_BGR2GRAY)
templateGray2 = cv2.cvtColor(template2, cv2.COLOR_BGR2GRAY)
templateGray3 = cv2.cvtColor(template3, cv2.COLOR_BGR2GRAY)
templateGray4 = cv2.cvtColor(template4, cv2.COLOR_BGR2GRAY)
templateGray5 = cv2.cvtColor(template5, cv2.COLOR_BGR2GRAY)
templateGray6 = cv2.cvtColor(template6, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(imageGray,templateGray0, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left0 = max_loc
h,w = templateGray0.shape
bottom_right = (top_left0[0] + w, top_left0[1] + h)
cv2.rectangle(image,top_left0, bottom_right,(0,0,255),4)

result = cv2.matchTemplate(imageGray,templateGray1, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left1 = max_loc
h,w = templateGray1.shape
bottom_right = (top_left1[0] + w, top_left1[1] + h)
cv2.rectangle(image,top_left1, bottom_right,(0,0,255),4)

result = cv2.matchTemplate(imageGray,templateGray2, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left2 = max_loc
h,w = templateGray2.shape
bottom_right = (top_left2[0] + w, top_left2[1] + h)
cv2.rectangle(image,top_left2, bottom_right,(0,0,255),4)

result = cv2.matchTemplate(imageGray,templateGray3, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left3 = max_loc
h,w = templateGray3.shape
bottom_right = (top_left3[0] + w, top_left3[1] + h)
cv2.rectangle(image,top_left3, bottom_right,(0,0,255),4)

result = cv2.matchTemplate(imageGray,templateGray4, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left4 = max_loc
h,w = templateGray4.shape
bottom_right = (top_left4[0] + w, top_left4[1] + h)
cv2.rectangle(image,top_left4, bottom_right,(0,0,255),4)

result = cv2.matchTemplate(imageGray,templateGray5, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left5 = max_loc
h,w = templateGray5.shape
bottom_right = (top_left5[0] + w, top_left5[1] + h)
cv2.rectangle(image,top_left5, bottom_right,(0,0,255),4)

result = cv2.matchTemplate(imageGray,templateGray6, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left6 = max_loc
h,w = templateGray6.shape
bottom_right = (top_left6[0] + w, top_left6[1] + h)
cv2.rectangle(image,top_left6, bottom_right,(0,0,255),4)

cv2.imshow("Result", image)

if (top_left0[0] == 21) & (top_left0[1] == 1) & (top_left1[0] == 106) & (top_left1[1] == 1) & (top_left2[0] == 302) & (top_left2[1] == 28):
    data = 'NBI ID'

elif (top_left3[0] == 15) & (top_left3[1] == 13) & (top_left4[0] == 45) & (top_left4[1] == 14) & (top_left5[0] == 11) & (top_left5[1] == 131):
    data = 'Pag-IBIG ID'
        
elif (top_left6[0] == 14) & (top_left6[1] == 10):
    data = 'PhilHealth ID'

else:
    data = 'Invalid ID'

with open('C:/Users/rowelfacunla/Desktop/data.json', 'w') as outfile:
    json.dump(data, outfile, sort_keys = True)
 
cv2.waitKey(0)

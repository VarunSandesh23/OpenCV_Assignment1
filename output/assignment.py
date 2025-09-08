import cv2

# Phase 1

# 1 OpenCV Version
print("OpenCV version: ", cv2.__version__)

# 2 read the image and display it
img = cv2.imread('luffy2.jpg')
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3 save the image to grayscale
grayscale_img = cv2.imread("luffy2.jpg", 0)
cv2.imwrite('luffy_grayscale.jpg',grayscale_img)
cv2.imshow("grayscale_image", grayscale_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4 print the image dimensions (height, width, number of channels)
h, w, c = img.shape
print("Height: ", h)
print("Width: ", w)
print("Channels: ", c)



# Phase 2 


# 5 Resize the image to half of the original size
resized_image = cv2.resize(img, (w//2, h//2))
cv2.imshow("Resized_image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6 cropping the image 
cropped_image = img[0:200, 100:200]
cv2.imshow("Cropped Image", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 7 rotate the image by 90 degrees clockwise
center = (w//2, h//2)
matrix = cv2.getRotationMatrix2D(center,-90, 1)
rotated_img = cv2.warpAffine(img, matrix, (w,h))
cv2.imshow("rotated_image", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 8 flip the image horizantally
flipped_img = cv2.flip(img, 1)
cv2.imshow("Flipped Image", flipped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 9 saving the files 
cv2.imwrite('resized.jpg',resized_image)
cv2.imwrite('cropped.jpg',cropped_image)
cv2.imwrite('rotated.jpg',rotated_img)
cv2.imwrite('flipped.jpg',flipped_img)


# Phase 3


# 10

# Drawing the blue rectangle
rectangle_img = cv2.imread('luffy2.jpg')
pt1 = (100,100)
pt2 = (300,300)
color = (255, 0 , 0)
thickness = 1
cv2.rectangle(rectangle_img,pt1,pt2,color,thickness)
cv2.imshow('rectangle',rectangle_img)
cv2.imwrite('rectangle.jpg',rectangle_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Drawing the red circle in the blue rectangle of the image
circle_img = cv2.imread('rectangle.jpg')
pt = (200,200)
radius = 75
color = (0, 0, 255)
thickness = 1
cv2.circle(circle_img,pt,radius,color, thickness)
cv2.imshow('circle',circle_img)
cv2.imwrite('circle.jpg',circle_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Drawing the green line across the image
line_img = cv2.imread('circle.jpg')
pt1 = (0,0)
pt2 = (500, 500)
color = (0, 255, 0)
thickness = 1
cv2.line(line_img,pt1,pt2,color,thickness)
cv2.imshow('diagonal_line', line_img)
cv2.imwrite('diagonal.jpg',line_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Writing the text at the bottom of the image
text_img = cv2.imread('diagonal.jpg')
text = 'Varun Sandesh'
font = cv2.FONT_HERSHEY_SIMPLEX
size = 1
position = (250,500)
color = (255, 0, 0)
thickness = 1
cv2.putText(text_img, text, position, font, size, color, thickness)
cv2.imshow('text_image', text_img)
cv2.imwrite('text.jpg',text_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 11 On the original image, overlay the text *“OpenCV Assignment”* at the top.

original_img = cv2.imread('luffy2.jpg')
text = "OpenCV Assignment"
font = cv2.FONT_HERSHEY_SIMPLEX
size = 1
position = (100,25)
color = (255, 0, 0)
thickness = 1
cv2.putText(original_img, text, position, font, size, color, thickness)
cv2.imshow('text1_image', original_img)
cv2.imwrite('text1.jpg',original_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
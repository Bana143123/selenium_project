import cv2

# Read an image
image = cv2.imread('example.jpg')

# Display the image
cv2.imshow('Narendra', image)
resized=cv2.resize(image,(700,500))
cv2.imshow("resize",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
grey=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale image",grey)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("greyscale.jpg",grey)
print("image saved successfully")


# Draw a rectangle on the image
rectangle_image = image.copy()
cv2.rectangle(rectangle_image, (50, 50), (200, 200), (0, 255, 0), 3)

# Display the image with the rectangle
cv2.imshow('Rectangle', rectangle_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Display the blurred image
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Detect edges using Canny
edges = cv2.Canny(image, 100, 200)

# Display the edges
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2

# Function to apply grayscale filter to an image
def grayscale_filter(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

# Function to apply blur filter to an image
def blur_filter(image):
    blurred = cv2.GaussianBlur(image, (25, 25), 0)
    return blurred

# Function to apply edge detection filter to an image
def edge_detection_filter(image):
    edges = cv2.Canny(image, 100, 200)
    return edges

# Load an image from the file system
image = cv2.imread("image.jpg")

# Apply grayscale filter to the image
grayscale = grayscale_filter(image)

# Apply blur filter to the image
blurred = blur_filter(image)

# Apply edge detection filter to the image
edges = edge_detection_filter(image)

# Display the original image, grayscale image, blurred image, and edges image
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", grayscale)
cv2.imshow("Blurred Image", blurred)
cv2.imshow("Edges Image", edges)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

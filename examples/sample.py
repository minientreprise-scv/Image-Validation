from plantImageValidation import ValidPlantDetector  # Import the only class
import cv2  # To read and check qr content

# The ValidPlantDetector is looking for a QR code in the image.
# If a QR code is found it execute the provided function (here check_qr_content).
# This function can read and check the content of the QR code...


def check_qr_content(image):
    reader = cv2.QRCodeDetector()
    value, _, _ = reader.detectAndDecode(image)
    return value.startswith('https://server.camarm.fr')


detector = ValidPlantDetector(check_qr_content)

image_path = "examples/test2.jpeg"
image = cv2.imread(image_path)

valid_image = detector(image)

if valid_image:
    print(f"Image '{image_path}' is a valid image")
    exit()
print(f"Image '{image_path}' is not a valid image")
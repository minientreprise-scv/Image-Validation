# Does this image contain a photo of a Une e-plant pot ?
It's the question that this python package can answer. 
This package identify if the photo is valid to be uploaded.  

This repository is part of minientreprise-csv 's project. It provides a python package that say if the provided image is valid and can be uploaded.

## How it works
The scrip look for a QR code in the image. In a second check it verify if this QR code is provided by Une E Plante.

1. The script is looking for QR code in provided image.
2. If a QR is found, it crop the image to see just the QR.
3. It reads the content of the QR.
4. It verifies if it's a valid content.

## Examples

![](examples/test.jpeg)

```
Invalid
```

![](examples/test2.jpeg)

```
Valid image
```

## Documentation

### Use in your own project
```shell
pip install git+https://github.com/minientreprise-scv/Image-Validation
```

```python
from plantImageValidation import ValidPlantDetector # Import the only class
import cv2 # To read and check qr content

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
```

### Uninstall

```shell
pip uninstall plantImageValidation
```
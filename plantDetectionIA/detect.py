from qrdet import QRDetector


class ValidPlantDetector:

    def __init__(self, content_check=lambda image: True):
        self.detector = QRDetector()
        self.second_check = content_check

    def __call__(self, image):
        detections = self.detector.detect(image=image, is_bgr=True)
        if len(detections) > 0:
            coord = detections[0][0]
            image = image[coord[1]:coord[3], coord[0]:coord[2]]
            return self.second_check(image)
        return False

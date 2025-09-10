import cv2
import numpy as np
import os

# Lag mapper for bilder
os.makedirs("figurer_bilder", exist_ok=True)

for i in range(100):  # Lag 100 bilder
    img = np.ones((500, 500, 3), dtype=np.uint8) * 255

    # Tegn en sirkel
    cv2.circle(img, (100 + i*2, 100 + i*2), 40, (0, 0, 255), -1)

    # Tegn et kvadrat
    cv2.rectangle(img, (300, 300), (370, 370), (255, 0, 0), -1)

    cv2.imwrite(f"figurer_bilder/bilde_{i}.jpg", img)

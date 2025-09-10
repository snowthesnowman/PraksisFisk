import cv2
import numpy as np

# Lag et hvitt bilde
img = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Tegn flere sirkler (rød)
sirkel_posisjoner = [(100, 100), (300, 100), (250, 250), (400, 400)]
for (x, y) in sirkel_posisjoner:
    cv2.circle(img, (x, y), 40, (0, 0, 255), -1)

# Tegn flere firkanter (blå)
firkant_posisjoner = [(120, 120), (280, 280), (200, 350), (350, 150)]
for (x, y) in firkant_posisjoner:
    top_left = (x - 40, y - 40)
    bottom_right = (x + 40, y + 40)
    cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), -1)

# Lagre bildet
cv2.imwrite("testbilde_flere_figurer.jpg", img)

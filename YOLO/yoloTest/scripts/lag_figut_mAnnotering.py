import cv2
import numpy as np
import os

# Lag mapper
os.makedirs("dataset/images", exist_ok=True)
os.makedirs("dataset/labels", exist_ok=True)

# Bildestørrelse
img_size = 500

for i in range(100):
    img = np.ones((img_size, img_size, 3), dtype=np.uint8) * 255

    # Sirkelparametere
    circle_center = (np.random.randint(100, 400), np.random.randint(100, 400))
    circle_radius = np.random.randint(20, 50)
    cv2.circle(img, circle_center, circle_radius, (0, 0, 255), -1)

    # Firkantparametere
    square_top_left = (np.random.randint(100, 350), np.random.randint(100, 350))
    square_size = np.random.randint(40, 80)
    square_bottom_right = (square_top_left[0] + square_size, square_top_left[1] + square_size)
    cv2.rectangle(img, square_top_left, square_bottom_right, (255, 0, 0), -1)

    # Lagre bilde
    img_name = f"bilde_{i}.jpg"
    cv2.imwrite(f"dataset/images/{img_name}", img)

    # Lag YOLO-annotering
    label_lines = []

    # Sirkel: beregn bounding box
    x_c, y_c = circle_center
    w = h = circle_radius * 2
    x_center_norm = x_c / img_size
    y_center_norm = y_c / img_size
    w_norm = w / img_size
    h_norm = h / img_size
    label_lines.append(f"0 {x_center_norm:.6f} {y_center_norm:.6f} {w_norm:.6f} {h_norm:.6f}")

    # Firkant: beregn bounding box
    x1, y1 = square_top_left
    x2, y2 = square_bottom_right
    x_center = (x1 + x2) / 2
    y_center = (y1 + y2) / 2
    w = x2 - x1
    h = y2 - y1
    x_center_norm = x_center / img_size
    y_center_norm = y_center / img_size
    w_norm = w / img_size
    h_norm = h / img_size
    label_lines.append(f"1 {x_center_norm:.6f} {y_center_norm:.6f} {w_norm:.6f} {h_norm:.6f}")

    # Lagre annotering
    label_name = img_name.replace(".jpg", ".txt")
    with open(f"dataset/labels/{label_name}", "w") as f:
        f.write("\n".join(label_lines))

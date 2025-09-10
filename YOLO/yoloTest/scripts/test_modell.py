import torch

# Last inn modellen
model = torch.hub.load('ultralytics/yolov5', 'custom', path='../yolov5/runs/train/exp5/weights/best.pt')

# Test på bildet
results = model('testbilde_flere_figurer.jpg')

# Vis resultatene
results.show()

print(results.pandas().xyxy[0])

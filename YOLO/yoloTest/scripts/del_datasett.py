import os
import random
import shutil

# Kilde-mapper
image_dir = "dataset/images"
label_dir = "dataset/labels"

# Mål-mapper
for split in ["train", "val"]:
    os.makedirs(f"shapes_dataset/images/{split}", exist_ok=True)
    os.makedirs(f"shapes_dataset/labels/{split}", exist_ok=True)

# Hent alle bilde-filer
image_files = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]
random.shuffle(image_files)

# Del opp
split_index = int(len(image_files) * 0.8)
train_files = image_files[:split_index]
val_files = image_files[split_index:]

# Flytt filer
def move_files(file_list, split):
    for img_file in file_list:
        label_file = img_file.replace(".jpg", ".txt")
        shutil.copy(os.path.join(image_dir, img_file), f"shapes_dataset/images/{split}/{img_file}")
        shutil.copy(os.path.join(label_dir, label_file), f"shapes_dataset/labels/{split}/{label_file}")

move_files(train_files, "train")
move_files(val_files, "val")

print("Datasettet er delt og klart!")

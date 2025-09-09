from PIL import Image
import os

# Konfigurasjon
input_folder = "data/firkant"           # Endre til ønsket figurmappe
output_folder = "data/firkant"   # Ny mappe for skalerte bilder
target_size = (64, 64)               # Ønsket størrelse: bredde x høyde

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert("RGB")

        # Beskjær midten (valgfritt – her beskjæres til bredde:høyde-forhold)
        width, height = img.size
        aspect_ratio = target_size[0] / target_size[1]
        current_ratio = width / height

        if current_ratio > aspect_ratio:
            # Bildet er for bredt – beskjær sidene
            new_width = int(height * aspect_ratio)
            left = (width - new_width) // 2
            top = 0
            right = left + new_width
            bottom = height
        else:
            # Bildet er for høyt – beskjær topp/bunn
            new_height = int(width / aspect_ratio)
            left = 0
            top = (height - new_height) // 2
            right = width
            bottom = top + new_height

        img_cropped = img.crop((left, top, right, bottom))

        # Skaler til ønsket størrelse
        img_resized = img_cropped.resize(target_size)

        # Lagre
        save_path = os.path.join(output_folder, filename)
        img_resized.save(save_path)

print("✅ Ferdig! Alle bilder er beskjært og skalert til 770×500.")

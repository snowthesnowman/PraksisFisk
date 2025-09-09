import os

folder = "data/trekant"  # Endre til riktig mappe
prefix = "trekant"        # Endre til figurtype
counter = 1

for filename in os.listdir(folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        ext = filename.split('.')[-1]
        new_name = f"{prefix}_{counter:03d}.{ext}"
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)
        counter += 1

print("✅ Ferdig! Alle bilder har fått nye navn.")

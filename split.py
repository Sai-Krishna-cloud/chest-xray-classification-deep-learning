import os
import shutil
import random

# -------- Paths --------
source_dir = "dataset_all"   # original dataset
base_dir = "split_dataset"

train_dir = os.path.join(base_dir, "train")
val_dir = os.path.join(base_dir, "val")
test_dir = os.path.join(base_dir, "test")

# -------- Create folders --------
for folder in [train_dir, val_dir, test_dir]:
    for class_name in ["covid-19", "normal", "pneumonia"]:
        os.makedirs(os.path.join(folder, class_name), exist_ok=True)

# -------- Split ratios --------
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# -------- Splitting --------
for class_name in ["covid-19", "normal", "pneumonia"]:
    
    class_path = os.path.join(source_dir, class_name)
    images = os.listdir(class_path)
    
    random.shuffle(images)

    total = len(images)
    train_end = int(total * train_ratio)
    val_end = int(total * (train_ratio + val_ratio))

    train_images = images[:train_end]
    val_images = images[train_end:val_end]
    test_images = images[val_end:]

    # Copy files
    for img in train_images:
        shutil.copy(os.path.join(class_path, img),
                    os.path.join(train_dir, class_name, img))

    for img in val_images:
        shutil.copy(os.path.join(class_path, img),
                    os.path.join(val_dir, class_name, img))

    for img in test_images:
        shutil.copy(os.path.join(class_path, img),
                    os.path.join(test_dir, class_name, img))

    print(f"{class_name} -> Total: {total}, Train: {len(train_images)}, Val: {len(val_images)}, Test: {len(test_images)}")

print("✅ Dataset split completed correctly!")
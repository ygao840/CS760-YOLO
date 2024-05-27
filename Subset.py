import os
import random
import shutil

# Set the paths
data_dir = r'E:\YOLO\yolov8\datasets\Tomato Leaf Diseases.v3i.yolov8\train'
images_dir = os.path.join(data_dir, 'images')
labels_dir = os.path.join(data_dir, 'labels')
output_dir = r'E:\YOLO\yolov8\datasets\Tomato Leaf Diseases subset_700\train'
output_images_dir = os.path.join(output_dir, 'images')
output_labels_dir = os.path.join(output_dir, 'labels')

# Create the output directories if they don't exist
os.makedirs(output_images_dir, exist_ok=True)
os.makedirs(output_labels_dir, exist_ok=True)

# List all image files in the images directory
image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]

# Shuffle the list of image files
random.shuffle(image_files)

# Select 1500 files to reserve
reserve_files = image_files[:700]


# Function to copy files
def copy_files(file_list, src_images_dir, src_labels_dir, dest_images_dir, dest_labels_dir):
    for file_name in file_list:
        # Copy the image file
        src_image_path = os.path.join(src_images_dir, file_name)
        dest_image_path = os.path.join(dest_images_dir, file_name)
        shutil.copy(src_image_path, dest_image_path)

        # Copy the corresponding label file
        label_file_name = file_name.replace('.jpg', '.txt')
        src_label_path = os.path.join(src_labels_dir, label_file_name)
        dest_label_path = os.path.join(dest_labels_dir, label_file_name)
        shutil.copy(src_label_path, dest_label_path)


# Copy the reserved files to the respective directories
copy_files(reserve_files, images_dir, labels_dir, output_images_dir, output_labels_dir)

print(f'Reserved 1500 images and their corresponding labels.')

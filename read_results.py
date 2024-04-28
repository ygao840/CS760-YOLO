import pandas as pd
import matplotlib.pyplot as plt
import os

csv_files = [r'E:\YOLO\yolov8\runs\detect\v8s_new_tomato_non-pretrained\train3\results.csv', r'E:\YOLO\yolov8\runs\detect\v8s_new_tomato\train2\results.csv', r'E:\YOLO\yolov8\runs\detect\v8s_skin2new_tomato\train2\results.csv', r'E:\YOLO\yolov8\runs\detect\v8s_plants2new_tomato\train2\results.csv']  # Add your file paths here

# legend names
legend_names = ['non-pretrained(baseline)', 'tomato', 'skin2tomato', 'plant2tomato']
assert len(csv_files) == len(legend_names), "Number of CSV files and legend names must match"

for file_path, legend_name in zip(csv_files, legend_names):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()

    # Filter the DataFrame to include only rows where epoch <= 100
    df = df[df['epoch'] <= 100]

    # Plot the 'metrics/mAP50(B)' column with the custom legend name
    plt.plot(df['epoch'], df['metrics/mAP50(B)'], marker='o', linestyle='-', label=legend_name)

# Configure plot
plt.title('mAP50(B) Across 100 Epochs')
plt.xlabel('Epoch')
plt.ylabel('mAP50(B)')
plt.legend()
plt.grid(True)
plt.show()
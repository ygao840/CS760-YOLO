import matplotlib.pyplot as plt
import os
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

cn_path=open(r"E:\YOLO\yolov8\datasets\Tomato pest-diseases.v1-tomato_v1.yolov9\classes.TXT")

class_dict={}
classes=[i.replace("/n","") for i in cn_path.readlines()]
print(classes)

for i in classes:
    class_dict[i]=0
print("nc",len(class_dict))

def main():
    base_path=r"E:\YOLO\yolov8\datasets\Tomato pest-diseases.v1-tomato_v1.yolov9\train\labels\\"
    FileList=os.listdir(base_path)
    # print("F+++",FileList)
    for file in FileList:
        if file.endswith(".txt"):
            with open(base_path+file,'r') as f:
                for i in f.readlines():
                    i=i.split(' ')
                    print(i)
                    class_dict[classes[int(i[0])]]+=1
    print(class_dict)
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.title('Count')
    plt.xticks(rotation=90)
    bars = plt.bar(class_dict.keys(), class_dict.values())
    for b in bars:
        height = b.get_height()
        ax.annotate('{}'.format(height),

                    xy=(b.get_x() + b.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    va='bottom', ha='center'
        )
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()

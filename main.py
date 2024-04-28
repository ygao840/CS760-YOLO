from ultralytics import YOLO

if __name__ == '__main__':
    # model = YOLO("myyolov8.yaml")  # build a new model from scratch
    # model = YOLO("skindisease.pt")  # load a pretrained model (recommended for training)
    #
    # # Use the model
    # model.train(data="E:\YOLO\yolov8\datasets\Tomato Leaf Diseases.v3i.yolov8\data.yaml", epochs=200)  # train the model
    # metrics = model.val()  # evaluate model performance on the validation set







    # Non prtrained
    model = YOLO("yolov8s.yaml")  # build a new model from scratch

    # Use the model
    model.train(data="E:\YOLO\yolov8\datasets\Tomato Leaf Diseases.v3i.yolov8\data.yaml", epochs=200, pretrained = False)  # train the model
    metrics = model.val()  # evaluate model performance on the validation set




    # results = model("E:\YOLO\yolov8\test\5c77186a4ea326e5495c9d03cd89ce16_jpg.rf.bb36d993c9c1891deca1906ffead043a.jpg")  #
    # path = model.export(format="onnx")  # export the model to ONNX format
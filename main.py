from ultralytics import YOLO

if __name__ == '__main__':
    # model = YOLO("yolov8s.yaml")  # build a new model from scratch
    # model = YOLO("v8s_plants.pt")  # load a pretrained model (recommended for training)
    #
    # # Use the model
    # model.train(data="E:\YOLO\yolov8\datasets\Tomato pest-diseases.v1-tomato_v1.yolov9\data.yaml", epochs=200)  # train the model
    # metrics = model.val()  # evaluate model performance on the validation set




# # v8s_plants2new_tomato
#     model = YOLO("yolov8s.yaml")  # build a new model from scratch
#     model = YOLO("v8s_plants.pt")  # load a pretrained model (recommended for training)
#
#     # Use the model
#     model.train(data="E:\YOLO\yolov8\datasets\Tomato Leaf Diseases.v3i.yolov8\data.yaml", epochs=200)  # train the model
#     metrics = model.val()  # evaluate model performance on the validation set





# E:\YOLO\yolov8\datasets\Tomato pest-diseases.v1-tomato_v1.yolov9\data.yaml
# E:\YOLO\yolov8\datasets\Tomato Leaf Diseases.v3i.yolov8\data.yaml



    # # Non prtrained
    # model = YOLO("yolov8s.yaml")  # build a new model from scratch
    #
    # # Use the model
    # model.train(data="E:\YOLO\yolov8\datasets\Tomato Leaf Diseases.v3i.yolov8\data.yaml", epochs=200, pretrained = False)  # train the model
    # metrics = model.val()  # evaluate model performance on the validation set




    # results = model("E:\YOLO\yolov8\test\5c77186a4ea326e5495c9d03cd89ce16_jpg.rf.bb36d993c9c1891deca1906ffead043a.jpg")  #
    # path = model.export(format="onnx")  # export the model to ONNX format







# # v8s_plants2new_tomato_freeze_backbone
#     model = YOLO("yolov8s.yaml")  # build a new model from scratch
#     model = YOLO("v8s_plants.pt")  # load a pretrained model (recommended for training)
#
#     # Use the model
#     model.train(data="E:\YOLO\yolov8\datasets\Tomato Leaf Diseases.v3i.yolov8\data.yaml", epochs=200, freeze = 10)  # train the model
#     metrics = model.val()  # evaluate model performance on the validation set



# # v8s_plants2new_tomato_freeze_all
#     model = YOLO("yolov8s.yaml")  # build a new model from scratch
#     model = YOLO("v8s_plants.pt")  # load a pretrained model (recommended for training)
#
#     # Use the model
#     model.train(data="E:\YOLO\yolov8\datasets\Tomato Leaf Diseases.v3i.yolov8\data.yaml", epochs=200, freeze = 22)  # train the model
#     metrics = model.val()  # evaluate model performance on the validation set





#########################################################################################
#################            Subset  1500            ####################################

# # Non prtrained
#     model = YOLO("yolov8s.yaml")  # build a new model from scratch
#
#     # Use the model
#     model.train(data="E:\YOLO\yolov8\datasets\Tomato Leaf Diseases subset\data.yaml", epochs=200, pretrained = False)  # train the model
#     metrics = model.val()  # evaluate model performance on the validation set
#
# # Fine-tuning
#     model = YOLO("yolov8s.yaml")  # build a new model from scratch
#     model = YOLO("yolov8s.pt")
#
#     # Use the model
#     model.train(data="E:\YOLO\yolov8\datasets\Tomato Leaf Diseases subset\data.yaml", epochs=200)  # train the model
#     metrics = model.val()  # evaluate model performance on the validation set
#
# # skin2tomato
#     model = YOLO("yolov8s.yaml")  # build a new model from scratch
#     model = YOLO("skindisease.pt")
#
#     # Use the model
#     model.train(data="E:\YOLO\yolov8\datasets\Tomato Leaf Diseases subset\data.yaml", epochs=200)  # train the model
#     metrics = model.val()  # evaluate model performance on the validation set
#
# # plants2tomato
#     model = YOLO("yolov8s.yaml")  # build a new model from scratch
#     model = YOLO("v8s_plants.pt")
#
#     # Use the model
#     model.train(data="E:\YOLO\yolov8\datasets\Tomato Leaf Diseases subset\data.yaml", epochs=200)  # train the model
#     metrics = model.val()  # evaluate model performance on the validation set

# # plants2tomato_freeze_backbone
#     model = YOLO("yolov8s.yaml")  # build a new model from scratch
#     model = YOLO("v8s_plants.pt")  # load a pretrained model (recommended for training)
#
#     # Use the model
#     model.train(data="E:\YOLO\yolov8\datasets\Tomato Leaf Diseases subset\data.yaml", epochs=200, freeze = 10)  # train the model
#     metrics = model.val()  # evaluate model performance on the validation set
#
# # plants2new_tomato_freeze_all
#     model = YOLO("yolov8s.yaml")  # build a new model from scratch
#     model = YOLO("v8s_plants.pt")  # load a pretrained model (recommended for training)
#
#     # Use the model
#     model.train(data="E:\YOLO\yolov8\datasets\Tomato Leaf Diseases subset\data.yaml", epochs=200, freeze = 22)  # train the model
#     metrics = model.val()  # evaluate model performance on the validation set


#########################################################################################
#################             Subset  700            ####################################

# Non prtrained
    model = YOLO("yolov8s.yaml")  # build a new model from scratch

    # Use the model
    model.train(data="E:\YOLO\yolov8\datasets\Tomato Leaf Diseases subset_700\data.yaml", epochs=200, pretrained = False)  # train the model
    metrics = model.val()  # evaluate model performance on the validation set

# Fine-tuning
    model = YOLO("yolov8s.yaml")  # build a new model from scratch
    model = YOLO("yolov8s.pt")

    # Use the model
    model.train(data="E:\YOLO\yolov8\datasets\Tomato Leaf Diseases subset_700\data.yaml", epochs=200)  # train the model
    metrics = model.val()  # evaluate model performance on the validation set

# skin2tomato
    model = YOLO("yolov8s.yaml")  # build a new model from scratch
    model = YOLO("skindisease.pt")

    # Use the model
    model.train(data="E:\YOLO\yolov8\datasets\Tomato Leaf Diseases subset_700\data.yaml", epochs=200)  # train the model
    metrics = model.val()  # evaluate model performance on the validation set

# plants2tomato
    model = YOLO("yolov8s.yaml")  # build a new model from scratch
    model = YOLO("v8s_plants.pt")

    # Use the model
    model.train(data="E:\YOLO\yolov8\datasets\Tomato Leaf Diseases subset_700\data.yaml", epochs=200)  # train the model
    metrics = model.val()  # evaluate model performance on the validation set

# plants2tomato_freeze_backbone
    model = YOLO("yolov8s.yaml")  # build a new model from scratch
    model = YOLO("v8s_plants.pt")  # load a pretrained model (recommended for training)

    # Use the model
    model.train(data="E:\YOLO\yolov8\datasets\Tomato Leaf Diseases subset_700\data.yaml", epochs=200, freeze = 10)  # train the model
    metrics = model.val()  # evaluate model performance on the validation set

# plants2new_tomato_freeze_all
    model = YOLO("yolov8s.yaml")  # build a new model from scratch
    model = YOLO("v8s_plants.pt")  # load a pretrained model (recommended for training)

    # Use the model
    model.train(data="E:\YOLO\yolov8\datasets\Tomato Leaf Diseases subset_700\data.yaml", epochs=200, freeze = 22)  # train the model
    metrics = model.val()  # evaluate model performance on the validation set
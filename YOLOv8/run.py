from ultralytics import YOLO

# Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="bees.yaml", epochs=3)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
results = model("https://images.labelon.kr/2022/11/10/a8705ce21cf94d4e8410082eb29e65cf.jpg")  # predict on an image
path = model.export(format="onnx")  # export the model to ONNX format
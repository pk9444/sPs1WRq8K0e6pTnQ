import torch
from torchvision import models, transforms
from PIL import Image
from io import BytesIO

class_names = ['flip', 'not_flip']
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])

def load_model():
    model = models.resnet18(pretrained=True)
    for param in model.parameters():
        param.requires_grad = False
    model.fc = torch.nn.Linear(model.fc.in_features, 2)
    model.load_state_dict(torch.load("deployments/flip_classifier_weights_v1.pth", map_location=device))
    model.to(device)
    model.eval()
    return model

def predict_image(model, file_obj, conf_threshold=0.67):
    image = Image.open(file_obj).convert("RGB")
    input_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(input_tensor)
        probs = torch.softmax(output, dim=1)
        conf, pred = torch.max(probs, 1)

    result = {
        "prediction": class_names[pred.item()],
        "confidence": round(conf.item(), 4)
    }
    return result

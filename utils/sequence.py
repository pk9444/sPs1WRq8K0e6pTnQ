import torch

from .model import transform, device, class_names
from PIL import Image

def predict_sequence(model, image_files, conf_threshold=0.8):
    flip_found = False

    for file_obj in image_files:
        image = Image.open(file_obj).convert("RGB")
        input_tensor = transform(image).unsqueeze(0).to(device)

        with torch.no_grad():
            output = model(input_tensor)
            probs = torch.softmax(output, dim=1)
            conf, pred = torch.max(probs, 1)

        if class_names[pred.item()] == 'flip' and conf.item() >= conf_threshold:
            flip_found = True
            break  # early exit if one flip frame is found

    return {
        "sequence_prediction": "flip" if flip_found else "not_flip",
        "reason": "At least one frame exceeded confidence threshold" if flip_found else "No confident flip frames found"
    }
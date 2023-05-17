import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torchvision.transforms.functional as TF
import gradio as gr


class CNN(nn.Module):
    def __init__(self, K):
        super(CNN, self).__init__()
        self.conv_layers = nn.Sequential(
            # conv1
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, padding=1),  #filter matching
            nn.ReLU(),  #activation function
            nn.BatchNorm2d(32),  #increases speed and centers the data
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(32),
            nn.MaxPool2d(2),
            # conv2
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(64),
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(64),
            nn.MaxPool2d(2),  #selects the max value
            # conv3
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(128),
            nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(128),
            nn.MaxPool2d(2),
            # conv4
            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(256),
            nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(256),
            nn.MaxPool2d(2),
        )

        self.dense_layers = nn.Sequential(
            nn.Dropout(0.4),
            nn.Linear(50176, 1024),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(1024, K),
        )

    def forward(self, X):
        out = self.conv_layers(X)

        # Flatten
        out = out.view(-1, 50176)

        # Fully connected
        out = self.dense_layers(out)

        return out
    

targets_size = 39
model = CNN(targets_size)
model.load_state_dict(torch.load("plant_disease_model.pt"))
model.eval()
device = 'cpu'
model.to(device)

disease_info = pd.read_csv("disease_info.csv", encoding="cp1252", index_col=0)

def predict(image):
    
    image = image.resize((224, 224))
    input_data = TF.to_tensor(image)
    input_data = input_data.view((-1, 3, 224, 224))
    
    output = model(input_data.to(device))
    output = output.detach().cpu().numpy()
    index = np.argmax(output)

    results = disease_info.loc[index].to_dict()
    results = {
        "Disease Predicted": results["disease_name"],
        "Description": results["description"],
        "Notes/Remedy": results["remedy"]
    }

    text = ""
    for key, value in results.items():
        text += f"{key.title()}: \n{value}\n\n"

    return text


app = gr.Interface(fn=predict, inputs=gr.Image(type="pil"), outputs=gr.Textbox("Results"))

# Launch the app
app.launch(server_port=7001)

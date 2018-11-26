import torch
import torch.nn as nn
from PIL import Image
from torchvision import transforms
from torch.autograd import Variable

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

input_size = 224
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
loader = transforms.Compose([
    transforms.Resize(input_size),
    transforms.CenterCrop(input_size),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

def loadImage(imgPath):
    img = Image.open(imgPath)
    img = loader(img).float()
    img = Variable(img, requires_grad=False)
    img = img.unsqueeze(0)
    img = img.to(device)
    return img

model = torch.load('pretrained-batch1-squeezenet.pt')
model = model.to(device)
# model.classifier[1] = nn.Conv2d(512, 26, kernel_size=(1,1), stride=(1,1))
model.eval()
print("Model loaded and set to eval mode")

loadedImg = loadImage('sher-target.jpg')
print('Loaded image!')
with torch.set_grad_enabled(False):
    outputs = model(loadedImg)

    _, preds = torch.max(outputs, 1)
    print('Prediction == {}'.format(alphabet[preds[0]]))
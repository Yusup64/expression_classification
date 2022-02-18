import os
import json

import torch
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt

from model import AlexNet


def recognizePicture(img_path='./smile.jpg', result=[]):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    data_transform = transforms.Compose(
        [transforms.Resize((224, 224)),
         transforms.ToTensor(),
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    # load image
    # img_path = os.path.join(os.getcwd(),"smile.jpg")
    assert os.path.exists(
        img_path), "file: '{}' dose not exist.".format(img_path)
    img = Image.open(img_path)
    img = img.convert('RGB')

    plt.imshow(img)
    # [N, C, H, W]
    img = data_transform(img)
    # expand batch dimension
    img = torch.unsqueeze(img, dim=0)

    # read class_indict
    json_path = './class_indices.json'
    assert os.path.exists(
        json_path), "file: '{}' dose not exist.".format(json_path)

    json_file = open(json_path, "r")
    class_indict = json.load(json_file)

    # create model
    model = AlexNet(num_classes=7).to(device)

    # load model weights
    weights_path = "./AlexNet_Original_52.pth"
    assert os.path.exists(
        weights_path), "file: '{}' dose not exist.".format(weights_path)
    model.load_state_dict(torch.load(weights_path))

    model.eval()
    with torch.no_grad():
        # predict class
        output = torch.squeeze(model(img.to(device))).cpu()
        predict = torch.softmax(output, dim=0)
        predict_cla = torch.argmax(predict).numpy()

    """ print_res = "class: {}   prob: {:.3}".format(class_indict[str(predict_cla)],
                                                 predict[predict_cla].numpy())
    plt.title(print_res)
    print(print_res)
    plt.show()
 """
    rec_acc = round(float(predict[predict_cla]), 4)
    class_res = int(class_indict[str(predict_cla)])
    print(img_path, rec_acc, class_res)
    result.append({
        'acc': rec_acc,
        'class': class_res
    })
if __name__ == '__main__':
    result = {}
    rootpath = os.path.join(
        os.getcwd(), 'ExpressionClassification', 'expr_data', 'val')
    typeDirList = os.listdir(rootpath)
    for dirName in typeDirList:
        # print(os.path.join(rootpath,dirName));
        dataPath = os.path.join(rootpath, dirName)
        if(dirName not in result):
            result[dirName] = []
        imgsDirList = os.listdir(dataPath)
        # print(dataPath)
        for img in imgsDirList:
            imgAbsPath = os.path.join(dataPath, img)
            recognizePicture(imgAbsPath, result[dirName])
    with open('./result/original_52.json', 'w') as json_file:
        json_file.write(json.dumps(result))
    # print(json.dumps(result))

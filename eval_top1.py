import numpy as np
import torch
import os.path
from PIL import Image
from torch.autograd import Variable

from classification import Classification, _preprocess_input
from utils.utils import letterbox_image


class top1_Classification(Classification):
    def detect_image(self, image):        
        crop_img = letterbox_image(image, [self.input_shape[0],self.input_shape[1]])
        photo = np.array(crop_img,dtype = np.float32)

        # 图片预处理，归一化
        photo = np.reshape(_preprocess_input(photo),[1,self.input_shape[0],self.input_shape[1],self.input_shape[2]])
        photo = np.transpose(photo,(0,3,1,2))

        with torch.no_grad():
            photo = Variable(torch.from_numpy(photo).type(torch.FloatTensor))
            if self.cuda:
                photo = photo.cuda()
            preds = torch.softmax(self.model(photo)[0], dim=-1).cpu().numpy()

        arg_pred = np.argmax(preds)
        return arg_pred

# fw = open("E:/result/mobilenet.csv", 'w')

def evaluteTop1(classfication, lines):
    correct = 0
    total = len(lines)
    # fw = open("E:/result/mobilenet.txt", 'w') #创建一个文档，用于存放预测错误的图片信息
    for index, line in enumerate(lines):
        annotation_path = line.split(';')[1].replace('\n', '')
        x = Image.open(annotation_path)
        y = int(line.split(';')[0])

        pred = classfication.detect_image(x)

        # if y != pred: #判断是否预测错误，预测错误就写入文档中
        #     print(os.path.basename(annotation_path)) #输出预测错误的图像名称
        #     t = os.path.basename(annotation_path)
        #     fw.write(t)
        #     fw.write(",")
        #     fw.write(str(y))
        #     fw.write(",")
        #     fw.write(str(pred))
        #     fw.write("\n")

        correct += pred == y
        if index % 100 == 0:
            print("[%d/%d]"%(index,total))
    return correct / total

classfication = top1_Classification()
with open(r"./cls_test.txt","r") as f:
    lines = f.readlines()
top1 = evaluteTop1(classfication, lines)
print("top-1 accuracy = %.2f%%" % (top1*100))
# fw.write("top-1 accuracy = %.2f%%" % (top1*100))


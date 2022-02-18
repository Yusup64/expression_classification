""" trainAccFile = open('./trainAcc.txt', 'a')
trainAccFile.write('1312312' + " "+"\n")
 """
import os
import random
from shutil import rmtree, copy


def mk_file(file_path: str):
    if os.path.exists(file_path):
        # 如果文件夹存在，则先删除原文件夹在重新创建
        rmtree(file_path)
    os.makedirs(file_path)


root_path = os.path.join(os.getcwd(), 'ExpressionClassification')
data_dir = os.path.join(root_path, 'expr_data', 'expr_photo')
copy_dir = os.path.join(root_path, 'sample_data', 'expr_photo')

folderArr = os.listdir(data_dir)
for folderName in folderArr:
    newPath = os.path.join(data_dir, folderName)
    files = os.listdir(newPath)
    newImgList = random.sample(files, 500)
    new_copy_dir = os.path.join(copy_dir, folderName)
    mk_file(new_copy_dir)
    for item in newImgList:
        image_path = os.path.join(newPath, item)
        new_path = os.path.join(new_copy_dir, item)
        copy(image_path, new_path)

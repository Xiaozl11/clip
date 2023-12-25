import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--dataset_project',default="default_project", help='project_name')
parser.add_argument('--dataset_name',default="default_name", help='name')
parser.add_argument('--picture_name', help='name')

args = parser.parse_args()
dataset_project = args.dataset_project ## dataset中的project名字
dataset_name = args.dataset_name # 文件的名字
picture_name = args.picture_name # 训练路径图片文件夹的名字

'''
print(dataset_project)
print(dataset_name)
print("okokok")


dataset_project = "christmas" ## dataset中的project名字
dataset_name = "dataset-2023-12-14-1.0" # 文件的名字
'''

from clearml import Dataset
import os
import shutil
dataset_path = Dataset.get(dataset_name=dataset_name, dataset_project=dataset_project).get_local_copy() # 获取到下载路径
# 已经拿到下载下来的图片
data_name = os.path.basename(dataset_path) # 获取名字
src_path = dataset_path
des_path = os.getcwd()
shutil.move(src_path, des_path) # 移动
name_path = os.path.join(des_path,data_name)
new_name_path = os.path.join(os.getcwd(), picture_name)
os.rename(name_path, new_name_path) # 重命名
# print(new_name_path)

# print("dataset_path = ",dataset_path)

# D:\SDXL\clearml\arg_ceshi.py

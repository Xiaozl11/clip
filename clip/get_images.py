import argparse
from clearml import Dataset
import os
import shutil
parser = argparse.ArgumentParser()
# parser.add_argument('--dataset_project',default="default_project", help='project_name')
# parser.add_argument('--dataset_name',default="default_name", help='name')
parser.add_argument('--id', help='dataset_id')
parser.add_argument('--name', default="picture", help='folder_name')

args = parser.parse_args()
# dataset_project = args.dataset_project ## dataset中的project名字
# dataset_name = args.dataset_name # 文件的名字
id = args.id # 文件的名字
name = args.name # 训练路径图片文件夹的名字


# 这里要写try except
try:
    dataset_path = Dataset.get(dataset_id=id).get_local_copy() # 获取到下载路径
     # 已经拿到下载下来的图片
    data_name = os.path.basename(dataset_path) # 获取名字
    src_path = dataset_path
    des_path = os.getcwd()
    shutil.move(src_path, des_path) # 移动
    # print("stutil move is done")
    name_path = os.path.join(des_path,data_name)
    new_name_path = os.path.join(os.getcwd(), name)
    # print("new_name_alread")
    if os.path.exists(new_name_path): # 如果此路径下已经有了旧的文件夹
        # print("删除已有的文件夹")
        os.rmdir(new_name_path) # 删掉
    os.rename(name_path, new_name_path) # 重命名

except:
    print("Get_images Error!")
# print(new_name_path)

# print("dataset_path = ",dataset_path)

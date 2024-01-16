#!/bin/bash

dataset_id=$DATASET_ID
floder_name=$PIC_NAME
model_name=$MODEL
batch=$BATCH_SIZE
epoches=$MAX_EPOCHES
output_name=$floder_name
# cd /work_disk/clip-interrogator
# path_lora=/work_disk/lora-scripts
python3 /work_disk/clip-interrogator/get_images.py --id $dataset_id --name $floder_name
echo "### $floder_name is done ###"
# 这里如果./pic_folder/文件下有dog，则移动失败
if [ -d "./pic_folder/$floder_name" ]; then
    rm -rf ./pic_folder/$floder_name
fi
mv -f $floder_name ./pic_folder
echo "### mv is done ###"

python3 /work_disk/clip-interrogator/x_run_cli.py --folder ./pic_folder/$floder_name
echo "### run is done ###"
# read
cp -rf pic_folder/$floder_name ../lora-scripts/train/pic #dog
cd /work_disk/lora-scripts/train/pic # 进入目录
if [ -d "/work_disk/lora-scripts/train/pic/7_$floder_name" ]; then
   # echo "delect 7_$floder_name"
   rm -rf /work_disk/lora-scripts/train/pic/7_$floder_name
fi
mv -f $floder_name 7_$floder_name
echo "### rename is done ###"

cd /work_disk/lora-scripts
source xiao/bin/activate # 进入虚拟环境 
echo "######$model_name $batch $epoches $output_name######"
bash train_args.sh $model_name $batch $epoches $output_name
echo "### train is done ###"
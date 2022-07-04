import os
from glob import glob

lists = sorted(glob("./data/kitti/gt_depth/2011_09_26/"+"*"), key=lambda x : x.split('/')[-1].split('_')[-2])


for i in range(len(lists)):
  paths = lists[i] + "/proj_depth/groundtruth/"
  os.system(f"mkdir -p {paths}")
  os.system(f"mv {lists[i]}/* {paths}")

print("finish")

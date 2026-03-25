import open3d as o3d
import numpy as np
from graspnetAPI import GraspGroup

# 1. 读取点云
cloud = o3d.io.read_point_cloud('cloud_result.ply')

# 2. 读取抓取结果（*务必和结果保存时API版本一致*）
gg = GraspGroup(np.load('grasps_result.npy'))

# 3. 转为open3d可渲染几何体
grippers = gg.to_open3d_geometry_list()

# 4. 可视化（可旋转、截屏等）
o3d.visualization.draw_geometries([cloud, *grippers])

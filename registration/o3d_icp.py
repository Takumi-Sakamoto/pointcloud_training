from unittest import result
import open3d as o3d
import numpy as np
import copy

pcd1 = o3d.io.read_point_cloud("data/bun000.pcd")
pcd2 = o3d.io.read_point_cloud("data/bun045.pcd")

# down sampling
pcd_s = pcd1.voxel_down_sample(voxel_size=0.005)
pcd_t = pcd2.voxel_down_sample(voxel_size=0.005)

pcd_s.paint_uniform_color([0.0, 1.0, 0.0])
pcd_t.paint_uniform_color([0.0, 0.0, 1.0])
o3d.visualization.draw_geometries([pcd_s, pcd_t])

# ICP matching
th = 0.05  # max threshold distance of registration
trans_init = np.identity(4)  # initial pose of pcd_s
obj_func = o3d.pipelines.registration.TransformationEstimationPointToPoint()
icp_result = o3d.pipelines.registration.registration_icp(
    pcd_s, pcd_t, th, trans_init, obj_func)

# get transformation matrix
trans_reg = icp_result.transformation
print(trans_reg)

# visualization
pcd_reg = copy.deepcopy(pcd_s).transform(trans_reg)
pcd_reg.paint_uniform_color([1.0, 0.0, 0.0])
o3d.visualization.draw_geometries([pcd_reg, pcd_t])

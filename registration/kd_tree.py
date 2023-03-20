# kd-treeで近傍探索
# search_knn_vector_3d: クエリのk点近傍探索
# search_radius_vector_3d: 指定した半径の値以内の点を探索
# search_hybrid_vector_3d: 上記2つの条件を両方満たす点の探索

import open3d as o3d
import numpy as np

pcd = o3d.io.read_point_cloud("data/bun000.pcd")
pcd.paint_uniform_color([0.5, 0.5, 0.5])

# kd-treeの構築
pcd_tree = o3d.geometry.KDTreeFlann(pcd)

# 10000番目の近傍200点の探索
query = 10000
pcd.colors[query] = [1, 0, 0]

[k, idx, _] = pcd_tree.search_knn_vector_3d(pcd.points[query], 200)
np.asarray(pcd.colors)[idx[1:], :] = [0, 0, 1]
o3d.visualization.draw_geometries([pcd], width=600, height=400)

# 20000番目の近傍距離0.01以内の点の探索
query = 20000
pcd.colors[query] = [1, 0, 0]
[k, idx, d] = pcd_tree.search_radius_vector_3d(pcd.points[query], 0.01)
np.asarray(pcd.colors)[idx[1:], :] = [0, 1, 0]
o3d.visualization.draw_geometries([pcd], width=600, height=400)

# 5000番目の近傍距離0.01以内で200点の探索
query = 5000
pcd.colors[query] = [1, 0, 0]
[k, idx, d] = pcd_tree.search_hybrid_vector_3d(pcd.points[query],
                                               radius=0.01,
                                               max_nn=200)
np.asarray(pcd.colors)[idx[1:], :] = [0, 1, 1]
o3d.visualization.draw_geometries([pcd], width=600, height=400)

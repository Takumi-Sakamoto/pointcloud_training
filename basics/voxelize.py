# 等間隔サンプリング
import sys
import open3d as o3d


file_name = sys.argv[1]
s = float(sys.argv[2])
pcd = o3d.io.read_point_cloud(file_name)
print(pcd)

zoom = 0.3412
front = [0.4257, -0.2125, -0.8795]
lookat = [2.6172, 2.0475, 1.532]
up = [-0.0694, -0.9769, 0.2024]
o3d.visualization.draw_geometries(
    [pcd], zoom=zoom, front=front, lookat=lookat, up=up)

downpcd = pcd.voxel_down_sample(voxel_size=s)
print(downpcd)

o3d.visualization.draw_geometries(
    [downpcd], zoom=zoom, front=front, lookat=lookat, up=up)

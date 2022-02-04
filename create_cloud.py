import os
import open3d as o3d
import numpy as np

depth_folder = 'rgbd_lobby/lobby/depth/'
color_folder = 'rgbd_lobby/lobby/image/'
depth_imgs = sorted(os.listdir(depth_folder))
color_imgs = sorted(os.listdir(color_folder))
result = o3d.geometry.PointCloud()

option =o3d.pipelines.odometry.OdometryOption()
odo_init = np.identity(4)
pinhole_camera_intrinsic = o3d.camera.PinholeCameraIntrinsic(
    o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault)
count = 1
for i in range(len(depth_imgs)):
    color_path = color_folder+color_imgs[i]
    depth_path = depth_folder+depth_imgs[i]
    color_raw = o3d.io.read_image(color_path)
    depth_raw = o3d.io.read_image(depth_path)
    rgbd_img = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw, convert_rgb_to_intensity=True)

    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
    rgbd_img, pinhole_camera_intrinsic)
    pcd.transform([[1,0,0,0], [0,-1,0,0], [0,0,-1,0], [0,0,0,1]])
    print('Done: ',count)
    count+=1
    temp = 'point_clouds/'+str(count)+'.ply'
    o3d.io.write_point_cloud(temp, pcd)




    

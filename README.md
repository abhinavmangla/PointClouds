# PointClouds




![000000](https://user-images.githubusercontent.com/43683201/152600425-6e43d7bc-54de-495e-b58e-a33d20714d9e.jpg)

Output Video: https://youtu.be/HKaA1np1F7E

Output Point Clouds: https://drive.google.com/file/d/1WcJmVIIrlYx7jVc2dklHENFO19MqPMfo/view?usp=sharing

Dataset (Lobby): https://drive.google.com/file/d/1MhjCJuznp3pG6zxHrIbmcjPjXhvlBStu/view?usp=sharing

Extract the contents of the ZIP file in the directory containing the code files

# Dependencies
Open3D 0.11 or higher
Installation Instructions (for Linux based environments): pip install open3d

# Running The Program (for Linux based systems)

1. Run the Python program create_cloud.py using the command: python3 create_cloud.py. This command creates the point clouds for all the images present in the dataset. point_clouds.zip contains the point clouds for a part of the dataset as an example.
2. Use python3 create_video.py to view a moving animation of the dataset. The resulting video link is provided above.

# Directory Structure

PointClouds

    create_cloud.py
    
    create_video.py
    
    rgbd_lobby
    
        lobby
        
            image  ---rgb images of lobby
            
            depth  ---depth images of lobby

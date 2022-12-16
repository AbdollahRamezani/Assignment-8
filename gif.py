import os
import imageio
file_list=sorted(os.listdir("Assignment 8/images"))  

IMAGES=[]
for file_name in file_list:
    file_path="Assignment 8/images/"+file_name
    image=imageio.imread(file_path)

    IMAGES.append(image)

imageio.mimsave("Assignment 8/output_my_gif/my_gif.gif",IMAGES )  

    
    
    
import os
import cv2


path = "C105/ac105"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height,width,channel = frame.shape
size = (width,height)
alt = cv2.VideoWriter("Por_do_sol.mp4",cv2.VideoWriter_fourcc(*"DIVX"),5,size)
for i in range (count-1,0,-1):
    frame = cv2.imread(images[i])
    alt.write(frame)
alt.release()
print("Fim.")
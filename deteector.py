import os
import cv2

path = "C:/Users/risho/OneDrive/Documents/project friends/Images"

Images = []

for file in os.listdir(path):
    name, extension = os.path.splitext(file)
    if extension.lower() in ['.jpg', '.jpeg', '.png']:
        file_name = path + "/" + file
        print(file_name)
        Images.append(file_name)

count = len(Images)

frame = cv2.imread(Images[0])
size = (frame.shape[1], frame.shape[0])

print(size)

out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count):
    image = cv2.imread(Images[i])
    out.write(image)

out.release()
print("Done")

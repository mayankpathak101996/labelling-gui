import os
path = 'C:\project\Class_label_SSD\Images\Key_Dataset1'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpeg'))
    i = i+1
import os
import shutil
folder_path = r"D:\Cyber downloads\File_Organizer_Test"
files = os.listdir(folder_path)
for file in files:
    filename, extension = os.path.splitext(file)
    if extension == ".png"or extension == ".jpg":
        images_folder = os.path.join(folder_path, "Images")
        if not os.path.exists(images_folder):
            os.makedirs(images_folder)
        source = os.path.join(folder_path, file)
        shutil.move(source,images_folder)    
    elif extension == ".txt":
        txt_folder = os.path.join(folder_path,"Text files")
        if not os.path.exists(txt_folder):
            os.makedirs(txt_folder)
        source = os.path.join(folder_path,file)
        shutil.move(source,txt_folder)
    elif extension == ".mp4":
        Videos = os.path.join(folder_path,"Videos")
        if not os.path.exists(Videos):
            os.makedirs(Videos)
        source = os.path.join(folder_path,file)
        shutil.move(source,Videos)
    elif extension == ".mp3":
        Audio = os.path.join(folder_path, "Audio")
        if not os.path.exists(Audio):
            os.makedirs(Audio)
        source = os.path.join(folder_path, file)
        shutil.move(source, Audio)
    elif extension == ".docx":
        Document = os.path.join(folder_path, "Documents")
        if not os.path.exists(Document):
            os.makedirs(Document)
        source = os.path.join(folder_path, file)
        shutil.move(source, Document)
    elif extension == ".py":
        Python = os.path.join(folder_path, "Python Files")
        if not os.path.exists(Python):
            os.makedirs(Python)
        source = os.path.join(folder_path, file)
        shutil.move(source, Python)
    else:
        Others = os.path.join(folder_path, "Others")
        if not os.path.exists(Others):
            os.makedirs(Others)
        source = os.path.join(folder_path, file)
        shutil.move(source, Others)    
    
    
    
    print(filename, extension)

import os
import pathlib


def get_all_subfolders(path,extention=""):
    subfolders = []
    files = []
    split =len(folder_path)
    try:
        for f in os.scandir(path):
            if f.is_dir():
                subfolders.append(f.path)
                res=get_all_subfolders(f.path)
                subfolders.extend(res[0])
                files.extend(res[1])
            else:
                if pathlib.Path(f.path).suffix==extention or extention=="":
                    files.append(f.path[split::])
    except PermissionError:
        pass
    except :
        pass
    # return subfolders and files 
    return [subfolders,files]

folder_path = "/Users/aechaoub/Desktop/was/"
all_subfolders = get_all_subfolders(folder_path)[1]
i=0 
for el in all_subfolders:
    i+=1
    print(f"{i} {el}")

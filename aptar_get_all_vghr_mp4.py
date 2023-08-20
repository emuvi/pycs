import os
import shutil


def get_all_mp4(path, destiny):
    for inside in os.listdir(path):
        compound = os.path.join(path, inside)
        if os.path.isdir(compound):
            get_all_mp4(compound, destiny)
        else:
            kind = os.path.splitext(inside)[1]
            if kind == '.mp4':
                destiny_file = os.path.join(destiny, inside)
                print(compound, " -> ", destiny_file)
                shutil.copyfile(compound, destiny_file)
            

def get_all_vg_mp4(path, destiny):
    for inside in os.listdir(path):
        if inside.startswith("VGHR"):
            compound = os.path.join(path, inside)
            get_all_mp4(compound, destiny)


if __name__ == "__main__":
    get_all_vg_mp4('C:\\Users\\emuvi\\OneDrive\\Documentos\\Aptar',
               'C:\\Users\\emuvi\\Downloads')

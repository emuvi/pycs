import os
import random
import shutil
import time


def get_all_of_tema(path, extension, destiny_dir):
    if os.path.isdir(path):
        for inside in os.listdir(path):
            origin = os.path.join(path, inside)
            if os.path.isfile(origin):
                if origin.lower().endswith(extension):
                    name = os.path.basename(origin)
                    destiny = os.path.join(destiny_dir, name)
                    print("Coping", origin, " -> ", destiny)
                    try:
                        shutil.copyfile(origin, destiny)
                        print("Copied", origin, " -> ", destiny)
                    except Exception as e:
                        print("------------------------------------")
                        print("Error!!!!!")
                        print(e)
                        print("------------------------------------")
                        time.sleep(5)

            elif os.path.isdir(origin):
                get_all_of_tema(origin, extension, destiny_dir)


def find_folder_starting_with(path, prefix):
    if os.path.isdir(path):
        for inside in os.listdir(path):
            compound = os.path.join(path, inside)
            if os.path.isdir(compound) and inside.startswith(prefix):
                return compound
    return None


def get_tema(root):
    tag = find_folder_starting_with(
        root, input("Qual o começo do nome da disciplina? : "))
    while not tag:
        tag = find_folder_starting_with(
            root, input("Qual o começo do nome da disciplina? : "))
    tema = find_folder_starting_with(
        tag, input("Qual o começo do nome do tema? : "))
    while not tema:
        tema = find_folder_starting_with(
            tag,  input("Qual o começo do nome do tema? : "))
    return tema


get_all_of_tema(get_tema('C:\\Users\\emuvi\\OneDrive\\Documentos\\Aptar'),
                '.mp4', 'C:\\Users\\emuvi\\Downloads')

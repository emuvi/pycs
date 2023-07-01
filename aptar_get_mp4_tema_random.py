import os
import random
import shutil
import time


def get_tema_random(path):
    temas = []
    if os.path.isdir(path):
        for disciplina in os.listdir(path):
            disciplina = os.path.join(path, disciplina)
            if os.path.isdir(disciplina):
                for tema in os.listdir(disciplina):
                    tema = os.path.join(disciplina, tema)
                    if os.path.isdir(tema):
                        temas.append(tema)
    if len(temas) > 0:
        return temas[random.randint(0, len(temas) - 1)]
    return None


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


def get_random(origin_dir, extension, destiny_dir):
    tema = get_tema_random(origin_dir)
    print("Tema: ", tema)
    get_all_of_tema(tema, extension, destiny_dir)


get_random('C:\\Users\\emuvi\\OneDrive\\Documentos\\Aptar',
           '.mp4', 'C:\\Users\\emuvi\\Downloads')

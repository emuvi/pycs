import os
import random
import shutil
import time

import vlc


def get_all(path, extension, results):
    if os.path.isdir(path):
        for inside in os.listdir(path):
            compound = os.path.join(path, inside)
            if os.path.isfile(compound):
                name = inside.lower()
                kind = os.path.splitext(name)[1]
                if kind == extension:
                    results.append(compound)
            else:
                get_all(compound, extension, results)
    return results


def get_random(origin_dir, extension, destiny_dir):
    options = get_all(origin_dir, extension, [])
    while True:
        origin = options[random.randint(0, len(options) - 1)]
        name = os.path.basename(origin)
        destiny = os.path.join(destiny_dir, name)
        if not os.path.exists(destiny):
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
                continue
        else:
            print("Already exists", destiny)
        return destiny


def play_mp4(path):
    print("Playing", path)
    player = vlc.MediaPlayer(path)
    player.play()
    time.sleep(3)
    while player.is_playing():
        time.sleep(3)


if __name__ == '__main__':
    destiny = get_random('C:\\Users\\emuvi\\OneDrive\\Documentos\\Aptar',
           '.mp4', 'C:\\Users\\emuvi\\Downloads')
    play_mp4(destiny)

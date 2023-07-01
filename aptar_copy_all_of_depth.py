import os
import shutil

root = 'C:\\Users\\emuvi\\OneDrive\\Documentos\\Aptar'
folder = 'C:\\Users\\emuvi\\Downloads'


def copy_all(path, depth, expected, folder, ends_with):
    if os.path.isdir(path):
        if depth == expected:
            for inside in os.listdir(path):
                origin = os.path.join(path, inside)
                if os.path.isfile(origin):
                    _, name = os.path.split(origin)
                    if name.endswith(ends_with):
                        destiny = os.path.join(folder, name)
                        shutil.copy(origin, destiny)
                        print(origin, " -> ", destiny)
        if depth < expected:
            for inside in os.listdir(path):
                compound = os.path.join(path, inside)
                if os.path.isdir(compound):
                    copy_all(compound, depth + 1, expected, folder, ends_with)


if __name__ == "__main__":
    copy_all(root, 0, 2, folder, '(1).pdf')

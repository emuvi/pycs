import os


def move_all(path, depth):
    if os.path.isdir(path):
        for inside in os.listdir(path):
            joined = os.path.join(path, inside)
            print(depth, joined)
            move_all(joined, depth + 1)


if __name__ == "__main__":
    move_all('C:\\Users\\emuvi\\OneDrive\\Documentos\\Aptar', 0)

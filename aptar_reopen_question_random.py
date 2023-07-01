import os
import random

root = "C:\\Users\\emuvi\\OneDrive\\Documentos\\Aptar\\QG - Questões Gerais"
group = os.listdir(root)
while True:
    inside = group[random.randint(0, len(group) - 1)]
    if not inside.endswith(".html"):
        continue
    target = os.path.join(root, inside)
    os.startfile(target)
    break

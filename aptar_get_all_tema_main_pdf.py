import os
import shutil


def get_all(path, depth, destiny):
    if os.path.isdir(path):
        files_and_size = []
        for inside in os.listdir(path):
            compound = os.path.join(path, inside)
            if os.path.isfile(compound):
                files_and_size.append((compound, os.path.getsize(compound)))
        files_and_size.sort(key=lambda tup: tup[1], reverse=True)
        found = False
        for item in files_and_size:
            origin = item[0]
            kind = os.path.splitext(origin)[1]
            if kind == '.pdf':
                parts = origin.split(os.sep)
                prefix = ''
                if depth > 1:
                    for i in range(2, depth + 2):
                        part = parts[-i]
                        index = part.find(' - ')
                        if index >= 0:
                            part = part[index + 3:].strip()
                            if prefix == '':
                                prefix = part
                            else:
                                prefix = part + ' - ' + prefix                
                destiny_file = prefix + kind
                destiny_file = os.path.join(destiny, destiny_file)
                print(origin, " -> ", destiny_file)
                shutil.copyfile(origin, destiny_file)
                found = True
            if found:
                break
        if depth < 2:
            for inside in os.listdir(path):
                compound = os.path.join(path, inside)
                if os.path.isdir(compound):
                    get_all(compound, depth + 1, destiny)


if __name__ == "__main__":
    get_all('C:\\Users\\emuvi\\OneDrive\\Documentos\\Aptar',
               0, 'C:\\Users\\emuvi\\Downloads')

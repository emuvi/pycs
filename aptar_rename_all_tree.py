import os

last_prefix = 'APT - '

def rename_all(path, depth):
    global last_prefix
    if os.path.isdir(path):
        files_and_size = []
        for inside in os.listdir(path):
            compound = os.path.join(path, inside)
            if os.path.isfile(compound):
                files_and_size.append((compound, os.path.getsize(compound)))
        files_and_size.sort(key=lambda tup: tup[1], reverse=True)
        for item in files_and_size:
            origin = item[0]
            parts = origin.split(os.sep)
            prefix = parts[-2]
            if not parts[-1].startswith('APT - ') and not parts[-1].startswith('AP - '):
                prefix = last_prefix + prefix
            elif not parts[-1].startswith('APT - '):
                prefix = 'APT - ' + prefix
                last_prefix = 'APT - '
            else:
                prefix = 'AP - ' + prefix
                last_prefix = 'AP - '
            kind = os.path.splitext(origin)[1]
            folder = os.path.dirname(origin)
            attempt = 1
            destiny = os.path.join(folder, prefix + ' (' + str(attempt) + ')' + kind)
            while os.path.exists(destiny):
                attempt += 1
                destiny = os.path.join(folder, prefix + ' (' + str(attempt) + ')' + kind)
            os.rename(origin, destiny)
            print(origin, " -> ", destiny)
        for inside in os.listdir(path):
            compound = os.path.join(path, inside)
            if os.path.isdir(compound):
                rename_all(compound, depth + 1)


if __name__ == "__main__":
    rename_all('C:\\Users\\emuvi\\OneDrive\\Documentos\\Aptar', 0)

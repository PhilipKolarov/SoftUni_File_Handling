from os import listdir
from os.path import isdir, join

def directory_traversal(path, files_by_ext):
    for el in listdir(path):
        if isdir(join(path, el)):
            directory_traversal(join(path, el), files_by_ext)
        else:
            extension = el.split('.')[-1]
            if extension not in files_by_ext:
                files_by_ext[extension] = []
            files_by_ext[extension].append(el)
    return files_by_ext

result = {}
result = directory_traversal('./', result)

for key, values in result.items():
    print(f".{key}")
    for value in values:
        print(f"- - - {value}")

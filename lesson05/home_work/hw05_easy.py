# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def mk_dir(dir):
    dir_path = os.path.join(os.getcwd(), dir)
    try:
        os.mkdir(dir_path)
        print('Создана папка ', dir_path)
    except FileExistsError:
        print('Такая директория уже существует')
    
def rm_dir(dir):
    dir_path = os.path.join(os.getcwd(), dir)
    try:
        os.rmdir(dir_path)
        print('Удалена папка ', dir_path)
    except FileExistsError:
        print('Такая директория не существует')
        
n = ['dir_'+str(_+1) for _ in range(9)]

for i in n:
    mk_dir(str(i))

for i in n:
    rm_dir(str(i))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

dirs = os.listdir(os.getcwd())

for i in dirs:
    if os.path.isdir(os.getcwd()+'/'+i):
        print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys
import shutil

try:
    shutil.copy(sys.argv[0], 'copy_'+sys.argv[0])
    print('Создана копия текущего файла',sys.argv[0])
except:
    print('Текущий файл скопировать неудалось')
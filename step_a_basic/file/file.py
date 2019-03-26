import os
from operator import itemgetter

# Saman Alishiri samanalishiri@gmail.com

files = os.listdir('./')
python_files = [name for name in files if name.endswith('.py')]
sorted_files = sorted(python_files, key=lambda file: file)
for file in sorted_files:
    print(file)

print('###################################################')
files = os.listdir('./')
python_files = [{'file': name} for name in files if name.endswith('.py')]
python_files.sort(key=itemgetter('file'))
for file in python_files:
    print(file['file'])

print('###################################################')
index = 1
with open('sample.txt') as file:
    for line in file:
        print('line {}: {}'.format(index, line))
        index += 1

print('###################################################')
if not os.path.exists('hello.txt'):
    with open('hello.txt', 'wt') as file:
        file.write('Hello')

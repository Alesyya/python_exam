import os
#
# список тегов, которые должны иметь метку i18n
TAGS = ['p', 'button', 'h2', 'h']

# функция для проверки файла на наличие меток i18n у тегов
def check_file(filename):
   with open(filename, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            for tag in TAGS:
                if f'<{tag}' in line and 'i18n' not in line:
                    print(f'{filename} {i+1}: {line.strip()}')

 # функция для рекурсивного прохода по директории и проверки всех файлов
def check_directory(path):
    for filename in os.listdir(path):
        fullpath = os.path.join(path, filename)
        if os.path.isdir(fullpath):
            check_directory(fullpath)
        elif filename.endswith('.html'):
            check_file(fullpath)


check_directory('C:\\Users\\Неон\\Desktop\\test-i18n')

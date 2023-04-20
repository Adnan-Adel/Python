import os
import shutil
current_dir = os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir(current_dir):

    ## moving images('.png', .'.jpg', '.jpeg', '.gif') to 'Images' folder
    if filename.endswith(('.png', '.jpg', 'jpeg', 'gif')):
        if not os.path.exists('Images'):
            os.mkdir('Images')
        shutil.copy(filename, 'Images')
        os.remove(filename)

    ## moving docs('.pdf', '.doc', '.xlsx', '.pptx', '.docx', 'csv') to 'Documents' folder
    if filename.endswith(('.pdf', '.doc', '.xlsx', '.pptx', '.docx', 'csv')):
        if not os.path.exists('Documents'):
            os.mkdir('Documents')
        shutil.copy(filename, 'Documents')
        os.remove(filename)

    ## moving videos('.mp4', '.wmv') to 'Videos' folder
    if filename.endswith(('.mp4', '.wmv')):
        if not os.path.exists('Videos'):
            os.mkdir('Videos')
        shutil.copy(filename, 'Videos')
        os.remove(filename)

    ## moving apps('.exe', '.dmg') to 'Apps' folder
    if filename.endswith(('.exe', '.dmg')):
        if not os.path.exists('Apps'):
            os.mkdir('Apps')
        shutil.copy(filename, 'Apps')
        os.remove(filename)

    ## moving archive('.rar', '.zip') to 'Archives' folder
    if filename.endswith(('.rar', '.zip')):
        if not os.path.exists('Archives'):
            os.mkdir('Archives')
        shutil.copy(filename, 'Archives')
        os.remove(filename)

    ## moving codes('.c', .'.py', '.cpp') to 'Codes' folder
    if filename.endswith(('.c', '.py', '.cpp')):
        if not os.path.exists('Codes'):
            os.mkdir('Codes')
        shutil.copy(filename, 'Codes')
        os.remove(filename)
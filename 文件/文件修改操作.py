
import os

with open('file.txt','r',encoding='UTF-8') as f:
    with open('filebak.txt', 'w',encoding='UTF-8')as f1:
        old_content = f.read()
        new_content = old_content.replace('kangkai','kkkkk')
        f1.write(new_content)

os.remove('file.txt')
os.rename('filebak.txt', 'file.txt')


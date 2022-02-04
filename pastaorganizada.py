import os
import shutil


def Extensao(file_name):
    splited = file_name.split(".")
    return splited[-1]
# declara a função extensão com a variavel do nome do arquivo para poder
# vizualizar


def Validate_path(path):
    if os.path.isdir(path):
        return True
    else:
        os.mkdir(path)
# Cria pasta caso não tenha, o True é para vizualizar no debug


raiz = os.path.expanduser('~\\')
img_path = os.path.join(raiz, "Pictures")
# Acha a pasta raiz e define a pasta padrão como Imagens/Pictures
Ext_list = {
    "png": os.path.join(img_path, "png"),
    "pdf": os.path.join(img_path, "pdf"),
    "jpeg": os.path.join(img_path, "jpeg"),
    "gif": os.path.join(img_path, "gif"),
    "mp4": os.path.join(img_path, "mp4"),
    "exe": os.path.join(img_path, "exe"),
    "zip": os.path.join(img_path, "zip"),
    "jpeg": os.path.join(img_path, "jpeg"),
    "jpg": os.path.join(img_path, "jpg"),
    "outros": os.path.join(img_path, "outros")}

for Ext_name in Ext_list:
    Validate_path(Ext_list[Ext_name])
    # Convoca o nome da extensão dentro do dicionario de extensões

img_path_list_dir = os.listdir(img_path)
for file in img_path_list_dir:
    file_path = os.path.join(img_path, file)
    if os.path.isfile(file_path):

       # print(file_path,Ext)
        Ext = Extensao(file)
        if Ext in Ext_list:
            shutil.copy(file_path, Ext_list[Ext])
        else:
            shutil.copy(file_path, Ext_list["outros"])

# print(img_path_list_dir)

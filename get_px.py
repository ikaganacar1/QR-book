from PIL import Image
from qr import create_list_of_files
import json
from random import choice

def qr_130():
    dict1 = {}
    a = 0
    for j in create_list_of_files('cropped_qr'):

        im = Image.open(f"cropped_qr/{j}")

        width, height = im.size

        pixel_values = list(im.getdata())
        txt=""
        for i in pixel_values:
            
            if str(i) =='255':
                txt+='1'
            else:
                txt+='0'
        dict1[f"{a:03d}"] = txt
        a+=1

    with open('result.json', 'w') as fp:
        json.dump(dict1, fp)

def qr_00000000():
    dict1 = {}
    a = 0
    list0 = ['2','4','6','8']
    list1 = ['3','5','7','9']

    for j in create_list_of_files('cropped_qr_00000000'):

        im = Image.open(f"cropped_qr_00000000/{j}")

        pixel_values = list(im.getdata())
        txt=""
        for i in pixel_values:
            
            if str(i) =='255':
                txt+= str(choice(list1))
            else:
                txt+= str(choice(list0))

        dict1[f"{a:03d}"] = txt
        a+=1

    with open('result_00000000.json', 'w') as fp:
        json.dump(dict1, fp)

qr_00000000()

    
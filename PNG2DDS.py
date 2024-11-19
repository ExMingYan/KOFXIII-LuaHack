#!/usr/bin/env python3

import os
import platform
import sys
from PIL import Image

def ProcessFile(path:str):
    if os.path.isdir(path):
        files = os.listdir(path)
        for file in files: ProcessFile(os.path.join(path, file))
    elif path.endswith('.png'):
        png_image = Image.open(path)
        newpath = f'{os.path.splitext(path)[0]}.dds'
        png_image.save(newpath, 'dds')
        os.remove(path)
        os.system(f'echo {path}')

if __name__ == '__main__':
	try:
		FilePaths = sys.argv[1:]
		if len(FilePaths) == 0: raise Exception
	except:
		InputPaths = input('请输入文件路径或文件名（多文件以,隔开）：')
		FilePaths = InputPaths.split(',')
	finally:
		for FilePath in FilePaths:
			ProcessFile(FilePath)
		if platform.system() == 'Windows': os.system("pause")

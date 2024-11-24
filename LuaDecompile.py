#!/usr/bin/env python3

import os
import platform
import sys
from LuaCode import LUAFILEMAXSIZE

def ProcessFile(path:str)->None:
	if os.path.isdir(path):
		files = os.listdir(path)
		for file in files: ProcessFile(os.path.join(path, file))
	elif path.endswith('.lua'):
		if os.path.getsize(path) > LUAFILEMAXSIZE: sys.exit(f'{path}文件太大无法转换。')
		newpath = path.split('.')[0] + '_deCompile.' + path.split('.')[1]
		if (os.system(f'java -jar unluac.jar "{path}">"{newpath}"')):
			os.system(f'echo {path}错误')
			os.system(f'rm -f "{newpath}')
		else:
			os.system(f'mv -f "{newpath}" "{path}"')
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

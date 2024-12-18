#!/usr/bin/env python3

import os
import platform
import sys
from LuaCode import LUAFILEMAXSIZE

def deCodeCompile(path:str)->None:
	with open(path, 'rb') as fread:
		waitdeCode = fread.read()
		afterdeCode = list(map(lambda x: int(x) ^ 0x66, waitdeCode))
	newpath = path.split('.')[0] + '_deCode.' + path.split('.')[1]
	with open(newpath, 'wb') as fwrite:
		fwrite.write(bytes(afterdeCode))
	if (os.system(f'java -jar unluac.jar "{newpath}">"{path}"')):
		os.system(f'echo {path}错误')
	else:
		os.system(f'echo {path}')
	os.system(f'rm -f {newpath}')

def ProcessFile(path:str)->None:
	if os.path.isdir(path):
		files = os.listdir(path)
		for file in files: ProcessFile(os.path.join(path, file))
	elif path.endswith('.lua'):
		if os.path.getsize(path) > LUAFILEMAXSIZE: sys.exit(f'{path}文件太大无法转换。')
		deCodeCompile(path)

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

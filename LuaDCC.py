#/usr/bin/env python3

import os
import sys
from LuaCode import CONVERTLIST, LUAFILEMAXSIZE


def deCodeCompile(path:str)->None:
	with open(path, 'rb') as fread:
		waitdeCode = fread.read()
		afterdeCode = list(map(lambda x: (CONVERTLIST[int(x) >> 4] << 4) | CONVERTLIST[int(x) & 0xF], waitdeCode))
	newpath = path.split('.')[0] + '_deCode.' + path.split('.')[1]
	with open(newpath, 'wb') as fwrite:
		fwrite.write(bytes(afterdeCode))
	os.system(f'java -jar unluac.jar "{newpath}">"{path}"')
	os.remove(newpath)

def ProcessFile(path:str)->None:
	if os.path.isdir(path):
		files = os.listdir(path)
		for file in files: ProcessFile(os.path.join(path, file))
	elif path.endswith('.lua'):
		if os.path.getsize(path) > LUAFILEMAXSIZE: exit(f'{path}文件太大无法转换。')
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

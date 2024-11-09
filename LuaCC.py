#/usr/bin/env python3

import os
import sys
from LuaCode import CONVERTLIST, LUAFILEMAXSIZE

def Code(path:str, Size:int)->None:
	os.system(f'luac -o "{path}" "{path}"')
	with open(path, 'rb') as fread:
		waitCode = fread.read(Size)
		afterCode = list(map(lambda x: (CONVERTLIST[int(x) >> 4] << 4) | CONVERTLIST[int(x) & 0xF], waitCode))
	with open(path, "wb") as fwrite:
		fwrite.write(bytes(afterCode))

def ProcessFile(path:str)->None:
	if os.path.isdir(path):
		files = os.listdir(path)
		for file in files: ProcessFile(os.path.join(path, file))
	elif path.endswith('.lua'):
		filesize = os.path.getsize(path)
		if filesize > LUAFILEMAXSIZE: exit(f'{path}文件太大无法转换。')
		Code(path, filesize)

if __name__ == '__main__':
	try:
		FilePaths = sys.argv[1:]
		if len(FilePaths) == 0: raise Exception
	except:
		InputPath = input('请输入文件路径或文件名（多文件以,隔开）：')
		FilePaths = InputPath.split(',')
	finally:
		for FilePath in FilePaths:
			ProcessFile(FilePath)

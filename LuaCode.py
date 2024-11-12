#/usr/bin/env python3

import os
import sys

LUAFILEMAXSIZE = 32 * 1024 * 1024
CONVERTLIST = [6, 7, 4, 5, 2, 3, 0, 1, 14, 15, 12, 13, 10, 11, 8, 9]

def ProcessFile(path:str):
	if os.path.isdir(path):
		files = os.listdir(path)
		for file in files: ProcessFile(os.path.join(path, file))
	elif path.endswith('.lua'):
		if os.path.getsize(path) > LUAFILEMAXSIZE: exit(f'{path}文件太大无法转换。')
		with open(path, 'rb') as fread:
			waitCode = fread.read()
			afterCode = list(map(lambda x: (CONVERTLIST[int(x) >> 4] << 4) | CONVERTLIST[int(x) & 0xF], waitCode))
		with open(path, "wb") as fwrite:
			fwrite.write(bytes(afterCode))

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

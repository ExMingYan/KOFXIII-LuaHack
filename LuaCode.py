#/usr/bin/env python3

import os
import sys

LUAFILEMAXSIZE = 20 * 1024 * 1024

def ConvertValue(value:int)->int:
	Remainder = value % 8
	if Remainder < 2: value += 6
	elif Remainder < 4: value += 2
	elif Remainder < 6: value -= 2
	else: value -= 6
	return value

def ProcessFile(path:str):
	if os.path.isdir(path):
		files = os.listdir(path)
		for file in files: ProcessFile(os.path.join(path, file))
	elif path.endswith('.lua'):
		filesize = os.path.getsize(path)
		if filesize > LUAFILEMAXSIZE: exit(f'{path}文件太大无法转换。')
		with open(path, 'rb') as fread:
			waitCode = fread.read(filesize)
			afterCode = list(map(lambda x: (ConvertValue(int(x) >> 4) << 4) | ConvertValue(int(x) & 0xF), waitCode))
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
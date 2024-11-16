#/usr/bin/env python3

import os
import platform
import sys

def ProcessFile(path:str):
	if os.path.isdir(path):
		files = os.listdir(path)
		for file in files: ProcessFile(os.path.join(path, file))
	elif path.endswith('.png'):
		with open(path, 'rb') as fread:
			waitCode = fread.read()
			afterCode = list(map(lambda x: int(x) ^ 0x75, waitCode))
		with open(path, "wb") as fwrite:
			fwrite.write(bytes(afterCode))
		os.system(f'echo {path}')

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
		if platform.system() == 'Windows': os.system('pause')

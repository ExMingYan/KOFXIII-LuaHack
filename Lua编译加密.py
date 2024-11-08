import struct
import os
import sys

def ConvertValue(value):
	Remainder = value % 8
	if Remainder < 2: value += 6
	elif Remainder < 4: value += 2
	elif Remainder < 6: value -= 2
	else: value -= 6
	return value

def Code(path:str, Size:int)->None:
	os.system(f'luac -o {path} {path}')
	with open(path, 'rb') as fread:
		waitCode = fread.read(Size)
		afterCode = []
		for value in waitCode:
			tens = ConvertValue(int(value) // 16)
			units = ConvertValue(int(value) % 16)
			afterCode.append(tens * 16 + units)
	with open(path, "wb") as fwrite:
		for x in afterCode:
			a = struct.pack('B',x)
			fwrite.write(a)

def ProcessFile(path:str):
	if os.path.isdir(path):
		files = os.listdir(path)
		for file in files:
			ProcessFile(os.path.join(path, file))
	elif str(path).endswith('.lua'):
		filesize = os.path.getsize(path)
		if filesize > 20971520:
			exit(f'{path}文件太大无法转换。')
		Code(path, filesize)

if __name__ == '__main__':
	try:
		FilePaths = sys.argv[1:]
		if len(FilePaths) == 0: raise Exception
	except:
		InputPath = input("请输入文件路径或文件名（多文件以,隔开）：")
		FilePaths = InputPath.split(',')
	finally:
		for FilePath in FilePaths:
			ProcessFile(FilePath)

import struct
import os
import sys

def ConvertValue(value:int)->int:
	Remainder = value % 8
	if Remainder < 2: value += 6
	elif Remainder < 4: value += 2
	elif Remainder < 6: value -= 2
	else: value -= 6
	return value

def deCodeCompile(path:str, Size:int)->None:
	with open(path, 'rb') as fread:
		waitdeCode = fread.read(Size)
		afterdeCode = []
		for value in waitdeCode:
			tens = ConvertValue(int(value) // 16)
			units = ConvertValue(int(value) % 16)
			afterdeCode.append(tens * 16 + units)
	newpath = path.split('.')[0] + '_deCode.' + path.split('.')[1]
	with open(newpath, "wb") as fwrite:
		for x in afterdeCode:
			a = struct.pack('B',x)
			fwrite.write(a)
	os.system(f"java -jar unluac.jar {newpath}>{path}")
	os.remove(newpath)

def ProcessFile(path:str):
	if os.path.isdir(path):
		files = os.listdir(path)
		for file in files:
			ProcessFile(os.path.join(path, file))
	elif str(path).endswith('.lua'):
		filesize = os.path.getsize(path)
		if filesize > 20971520:
			exit(f'{path}文件太大无法转换。')
		deCodeCompile(path, filesize)

if __name__ == '__main__':
	try:
		FilePaths = sys.argv[1:]
		if len(FilePaths) == 0: raise Exception
	except:
		InputPaths = input("请输入文件路径或文件名（多文件以,隔开）：")
		FilePaths = InputPaths.split(',')
	finally:
		for FilePath in FilePaths:
			ProcessFile(FilePath)

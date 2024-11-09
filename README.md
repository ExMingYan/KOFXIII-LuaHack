# 使用指南

## 使用的其他项目源码链接

1. [unluac](https://github.com/HansWessels/unluac)
2. [lua](https://github.com/lua/lua)

## 环境配置

1. Python3.12
2. Java

## 使用方法

1. 将py文件和unluac.jar、luac.exe放在同一个文件夹
2. 将需要解密反编译的文件拖到Lua解密反编译.py上，等待py执行完毕后修改
3. 将修改后的文件拖到Lua编译加密.py上，等待执行完毕

## 自编译luac.exe（可选）

```cmd
cd Lua/src
make lua luac
mv luac.exe ../..
```

## 注意

1. 本项目中编译和使用lua和luac使用的版本为5.1.4，数据类型为int32和float
2. Java和Python均需加入环境变量
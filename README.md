# 使用指南

## 使用的其他项目源码链接

1. [unluac](https://github.com/HansWessels/unluac)
2. [lua](https://github.com/lua/lua)

## 环境配置

1. Python3.12
2. Java

## 使用方法

- 解密反编译+编译加密

  1. 将py文件和unluac.jar、luac.exe放在同一个文件夹
  2. 将需要解密反编译的文件拖到LuaDCC.py上，等待py执行完毕后修改
  3. 将修改后的文件拖到LuaCC.py上，等待执行完毕

- 仅加解密

  - 将需要加密/解密的文件拖到LuaCode.py上，等待py执行完毕

- 仅反编译/编译（单个文件）

  1. 反编译

     ```cmd
     java -jar unluac.jar "Lua文件路径">"输出文件路径"
     ```

  2. 编译

     ```cmd
     luac -o "输出文件路径" "Lua文件路径"
     ```

## 自编译luac.exe（可选）

```cmd
cd Lua/src
make lua luac
mv luac.exe ../..
```

## 注意

1. 本项目中编译和使用lua和luac使用的版本为5.1.4，数据类型为int32和float
2. Java和Python均需加入环境变量
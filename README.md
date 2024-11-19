# 使用指南

## 使用的其他项目源码链接

1. [unluac](https://github.com/HansWessels/unluac)
2. [lua](https://github.com/lua/lua)

## 环境配置

1. Python3.12
2. Java

## 使用方法

- Lua解密反编译+编译加密

  1. 将py文件和unluac.jar、luac.exe放在同一个文件夹
  2. 将需要解密反编译的Lua文件拖到LuaDCC.py上，等待py执行完毕后按需修改
  3. 将修改后的Lua文件拖到LuaCC.py上，等待执行完毕

- Lua加解密

  - 将需要加密/解密的Lua文件拖到LuaCode.py上，等待py执行完毕

- Lua反编译/编译

  - 将需要反编译的Lua文件拖到LuaDecompile.py上，等待py执行完毕
  - 将需要编译的Lua文件拖到LuaCompile.py上，等待py执行完毕

- PNG加解密

  - 将需要加密/解密的png文件拖到PNGCode.py上，等待py执行完毕

- DDS转PNG

  1. 安装Pillow库

     ```cmd
     pip install Pillow
     ```

  2. 将需要转换的dds文件拖到DDS2PNG.py上，等待py执行完毕

- PNG转DDS

  1. 安装Pillow库

     ```cmd
     pip install Pillow
     ```

  2. 将需要转换的png文件拖到PNG2DDS.py上，等待py执行完毕

- 仅反编译/编译（单个文件）

  1. 反编译

     ```cmd
     java -jar unluac.jar "Lua文件路径">"输出文件路径"
     ```

  2. 编译

     ```cmd
     luac -o "输出文件路径" "Lua文件路径"
     ```

- 注入字节码
  1. 将kofxiii.exe移至和Insert.py、InsertConfig.py所在目录
  2. 按需修改Insert.py和InsertConfig.py
  3. 运行Insert.py

## 目前支持编译的lua文件

- fighter/ai_config.lua
- fighter/command_table.lua
- fighter/collision_table.lua
- script/game_config.lua
- script/game_params.lua
- script/menu.lua
- script/scene_config.lua
- script/sound_config.lua
- ui/lua_files/Skill_*.lua
- ui/lua_files/trial_*.lua
- ui/lua_files/Story.lua
- ui/lua_files/Tutorial.lua

## 自编译luac.exe（可选）

```cmd
cd Lua/src
make lua luac
mv -f luac.exe ../..
```

## 注意

1. 本项目中编译和使用的lua和luac版本为5.1.4，数据类型为int32和float
2. Java和Python均需加入环境变量
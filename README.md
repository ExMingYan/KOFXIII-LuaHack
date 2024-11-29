# 使用指南

## 使用的其他项目源码链接

- [unluac](https://github.com/HansWessels/unluac)
- [lua](https://github.com/lua/lua)

## 环境配置需求

- Python3.10
- Java

## 使用方法

- Lua解密反编译+编译加密

  1. 将LuaCode.py、LuaDCC.py、LuaCC.py、unluac.jar和luac.exe放在同一个文件夹
  2. 将需要解密反编译的Lua文件拖到LuaDCC.py上，等待py执行完毕后按需修改
  3. 将修改后的Lua文件拖到LuaCC.py上，等待执行完毕

- Lua加解密

  - 将需要加密/解密的Lua文件拖到LuaCode.py上，等待py执行完毕

- Lua反编译/编译

  - 将LuaCode.py、LuaDecompile.py、LuaCompile.py、unluac.jar和luac.exe放在同一个文件夹
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
- script/bg_params.lua
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

## 附录

### 角色代码表

|   角色   | 代码（HEX） | 代码（DEC） |
| :------: | :---------: | :---------: |
| 伊丽莎白 |    0x00     |      0      |
|   神武   |    0x01     |      1      |
|   堕珑   |    0x02     |      2      |
|  草薙京  |    0x03     |      3      |
|   红丸   |    0x04     |      4      |
|   大门   |    0x05     |      5      |
|   爪八   |    0x06     |      6      |
|   麦卓   |    0x07     |      7      |
|   薇丝   |    0x08     |      8      |
|   特瑞   |    0x09     |      9      |
|   安迪   |    0x0A     |     10      |
|   东丈   |    0x0B     |     11      |
|  雅典娜  |    0x0C     |     12      |
|  椎拳崇  |    0x0D     |     13      |
|  镇元斋  |    0x0E     |     14      |
|  金家藩  |    0x0F     |     15      |
|   霍查   |    0x10     |     16      |
|   雷电   |    0x11     |     17      |
|  坂崎良  |    0x12     |     18      |
|  罗伯特  |    0x13     |     19      |
| 坂崎琢磨 |    0x14     |     20      |
|  拉尔夫  |    0x15     |     21      |
|  克拉克  |    0x16     |     22      |
|  莉安娜  |    0x17     |     23      |
|   阿修   |    0x18     |     24      |
|  红斋祀  |    0x19     |     25      |
|   黑修   |    0x1A     |     26      |
| 不知火舞 |    0x1B     |     27      |
|    琼    |    0x1C     |     28      |
| 坂崎尤莉 |    0x1D     |     29      |
|   火八   |    0x1E     |     30      |
|   比利   |    0x1F     |     31      |
|    K'    |    0x20     |     32      |
|   库拉   |    0x21     |     33      |
| 马克西马 |    0x22     |     34      |
|   咬草   |    0x23     |     35      |
|   天狗   |    0x24     |     36      |
|  白斋祀  |    0x25     |     37      |

## 注意

1. 本项目中编译和使用的lua和luac版本为5.1.4，数据类型为int32和float
2. Java和Python均需加入环境变量
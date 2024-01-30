<div align="center">

![botpy](https://socialify.git.ci/StarXinXin/PickStars-Bot/image?description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Fvip.helloimg.com%2Fi%2F2023%2F11%2F24%2F6560b3298b7e0.png&name=1&owner=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Light)
[![Language](https://img.shields.io/badge/language-python-green.svg?style=plastic)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-orange.svg?style=plastic)](https://github.com/StarXinXin/PickStars-Bot/blob/master/LICENSE)
![Python](https://img.shields.io/badge/python-3.12+-blue)

_✨ 摘星辰 QQ频道机器人 ✨_

[爱发电]()
·
[开发者频道]()

</div>

## 机器人指令

    /菜单
        获取机器人菜单
        示例：/菜单
    /天气查询 城市
        查询当地天气情况
        示例：/天气查询 深圳

## 使用方法

使用代码库前需要配置好相关的信息，可以跟随下面的步骤进行

### 环境安装

py包的依赖配置，通过`pip install -r requirements.txt` 可以安装所有的依赖包

### 运行机器人

在代码库根目录执行下面命令

```shell
python3 bot.py
```

## 代码说明

    .
    ├── util.py             # 字符相关的处理
    ├── command_register.py # 指令的装饰器处理
    ├── requirements.txt    # py包的依赖配置，通过`pip install -r requirements.txt` 可以安装所有的依赖包
    ├── bot.py              # 程序运行入口，包括不同指令的处理

## 特别感谢

- [Python SDK](https://github.com/tencent-connect/botpy) 为摘星辰开发提供SDK

[//]: # (## 免责声明)
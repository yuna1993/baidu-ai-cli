# Name

 Author：@Yuna Pan

## Introduction - 介绍

本项目将Baidu AI相关API接口转化为CLI，方便客户/售前/售后利用该项目批量操作，使接口更易用。使用者用一条Command，最多三个要素完成测试：提供AppKey/SecretKey以及需要检测的Source文档，就可以获得对应Json Results（按照检测资源文件名生成Json文件）

### Summary - 概要

已经完成开发：
百度内容审核 - 文本审核
CLI转换相关的基本功能包括：
1. Get Baidu Token
2. AK/SK注册
3. yaml文件AK/SK读写
4. 批量Assets调用接口支持CLI
5. 单个Assets调用接口支持CLI

待开发：
内容审核其他API
其他AI相关的API

### Features - 特性

目前支持的功能：
内容审核-文本审核：
1. 读取config.yaml验证AK/SK是否存在或有效，若不存在需要注册在config.yaml.仅需注册一次就可以，无需每次重复输入AK/SK。
2. 读取config.yaml认证，单个txt文件(一行一个)Scan并输出json结果，结果输出在output/文件夹下，命令如下：
    
    python3 main.py -t -p assets/text/a.txt 

    也可以将命令补全：
    python3 main.py --text_audit --path assets/text/a.txt 
    

3.  读取config.yaml认证，扫描全量assets/text/*并输出json结果，结果输出在output/文件夹下，文件名与txt文件名一一对应。命令如下：
    
    python3 main.py -t 

    也可以将命令补全：
    python3 main.py --text_audit


## Requirements - 必要条件（环境，对所有项目，和所有子模块和库的描述。）

环境：


requests==2.25.1


PyYAML==6.0

安装环境：pip3 install -r requirements.txt 

## Configuration - 配置（配置信息。）

## Installation - 安装（如何安装。）

## Usage - 用法（用法。）
1. 读取config.yaml验证AK/SK是否存在或有效，若不存在需要注册在config.yaml.仅需注册一次就可以，无需每次重复输入AK/SK。
2. 读取config.yaml认证，单个txt文件Scan并输出json结果，结果输出在output/文件夹下，命令如下：
    
    python3 main.py -t -p assets/text/a.txt 

    也可以将命令补全：
    python3 main.py --text_audit --path assets/text/a.txt 
    

3.  读取config.yaml认证，扫描全量assets/text/*并输出json结果，结果输出在output/文件夹下，文件名与txt文件名一一对应。命令如下：
    
    python3 main.py -t 

    也可以将命令补全：
    python3 main.py --text_audit


## Support - 支持

Please contact panyunan2015@163.com



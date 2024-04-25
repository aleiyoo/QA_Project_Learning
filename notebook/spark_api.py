#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2024/1/16 14:14
# @Author  : alei
# @File    : spark_api.py
# 封装本地api

from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()  # 创建 api 对象


# 定义一个数据模型，用于接收POST请求中的数据
class Item(BaseModel):
    prompt: str  # 用户 prompt
    temperature: float  # 温度系数
    max_tokens: int  # token 上限
    if_list: bool = False  # 是否多轮对话


@app.post("/spark/")
async def get_spark_response(item: Item):
    # 实现星火大模型调用的 API 端点
    response = get_spark(item)
    return response


import SparkApiSelf
# 首先定义一个构造参数函数
def getText(role, content, text=[]):
    # role 是指定角色，content 是 prompt 内容
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text


def get_spark(item):
    # 配置 spark 秘钥
    # 以下密钥信息从控制台获取
    appid = "b0e2bce3"  # 填写控制台中获取的 APPID 信息
    api_secret = "YTQ5YmQ4OTQ5MTlmOTgwYmNlYTk0Mjg3"  # 填写控制台中获取的 APISecret 信息
    api_key = "668d1d0234bd9c3cc53e57dba147a840"  # 填写控制台中获取的 APIKey 信息
    domain = "generalv3"  # v3.0版本
    Spark_url = "ws://spark-api.xf-yun.com/v3.1/chat"  # v3.0环境的地址

    # 构造请求参数
    if item.if_list:
        prompt = item.prompt
    else:
        prompt = getText("user", item.prompt)

    response = SparkApiSelf.main(appid, api_key, api_secret, Spark_url, domain, prompt, item.temperature,
                                 item.max_tokens)
    return response


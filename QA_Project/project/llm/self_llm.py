#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2024/2/3 10:38
# @Author  : alei
# @File    : self_llm.py
# 基于LangChain的自定义LLM基类

from langchain.llms.base import LLM
from typing import Dict, Any, Mapping
from pydantic import Field


class Self_LLM(LLM):
    # 自定义 LLM
    # 继承自 langchain.llms.base.LLM
    # 原生接口地址
    url: str = None
    # 默认选用 ERNIE-Bot-4 模型，即目前一般所说的百度文心大模型
    model_name: str = "ERNIE-Bot-4"
    # 访问时延上限
    request_timeout: float = None
    # 温度系数
    temperature: float = 0.1
    # API_Key
    api_key: str = None
    # 必备的可选参数
    model_kwargs: Dict[str, Any] = Field(default_factory=dict)

    # 定义一个返回默认参数的方法
    @property
    def _default_params(self) -> Dict[str, Any]:
        """获取调用默认参数。"""
        normal_params = {
            "temperature": self.temperature,
            "request_timeout": self.request_timeout,
        }
        # print(type(self.model_kwargs))
        return {**normal_params}

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {**{"model_name": self.model_name}, **self._default_params}


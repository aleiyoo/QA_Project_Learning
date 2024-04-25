#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2024/2/27 17:48
# @Author  : alei
# @File    : call_embedding.py
# 封装Embedding
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from embedding.zhipuai_embedding import ZhipuAIEmbeddings
from langchain_community.embeddings import QianfanEmbeddingsEndpoint
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
# from langchain.embeddings.openai import OpenAIEmbeddings
from llm.call_llm import parse_llm_api_key

def get_embedding(embedding: str, embedding_key: str=None, env_file: str=None):
    if embedding_key == None:
        embedding_key = parse_llm_api_key(embedding)
        # print(embedding_key)
    if embedding == "wenxin":
        # print(embedding_key)
        return QianfanEmbeddingsEndpoint(qianfan_ak=embedding_key[0],qianfan_sk=embedding_key[1])
    elif embedding == "zhipuai":
        return ZhipuAIEmbeddings(zhipuai_api_key=embedding_key)
    elif embedding == 'm3e':
        return HuggingFaceEmbeddings(model_name="moka-ai/m3e-base")
    else:
        raise ValueError(f"embedding {embedding} not support ")

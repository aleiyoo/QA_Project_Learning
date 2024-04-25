# 基于LangChain的个人知识库问答助手
- notebook文件夹：各步骤的一些示例代码。
- QA_Project：项目数据、代码

## 一. 核心功能
1. MarkDown 文件及用户上传文档向量化，并创建知识库.
2. 选择知识库，检索用户提问的知识片段.
3. 提供知识片段与提问，获取大模型回答.
4. 流式回复.
5. 历史对话记录.
## 二. 技术架构和工具
1. 框架：LangChain
2. Embedding 模型：智谱、百度文心
3. 数据库：Chroma
4. 大模型：讯飞星火、文心一言、GLM 等
5. 前后端：Gradio
① LLM 层主要基于几种流行 LLM API 进行了 LLM 调用封装，支持用户以统一的入口、方式来访问不同的模型，支持随时进行模型的切换；

② 数据层主要包括个人知识库的源数据以及 Embedding API，源数据经过 Embedding 处理可以被向量数据库使用；

③ 数据库层主要为基于个人知识库源数据搭建的向量数据库，在本项目中选择了Chroma；

④ 应用层为核心功能的最顶层封装，基于 LangChain 提供的检索问答链基类进行了进一步封装，从而支持不同模型切换以及便捷实现基于数据库的检索问答；

⑤ 最顶层为服务层，分别实现了 Gradio 搭建 Demo 与 FastAPI 组建 API 两种方式来支持本项目的服务访问。

## 最终效果
![image](https://github.com/aleiyoo/QA_Project_Learning/assets/76715957/5bec851c-4a6d-4e6d-a30b-ab285bfbfddc)

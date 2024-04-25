import sys 
sys.path.append("../")
from llm.spark_llm import Spark_LLM

from langchain_community.chat_models.baidu_qianfan_endpoint import QianfanChatEndpoint
from llm.call_llm import parse_llm_api_key
from llm.zhipuai_llm import ZhipuAILLM

def model_to_llm(model:str=None, temperature:float=0.1, appid:str=None, api_key:str=None,Spark_api_secret:str=None,Wenxin_secret_key:str=None):
        """
        星火：model,temperature,appid,api_key,api_secret
        百度文心：model,temperature,api_key,api_secret
        智谱：model,temperature,api_key
        """
        if model in ["ERNIE-Bot", "ERNIE-Bot-4", "ERNIE-Bot-turbo"]:
            if api_key == None or Wenxin_secret_key == None:
                api_key, Wenxin_secret_key = parse_llm_api_key("wenxin")
            # print(f"qianfan_ak:{api_key}")
            # print(f"qianfan_sk:{Wenxin_secret_key}")
            llm = QianfanChatEndpoint(model=model, temperature = temperature, qianfan_ak=api_key, qianfan_sk=Wenxin_secret_key)
        elif model in ["Spark-1.5", "Spark-3.0"]:
            if api_key == None or appid == None and Spark_api_secret == None:
                api_key, appid, Spark_api_secret = parse_llm_api_key("spark")
            llm = Spark_LLM(model=model, temperature = temperature, appid=appid, api_secret=Spark_api_secret, api_key=api_key)
        elif model in ["glm-4", "glm-4v", "glm-3-turbo"]:
            if api_key == None:
                api_key = parse_llm_api_key("zhipuai")
            llm = ZhipuAILLM(model=model, api_key=api_key, temperature = temperature)
        else:
            raise ValueError(f"model{model} not support!!!")
        return llm
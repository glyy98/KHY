import pytest
import requests
import yaml 
import allure
from test_login import login

def load_yaml(file_path):     
    with open (file_path,'r',encoding='utf-8') as file :
        return yaml.safe_load(file)
    
@allure.title("引用登录用例")
@pytest.fixture    #装饰器核心在于减少重复代码，调用登录函数返回token
def token():
    return login()


@allure.title("测试新增任务功能（任务看板）")  #给用例定义标题
def test_addtask(token):   
    
    #先将任务所有的值拿过来，引入顶层键
    task_data=load_yaml('./data/task_data.yaml')['task_data']  
    task_url=task_data['task_url']
    headers = {**task_data['headers'], 'Authorization': f'Bearer {token}'}  #组装请求头，这个Bearer在加token时需要空格
    addtask=task_data['addtask']   #新增任务时所传的参数
    print(f'任务数据{task_data}')

    
    response=requests.post(task_url,json=addtask,headers=headers)  #组装请求参数
    #校验响应数据的状态码是否为200，否则输出提示
    assert response.status_code==200,f'添加任务失败,{response.text}'

    response_data=response.json()
    print(response_data)
    assert response_data['isSuccess']==True,f'添加任务失败,{response.text}'

  
# pytest .\test_case\test_addtast.py  --alluredir=./allure-results




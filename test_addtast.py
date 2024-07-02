import pytest
import requests
from test_login import login


@pytest.fixture    #装饰器核心在于减少重复代码，调用登录函数返回token
def token():
    return login()

def test_addtask(token):
    base_url='https://dev.mhiiot.cn/openapi/project/api'   #基础地址
    add_task_url=f'{base_url}/TaskTable/add'  #基础地址+接口路径

    headers={'Content-Type':'application/json',
             'Authorization':f'Bearer {token}'}  #这个Bearer在加token时需要空格
    #传参
    task_data={
  "taskType": 3,   #维修
  "deviceDynamicInfoId": [ "495096115801096261"],  #设备小类
  "maintenanceContent": "调用测试",   #检修内容
  "maintenanceMethods": "",
  "maintenanceStandards": "",
  "maintenanceTime": "2024-07-03 00:00:00",  #检修时间
  "leader": ["558143240922988613"],  #负责人
  "taskStatus": 1,   #进行中
  "craneId": "421471904994426949",   #起重机id
  "remark": ""   }#自定义设备
    
    response=requests.post(add_task_url,json=task_data,headers=headers)
    #校验响应数据的状态码是否为200，否则输出提示
    assert response.status_code==200,f'添加任务失败,{response.text}'

    response_data=response.json()
    print(response_data)
    assert response_data['isSuccess']==True,f'添加任务失败,{response.text}'



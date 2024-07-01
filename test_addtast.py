import pytest
import requests
from test_login import login


@pytest.fixture
def token():
    return login()

def test_addtask(token):
    base_url='https://dev.mhiiot.cn/openapi/project/api'  
    add_task_url=f'{base_url}/TaskTable/add'

    headers={'Content-Type':'application/json',
             'Authorization':f'Bearer {token}'}
    
    task_data={
  "taskType": 3,   #维修
  "deviceDynamicInfoId": [ "495096115801096261"],  #设备小类
  "maintenanceContent": "接口自动化",   #检修内容
  "maintenanceMethods": "",
  "maintenanceStandards": "",
  "maintenanceTime": "2024-06-28 00:00:00",  #检修时间
  "leader": ["558143240922988613"],  #负责人
  "taskStatus": 1,   #进行中
  "craneId": "421471904994426949",   #起重机id
  "remark": ""   }#自定义设备
    
    response=requests.post(add_task_url,json=task_data,headers=headers)

    assert response.status_code==200,f'添加任务失败,{response.text}'

    response_data=response.json()
    print(response_data)
    assert response_data['isSuccess']==True,f'添加任务失败,{response.text}'



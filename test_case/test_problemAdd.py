import requests
import pytest
from test_case.test_login import login

@pytest.fixture
def token():
    return login()  #注意是返回login方法加括号

def test_problemAdd(token):
    base_url='https://dev.mhiiot.cn/openapi/project/api'
    problemAdd_url=f'{base_url}/ProblemFeedback/Add'

    headers={'Content-Type':'application/json',
             'Authorization':f'Bearer {token}'}  #这个Bearer在加token时需要空格
    problem_data={
  "deviceDymaicId": "495097280756449349",
  "craneId": "421471904994426949",
  "startTime": "2024-06-01 00:00:00",
  "endTime": "2024-06-01 00:00:00",
  "problemDescription": "66",
  "submitterId": "",
  "submissionTime": "2024-07-01 15:06:18",
  "acceptanceStatus": 1,
  "submitterImagesList": [],
  "submitterAccessoriesList": [],
  "submitterAccessoriesOriginList": [],
  "accepterId": "558143240922988613",
  "accepterName": "",
  "contact": "",
  "remark": ""
}    
    
    
    response=requests.post(problemAdd_url,json=problem_data,headers=headers)
  
    response_data=response.json()
    assert response.status_code==200,f'提交反馈失败,{response.text}'
    assert response_data['isSuccess']==True,f'提交反馈失败,{response.text}'


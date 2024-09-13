import requests
import yaml
import allure

def load_yaml(file_path):     #定义一个函数，传参数file_path 
    with open (file_path,'r',encoding='utf-8') as file :  # 'r'是只读模式   
        return yaml.safe_load(file)  #safe_load是一种安全解析的方法，为了防止执行yaml文件中不安全的代码



@allure.feature('正常操作的登录用例')
@allure.story("这里是写故事")
@allure.severity(allure.severity_level.BLOCKER)
#登录函数
def login():   
    login_data=load_yaml('./data/login_data.yaml')['login_data']  #获取登录参数yaml地址，获取顶层键
    login_url=login_data['loginAPI']  #登录API  再从顶层键中拿键值对
    zhanghao=login_data['payload']    #账号密码
    headers=login_data['headers']     #请求头

    #发送post请求  其实就是将所有条件打包
    response=requests.post(login_url,headers=headers,json=zhanghao)
    response.raise_for_status()  #如果状态码不是200就会报httperror
    #获取响应数据  
    response_data=response.json()
    #字典使用get方法获取键值，如果键值不存在也不会报错，会返回none
    accessToken=response_data['data'].get('accessToken',None)
    if accessToken is None:
        raise ValueError("您的登录未获取到token")

    return accessToken    #该函数返回token




    


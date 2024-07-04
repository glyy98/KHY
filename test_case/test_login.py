import requests
import yaml

def load_yaml(file_path):     #定义一个函数，传参数file_path 
    with open (file_path,'r',encoding='utf-8') as file :  # 'r'是只读模式   
        return yaml.safe_load(file)  #safe_load是一种安全解析的方法，为了防止执行yaml文件中不安全的代码
     
#登录函数
def login():   
    login_data=load_yaml('../data/login_data.yaml')['login_data']  #获取登录参数yaml地址，获取顶层键
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




    
    # #基础地址
    # base_url='https://dev.mhiiot.cn/openapi/client/api'  
    # #基础地址+接口名
    # url=f'{base_url}/login'  
    # #定义请求体  字典形式  账号密码
    # zhanghao={'username':"superadmin",'password':'123456'}
    # #定义请求头  
    # headers={"Content-Type":"application/json"}

    # #发送post请求  其实就是将所有条件打包
    # response=requests.post(url,headers=headers,json=zhanghao)
    # response.raise_for_status()  #如果状态码不是200就会报httperror
    # #获取响应数据  
    # response_data=response.json()
    # #字典使用get方法获取键值，如果键值不存在也不会报错，会返回none
    # accessToken=response_data['data'].get('accessToken',None)
    # if accessToken is None:
    #     raise ValueError("您的登录未获取到token")

    # return accessToken    #该函数返回token


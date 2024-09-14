import requests
import os  
import json
import multiprocessing
import time

def allure_report():   #在控制台执行allure的命令  
    # 运行测试用例，将报告结果存储到指定目录
    os.system('pytest test_case/test_addtast.py --alluredir ./report/result  ')
    # 生成 Allure 报告，生成一次就清除覆盖之前的
    os.system('allure generate report/result/ -o report/html --clean')
    # 忽略 localhost 和 127.0.0.1 的代理
    os.environ['no_proxy'] = 'localhost,127.0.0.1,192.168.101.124'
    # 自动打开 Allure 报告
    os.system('allure serve report/result  -p 4545')
    return './report/html'

def send_feishu():
    # allure报告结果json路径
    report_path = allure_report()
    file_name = os.path.join(report_path, 'widgets', 'summary.json')
    # file_name = r"C:\Users\Administrator\Desktop\KHY\report\html\widgets\summary.json"
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    case_json = data['statistic']
    case_all = case_json['total']   # 测试用例总数
    case_fail = case_json['failed']     # 失败用例数量
    case_pass = case_json['passed']     # 成功用例数量
    
    if case_all > 0:
        # 计算通过率
        case_rate = round((case_pass / case_all) * 100, 2)
    else:
        print('未获取到执行结果')
        return
    
    # 发送报告内容
    text = f"用例通过率：{case_rate}%\n" \
           f"执行用例数：{case_all}个\n" \
           f"成功用例数：{case_pass}个\n" \
           f"失败用例数：{case_fail}个\n" \
           f"测试报告地址：http://192.168.101.124:4545/index.html"
    
    print(text)

        # 构造飞书消息体
    data = {
        "msg_type": "text",
        "content": {
            "text": text
        }
    }

    
    # 飞书 Webhook URL
    url = 'https://open.feishu.cn/open-apis/bot/v2/hook/54851639-bfec-40f4-bf3e-35a0937e1b0a'  # 替换为你的飞书 Webhook URL
    headers = {'Content-Type':'application/json'}
    
    # 发送请求
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    # 打印响应状态码和内容
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

if __name__ == '__main__':
    # 执行生成 Allure 报告
    a = multiprocessing.Process(target=allure_report)
    # 执行发送飞书消息
    b = multiprocessing.Process(target=send_feishu)
    a.start()
    time.sleep(10)  # 等待报告生成完成
    b.start()

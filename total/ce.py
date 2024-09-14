import os  
import multiprocessing

def allure_report():   #在控制台执行allure的命令  
    # 运行测试用例，将报告结果存储到指定目录
    os.system('pytest test_case/test_addtast.py --alluredir ./report/result --clean')
    # 生成 Allure 报告，生成一次就清除覆盖之前的
    os.system('allure generate report/result/ -o report/html  --clean')
    # 忽略 localhost 和 127.0.0.1 的代理
    os.environ['no_proxy'] = 'localhost,127.0.0.1,192.168.101.124'
    # 自动打开 Allure 报告
    os.system('allure serve report/result  -p 4545')
    return './report/html'

if __name__ == '__main__':
    # 执行生成 Allure 报告
    a = multiprocessing.Process(target=allure_report)
    a.start()
   
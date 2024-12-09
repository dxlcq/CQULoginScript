'''第一条为电脑，第二条为手机
http://10.10.8.162:801/eportal/portal/login?callback=dr1004&user_account=%2C0%2C账号&user_password=密码
http://10.10.8.162:801/eportal/portal/login?callback=dr1005&user_account=%2C1%2C账号&user_password=密码
'''

import requests
import sys
from datetime import datetime

# 检查命令行参数数量
if len(sys.argv) != 4:
    print("使用方法: python3 cqu.py 账号 密码 客户端")
    sys.exit(1)

# 获取命令行参数
USER = sys.argv[1]
PAWD = sys.argv[2]
flg = int(sys.argv[3])  # 将 flg 转换为整数

# 根据 flg 设置 PRE 和 DR
if flg == 0:
    PRE = "%2C0%2C"
    DR = "dr1004"
else:
    PRE = "%2C1%2C"
    DR = "dr1005"

# 设置 URL 和参数
url = "http://10.10.8.162:801/eportal/portal/login?callback="+DR+"&user_account="+PRE+USER+"&user_password="+PAWD

# 发送请求
response = requests.get(url)

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + response.text)
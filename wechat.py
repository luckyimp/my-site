# _*_ coding:utf-8 _*_
import hashlib
import time
 
import xmltodict
from flask import Flask, request, make_response
 
app = Flask(__name__)
 
 
@app.route("/")
def hello():
    return "Hello World!"
 
 
@app.route('/wechat', methods=['GET', 'POST'])
def wechat():
    WECHAT_TOKEN = 'xinqingshishuidanruoyun'  # 这个token要和我们测试的token一致
 
    if request.method == "GET":
        """对接微信服务器"""
        signature = request.args.get('signature')
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        echostr = request.args.get('echostr')
 
        tmp = [WECHAT_TOKEN, timestamp, nonce]
        tmp.sort()
        tmp = "".join(tmp).encode('utf-8')
        tmp = hashlib.sha1(tmp).hexdigest()
        if tmp == signature:
 
            return make_response(echostr)
        else:
            return "error"
if __name__ == '__main__':
    app.run(debug=True, host='66.112.221.82', port=52001)

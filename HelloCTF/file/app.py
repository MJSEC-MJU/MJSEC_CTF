from flask import Flask
from flask import request
from flask import make_response
import sys
sys.path.append('/app')
#HelloCTF
from connectdb import getsecretkey
app = Flask(__name__)
app.secret_key = getsecretkey()

@app.route('/')
def hello_world():
    resp = make_response('Hello stranger!! This is CTF Master Moon.<br> \
        This is very easy problem to exersise.<br> \
        check /source and think how to solve!<br> \
        GOOD LUCK!', 200)
    return resp

@app.route('/source')
def read_source():
    f = open('/app/app.py', 'r')
    str1 = "<"
    str2 = "/br>"
    br = str1+str2
    return br.join(f.readlines()).replace(" ", "&nbsp;")
    
@app.route('/flag')
def flag():
    f = open('/flag', 'r')
    rtn_val = f.readlines()
    return rtn_val

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')



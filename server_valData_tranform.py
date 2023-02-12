from flask import Flask,request
import json

app = Flask(__name__)

@app.route("/pyserver",methods=['POST'])
def home():
	data = json.loads(request.data)
	print(data)
	return "server get data"
	

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)
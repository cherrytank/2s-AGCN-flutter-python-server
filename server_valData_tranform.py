from flask import Flask,request
import json
from flutter_Data_transform import create_output_file
app = Flask(__name__)

@app.route("/pyserver",methods=['POST'])
def home():
	data = json.loads(request.data)
	print(data)
	print(create_output_file(data))
	return "server get data"
	

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)
#!/usr/bin/python
from flask import Flask, jsonify, request
import json

import natprocess

app = Flask(__name__)

interface = [
	{

	}
]

@app.route('/get_interface', methods=['GET'])
def get_int():
        return jsonify({'interface': natprocess.get_interface()})

@app.route('/set_interface', methods=['POST'])
def set_int():
	function = {
		'ethernet': request.json['ethernet'],
		'ip': request.json['ip']
	}
	interface.append(function)
	natprocess.set_interface(function['ethernet'],function['ip'])
	return jsonify({'interface': natprocess.get_interface()})

@app.route('/del_interface', methods=['POST'])
def del_int():
	function = {
		'ethernet': request.json['ethernet'],
        	'ip': request.json['ip']
        }
	interface.append(function)
	natprocess.del_interface(function['ethernet'],function['ip'])
        return jsonify({'interface' : natprocess.get_interface()})

@app.route('/set_intdesc', methods=['POST'])
def set_intd():
        function = {
                'ethernet': request.json['ethernet'],
                'desc': request.json['desc']
        }
        interface.append(function)
        natprocess.set_intdesc(function['ethernet'],function['desc'])
        return jsonify({'interface': natprocess.get_interface()})

@app.route('/set_natsrc', methods=['POST'])
def set_natsrc():
        function = {
                'no': request.json['no'],
                'ethernet': request.json['ethernet'],
		'ip': request.json['ip']
        }
        interface.append(function)
        natprocess.set_natsrc(function['no'],function['ethernet'],function['ip'])
        return jsonify({'interface': natprocess.get_natsrc()})

@app.route('/get_natsrc', methods=['GET'])
def get_natsrc():
        return jsonify({'interface': natprocess.get_natsrc()})

@app.route('/del_natsrc', methods=['POST'])
def del_natsrc():
        function = {
                'no': request.json['no'],
        }
        interface.append(function)
        natprocess.del_natsrc(function['no'])
        return jsonify({'interface': natprocess.get_natsrc()})

@app.route('/set_natreflec', methods=['POST'])
def set_natr():
        function = {
		'no': request.json['no'],
                'ip': request.json['ip'],
                'ip2': request.json['ip2']
        }
        interface.append(function)
        natprocess.set_natreflec(function['no'],function['ip'],function['ip2'])
        return jsonify({'interface': natprocess.get_natreflec()})

@app.route('/get_natreflec', methods=['GET'])
def get_natr():
        return jsonify({'interface': natprocess.get_natreflec()})

@app.route('/del_natreflec', methods=['POST'])
def del_natr():
        function = {
                'no': request.json['no']
        }
        interface.append(function)
        natprocess.del_natreflec(function['no'])
        return jsonify({'interface': natprocess.get_natreflec()})

if __name__ == '__main__':
        app.run(debug=True)

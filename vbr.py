#!/usr/bin/python
from flask import Flask, jsonify, request
import json

import brprocess

app = Flask(__name__)

interface = [
        {

        }
]

@app.route('/get_vlan', methods=['GET'])
def get_vlan():
        return jsonify({'interface': brprocess.get_vlan()})

@app.route('/set_vlan', methods=['POST'])
def set_vlan():
        function = {
                'ethernet': request.json['ethernet'],
		'vlan': request.json['vlan'],
		'desc': request.json['desc'],
                'ip': request.json['ip']
        }
        interface.append(function)
        brprocess.set_vlan(function['ethernet'],function['vlan'],function['desc'],function['ip'])
        return jsonify({'interface': brprocess.get_vlan()})

@app.route('/del_vlan', methods=['POST'])
def del_vlan():
        function = {
                'ethernet': request.json['ethernet'],
                'vlan': request.json['vlan']
        }
        interface.append(function)
        brprocess.del_vlan(function['ethernet'],function['vlan'])
        return jsonify({'interface': brprocess.get_vlan()})

@app.route('/set_bridge', methods=['POST'])
def set_bridge():
        function = {
		'bridge': request.json['bridge'],
                'ethernet': request.json['ethernet'],
		'ip': request.json['ip']
        }
        interface.append(function)
        brprocess.set_bridge(function['bridge'],function['ethernet'],function['ip'])
        return jsonify({'interface': brprocess.get_bridge()})

@app.route('/get_bridge', methods=['GET'])
def get_bridge():
        return jsonify({'interface': brprocess.get_bridge()})

@app.route('/del_bridge', methods=['POST'])
def del_bridge():
        function = {
                'bridge': request.json['bridge']
        }
        interface.append(function)
        brprocess.del_bridge(function['bridge'])
        return jsonify({'interface': brprocess.get_bridge()})

if __name__ == '__main__':
        app.run(debug=True)



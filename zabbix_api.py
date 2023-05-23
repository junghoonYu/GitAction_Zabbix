# -*- coding: utf-8 -*-
import requests
import json
import urllib3
import os

# HTTPS 요청 시 경고 표시 비활성화
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Zabbix API 요청 헤더
headers = {'Content-Type': 'application/json'}

def get_token(url,username,password):
    # Zabbix API에 로그인 요청
    data = {
        'jsonrpc': '2.0',
        'method': 'user.login',
        'params': {
            'user': username,
            'password': password
        },
        'id': 1
    }

    response = requests.post(url, json=data, headers=headers)
    auth_token = response.json()['result']
    return auth_token

def get_problems(auth_token,url):
    # 로그인이 성공했으면 Zabbix API를 사용하여 unacknowledged problem을 가져옴
    data = {
        'jsonrpc': '2.0',
        'method': 'problem.get',
        'params': {
            'filter': {
                'acknowledged': 0  # 0은 미확인된 문제를 나타냅니다.
            },
            'output': 'extend',
            'selectAcknowledges': 'extend',
            'selectTags': 'extend'
        },
        'auth': auth_token,
        'id': 2
    }
    
    response = requests.post(url, json=data, headers=headers)
    problems = response
    return problems

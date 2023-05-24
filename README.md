# GitAction_Zabbix

Linux
```
export ZBX_URL='https:/<ZABBIX_URL>/zabbix/api_jsonrpc.php'
export ZBX_USER='<ZABBIX_USERNAME>'
export ZBX_PASS='<ZABBIX_PASSWORD>'
export MY_GITHUB_TOKEN='<GITHUB_TOKEN>'

python3 ./main.py
```

Docker
```
docker run \
-e ZBX_URL='http://<ZABBIX_URL>/zabbix/api_jsonrpc.php>' 
-e ZBX_USER='<ZABBIX_USERNAME>' 
-e ZBX_PASS='<ZABBIX_PASSWORD>'
-e MY_GITHUB_TOKEN='<GITHUB_TOKEN>' 
[DOCKER IMAGE]]
```

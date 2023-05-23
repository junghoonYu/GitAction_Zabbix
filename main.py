import os
import json
import time
from datetime import datetime
from pytz import timezone
from github_utils import get_github_repo, upload_github_issue
from zabbix_api import get_token, get_problems


if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "GitAction_Zabbix"

    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일")

    zbx_url = os.environ['ZBX_URL']
    zbx_username = os.environ['ZBX_USER']
    zbx_password = os.environ['ZBX_PASS']
    
    zbx_token = get_token(zbx_url,zbx_username,zbx_password)
    zbx_problems = get_problems(zbx_token,zbx_url).json()['result']

    for problem in zbx_problems:

        # 발생 9시간 이내의 Problem은 집계하지 않음
        time_diff = int(time.time()) - int(problem['clock'])
        if time_diff < 32400:
            continue

        issue_title = f"{today_date} - {problem['name']}"
        upload_contents = "yet.."

        repo = get_github_repo(access_token, repository_name)
        upload_github_issue(repo, issue_title, upload_contents)

    print("Upload Github Issue Success!")

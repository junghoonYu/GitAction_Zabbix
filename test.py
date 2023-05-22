import os
from datetime import datetime
from pytz import timezone
from github_utils import get_github_repo, upload_github_issue


if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "GitAction_Zabbix"

    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일")

    #yes24_it_new_product_url = "http://www.yes24.com/24/Category/NewProductList/001001003?sumGb=01"
    #soup = parsing_beautifulsoup(yes24_it_new_product_url)
    
    issue_title = f"Zabbix 알림({today_date})"
    #upload_contents = extract_book_data(soup)
    upload_contents = 'This is test.'
    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success!")

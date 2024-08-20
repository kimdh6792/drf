import requests
import os

github_api_url = os.getenv("APIGITHUB_URL")
github_token = os.getenv("GITHUB_TOKEN")
slack_token = os.getenv("SLACK_TOKEN")
channel_id = os.getenv("SLACK_CHANNEL_ID")
print(github_api_url)
res = requests.get(github_api_url + "?state=open", headers={"Authorization": f"Bearer {github_token}"})

if res.status_code == 200:
    if res.json():
        data = {
            "channel": channel_id,
            "text": f"{len(res.json())}개의 pr이 있습니다."
        }
        slack_url = "https://slack.com/api/chat.postMessage"
        slack_headers = {"Authorization": f"Bearer {slack_token}"}
        slack_res = requests.post(url=slack_url, json={}, headers=slack_headers)
        ts = slack_res.json()["ts"]
        for i in res.json():
            pr_url = i["html_url"]
            pr_title = i["pr_title"]
            data = {
                "channel": channel_id,
                "thread_ts": ts,
                "attachments": [
                                    {
                    "text": f"title: {pr_title}",
                    "attachment_type": "default",
                    "color": "#3AA3E3",
                    "actions": [
                        {
                        "name": "리뷰버튼",
                        "text": "리뷰하러가기",
                        "type": "button",
                        "url": pr_url
                        }
                    ]
                    }
                ]
            }
            requests.post(url=slack_url, json=data, headers=slack_headers)
            




import requests

pt = 'https://try.requesttracker.io/REST/1.0/ticket/new?content=Queue: General\n' \
     'Subject: LIVE TEST FOR USER FILE ISSUE\n' \
     'Requestor: thabang@gmail.com\n' \
     'Owner: guest\n' \
     'Status: New'

login = {
    "user": "guest",
    "pass": "guest"
}
with requests.Session() as session:
    post = session.post(pt, data=login)
    print(post.text)

# Corona-Notifier
A simple python script which can be used to automatically show a notification with stats such as total number of cases, cured, deaths etc.

Requirements:
1. lxml
2. requests
3. notify2

Run this with     <i>python notifier.py</i>


## How to create your own
1. select a reliable data source in this case it is [https://www.mohfw.gov.in/](https://www.mohfw.gov.in/)
2. select a tool for notification in this case it is [notify2](https://pypi.org/project/notify2/)
3. Use [requests](https://2.python-requests.org/en/master/) and [lxml](https://pypi.org/project/lxml/) or [bs4](https://pypi.org/project/bs4/) for getting web data and parsing.

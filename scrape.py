import requests
from lxml import html


def getData():
    page=requests.get("https://www.mohfw.gov.in/")

    tree=html.fromstring(page.content)

    confirmed=tree.xpath("//*[@id='cases']/div/div/table/tbody/tr[28]/td[2]/strong")
    cured=tree.xpath("//*[@id='cases']/div/div/table/tbody/tr[28]/td[3]/strong")
    deaths=tree.xpath("//*[@id='cases']/div/div/table/tbody/tr[28]/td[5]/strong")

    return confirmed[0].text,cured[0].text,deaths[0].text

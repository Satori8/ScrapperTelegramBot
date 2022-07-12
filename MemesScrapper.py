import requests
from bs4 import BeautifulSoup


class MemesScrapper:
    def __init__(self):
        pass

    @staticmethod
    def get_memes():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
            'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
        }

        ses = requests.session()
        ses.get("https://dota2.ru/memes/", headers=headers)
        res = ses.post(
            "https://dota2.ru/memes/ajaxList?category%5B%5D=dota2&category%5B%5D=vk&tag=&period=all&sort-by=rating")
        soup = BeautifulSoup(res.content, "html.parser")
        memes = soup.find_all("a", attrs={"class": "mems-page__mem-img"})
        imgs = []
        for mem in memes:
            imgs.append("https://dota2.ru" + str(mem.find("img")['src']))
        return imgs




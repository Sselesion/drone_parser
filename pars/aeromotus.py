from random import randint
import time

from bs4 import BeautifulSoup
import requests

from .base import Parse
from models import Comp, CompEnum, CompBattery


class AeromotusParser(Parse):
    def __init__(self) -> None:
        super().__init__(url="https://aeromotus.ru/", idx=0)
        self.fabric = {
            # CompEnum.BATTERY: self.parse_battery,
        }
        self.key_words = {
            CompEnum.BATTERY: "аккумулятор",
        }
        self.name_key_words = {CompEnum.BATTERY: ["аккумулятор", "батарея"]}

    def run(self, comp: CompEnum):
        result = {}
        response = requests.get(
            self.url,
            params={
                "s": self.key_words[comp],
                "post_type": "product",
            },
        )
        time.sleep(randint(1, 4))

        soup = BeautifulSoup(response.text, "html.parser")
        nav = soup.find("nav", class_="electro-advanced-pagination")
        print('>>>>', nav.text.split()[-1][:-1])
        pages = int(nav.text.split()[-1][:-1]) if nav.text else 0
        print('>>>>', pages)
        for page in range(1, pages + 1):
            response = requests.get(
                self.url + f"page/{page}/",
                params={
                    "s": self.key_words[comp],
                    "post_type": "product",
                },
            )
            time.sleep(randint(1, 4))

            for card_url in self.detect_cards(response.text, self.name_key_words[comp]):
                result.update({card_url: self.parse_card(card_url, comp)})
        return result

    def detect_cards(self, html_text: str, name_key_words: list) -> list[str]:
        url_list = []
        soup = BeautifulSoup(html_text, "html.parser")
        for li in soup.find_all("li", class_="product"):
            h2 = li.find("h2", class_="woocommerce-loop-product__title")
            if any(map(lambda name_key_word: name_key_word in h2.string.lower(), name_key_words)):
                a = li.find("a", class_="woocommerce-LoopProduct-link")
                url_list.append(a.get("href"))
        return url_list

    # parsers
    def parse_card(self, url: str, comp: CompEnum) -> CompBattery:
        response = requests.get(url)
        time.sleep(randint(1, 4))
        soup = BeautifulSoup(response.text, "html.parser")

        a = soup.find("img", class_="wp-post-image")
        print('>>>>', a, url, sep='\n')
        image = a.get("src")
        div = soup.find("div", id="tab-description")
        print('>>>>>', div.get_text())

        # comp = self.fabric[comp]()

        # return CompBattery(
        #     url=url,
        #     image=...,
        #     description=...,
        #     additional_features=...,
        #     price=...,
        #     current_discharge=...,
        #     capasity=...,
        #     voltage=...,
        # )


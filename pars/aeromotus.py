import time
from random import randint
from typing import Type

import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel

from models import *

from .base import Parse
from .regex import PtrnEnum, Regex



class AeromotusParser(Parse):
    def __init__(self) -> None:
        super().__init__(url="https://aeromotus.ru/", idx=0)

        self.request_fabric = {
            # КОМПОНЕНТ -> URL && ПАРАМЕТРЫ ЗАПРОСА
            CompEnum.BATTERY: (
                self.url,
                {
                    "s": "аккумулятор",
                    "post_type": "product",
                },
            ),
            CompEnum.MICROCONTROLLER: (
                self.url,
                {
                    "s": "миктроконтроллер",
                    "post_type": "product",
                },
            ),
            CompEnum.ELECTRICMOTOR: (
                self.url,
                {
                    "s": "мотор",
                    "post_type": "product",
                },
            ),
            CompEnum.MOTORCONTROLLER: (
                self.url,
                {
                    "s": "контроллер мотора",
                    "post_type": "product",
                },
            ),
            CompEnum.FLIGHTCONTROLLER: (
                self.url,
                {
                    "s": "полетный контроллер",
                    "post_type": "product",
                },
            ),
            CompEnum.LIDAR: (
                self.url,
                {
                    "s": "лидар",
                    "post_type": "product",
                },
            ),
            CompEnum.MICROFLIGHTCONTROLLER: (
                self.url,
                {
                    "s": "полетный микроконтроллер",
                    "post_type": "product",
                },
            ),
            CompEnum.RANGEFINDER: (
                self.url,
                {
                    "s": "дальномер",
                    "post_type": "product",
                },
            ),
            CompEnum.SATELLITECOMMMODULE: (
                self.url,
                {
                    "s": "модуль спутниковой связи",
                    "post_type": "product",
                },
            ),
            CompEnum.LEASHINGPLATFORM: (
                self.url,
                {
                    "s": "подвесная платформа",
                    "post_type": "product",
                },
            ),
            CompEnum.THERMALCAMERA: (
                self.url,
                {
                    "s": "тепловизор",
                    "post_type": "product",
                },
            ),
            CompEnum.UAVCOPTERTYPE: (self.url + "product-tag/bpla", {}),
            CompEnum.VIDEOTRANSMITTER: (
                self.url,
                {
                    "s": "видео передатчик",
                    "post_type": "product",
                },
            ),
            CompEnum.PAYLOAD: (
                self.url,
                {
                    "s": "полезная нагрузка",
                    "post_type": "product",
                },
            ),
            CompEnum.CONTROLPANEL: (
                self.url,
                {
                    "s": "пульт",
                    "post_type": "product",
                },
            ),
        }

    def run(self, comp: CompEnum) -> dict[str, Comp]:
        result = {}
        response = requests.get(*self.request_fabric[comp])
        time.sleep(randint(1, 4))

        soup = BeautifulSoup(response.text, "html.parser")
        nav = soup.find("nav", class_="electro-advanced-pagination")
        pages = int(nav.text.split()[-1][:-1]) if nav and nav.text else 0
        for page in range(1, pages + 1):
            
            response = requests.get(
                self.request_fabric[comp][0] + f"page/{page}/",
                self.request_fabric[comp][1],
            )
            time.sleep(randint(1, 4))

            for card_url in self.detect_cards(response.text, self.key_words[comp]):
                result.update({card_url: self.parse_card(card_url, comp).dict()})
        return result

    def detect_cards(self, html_text: str, key_words: list) -> list[str]:
        url_list = []
        soup = BeautifulSoup(html_text, "html.parser")
        for li in soup.find_all("li", class_="product"):
            h2 = li.find("h2", class_="woocommerce-loop-product__title")
            if not key_words:
                a = li.find("a", class_="woocommerce-LoopProduct-link")
                url_list.append(a.get("href"))
            else:
                for key_word in key_words:
                    for word in h2.string.lower().split():
                        if key_word == word:
                            a = li.find("a", class_="woocommerce-LoopProduct-link")
                            url_list.append(a.get("href"))
                            break
        return url_list

    def parse_card(self, url: str, comp: CompEnum) -> Comp:
        response = requests.get(url)
        time.sleep(randint(1, 4))
        soup = BeautifulSoup(response.text, "html.parser")

        img = soup.find("img", class_="wp-post-image")
        image = img.get("src")
        p = soup.find("p", class_="price")
        price = p.get_text().split("\\")[0]
        h1 = soup.find("h1", class_="product_title")
        name = h1.string

        text_list = []
        div_description = soup.find("div", id="tab-description")
        if div_description:
            text_list.append(div_description.get_text(" ", strip=True))
        div_specification = soup.find("div", id="tab-specification")
        if div_specification:
            text_list.append(div_specification.get_text(" ", strip=True))

        regex = Regex(text_list)

        return self.fabric[comp](url, image, price, name, regex)

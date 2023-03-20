import time
import re
from random import randint
from typing import Type

import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel

from models import *

from ._base import Parse


class FixFlyParser(Parse):
    def __init__(self) -> None:
        super().__init__(url="https://fixfly.ru/", idx=3)

        self.request_fabric = {
            # КОМПОНЕНТ -> URL && ПАРАМЕТРЫ ЗАПРОСА
            CompEnum.BATTERY: (
                self.url + "rc-zapchasti/bqo-akkumulyatory",
                {"show_all": "yes"},
            ),
            CompEnum.MICROCONTROLLER: (
                self.url + "search",
                {"text": "микроконтроллер", "show_all": "yes"},
            ),
            CompEnum.ELECTRICMOTOR: (
                self.url + "rc-zapchasti/bqy-motory",
                {"show_all": "yes"},
            ),
            CompEnum.MOTORCONTROLLER: (
                self.url + "rc-zapchasti/bqk-esc-regulyatory",
                {"show_all": "yes"},
            ),
            CompEnum.FLIGHTCONTROLLER: (
                self.url + "rc-zapchasti/bss-poletnye-kontrollery",
                {"show_all": "yes"},
            ),
            CompEnum.LIDAR: (
                self.url + "search",
                {"text": "лидар", "show_all": "yes"},
            ),
            CompEnum.MICROFLIGHTCONTROLLER: (
                self.url + "search",
                {"text": "полетный микроконтроллер", "show_all": "yes"},
            ),
            CompEnum.RANGEFINDER: (
                self.url + "search",
                {"text": "дальномер", "show_all": "yes"},
            ),
            CompEnum.SATELLITECOMMMODULE: (
                self.url + "rc-zapchasti/elz-antenny",
                {"show_all": "yes"},
            ),
            CompEnum.LEASHINGPLATFORM: (
                self.url + "search",
                {"text": "привязная платформа", "show_all": "yes"},
            ),
            CompEnum.THERMALCAMERA: (
                self.url + "search",
                {"text": "тепловизор", "show_all": "yes"},
            ),
            CompEnum.UAVCOPTERTYPE: (
                self.url + "modeli/kvadrokoptery-s-kameroj",
                {"show_all": "yes"},
            ),
            CompEnum.VIDEOTRANSMITTER: (
                self.url + "search",
                {"text": "видеопередатчик", "show_all": "yes"},
            ),
            CompEnum.PAYLOAD: (
                self.url + "search",
                {"text": "подвес", "show_all": "yes"},
            ),
            CompEnum.CONTROLPANEL: (
                self.url + "rc-zapchasti/bsf-upravlenie",
                {"show_all": "yes"},
            ),
        }

    def run(self, comp: CompEnum) -> dict[str, Comp]:
        result = {}
        response = requests.get(*self.request_fabric[comp])
        time.sleep(randint(1, 4))

        for card_url in self.detect_cards(response.text, self.key_words[comp], comp):
            result.update({card_url: self.parse_card(card_url, comp).dict()})
        return result

    def detect_cards(
        self, html_text: str, key_words: list, comp: CompEnum
    ) -> list[str]:
        url_list = []
        soup = BeautifulSoup(html_text, "html.parser")

        for div in soup.find_all("div", class_="item_zip"):
            span = div.find("span", class_="desc")
            # Итерация по ключевым словам
            if "text" in self.request_fabric[comp][1].keys():
                for key_word in key_words:
                    for word in span.string.lower().split():
                        # Точное соответсвие слова в названии
                        if key_word == word:
                            a = div.find("a", id=re.compile(r"zip_.+"))
                            url_list.append(self.url + a.get("href")[2::])
                            break
            else:
                a = div.find("a", id=re.compile(r"zip_.+"))
                url_list.append(self.url + a.get("href")[2::])
        return url_list

    def parse_card(self, url: str, comp: CompEnum) -> Comp:
        print("Получение данных для компонента '%s' по товару: %s" % (comp.value, url))

        response = requests.get(url)
        time.sleep(randint(1, 4))
        soup = BeautifulSoup(response.text, "html.parser")
        # Получение изображения, цены, названия товара
        img = soup.find("img", attrs={"itemprop": "image"})
        image = self.url + img.get("src")
        span_itemprop = soup.find("span", attrs={"itemprop": "price"})
        price = span_itemprop.string.strip()
        h1_itemprop = soup.find("h1", attrs={"itemprop": "name"})
        name = h1_itemprop.string.strip()

        text_list = []
        div_description = soup.find("div", attrs={"itemprop": "description"})
        if div_description:
            text_list.append(div_description.get_text(" ", strip=True))

        return self.fabric[comp](url, image, price, name, text_list)

import time
from random import randint
from typing import Type

import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel

from models import *

from .base import Parse
from .regex import PtrnEnum, Regex


class AirHobbyParser(Parse):
    def __init__(self) -> None:
        super().__init__(url="https://air-hobby.ru", idx=1)

        self.request_fabric = {
            # КОМПОНЕНТ -> URL && ПАРАМЕТРЫ ЗАПРОСА
            CompEnum.BATTERY: (
                self.url + '/katalog/category/90-akkumulyatori.html',
                {
                    "limit": "0",
                    "start": "0",
                },
            ),
            CompEnum.MICROCONTROLLER: (
                self.url + '/index.php',
                {
                    "keyword": "микроконтроллер",
                    "option": "com_virtuemart",
                    "page": "shop.browse",
                    "Itemid": "28",
                    "limit": "0",
                    "limitstart": "0",
                },
            ),
            CompEnum.ELECTRICMOTOR: (
                self.url + '/index.php',
                {
                    "keyword": "мотор",
                    "option": "com_virtuemart",
                    "page": "shop.browse",
                    "Itemid": "28",
                    "limit": "0",
                    "limitstart": "0",
                },
            ),
            CompEnum.MOTORCONTROLLER: (
                self.url + '/index.php',
                {
                    "keyword": "контроллер+мотора",
                    "option": "com_virtuemart",
                    "page": "shop.browse",
                    "Itemid": "28",
                    "limit": "0",
                    "limitstart": "0",
                },
            ),
            CompEnum.FLIGHTCONTROLLER: (
                self.url + '/katalog/category/52-poletnie-kontrolleri.html',
                {
                    "limit": "0",
                    "start": "0",
                },
            ),
            CompEnum.LIDAR: (
                self.url + '/index.php',
                {
                    "keyword": "лидар",
                    "option": "com_virtuemart",
                    "page": "shop.browse",
                    "Itemid": "28",
                    "limit": "0",
                    "limitstart": "0",
                },
            
            ),
            CompEnum.MICROFLIGHTCONTROLLER: (
                self.url + '/index.php',
                {
                    "keyword": "микроконтроллер",
                    "option": "com_virtuemart",
                    "page": "shop.browse",
                    "Itemid": "28",
                    "limit": "0",
                    "limitstart": "0",
                },
            ),
            CompEnum.RANGEFINDER: (
                self.url + '/index.php',
                {
                    "keyword": "дальномер",
                    "option": "com_virtuemart",
                    "page": "shop.browse",
                    "Itemid": "28",
                    "limit": "0",
                    "limitstart": "0",
                },
            ),
            CompEnum.SATELLITECOMMMODULE: (
                self.url + '/index.php',
                {
                    "keyword": "связь",
                    "option": "com_virtuemart",
                    "page": "shop.browse",
                    "Itemid": "28",
                    "limit": "0",
                    "limitstart": "0",
                },
            ),
            CompEnum.LEASHINGPLATFORM: (
                self.url + '/index.php',
                {
                    "keyword": "подвес",
                    "option": "com_virtuemart",
                    "page": "shop.browse",
                    "Itemid": "28",
                    "limit": "0",
                    "limitstart": "0",
                },
            ),
            CompEnum.THERMALCAMERA: (
                self.url + '/index.php',
                {
                    "keyword": "тепловизор",
                    "option": "com_virtuemart",
                    "page": "shop.browse",
                    "Itemid": "28",
                    "limit": "0",
                    "limitstart": "0",
                },
            ),
            CompEnum.UAVCOPTERTYPE: (
                self.url + '/index.php',
                {
                    "keyword": "коптер",
                    "option": "com_virtuemart",
                    "page": "shop.browse",
                    "Itemid": "28",
                    "limit": "0",
                    "limitstart": "0",
                },
                
            ),
            CompEnum.VIDEOTRANSMITTER: (
               self.url + '/index.php',
                {
                    "keyword": "видеопередатчик",
                    "option": "com_virtuemart",
                    "page": "shop.browse",
                    "Itemid": "28",
                    "limit": "0",
                    "limitstart": "0",
                },
            ),
            CompEnum.PAYLOAD: (
                self.url + '/index.php',
                {
                    "keyword": "камера",
                    "option": "com_virtuemart",
                    "page": "shop.browse",
                    "Itemid": "28",
                    "limit": "0",
                    "limitstart": "0",
                },
            ),
            CompEnum.CONTROLPANEL: (
                self.url + '/katalog/category/78-peredatchiki.html',
                {
                    "limit": "0",
                    "start": "0",
                },
            ),
        }
    
    def run(self, comp: CompEnum) -> dict[str, Comp]:
        result = {}
        response = requests.get(*self.request_fabric[comp])
        time.sleep(randint(1,4))

        for card_url in self.detect_cards(response.text, self.key_words[comp]):
                result.update({card_url: self.parse_card(card_url, comp).dict()})
        return result

    def detect_cards(self, html_text: str, key_words: list) -> list[str]:
        url_list = []
        soup = BeautifulSoup(html_text, "html.parser")
        cards = soup.find("div", class_="vmBrowse")
        if cards is None:
            return url_list
        
        for div in cards.find_all("div", class_="v_item-i"):
            name = div.find("a", class_="v_item-it")
            print(name.get("href"))
            if not key_words:
                url_list.append(self.url + name.get("href"))
            else:
                for key_word in key_words:
                    for word in name.get("title").lower().split():
                        if key_word == word:
                            url_list.append(self.url + name.get("href"))
                            break
        return url_list

    def parse_card(self, url: str, comp: CompEnum) -> Comp:
        response = requests.get(url)
        time.sleep(randint(1, 4))
        soup = BeautifulSoup(response.text, "html.parser")

        a = soup.find("a", class_="b_flypage-is__main")
        image = self.url + a.find('img').get("src") if a else ''
        span = soup.find("span", class_="vmRoduct_price-real")
        price = span.get_text().strip()
        h1 = soup.find("div", class_="b_flypage-ii").find('h1')
        name = h1.string

        text_list = []
        div_description = soup.find("div", id="js-product-desc")
        if div_description:
            text_list.append(div_description.get_text(" ", strip=True))
        
        cc =  Comp(
            url=url,
            image=image,
            price=price,
            name=name
        )
        print(cc.dict())
        
        return cc
        # regex = Regex(text_list)
        # print(">>>", regex.raw_text)

        # return self.fabric[comp](url, image, price, name, regex)

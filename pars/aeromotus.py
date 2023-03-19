from random import randint
import time

from bs4 import BeautifulSoup
import requests

from .base import Parse
from models import Comp, CompEnum, CompBattery, CompUAVCopterType
from .regex import Regex, PtrnEnum


class AeromotusParser(Parse):
    def __init__(self) -> None:
        super().__init__(url="https://aeromotus.ru/", idx=0)
        self.fabric = {
            # КОМПОНЕНТ -> МЕТОД ПАРСИНГА ХАРАКТЕРИСТИК КОМПОНЕНТА
            CompEnum.BATTERY: self.parse_battery,
            CompEnum.UAVCOPTERTYPE: self.parse_uavc_copter_type,
        }
        self.request_fabric = {
            # КОМПОНЕНТ -> URL && ПАРАМЕТРЫ ЗАПРОСА
            CompEnum.BATTERY: (
                self.url,
                {
                    "s": "аккумулятор",
                    "post_type": "product",
                },
            ),
            CompEnum.UAVCOPTERTYPE: (self.url + "product-tag/bpla", {}),
        }
        self.key_words = {
            CompEnum.BATTERY: ["аккумулятор", "батарея"],
            CompEnum.UAVCOPTERTYPE: [],
        }

    def run(self, comp: CompEnum) -> dict[str, Comp]:
        result = {}
        response = requests.get(*self.request_fabric[comp])
        time.sleep(randint(1, 4))

        soup = BeautifulSoup(response.text, "html.parser")
        nav = soup.find("nav", class_="electro-advanced-pagination")
        pages = int(nav.text.split()[-1][:-1]) if nav.text else 0
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
        price = p.get_text().split('\\')[0]
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
        print(">>>", regex.raw_text)

        return self.fabric[comp](url, image, price, name, regex)

    def parse_battery(
        self, url: str, image: str, price: str, name: str, regex: Regex
    ) -> CompBattery:
        return CompBattery(
            url=url,
            image=image,
            price=price,
            name=name,
            current_discharge=regex.find_by(PtrnEnum.CURRENT_DISCHARGE),
            capasity=regex.find_by(PtrnEnum.CAPASITY),
            shape=regex.find_by(PtrnEnum.SHAPE),
            voltage=regex.find_by(PtrnEnum.VOLTAGE),
        )

    def parse_uavc_copter_type(
        self, url: str, image: str, price: str, name: str, regex: Regex
    ) -> CompUAVCopterType:
        return CompUAVCopterType(
            url=url,
            image=image,
            price=price,
            name=name,
            maximal_speed = regex.find_by(PtrnEnum.MAXIMAL_SPEED),
            gaining_speed = regex.find_by(PtrnEnum.GAINING_SPEED),
            deceleration_speed = regex.find_by(PtrnEnum.DECELERATION_SPEED),
            maximal_range = regex.find_by(PtrnEnum.MAXIMAL_RANGE),
            maximum_flight_altitude = regex.find_by(PtrnEnum.MAXIMUM_FLIGHT_ALTITUDE),
            power_consumption = regex.find_by(PtrnEnum.POWER_CONSUMPTION),
            payload_weight = regex.find_by(PtrnEnum.PAYLOAD_WEIGHT),
            flight_time = regex.find_by(PtrnEnum.FLIGHT_TIME),
            number_of_screws = regex.find_by(PtrnEnum.NUMBER_OF_SCREWS)
        )
    

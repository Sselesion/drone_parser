import time
from random import randint
from typing import Type

import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel

from models import *

from .base import Parse
from .regex import PtrnEnum, Regex


class FixFlyParser(Parse):
    def __init__(self) -> None:
        super().__init__(url="https://fixfly.ru/", idx=2)

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

        for card_url in self.detect_cards(response.text, self.key_words[comp]):
            result.update({card_url: self.parse_card(card_url, comp).dict()})
        return result

    def detect_cards(self, html_text: str, key_words: list) -> list[str]:
        pass

    def parse_card(self, url: str, comp: CompEnum) -> Comp:
        pass
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

    def parse_microcontroller(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        return CompMicrocontroller(
            url="filler",
            image="filler",
            price="filler",
            name="filler",
            operating_frequency="filler",
            number_of_channels="filler",
            operating_current="filler",
            working_voltage="filler",
            transmission_power="filler",
            channel_resolution="filler",
            wireless_protocol="filler",
        )

    def parse_electricmotor(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        return CompElectricMotor(
            url="filler",
            image="filler",
            price="filler",
            name="filler",
            voltage="filler",
            maximum_power="filler",
            recommended_battery="filler",
            noload_current="filler",
            peak_current="filler",
            stator_length="filler",
            stator_diameter="filler",
            shaft_diameter="filler",
            number_of_revolutions_per_volt="filler",
            resistance="filler",
        )

    def parse_motorcontroller(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        return CompMotorController(
            url="filler",
            image="filler",
            price="filler",
            name="filler",
            operating_current="filler",
            peak_current="filler",
            power_support="filler",
        )

    def parse_flightcontroller(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        return CompFlightController(
            url="filler",
            image="filler",
            price="filler",
            name="filler",
            presence_of_a_barometer="filler",
            presence_of_a_black_box="filler",
            power="filler",
            firmware="filler",
            presence_of_a_usb_connector="filler",
            fastening=["filler"],
        )

    def parse_lidar(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        return CompLidar(
            url="filler",
            image="filler",
            price="filler",
            name="filler",
            max_range="filler",
            frequency="filler",
            power_supply="filler",
        )

    def parse_microflightcontroller(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        return CompMicroFlightController(
            url="filler",
            image="filler",
            price="filler",
            name="filler",
            clock_requency="filler",
            flash_memory_capacity="filler",
            mounting="filler",
            min_input_voltage="filler",
            max_input_voltage="filler",
            uart_ports_number="filler",
        )

    def parse_rangefinder(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        return CompRangeFinder(
            url="filler",
            image="filler",
            price="filler",
            name="filler",
            max_range="filler",
            frequency="filler",
            wave_length="filler",
            power_supply="filler",
        )

    def parse_satellitecommmodule(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        return CompSatelliteCommModule(
            url="filler",
            image="filler",
            price="filler",
            name="filler",
            battery_availability="filler",
            battery_life="filler",
            accuracy="filler",
        )

    def parse_leashingplatform(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        return CompLeashingPlatform(
            url="filler",
            image="filler",
            price="filler",
            name="filler",
            max_speed="filler",
            gaining_speed="filler",
            deceleration_speed="filler",
            flight_range="filler",
            flight_altitude="filler",
            power_consumption="filler",
            payload_weight="filler",
            flight_time="filler",
            screws_number="filler",
        )

    def parse_thermalcamera(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        return CompThermalCamera(
            url="filler",
            image="filler",
            price="filler",
            name="filler",
            range_detection="filler",
            range_observation="filler",
            interface="filler",
            voltage="filler",
            battery_availability="filler",
            battery_life="filler",
            field_of_view="filler",
            magnification="filler",
            protection_class="filler",
            work_temperature="filler",
            type_of_sensor="filler",
        )

    def parse_uavcoptertype(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        return CompUAVCopterType(
            url="filler",
            image="filler",
            price="filler",
            name="filler",
            maximal_speed="filler",
            gaining_speed="filler",
            deceleration_speed="filler",
            maximal_range="filler",
            maximum_flight_altitude="filler",
            power_consumption="filler",
            payload_weight="filler",
            flight_time="filler",
            number_of_screws="filler",
        )

    def parse_videotransmitter(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        return CompVideoTransmitter(
            url="filler",
            image="filler",
            price="filler",
            name="filler",
            frequency="filler",
            wattage="filler",
            number_of_channels="filler",
            antenna_connector="filler",
        )

    def parse_payload(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        return CompPayload(
            url="filler",
            image="filler",
            price="filler",
            name="filler",
            matrix="filler",
            lens="filler",
            magnification="filler",
            number_of_megapixels="filler",
            resolution_TVL="filler",
            companion_image="filler",
            thermal_imager_resolution="filler",
            field_of_view="filler",
            rangefinder="filler",
            axes="filler",
            accuracy="filler",
            tangent="filler",
            roll="filler",
            yaw="filler",
            wattage="filler",
            voltage="filler",
            current="filler",
            antenna="filler",
            frequency="filler",
            number_of_channels="filler",
        )

    def parse_controlpanel(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        return CompControlPanel(
            url="filler",
            image="filler",
            price="filler",
            name="filler",
            frequency="filler",
            number_of_channels="filler",
            current="filler",
            voltage="filler",
            transmission_power="filler",
            resolution="filler",
            wireless_protocol="filler",
        )

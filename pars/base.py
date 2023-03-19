from abc import ABC, abstractmethod
from typing import Type

from models import Comp, CompEnum


class Parse(ABC):
    def __init__(self, url, idx) -> None:
        self.url = url
        self.idx = idx
        self.fabric = {
            # КОМПОНЕНТ -> МЕТОД ПАРСИНГА ХАРАКТЕРИСТИК КОМПОНЕНТА
            CompEnum.BATTERY: self.parse_battery,
            CompEnum.MICROCONTROLLER: self.parse_microcontroller,
            CompEnum.ELECTRICMOTOR: self.parse_electricmotor,
            CompEnum.MOTORCONTROLLER: self.parse_motorcontroller,
            CompEnum.FLIGHTCONTROLLER: self.parse_flightcontroller,
            CompEnum.LIDAR: self.parse_lidar,
            CompEnum.MICROFLIGHTCONTROLLER: self.parse_microflightcontroller,
            CompEnum.RANGEFINDER: self.parse_rangefinder,
            CompEnum.SATELLITECOMMMODULE: self.parse_satellitecommmodule,
            CompEnum.LEASHINGPLATFORM: self.parse_leashingplatform,
            CompEnum.THERMALCAMERA: self.parse_thermalcamera,
            CompEnum.UAVCOPTERTYPE: self.parse_uavcoptertype,
            CompEnum.VIDEOTRANSMITTER: self.parse_videotransmitter,
            CompEnum.PAYLOAD: self.parse_payload,
            CompEnum.CONTROLPANEL: self.parse_controlpanel,
        }
        self.key_words = {
            # КОМПОНЕНТ -> КЛЮЧЕВЫЕ СЛОВА В НАЗВАНИИ КАРТОЧЕК C ТОВАРОМ
            CompEnum.BATTERY: ["аккумулятор", "батарея"],
            CompEnum.MICROCONTROLLER: [],
            CompEnum.ELECTRICMOTOR: [],
            CompEnum.MOTORCONTROLLER: [],
            CompEnum.FLIGHTCONTROLLER: [],
            CompEnum.LIDAR: [],
            CompEnum.MICROFLIGHTCONTROLLER: [],
            CompEnum.RANGEFINDER: [],
            CompEnum.SATELLITECOMMMODULE: [],
            CompEnum.LEASHINGPLATFORM: [],
            CompEnum.THERMALCAMERA: [],
            CompEnum.UAVCOPTERTYPE: [],
            CompEnum.VIDEOTRANSMITTER: [],
            CompEnum.PAYLOAD: [],
            CompEnum.CONTROLPANEL: [],
        }

    @abstractmethod
    def run(comp: int) -> list:
        pass

    @abstractmethod
    def parse_battery(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        pass

    @abstractmethod
    def parse_microcontroller(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        pass

    @abstractmethod
    def parse_electricmotor(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        pass

    @abstractmethod
    def parse_motorcontroller(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        pass

    @abstractmethod
    def parse_flightcontroller(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        pass

    @abstractmethod
    def parse_lidar(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        pass

    @abstractmethod
    def parse_microflightcontroller(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        pass

    @abstractmethod
    def parse_rangefinder(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        pass

    @abstractmethod
    def parse_satellitecommmodule(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        pass

    @abstractmethod
    def parse_leashingplatform(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        pass

    @abstractmethod
    def parse_thermalcamera(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        pass

    @abstractmethod
    def parse_uavcoptertype(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        pass

    @abstractmethod
    def parse_videotransmitter(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        pass

    @abstractmethod
    def parse_payload(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        pass

    @abstractmethod
    def parse_controlpanel(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> Comp:
        pass

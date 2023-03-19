from abc import ABC, abstractmethod
from typing import Type

from models import *


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
            CompEnum.ELECTRICMOTOR: ["электромотор", "мотор"],
            CompEnum.MOTORCONTROLLER: [],
            CompEnum.FLIGHTCONTROLLER: ['полетный', 'полётный'],
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

    def parse_battery(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> CompBattery:
        return CompBattery(
            url=url,
            image=image,
            price=price,
            name=name,
            current_discharge="filler",
            capasity="filler",
            shape="filler",
            voltage="filler",
        )

    def parse_microcontroller(
        self, url: str, image: str, price: str, name: str, tiplyakov: Type
    ) -> CompMicrocontroller:
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
    ) -> CompElectricMotor:
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
    ) -> CompMotorController:
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
    ) -> CompFlightController:
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
    ) -> CompLidar:
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
    ) -> CompMicroFlightController:
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
    ) -> CompRangeFinder:
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
    ) -> CompSatelliteCommModule:
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
    ) -> CompLeashingPlatform:
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
    ) -> CompThermalCamera:
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
    ) -> CompUAVCopterType:
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
    ) -> CompVideoTransmitter:
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
    ) -> CompPayload:
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
    ) -> CompControlPanel:
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
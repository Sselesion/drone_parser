from abc import ABC, abstractmethod
from ._get_values import GetValues

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

    @staticmethod
    def parse_battery(
        url: str, image: str, price: str, name: str, text_list: list[str]
    ) -> CompBattery:
        get_values = GetValues(text_list)
        return CompBattery(
            url=url,
            image=image,
            price=price,
            name=name,
            current_discharge=get_values.get_numeric_value(
                SearchParamEnum.CURRENT_DISCHARGE
            ),
            capasity=get_values.get_numeric_value(SearchParamEnum.CAPASITY),
            shape=get_values.get_numeric_value(SearchParamEnum.SHAPE),
            voltage=get_values.get_numeric_value(SearchParamEnum.VOLTAGE),
        )

    @staticmethod
    def parse_microcontroller(
        url: str, image: str, price: str, name: str, text_list: list[str]
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

    @staticmethod
    def parse_electricmotor(
        url: str, image: str, price: str, name: str, text_list: list[str]
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

    @staticmethod
    def parse_motorcontroller(
        url: str, image: str, price: str, name: str, text_list: list[str]
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

    @staticmethod
    def parse_flightcontroller(
        url: str, image: str, price: str, name: str, text_list: list[str]
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

    @staticmethod
    def parse_lidar(
        url: str, image: str, price: str, name: str, text_list: list[str]
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

    @staticmethod
    def parse_microflightcontroller(
        url: str, image: str, price: str, name: str, text_list: list[str]
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

    @staticmethod
    def parse_rangefinder(
        url: str, image: str, price: str, name: str, text_list: list[str]
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

    @staticmethod
    def parse_satellitecommmodule(
        url: str, image: str, price: str, name: str, text_list: list[str]
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

    @staticmethod
    def parse_leashingplatform(
        url: str, image: str, price: str, name: str, text_list: list[str]
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

    @staticmethod
    def parse_thermalcamera(
        url: str, image: str, price: str, name: str, text_list: list[str]
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

    @staticmethod
    def parse_uavcoptertype(
        url: str, image: str, price: str, name: str, text_list: list[str]
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

    @staticmethod
    def parse_videotransmitter(
        url: str, image: str, price: str, name: str, text_list: list[str]
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

    @staticmethod
    def parse_payload(
        url: str, image: str, price: str, name: str, text_list: list[str]
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

    @staticmethod
    def parse_controlpanel(
        url: str, image: str, price: str, name: str, text_list: list[str]
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

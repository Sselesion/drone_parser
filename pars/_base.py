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
            # capasity=get_values.get_numeric_value(SearchParamEnum.CAPASITY),
            # shape=get_values.get_numeric_value(SearchParamEnum.SHAPE),
            # voltage=get_values.get_numeric_value(SearchParamEnum.VOLTAGE),
            url=url,
            image=image,
            price=price,
            name=name,
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
            url=url,
            image=image,
            price=price,
            name=name,
            range_detection=get_values.get_numeric_value(SearchParamEnum.RANGE_DETECTION),
            range_observation=get_values.get_numeric_value(SearchParamEnum.RANGE_OBSERVATION),
            interface=get_values.get_numeric_value(SearchParamEnum.INTERFACE),
            voltage=get_values.get_numeric_value(SearchParamEnum.VOLTAGE),
            battery_availability=get_values.get_numeric_value(SearchParamEnum.BATTERY_AVAILABILITY),
            battery_life=get_values.get_numeric_value(SearchParamEnum.FIELD_OF_VIEW),
            field_of_view=get_values.get_numeric_value(SearchParamEnum.CAPASITY),
            magnification=get_values.get_numeric_value(SearchParamEnum.MAGNIFICATION),
            protection_class=get_values.get_numeric_value(SearchParamEnum.PROTECTION_CLASS),
            work_temperature=get_values.get_numeric_value(SearchParamEnum.WORK_TEMPERATURE),
            type_of_sensor=get_values.get_numeric_value(SearchParamEnum.TYPE_OF_SENSOR),
        )

    @staticmethod
    def parse_uavcoptertype(
        url: str, image: str, price: str, name: str, text_list: list[str]
    ) -> CompUAVCopterType:
        return CompUAVCopterType(
            url=url,
            image=image,
            price=price,
            name=name,
            maximal_speed=get_values.get_numeric_value(SearchParamEnum.MAXIMAL_SPEED),
            gaining_speed=get_values.get_numeric_value(SearchParamEnum.GAINING_SPEED),
            deceleration_speed=get_values.get_numeric_value(SearchParamEnum.DECELERATION_SPEED),
            maximal_range=get_values.get_numeric_value(SearchParamEnum.MAXIMAL_RANGE),
            maximum_flight_altitude=get_values.get_numeric_value(SearchParamEnum.MAXIMUM_FLIGHT_ALTITUDE),
            power_consumption=get_values.get_numeric_value(SearchParamEnum.POWER_CONSUMPTION),
            payload_weight=get_values.get_numeric_value(SearchParamEnum.PAYLOAD_WEIGHT),
            flight_time=get_values.get_numeric_value(SearchParamEnum.FLIGHT_TIME),
            number_of_screws=get_values.get_numeric_value(SearchParamEnum.NUMBER_OF_SCREws),
        )

    @staticmethod
    def parse_videotransmitter(
        url: str, image: str, price: str, name: str, text_list: list[str]
    ) -> CompVideoTransmitter:
        return CompVideoTransmitter(
            url=url,
            image=image,
            price=price,
            name=name,
            frequency=get_values.get_numeric_value(SearchParamEnum.FREQUENCY),
            wattage=get_values.get_numeric_value(SearchParamEnum.WATTAGE),
            number_of_channels=get_values.get_numeric_value(SearchParamEnum.NUMBER_OF_CHANNELS),
            antenna_connector=get_values.get_numeric_value(SearchParamEnum.ANTENNA_CONNECTOR),
        )

    @staticmethod
    def parse_payload(
        url: str, image: str, price: str, name: str, text_list: list[str]
    ) -> CompPayload:
        return CompPayload(
            url=url,
            image=image,
            price=price,
            name=name,
            matrix=get_values.get_numeric_value(SearchParamEnum.MATRIX),
            lens=get_values.get_numeric_value(SearchParamEnum.LENS),
            magnification=get_values.get_numeric_value(SearchParamEnum.MAGNIFICATION),
            number_of_megapixels=get_values.get_numeric_value(SearchParamEnum.NUMBER_OF_MEGAPIXELS),
            resolution_TVL=get_values.get_numeric_value(SearchParamEnum.RESOLUTION_TVL),
            companion_image=get_values.get_numeric_value(SearchParamEnum.COMPANION_IMAGE),
            thermal_imager_resolution=get_values.get_numeric_value(SearchParamEnum.THERMAL_IMAGER_RESOLUTION),
            field_of_view=get_values.get_numeric_value(SearchParamEnum.FIELD_OF_VIEW),
            rangefinder=get_values.get_numeric_value(SearchParamEnum.RANGEFINDER),
            axes=get_values.get_numeric_value(SearchParamEnum.AXES),
            accuracy=get_values.get_numeric_value(SearchParamEnum.accuracy),
            tangent=get_values.get_numeric_value(SearchParamEnum.tangent),
            roll=get_values.get_numeric_value(SearchParamEnum.roll),
            yaw=get_values.get_numeric_value(SearchParamEnum.yaw),
            wattage=get_values.get_numeric_value(SearchParamEnum.WATTAGE),
            voltage=get_values.get_numeric_value(SearchParamEnum.VOLTAGE),
            current=get_values.get_numeric_value(SearchParamEnum.CURRENT),
            antenna=get_values.get_numeric_value(SearchParamEnum.ANTENNA),
            frequency=get_values.get_numeric_value(SearchParamEnum.FREQUENCY),
            number_of_channels=get_values.get_numeric_value(SearchParamEnum.NUMBER_OF_CHANNELS),
        )

    @staticmethod
    def parse_controlpanel(
        url: str, image: str, price: str, name: str, text_list: list[str]
    ) -> CompControlPanel:
        return CompControlPanel(
            url=url,
            image=image,
            price=price,
            name=name,
            frequency=get_values.get_numeric_value(SearchParamEnum.FREQUENCY),
            number_of_channels=get_values.get_numeric_value(SearchParamEnum.NUMBER_OF_CHANNELS),
            current=get_values.get_numeric_value(SearchParamEnum.CURRENT),
            voltage=get_values.get_numeric_value(SearchParamEnum.VOLTAGE),
            transmission_power=get_values.get_numeric_value(SearchParamEnum.TRANSMISSION_POWER),
            resolution=get_values.get_numeric_value(SearchParamEnum.RESOLUTION),
            wireless_protocol=get_values.get_numeric_value(SearchParamEnum.WIRELESS_PROTOCOL),
        )

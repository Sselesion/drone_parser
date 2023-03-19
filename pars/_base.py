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
        get_values = GetValues(text_list)
        return CompMicrocontroller(
            url=url,
            image=image,
            price=price,
            name=name,
            operating_frequency=get_values.get_numeric_value(SearchParamEnum.OPERATING_FREQUENCY),
            number_of_channels=get_values.get_numeric_value(SearchParamEnum.NUMBER_OF_CHANNELS),
            operating_current=get_values.get_numeric_value(SearchParamEnum.OPERATING_CURRENT),
            working_voltage=get_values.get_numeric_value(SearchParamEnum.WORKING_VOLTAGE),
            transmission_power=get_values.get_numeric_value(SearchParamEnum.TRANSMISSION_POWER),
            channel_resolution=get_values.get_numeric_value(SearchParamEnum.CHANNEL_RESOLUTION),
            wireless_protocol=get_values.get_numeric_value(SearchParamEnum.WIRELESS_PROTOCOL),
        )

    @staticmethod
    def parse_electricmotor(
        url: str, image: str, price: str, name: str, text_list: list[str]
    ) -> CompElectricMotor:
        get_values = GetValues(text_list)
        return CompElectricMotor(
            url=url,
            image=image,
            price=price,
            name=name,
            voltage=get_values.get_numeric_value(SearchParamEnum.VOLTAGE),
            maximum_power=get_values.get_numeric_value(SearchParamEnum.MAXIMUM_POWER),
            recommended_battery=get_values.get_numeric_value(SearchParamEnum.RECOMMENDED_BATTERY),
            noload_current=get_values.get_numeric_value(SearchParamEnum.NOLOAD_CURRENT),
            peak_current=get_values.get_numeric_value(SearchParamEnum.PEAK_CURRENT),
            stator_length=get_values.get_numeric_value(SearchParamEnum.STATOR_LENGTH),
            stator_diameter=get_values.get_numeric_value(SearchParamEnum.STATOR_DIAMETER),
            shaft_diameter=get_values.get_numeric_value(SearchParamEnum.SHAFT_DIAMETER),
            number_of_revolutions_per_volt=get_values.get_numeric_value(SearchParamEnum.NUMBER_OF_REVOLUTIONS_PER_VOLT),
            resistance=get_values.get_numeric_value(SearchParamEnum.RESISTANCE),
        )

    @staticmethod
    def parse_motorcontroller(
        url: str, image: str, price: str, name: str, text_list: list[str]
    ) -> CompMotorController:
        get_values = GetValues(text_list)
        return CompMotorController(
            url=url,
            image=image,
            price=price,
            name=name,
            operating_current=get_values.get_numeric_value(SearchParamEnum.OPERATING_CURRENT),
            peak_current=get_values.get_numeric_value(SearchParamEnum.PEAK_CURRENT),
            power_support=get_values.get_numeric_value(SearchParamEnum.POWER_SUPPORT),
        )

    @staticmethod
    def parse_flightcontroller(
        url: str, image: str, price: str, name: str, text_list: list[str]
    ) -> CompFlightController:
        get_values = GetValues(text_list)
        return CompFlightController(
            url=url,
            image=image,
            price=price,
            name=name,
            presence_of_a_barometer=get_values.get_numeric_value(SearchParamEnum.PRESENCE_OF_A_BAROMETER),
            presence_of_a_black_box=get_values.get_numeric_value(SearchParamEnum.PRESENCE_OF_A_BLACK_BOX),
            power=get_values.get_numeric_value(SearchParamEnum.POWER),
            firmware=get_values.get_numeric_value(SearchParamEnum.FIRMWARE),
            presence_of_a_usb_connector=get_values.get_numeric_value(SearchParamEnum.PRESENCE_OF_A_USB_CONNECTOR),
            fastening=[get_values.get_numeric_value(SearchParamEnum.FASTENING)],
        )

    @staticmethod
    def parse_lidar(
        url: str, image: str, price: str, name: str, text_list: list[str]
    ) -> CompLidar:
        get_values = GetValues(text_list)
        return CompLidar(
            url=url,
            image=image,
            price=price,
            name=name,
            max_range=get_values.get_numeric_value(SearchParamEnum.MATRIX),
            frequency=get_values.get_numeric_value(SearchParamEnum.FREQUENCY),
            power_supply=get_values.get_numeric_value(SearchParamEnum.POWER_SUPPLY),
        )

    @staticmethod
    def parse_microflightcontroller(
        url: str, image: str, price: str, name: str, text_list: list[str]
    ) -> CompMicroFlightController:
        get_values = GetValues(text_list)
        return CompMicroFlightController(
            url=url,
            image=image,
            price=price,
            name=name,
            clock_requency=get_values.get_numeric_value(SearchParamEnum.CLOCK_FREQUENCY),
            flash_memory_capacity=get_values.get_numeric_value(SearchParamEnum.FLASH_MEMORY_CAPACITY),
            mounting=get_values.get_numeric_value(SearchParamEnum.MOUNTING),
            min_input_voltage=get_values.get_numeric_value(SearchParamEnum.MIN_INPUT_VOLTAGE),
            max_input_voltage=get_values.get_numeric_value(SearchParamEnum.MAX_INPUT_VOLTAGE),
            uart_ports_number=get_values.get_numeric_value(SearchParamEnum.UART_PORTS_NUMBER),
        )

    @staticmethod
    def parse_rangefinder(
        url: str, image: str, price: str, name: str, text_list: list[str]
    ) -> CompRangeFinder:
        get_values = GetValues(text_list)
        return CompRangeFinder(
            url=url,
            image=image,
            price=price,
            name=name,
            max_range=get_values.get_numeric_value(SearchParamEnum.MAX_RANGE),
            frequency=get_values.get_numeric_value(SearchParamEnum.FREQUENCY),
            wave_length=get_values.get_numeric_value(SearchParamEnum.WAVE_LENGTH),
            power_supply=get_values.get_numeric_value(SearchParamEnum.POWER_SUPPLY),
        )

    @staticmethod
    def parse_satellitecommmodule(
        url: str, image: str, price: str, name: str, text_list: list[str]
    ) -> CompSatelliteCommModule:
        get_values = GetValues(text_list)
        return CompSatelliteCommModule(
            url=url,
            image=image,
            price=price,
            name=name,
            battery_availability=get_values.get_numeric_value(SearchParamEnum.BATTERY_AVAILABILITY),
            battery_life=get_values.get_numeric_value(SearchParamEnum.BATTERY_LIFE),
            accuracy=get_values.get_numeric_value(SearchParamEnum.ACCURACY),
        )

    @staticmethod
    def parse_leashingplatform(
        url: str, image: str, price: str, name: str, text_list: list[str]
    ) -> CompLeashingPlatform:
        get_values = GetValues(text_list)
        return CompLeashingPlatform(
            url=url,
            image=image,
            price=price,
            name=name,
            max_speed=get_values.get_numeric_value(SearchParamEnum.MAX_SPEED),
            gaining_speed=get_values.get_numeric_value(SearchParamEnum.GAINING_SPEED),
            deceleration_speed=get_values.get_numeric_value(SearchParamEnum.DECELERATION_SPEED),
            flight_range=get_values.get_numeric_value(SearchParamEnum.FLIGHT_RANGE),
            flight_altitude=get_values.get_numeric_value(SearchParamEnum.FLIGHT_ALTITUDE),
            power_consumption=get_values.get_numeric_value(SearchParamEnum.POWER_CONSUMPTION),
            payload_weight=get_values.get_numeric_value(SearchParamEnum.PAYLOAD_WEIGHT),
            flight_time=get_values.get_numeric_value(SearchParamEnum.FLIGHT_TIME),
            screws_number=get_values.get_numeric_value(SearchParamEnum.SCREWS_NUMBER),
        )

    @staticmethod
    def parse_thermalcamera(
        url: str, image: str, price: str, name: str, text_list: list[str]
    ) -> CompThermalCamera:
        get_values = GetValues(text_list)
        return CompThermalCamera(
            url=url,
            image=image,
            price=price,
            name=name,
            range_detection=get_values.get_numeric_value(SearchParamEnum),
            range_observation=get_values.get_numeric_value(SearchParamEnum),
            interface=get_values.get_numeric_value(SearchParamEnum),
            voltage=get_values.get_numeric_value(SearchParamEnum),
            battery_availability=get_values.get_numeric_value(SearchParamEnum),
            battery_life=get_values.get_numeric_value(SearchParamEnum),
            field_of_view=get_values.get_numeric_value(SearchParamEnum),
            magnification=get_values.get_numeric_value(SearchParamEnum),
            protection_class=get_values.get_numeric_value(SearchParamEnum),
            work_temperature=get_values.get_numeric_value(SearchParamEnum),
            type_of_sensor=get_values.get_numeric_value(SearchParamEnum),
        )

    @staticmethod
    def parse_uavcoptertype(
        url: str, image: str, price: str, name: str, text_list: list[str]
    ) -> CompUAVCopterType:
        get_values = GetValues(text_list)
        return CompUAVCopterType(
            url=url,
            image=image,
            price=price,
            name=name,
            maximal_speed=get_values.get_numeric_value(SearchParamEnum),
            gaining_speed=get_values.get_numeric_value(SearchParamEnum),
            deceleration_speed=get_values.get_numeric_value(SearchParamEnum),
            maximal_range=get_values.get_numeric_value(SearchParamEnum),
            maximum_flight_altitude=get_values.get_numeric_value(SearchParamEnum),
            power_consumption=get_values.get_numeric_value(SearchParamEnum),
            payload_weight=get_values.get_numeric_value(SearchParamEnum),
            flight_time=get_values.get_numeric_value(SearchParamEnum),
            number_of_screws=get_values.get_numeric_value(SearchParamEnum),
        )

    @staticmethod
    def parse_videotransmitter(
        url: str, image: str, price: str, name: str, text_list: list[str]
    ) -> CompVideoTransmitter:
        get_values = GetValues(text_list)
        return CompVideoTransmitter(
            url=url,
            image=image,
            price=price,
            name=name,
            frequency=get_values.get_numeric_value(SearchParamEnum),
            wattage=get_values.get_numeric_value(SearchParamEnum),
            number_of_channels=get_values.get_numeric_value(SearchParamEnum),
            antenna_connector=get_values.get_numeric_value(SearchParamEnum),
        )

    @staticmethod
    def parse_payload(
        url: str, image: str, price: str, name: str, text_list: list[str]
    ) -> CompPayload:
        get_values = GetValues(text_list)
        return CompPayload(
            url=url,
            image=image,
            price=price,
            name=name,
            matrix=get_values.get_numeric_value(SearchParamEnum),
            lens=get_values.get_numeric_value(SearchParamEnum),
            magnification=get_values.get_numeric_value(SearchParamEnum),
            number_of_megapixels=get_values.get_numeric_value(SearchParamEnum),
            resolution_TVL=get_values.get_numeric_value(SearchParamEnum),
            companion_image=get_values.get_numeric_value(SearchParamEnum),
            thermal_imager_resolution=get_values.get_numeric_value(SearchParamEnum),
            field_of_view=get_values.get_numeric_value(SearchParamEnum),
            rangefinder=get_values.get_numeric_value(SearchParamEnum),
            axes=get_values.get_numeric_value(SearchParamEnum),
            accuracy=get_values.get_numeric_value(SearchParamEnum),
            tangent=get_values.get_numeric_value(SearchParamEnum),
            roll=get_values.get_numeric_value(SearchParamEnum),
            yaw=get_values.get_numeric_value(SearchParamEnum),
            wattage=get_values.get_numeric_value(SearchParamEnum),
            voltage=get_values.get_numeric_value(SearchParamEnum),
            current=get_values.get_numeric_value(SearchParamEnum),
            antenna=get_values.get_numeric_value(SearchParamEnum),
            frequency=get_values.get_numeric_value(SearchParamEnum),
            number_of_channels=get_values.get_numeric_value(SearchParamEnum),
        )

    @staticmethod
    def parse_controlpanel(
        url: str, image: str, price: str, name: str, text_list: list[str]
    ) -> CompControlPanel:
        get_values = GetValues(text_list)
        return CompControlPanel(
            url=url,
            image=image,
            price=price,
            name=name,
            frequency=get_values.get_numeric_value(SearchParamEnum),
            number_of_channels=get_values.get_numeric_value(SearchParamEnum),
            current=get_values.get_numeric_value(SearchParamEnum),
            voltage=get_values.get_numeric_value(SearchParamEnum),
            transmission_power=get_values.get_numeric_value(SearchParamEnum),
            resolution=get_values.get_numeric_value(SearchParamEnum),
            wireless_protocol=get_values.get_numeric_value(SearchParamEnum),
        )

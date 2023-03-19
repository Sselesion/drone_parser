from enum import Enum, auto
from dataclasses import dataclass

from pydantic import BaseModel


class Comp(BaseModel):
    url: str
    image: str
    price: str
    name: str


class CompBattery(Comp):
    current_discharge: str  # Разряд тока (Ампер);
    capasity: str  # Емкость (мА/ч);
    shape: str  # Форм фактор (длина * ширина * высота);
    voltage: str  # Напряжение (Вольт);


class CompMicrocontroller(Comp):
    operating_frequency: str  # Рабочая частота (ГГц);
    number_of_channels: str  # Число каналов;
    operating_current: str  # Рабочий ток (мАмпер);
    working_voltage: str  # Рабочее напряжение (Вольт);
    transmission_power: str  # Мощность передачи (дБм);
    channel_resolution: str  # Разрешение канала;
    wireless_protocol: str  # Беспроводной протокол;


class CompElectricMotor(Comp):
    voltage: str  # Напряжение (Вольт);
    maximum_power: str  # Максимальная мощность (Ватт);
    recommended_battery: str  # Рекомендуемая батарея (название модели или ссылка);
    noload_current: str  # Ток холостого хода (Ампер);
    peak_current: str  # Пиковый ток (Ампер);
    stator_length: str  # Длина статора (мм);
    stator_diameter: str  # Диаметр статора (мм);
    shaft_diameter: str  # Диаметр вала (мм);
    number_of_revolutions_per_volt: str  # Число оборотов на 1 вольт;
    resistance: str  # Сопротивление (Ом);


class CompMotorController(Comp):
    operating_current: str  # Рабочий ток (Ампер);
    peak_current: str  # Пиковый ток (Ампер);
    power_support: bool  # Поддержка питания (Да/Нет);


class CompFlightController(Comp):
    presence_of_a_barometer: bool  # Наличие барометра;
    presence_of_a_black_box: bool  # Наличие черного ящика;
    power: str  # Питание (Вольт);
    firmware: str  # Прошивка (название);
    presence_of_a_usb_connector: str  # Наличие usb разъема;
    fastening: list[
        str
    ]  # Крепление (посадочное место для крепления. Здесь нужно расстояние между отверстиями т.е. 40мм*50мм);


class CompLidar(Comp):
    max_range: str  # Максимальная дальность использования (метров)
    frequency: str  # Частота импульсов (Герц)
    power_supply: str  # Питание (вольт)


class CompMicroFlightController(Comp):
    clock_requency: str  # Тактовая частота (МГц)
    flash_memory_capacity: str  # Объем флеш памяти (Кб)
    # посадочное место для крепления (расстояние между отверстиями т.е. 40мм*50мм)
    mounting: list[str]
    min_input_voltage: str  # Минимальное входное напряжение (Вольт)
    max_input_voltage: str  # Максимальное входное напряжение (Вольт)
    uart_ports_number: str  # Число UART портов


class CompRangeFinder(Comp):
    max_range: str  # Максимальная дальность использования (метров)
    frequency: str  # Частота работы (Гц)
    wave_length: str  # Длина волны (нм)
    power_supply: str  # Питание (вольт)


class CompSatelliteCommModule(Comp):
    battery_availability: bool  # Наличие батареи
    battery_life: str  # Время работы от батареи (часов)
    accuracy: str  # Погрешность (м)


class CompLeashingPlatform(Comp):
    max_speed: str  # Максимальная скорость (км/ч)
    gaining_speed: str  # Скорость набора высоты (км/ч)
    deceleration_speed: str  # Скорость снижения (км/ч)
    flight_range: str  # Максимальная дальность полета (м)
    flight_altitude: str  # Максимальная высота полета (м)
    power_consumption: str  # Энергопотребление (Вт/ч)
    payload_weight: str  # Масса полезной погрузки (г)
    flight_time: str  # Продолжительность полета (мин)
    screws_number: str  # Число винтов


class CompThermalCamera(Comp):
    range_detection: str  # Дальность обнаружения (м)
    range_observation: str  # Дистанция наблюдения (м)
    interface: str  # Интерфейс
    voltage: str  # Напряжение (Вольт)
    battery_availability: str  # Наличие батареи (Вт/ч)
    battery_life: str  # Время работы от батареи (ч)
    field_of_view: str  # Поле зрения
    magnification: str  # Увеличение
    protection_class: str  # Класс защиты
    work_temperature: str  # Рабочая температура
    type_of_sensor: str  # Тип матрицы


class CompUAVCopterType(Comp):
    maximal_speed = str  # Максимальная скорость (км/ч)
    gaining_speed = str  # Скорость набора (км/ч)
    deceleration_speed = str  # Скорость снижения (км/ч)
    maximal_range = str  # Максимальная дальность полета (м)
    maximum_flight_altitude = str  # Максимальная дальность полета (м)
    power_consumption = str  # Энергопотребление (Вт/ч)
    payload_weight = str  # Масса полезной погрузки (г)
    flight_time = str  # Продолжительность полета (мин)
    number_of_screws = int  # Число винтов


class CompVideoTransmitter(Comp):
    frequency = str  # Частота приема (ГГц)
    wattage = str  # Мощность (мВт)
    number_of_channels = int  # Число каналов
    antenna_connector = str  # Разъем антенны


class CompPayload(Comp):
    matrix = str  # Матрица
    lens = str  # Объектив
    magnification = str  # Увеличение
    number_of_megapixels = str  # Число мегапикселей
    resolution_TVL = str  # Разрешение, TVL
    companion_image = str  # Сопровождение
    thermal_imager_resolution = str  # Разрешение тепловизора
    field_of_view = str  # Поле зрения
    rangefinder = str  # Дальномер
    axes = str  # Число осей стабилизации
    accuracy = str  # Точность
    tangent = str  # Рабочие углы стабилизации, Тангаж
    roll = str  # Рабочие углы стабилизации, Крен
    yaw = str  # Рабочие углы стабилизации, Рысканье
    wattage = str  # Мощность (мВт)
    voltage = str  # Питание (Вольт)
    current = str  # Ток (мА)
    antenna = str  # Антенна (при наличии указать название)
    frequency = str  # Частота (ГГц)
    number_of_channels = str  # Число каналов


class CompControlPanel(Comp):
    frequency = str  # Рабочая частота (ГГц)
    number_of_channels = str  # Число каналов
    current = str  # Рабочий ток (мА)
    voltage = str  # Рабочее напряжение (Вольт)
    transmission_power = str  # Мощность передачи (дБм)
    resolution = str  # Разрешение канала
    wireless_protocol = str  # Беспроводной протокол


class CompEnum(Enum):
    BATTERY = auto()
    MICROCONTROLLER = auto()
    ELECTRICMOTOR = auto()
    MOTORCONTROLLER = auto()
    FLIGHTCONTROLLER = auto()
    LIDAR = auto()
    MICROFLIGHTCONTROLLER = auto()
    RANGEFINDER = auto()
    SATELLITECOMMMODULE = auto()
    LEASHINGPLATFORM = auto()
    THERMALCAMERA = auto()
    UAVCOPTERTYPE = auto()
    VIDEOTRANSMITTER = auto()
    PAYLOAD = auto()
    CONTROLPANEL = auto()

from enum import Enum
from dataclasses import dataclass

from pydantic import BaseModel


class Comp(BaseModel):
    url: str
    comp_type: str


class CompBattery(Comp):
    current_discharge: str # Разряд тока (Ампер);
    capasity: str  # Емкость (мА/ч);
    shape: list[int] # Форм фактор (длина * ширина * высота);
    voltage: str # Напряжение (Вольт);

class ThermalCamera(Comp):
    range_detection: str # Дальность обнаружения (м)
    range_observation: str # Дистанция наблюдения (м)
    interface: str # Интерфейс
    voltage: str # Напряжение (Вольт)
    battery_availability: str # Наличие батареи (Вт/ч)
    battery_life: str # Время работы от батареи (ч)
    field_of_view: str # Поле зрения
    magnification: str # Увеличение
    protection_class: str # Класс защиты
    work_temperature: str # Рабочая температура
    type_of_sensor: str # Тип матрицы

class UAVCopterType(Comp):
    maximal_speed = str # Максимальная скорость (км/ч)
    gaining_speed = str # Скорость набора (км/ч)
    deceleration_speed = str # Скорость снижения (км/ч)
    maximal_range = str # Максимальная дальность полета (м)
    maximum_flight_altitude = str # Максимальная дальность полета (м)
    power_consumption = str # Энергопотребление (Вт/ч)
    payload_weight = str # Масса полезной погрузки (г)
    flight_time = str # Продолжительность полета (мин)
    number_of_screws = int # Число винтов


class VideoTransmitter(Comp):
    frequency = str # Частота приема (ГГц)
    wattage = str # Мощность (мВт)
    number_of_channels = int # Число каналов
    antenna_connector = str # Разъем антенны


class Payload(Comp):
    matrix = str # Матрица
    lens = str # Объектив
    magnification = str # Увеличение
    number_of_megapixels = str # Число мегапикселей
    resolution_TVL = str # Разрешение, TVL
    companion_image = str # Сопровождение
    thermal_imager_resolution = str # Разрешение тепловизора
    field_of_view = str # Поле зрения
    rangefinder = str # Дальномер
    axes = str # Число осей стабилизации
    accuracy = str # Точность
    tangent = str # Рабочие углы стабилизации, Тангаж
    roll = str # Рабочие углы стабилизации, Крен
    yaw = str # Рабочие углы стабилизации, Рысканье
    wattage = str # Мощность (мВт)
    voltage = str # Питание (Вольт)
    current = str # Ток (мА)
    antenna = str # Антенна (при наличии указать название)
    frequency = str # Частота (ГГц)
    number_of_channels = str # Число каналов


class ControlPanel(Comp):
    frequency = str # Рабочая частота (ГГц)
    number_of_channels = str # Число каналов
    current = str # Рабочий ток (мА)
    voltage = str # Рабочее напряжение (Вольт)
    transmission_power = str # Мощность передачи (дБм)
    resolution = str # Разрешение канала
    wireless_protocol = str # Беспроводной протокол

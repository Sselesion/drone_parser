from enum import Enum
from dataclasses import dataclass

from pydantic import BaseModel


class Comp(BaseModel):
    url: str
    comp_type: str


class CompBattery(Comp):
    current_discharge: str  # Разряд тока (Ампер);
    capasity: str  # Емкость (мА/ч);
    shape: list[str]  # Форм фактор (длина * ширина * высота);
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
    fastening: list[str]  # Крепление (посадочное место для крепления. Здесь нужно расстояние между отверстиями т.е. 40мм*50мм);

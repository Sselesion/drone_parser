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

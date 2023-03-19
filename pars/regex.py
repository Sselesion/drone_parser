import re
from enum import Enum


class PtrnEnum(Enum):
    CAPASITY = r" [е|ё]мкость[ а-я]*:? (\d+)"
    VOLTAGE = r" напряжение[ а-я]*:? (\d+,?\d+)"
    SHAPE = r" размер[ а-я]*:? ([\d+[×XxхХ\]?\d+]+)"
    CURRENT_DISCHARGE = r" разряд тока:? (\d+) [м]?[А]"

    # CompUAVCopterType
    MAXIMAL_SPEED = r" [е|ё]мкость[ а-я]*:? (\d+)"
    GAINING_SPEED = r" [е|ё]мкость[ а-я]*:? (\d+)"
    DECELERATION_SPEED = r" [е|ё]мкость[ а-я]*:? (\d+)"
    MAXIMAL_RANGE = r" [е|ё]мкость[ а-я]*:? (\d+)"
    MAXIMUM_FLIGHT_ALTITUDE = r" [е|ё]мкость[ а-я]*:? (\d+)"
    POWER_CONSUMPTION = r" [е|ё]мкость[ а-я]*:? (\d+)"
    PAYLOAD_WEIGHT = r" [е|ё]мкость[ а-я]*:? (\d+)"
    FLIGHT_TIME = r" [е|ё]мкость[ а-я]*:? (\d+)"
    NUMBER_OF_SCREWS = r" [е|ё]мкость[ а-я]*:? (\d+)"


class Regex:
    def __init__(self, texts) -> None:
        self.raw_text = self.format_text(texts)

    def format_text(self, texts):
        return " " + " ".join(texts).lower().replace("\n", " ").strip()

    def find_by(self, ptrn: PtrnEnum) -> str:
        regexp = re.compile(ptrn.value)
        re_match = regexp.search(self.raw_text)
        if re_match:
            print(list(re_match.groups()))
        results = list(re_match.groups()) if re_match else []
        return results[0] if results else "-"

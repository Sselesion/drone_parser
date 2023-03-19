import re
from enum import Enum


class PtrnEnum(Enum):
    CAPASITY = (r" [е|ё]мкость[ а-я]*:? (\d+)", 0)
    VOLTAGE = (r" напряжение[ а-я]*:? (\d+,?\d+)", 0)
    SHAPE = (r" размер[ а-я]*:? ([\d+[×XxхХ\]?\d+]+)", 0)
    CURRENT_DISCHARGE = (r" разряд тока:? (\d+) [м]?[А]", 0)

    # CompUAVCopterType
    MAXIMAL_SPEED = (r" (максимальная горизонтальная|горизонтальная|макс.?|максимальная) скорость:? (\d*)", 1)
    GAINING_SPEED = (r" (максимальная|макс.?) скорость (набора высоты|набора)( режим [a-z]:?)? (\d*)", 3)
    DECELERATION_SPEED = (r" (максимальная|макс.?) скорость (снижения высоты|снижения) (\(наклон\)|\(по вертикали\))? (режим [a-z]:?)? (\d*)", 4)
    MAXIMAL_RANGE = (r" [е|ё]мкость[ а-я]*:? (\d+)", 0)
    MAXIMUM_FLIGHT_ALTITUDE = (r" [е|ё]мкость[ а-я]*:? (\d+)", 0)
    POWER_CONSUMPTION = (r" [е|ё]мкость[ а-я]*:? (\d+)", 0)
    PAYLOAD_WEIGHT = (r" [е|ё]мкость[ а-я]*:? (\d+)", 0)
    FLIGHT_TIME = (r" [е|ё]мкость[ а-я]*:? (\d+)", 0)
    NUMBER_OF_SCREWS = (r" [е|ё]мкость[ а-я]*:? (\d+)", 0)

    def __init__(self, reg: str, n_group: int) -> None:
        self.reg = reg
        self.n_group = n_group

class PtrnGroupEnum(Enum):
    CAPASITY = 0
    VOLTAGE = 0
    SHAPE = 0
    CURRENT_DISCHARGE = 0

class Regex:
    def __init__(self, texts) -> None:
        self.raw_text = self.format_text(texts)


    def format_text(self, texts):
        return " " + " ".join(texts).lower().replace("\n", " ").strip()

    def find_by(self, ptrn: PtrnEnum) -> str:
        regexp = re.compile(ptrn.reg)
        re_match = regexp.search(self.raw_text)
        # if re_match:
        #     print(list(re_match.groups()))
        results = list(re_match.groups()) if re_match else []
        return results[ptrn.n_group] if ptrn.n_group < len(results) else "-"

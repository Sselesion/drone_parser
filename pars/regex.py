import re
from enum import Enum


class PtrnEnum(Enum):

    CAPASITY = (r" [е|ё]мкость[ а-я]*:? (\d+)", 0)
    VOLTAGE = (r" напряжение[ а-я]*:? (\d+,?\d+)", 0)
    SHAPE = (r" размер[ а-я]*:? ([\d+[×XxхХ\]?\d+]+)", 0)
    CURRENT_DISCHARGE = (r" разряд тока:? (\d+) [м]?[А]", 0)
    INTERFACE = r""


    # CompUAVCopterType
    MAXIMAL_SPEED = (r" (максимальная горизонтальная|горизонтальная|макс.?|максимальная) скорость:? (\d*)", 1)
    GAINING_SPEED = (r" (максимальная|макс.?) скорость (набора высоты|набора)( режим [a-z]:?)? (\d*)", 3)
    DECELERATION_SPEED = (r" (максимальная|макс.?) скорость (снижения высоты|снижения) (\(наклон\)|\(по вертикали\))? (режим [a-z]:?)? (\d*)", 4)
    MAX_RANGE = (r" [е|ё]мкость[ а-я]*:? (\d+)", 0)
    MAX_FLIGHT_ALTITUDE = (r" (макс.?|максимальная) (высота полета|высота) (над уровнем моря )?:?(\d+)", 3)
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
    def __init__(self, texts: list) -> None:
        self.raw_text = self.format_text(texts)


    def format_text(self, texts: list):
        result = " ".join(texts).lower().replace("\n", " ").strip()
        filter_result = list(filter(lambda el: el != '', result.split()))
        return " " + " ".join(filter_result)


    def find_by(self, ptrn: PtrnEnum) -> str:
        regexp = re.compile(ptrn.reg)
        re_match = regexp.search(self.raw_text)
        
        results = list(re_match.groups()) if re_match else []
        return results[ptrn.n_group] if ptrn.n_group < len(results) else "-"

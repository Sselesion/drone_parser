from abc import ABC, abstractmethod

from models import *

comp_type = {
    0: CompBattery,
    1: CompMicrocontroller,
    2: CompElectricMotor,
    4: CompMotorController,
    5: CompFlightController,
    6: CompLidar,
    7: CompMicroFlightController,
    8: CompRangeFinder,
    9: CompSatelliteCommModule,
    10: CompLeashingPlatform,
    11: CompThermalCamera,
    12: CompUAVCopterType,
    13: CompVideoTransmitter,
    14: CompPayload,
    15: CompControlPanel,
}


class Parse(ABC):
    def __init__(self, url, idx) -> None:
        self.url = url
        self.idx = idx

    @abstractmethod
    def run(comp: int) -> list:
        pass

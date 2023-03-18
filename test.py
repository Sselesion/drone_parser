from pars.aeromotus import AeromotusParser
from models import CompEnum

if __name__ == "__main__":
    aero = AeromotusParser()
    aero.run(CompEnum.BATTERY)

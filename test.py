from pars.aeromotus import AeromotusParser
from models import CompEnum

if __name__ == "__main__":
    aero = AeromotusParser()
    print('result >>>>>>>> ', aero.run(CompEnum.BATTERY))

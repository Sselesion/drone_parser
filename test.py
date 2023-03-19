import pprint
from pars.aeromotus import AeromotusParser
from models import CompEnum

parsers = [
    AeromotusParser(),
]

if __name__ == "__main__":
    parse_results = {}
    for comp in CompEnum:
        print("COMP\t>>>>>>>> ", comp)
        for parse in parsers:
            if parse.idx in [0]:
                print("PARSE\t>>>>>>>> ", parse.__class__.__name__)
                parse_results.update({comp: parse.run(comp)})
    pprint.pprint(
        object=("result\t>>>>>>>> ", parse_results), indent=2, sort_dicts=True, width=40
    )
    # aero = AeromotusParser()
    # result = aero.run(CompEnum.BATTERY)
    # print('result >>>>>>>> ', result)

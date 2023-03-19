from models import CompEnum

from .aeromotus import AeromotusParser
from .fixfly import FixFlyParser
from .air_hobby import AirHobbyParser
from .mydrone import MyDroneParser

parsers = [
    AeromotusParser(),
    AirHobbyParser(),
    MyDroneParser(),
]


def parse(site_idxs: list) -> dict[CompEnum, dict]:
    parse_results = {}
    for comp in CompEnum:
        print('>>>>\t', comp)
        for parse in parsers:
            if parse.idx in site_idxs:
                print('>>>>\t', parse.url)
                parse_results.update({comp: parse.run(comp)})
    print('RESULT >>>>\t', parse_results)
    return parse_results

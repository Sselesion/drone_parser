from models import CompEnum

from .aeromotus import AeromotusParser
from .fixfly import FixFlyParser
from .air_hobby import AirHobbyParser
from .mydrone import MyDroneParser

parsers = [
    AeromotusParser(),
    AirHobbyParser(),
    MyDroneParser(),
    FixFlyParser(),
]


def parse(site_idxs: list) -> dict[CompEnum, dict]:
    parse_results = {}
    for comp in CompEnum:
        print("Поиск для компонента: ", comp.value)

        curr_parse_result = {}
        for parse in parsers:
            if parse.idx in site_idxs:
                print("На сайте: ", parse.url)
                curr_parse_result.update(parse.run(comp))

        parse_results.update({comp: curr_parse_result})

    print("Парсинг завершен!")
    return parse_results

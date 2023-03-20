import pprint
from pars.aeromotus import AeromotusParser
from pars.air_hobby import AirHobbyParser
from pars.mydrone import MyDroneParser
from models import CompEnum
from get_excel import parse_and_write_excel

parsers = [
    AeromotusParser(),
    AirHobbyParser(),
    MyDroneParser(),
]

if __name__ == "__main__":
    # for comp in CompEnum:
    #     print("COMP\t>>>>>>>> ", comp)
    #     for parse in parsers:
    #         if parse.idx in [0]:
    #             print("PARSE\t>>>>>>>> ", parse.__class__.__name__)
    #             parse_results.update({comp: parse.run(comp)})
    # pprint.pprint(
    #     object=("result\t>>>>>>>> ", parse_results), indent=2, sort_dicts=True, width=40
    # )
    parse_results = {}
    for comp in CompEnum:
        print(comp)
        curr_parse_result = {}
        for parse in parsers:
            curr_parse_result.update(parse.run(comp))
            print(parse.url)
        parse_results.update({comp: curr_parse_result})
    parse_and_write_excel(parse_results)


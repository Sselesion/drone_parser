import pprint
from pars.aeromotus import AeromotusParser
from pars.air_hobby import AirHobbyParser
from pars.mydrone import MyDroneParser
from pars.fixfly import FixFlyParser
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
    fix_fly = FixFlyParser()
    parse_results = {}
    for comp in [CompEnum.BATTERY]:
        print(comp)
        curr_parse_result = {}
        curr_parse_result.update(fix_fly.run(comp))
        
        # for parse in parsers:
        #     print(parse.url)
        parse_results.update({comp: curr_parse_result})
    print(parse_results)
    parse_and_write_excel(parse_results)


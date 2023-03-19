from .aeromotus import AeromotusParser
from models import CompEnum

parsers = [
    AeromotusParser(),
]


def parse(site_idxs: list) -> dict[CompEnum, dict]:
    parse_results = {}
    for comp in CompEnum:
        for parse in parsers:
            if parse.idx in site_idxs:
                parse_results.update({comp: parse.run(comp)})
    return parse_results

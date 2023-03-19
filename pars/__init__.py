from models import CompEnum

from .aeromotus import AeromotusParser
from .fixfly import FixFlyParser

parsers = [AeromotusParser(), FixFlyParser()]


def parse(site_idxs: list) -> dict[CompEnum, dict]:
    parse_results = {}
    for comp in CompEnum:
        for parse in parsers:
            if parse.idx in site_idxs:
                parse_results.update({comp: parse.run(comp)})
    return parse_results

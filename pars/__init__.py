from models import CompEnum

from ui.appLoggerWidget import LoggerWidget
from .aeromotus import AeromotusParser
from .fixfly import FixFlyParser

parsers = [AeromotusParser(), FixFlyParser()]


def parse(site_idxs: list, loggerWidget: LoggerWidget) -> dict[CompEnum, dict]:
    parse_results = {}
    for comp in CompEnum:
        loggerWidget.info("Запущен поиск для компонента '%s'" % comp)
        for parse in parsers:
            if parse.idx in site_idxs:
                loggerWidget.info("Поиск компонента произодится для сайта %s" % parse.url)
                parse_results.update({comp: parse.run(comp)})
    return parse_results

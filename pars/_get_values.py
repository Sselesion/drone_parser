import re

from models import SearchParamEnum


class GetValues:
    def __init__(self, text_list: list[str]) -> None:
        self.raw_text = self._format_text(text_list)

    def get_numeric_value(
        self, search_param: SearchParamEnum, localization=50
    ) -> list[str]:
        """Получение числового значения с учетом его системы
        измерения. e.g. 5600 mah"""
        cuurent_text = self.raw_text
        for keyw in search_param.key_words:
            idx = cuurent_text.find(keyw)
            if idx == -1:
                continue
            idx_end = idx + localization
            if idx_end > len(cuurent_text):
                idx_end = len(cuurent_text)
            target_area = cuurent_text[idx:idx_end]
            for unit in search_param.units:
                index_list = target_area.find(" " + unit + " ")
                if index_list == []:
                    continue
                if index_list == -1:
                    continue
                nums = re.findall(r"\d+[.,\d*]*", target_area[:index_list])
                return nums[-1] if nums else '-'
        return '-'

    def _format_text(self, text_list: list):
        result = " ".join(text_list).lower().replace("\n", " ").strip()
        filter_result = list(filter(lambda el: el != "", result.split()))
        return " " + " ".join(filter_result)

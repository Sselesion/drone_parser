import re

"""

"""

battery_dict = {
                'current_discharge': {
                    'keyw': ['разряд тока','разряд','ток разряда','выходной ток','ток выхода'],
                    'units': ['Ампер','А','Амп','A'],
                    'rezValue':''
                },
                'capacity': {
                    'keyw': ['емкость','ёмкость','capacity'],
                    'units': ['мач','ач','ah','mah', 'мaч', 'maч', 'mач'],
                    'rezValue':''
                },
                'form_factor': {
                    'keyw': ['длина','ширина','высота', 'размер','форм фактор','габариты'],
                    'units': ['см','м','дм','cm', 'm', 'dm', 'cм'],
                    'rezValue':''
                }
}


def ParseDict(objDict,text):
    
    text=format_text(text)
    localization = 50
    all_fields=objDict.keys()
    for component in all_fields:
        
        list_keyw=[format_text(i) for i in objDict[component]['keyw']]
        list_unit=[format_text(i) for i in objDict[component]['units']]
        for keyw in list_keyw:
            idx=text.find(keyw)
            if idx ==-1:
                continue
            idx_end = idx+localization
            if idx_end>len(text):
                idx_end=len(text)
            target_area=text[idx:idx_end]
            for unit in list_unit:
                index_list = target_area.find(' '+unit+' ')
                if index_list==[]:
                    continue
                if index_list==-1:
                    continue

                nums = re.findall(r'\d*\.\d+|\d+',target_area[:index_list] )
                nums = [float(i) for i in nums]
                
                objDict[component]['rezValue'] = nums
                
    print(objDict)
    return objDict
    
class emptyClass:
    pass

def ClassGenerator(url, image, price, name, objDict):
    if [objDict.keys()]==[battery_dict.keys()]:
        CompBattery = emptyClass()
        CompBattery.url=url
        CompBattery.image=image
        CompBattery.price=price
        CompBattery.name=name
        CompBattery.current_discharge=objDict['current_discharge']['rezValue']
        CompBattery.capasity=objDict['current_discharge']['rezValue']
        CompBattery.shape=objDict['current_discharge']['rezValue']
        return CompBattery
    # if [objDict.keys()]==:
    # if [objDict.keys()]==:
    # if [objDict.keys()]==:
    
def format_text(text):
    return text.lower().replace("\n", " ").strip().replace(',', '.')

def StartPars(url, image, price, name, CompType: str, text: str):
    if CompType=='CompBattery':
        mybattery=battery_dict 
        batteryDict = ParseDict(mybattery, text)
        batteryObject = ClassGenerator(url, image, price, name, batteryDict)
        return batteryObject
    
    

if __name__ == "__main__":
    text="""
    # перейти к навигацииперейти к содержанию aeromotus главная каталог специализированные решения программное обеспечение о нас блог кейсы обучение вебинары лекции контакты позвоните нам поиск: поиск товара официальный дилер   +7 (499) 938-89-09  00 ₽ меню главная обучение софт промышленные решения вебинары оплата и доставка о нас блог вакансии контакты главнаяаксессуары и запчастиаккумуляторы и зарядные устройствааккумулятор dji matrice 300 tb 60 intelligent flight battery (part08) -32%    аккумулятор dji matrice 300 tb 60 intelligent flight battery (part08) аккумулятор dji разряд тока ыфва 10 А matrice 300 tb60 intelligent flight battery (part08) для платформы dji matrice 300 rtk (universal edition). 87 400 ₽ 129 298 ₽  в наличии  категории dji matrice, аккумуляторы и зарядные устройства метки dji enterprise, гео описание   оплата   доставка аккумулятор dji matrice 300 tb60 intelligent flight battery (part08) для платформы dji matrice 300 rtk (universal edition). емкость     привет 546 мач модель tb60 напряжение 52,8 в тип      литий-полимерный 12s время зарядки      при использовании зарядной станции для аккумуляторов intelligent battery bs60: входной ток 220 в: 60 минут (полный заряд двух аккумуляторов tb60), 30 минут (заряд двух аккумуляторов tb60 с 20% до 90%); входной ток 110 в: 70 минут (полный заряд двух аккумуляторов tb60), 40 минут (заряд двух аккумуляторов tb60 с 20% до 90%) вес     около 1,35 кг энергоемкость     274 вт·ч диапазон температур зарядки -20°c…+40°c (функция самонагревания автоматически активируется при температуре зарядки менее +5°c. зарядка при низкой температуре воздуха может сократить срок службы аккумулятора.) рабочая температура       -20°c…+50°c температурный диапазон хранения     +22°c…+30°c категории: dji matrice, аккумуляторы и зарядные устройства метки: dji enterprise, гео aeromotus позвоните нам +7 (499) 938-89-09 адрес: г. москва, варшавское шоссе, дом 42, 6 этаж, офис 6240 главная обучение софт промышленные решения вебинары оплата и доставка о нас блог вакансии контакты недавно просмотренные товары  аккумулятор dji mavic 2 enterprise battery (part 2) 24 400 ₽  аккумулятор dji matrice 200 - tb50-m200 intelligent flight battery (part2)  комплект ecoflow delta 2 + внешняя батарея  принимаем к оплате  доставляем
    #     """
    rez = StartPars('','','','','CompBattery', text)
    print(rez)
    print(dir(rez))
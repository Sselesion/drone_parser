import re

"""

"""

battery_dict = {
                'current_discharge': {
                    'keyw': ['разряд тока','разряд','ток разряда','выходной ток','ток выхода'],
                    'units': ['Ампер','А','Амп','A'],
                    'answerType':['Число'],
                    'rezValue':''
                },
                'capacity': {
                    'keyw': ['емкость','ёмкость','capacity'],
                    'units': ['мач','ач','ah','mah', 'мaч', 'maч', 'mач'],
                    'answerType':['Число'],
                    'rezValue':''
                },
                'form_factor': {
                    'keyw': ['длина','ширина','высота', 'размер','форм фактор','габариты'],
                    'units': ['см','м','дм','cm', 'm', 'dm', 'cм',"мм","mm"],
                    'answerType':['Число'],
                    'rezValue':''
                },
                'voltmeter':{
                    'keyw': ['вольтметр'],
                    'units': ['да','нет'],
                    'answerType':['Текст'],
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
            if objDict[component]['answerType']=="Число":
                for unit in list_unit:
                    index_list = target_area.find(unit)
                    if index_list==[]:
                        continue
                    if index_list==-1:
                        continue

                    nums = re.findall(r'\d*\.\d+|\d+',target_area[:index_list] )
                    nums = [float(i) for i in nums]
                    
                    objDict[component]['rezValue'] = nums
            else:
                for unit in list_unit:
                    if unit!=[]:
                        for unit in list_unit:
                            if target_area.find(unit)!=-1:
                                objDict[component]['rezValue'] = unit

                
    print(objDict)
    return objDict
    
class emptyClass:
    pass

def ClassGenerator(url, image, price, name, objDict):
    if objDict.keys() == battery_dict.keys():
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
Характеристики

Емкость – 4920 мАч;
Напряжение – 7.6 В;
Тип аккумулятора – LiPo;
Размер: 30х30х8мм
Энергия – 37.39 Вт/ч;
Вольтметр: да (коэффициент 110)
Совместимость – CrystalSky, Cendence, CrystalSky и Cendence – хаб для зарядки. """
    rez = StartPars('','','','','CompBattery', text)
    print(rez)
    #print(dir(rez))
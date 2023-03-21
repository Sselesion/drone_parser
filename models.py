from enum import Enum

from pydantic import BaseModel


class Comp(BaseModel):
    url: str
    image: str
    price: str
    name: str


class CompBattery(Comp):
    """Батарея (аккумулятор)"""

    current_discharge: str  # Разряд тока (Ампер);
    capasity: str  # Емкость (мА/ч);
    shape: str  # Форм фактор (длина * ширина * высота);
    voltage: str  # Напряжение (Вольт);


class CompMicrocontroller(Comp):
    """Микроконтроллер"""

    operating_frequency: str  # Рабочая частота (ГГц);
    number_of_channels: str  # Число каналов;
    operating_current: str  # Рабочий ток (мАмпер);
    working_voltage: str  # Рабочее напряжение (Вольт);
    transmission_power: str  # Мощность передачи (дБм);
    channel_resolution: str  # Разрешение канала;
    wireless_protocol: str  # Беспроводной протокол;


class CompElectricMotor(Comp):
    """Электрический мотор (применяемые для БПЛА)"""

    voltage: str  # Напряжение (Вольт);
    maximum_power: str  # Максимальная мощность (Ватт);
    recommended_battery: str  # Рекомендуемая батарея (название модели или ссылка);
    noload_current: str  # Ток холостого хода (Ампер);
    peak_current: str  # Пиковый ток (Ампер);
    stator_length: str  # Длина статора (мм);
    stator_diameter: str  # Диаметр статора (мм);
    shaft_diameter: str  # Диаметр вала (мм);
    number_of_revolutions_per_volt: str  # Число оборотов на 1 вольт;
    resistance: str  # Сопротивление (Ом);


class CompMotorController(Comp):
    """Контроллер мотора"""

    operating_current: str  # Рабочий ток (Ампер);
    peak_current: str  # Пиковый ток (Ампер);
    power_support: str  # Поддержка питания (Да/Нет);


class CompFlightController(Comp):
    """Полетный контролер"""

    presence_of_a_barometer: str  # Наличие барометра;
    presence_of_a_black_box: str  # Наличие черного ящика;
    power: str  # Питание (Вольт);
    firmware: str  # Прошивка (название);
    presence_of_a_usb_connector: str  # Наличие usb разъема;
    fastening: str  # Крепление (посадочное место для крепления. Здесь нужно расстояние между отверстиями т.е. 40мм*50мм);


class CompLidar(Comp):
    """Лидар"""

    max_range: str  # Максимальная дальность использования (метров)
    frequency: str  # Частота импульсов (Герц)
    power_supply: str  # Питание (вольт)


class CompMicroFlightController(Comp):
    """Микроконтроллер (полетный контроллер)"""

    clock_requency: str  # Тактовая частота (МГц)
    flash_memory_capacity: str  # Объем флеш памяти (Кб)
    # посадочное место для крепления (расстояние между отверстиями т.е. 40мм*50мм)
    mounting: list[str]
    min_input_voltage: str  # Минимальное входное напряжение (Вольт)
    max_input_voltage: str  # Максимальное входное напряжение (Вольт)
    uart_ports_number: str  # Число UART портов


class CompRangeFinder(Comp):
    """Дальномер"""

    max_range: str  # Максимальная дальность использования (метров)
    frequency: str  # Частота работы (Гц)
    wave_length: str  # Длина волны (нм)
    power_supply: str  # Питание (вольт)


class CompSatelliteCommModule(Comp):
    """Модуль спутниковой связи"""

    battery_availability: str  # Наличие батареи
    battery_life: str  # Время работы от батареи (часов)
    accuracy: str  # Погрешность (м)


class CompLeashingPlatform(Comp):
    """Привязная платформа"""

    max_speed: str  # Максимальная скорость (км/ч)
    gaining_speed: str  # Скорость набора высоты (км/ч)
    deceleration_speed: str  # Скорость снижения (км/ч)
    flight_range: str  # Максимальная дальность полета (м)
    flight_altitude: str  # Максимальная высота полета (м)
    power_consumption: str  # Энергопотребление (Вт/ч)
    payload_weight: str  # Масса полезной погрузки (г)
    flight_time: str  # Продолжительность полета (мин)
    screws_number: str  # Число винтов


class CompThermalCamera(Comp):
    """Тепловизор"""

    range_detection: str  # Дальность обнаружения (м)
    range_observation: str  # Дистанция наблюдения (м)
    interface: str  # Интерфейс
    voltage: str  # Напряжение (Вольт)
    battery_availability: str  # Наличие батареи (Вт/ч)
    battery_life: str  # Время работы от батареи (ч)
    field_of_view: str  # Поле зрения
    magnification: str  # Увеличение
    protection_class: str  # Класс защиты
    work_temperature: str  # Рабочая температура
    type_of_sensor: str  # Тип матрицы


class CompUAVCopterType(Comp):
    """БПЛА коптерного типа"""

    maximal_speed: str  # Максимальная скорость (км/ч)
    gaining_speed: str  # Скорость набора (км/ч)
    deceleration_speed: str  # Скорость снижения (км/ч)
    maximal_range: str  # Максимальная дальность полета (м)
    maximum_flight_altitude: str  # Максимальная дальность полета (м)
    power_consumption: str  # Энергопотребление (Вт/ч)
    payload_weight: str  # Масса полезной погрузки (г)
    flight_time: str  # Продолжительность полета (мин)
    number_of_screws: str  # Число винтов


class CompVideoTransmitter(Comp):
    """Видео передатчик"""

    frequency: str  # Частота приема (ГГц)
    wattage: str  # Мощность (мВт)
    number_of_channels: str  # Число каналов
    antenna_connector: str  # Разъем антенны


class CompPayload(Comp):
    """Полезная нагрузка (подвес, который прикрепляется к коптеру)"""

    matrix: str  # Матрица
    lens: str  # Объектив
    magnification: str  # Увеличение
    number_of_megapixels: str  # Число мегапикселей
    resolution_TVL: str  # Разрешение, TVL
    companion_image: str  # Сопровождение
    thermal_imager_resolution: str  # Разрешение тепловизора
    field_of_view: str  # Поле зрения
    rangefinder: str  # Дальномер
    axes: str  # Число осей стабилизации
    accuracy: str  # Точность
    tangent: str  # Рабочие углы стабилизации, Тангаж
    roll: str  # Рабочие углы стабилизации, Крен
    yaw: str  # Рабочие углы стабилизации, Рысканье
    wattage: str  # Мощность (мВт)
    voltage: str  # Питание (Вольт)
    current: str  # Ток (мА)
    antenna: str  # Антенна (при наличии указать название)
    frequency: str  # Частота (ГГц)
    number_of_channels: str  # Число каналов


class CompControlPanel(Comp):
    """Пульт управления (control panel)"""

    frequency: str  # Рабочая частота (ГГц)
    number_of_channels: str  # Число каналов
    current: str  # Рабочий ток (мА)
    voltage: str  # Рабочее напряжение (Вольт)
    transmission_power: str  # Мощность передачи (дБм)
    resolution: str  # Разрешение канала
    wireless_protocol: str  # Беспроводной протокол


class CompEnum(Enum):
    """Перечисления компонентов"""

    BATTERY = "Батарея"
    MICROCONTROLLER = "Микроконтроллер"
    ELECTRICMOTOR = "Мотор"
    MOTORCONTROLLER = "Контроллер мотора"
    FLIGHTCONTROLLER = "Полетный контроллер"
    LIDAR = "Лидар"
    MICROFLIGHTCONTROLLER = "Полетный микроконтроллер"
    RANGEFINDER = "Дальномер"
    SATELLITECOMMMODULE = "Модуль спутниковой связи"
    LEASHINGPLATFORM = "Привязная платформа"
    THERMALCAMERA = "Тепловизор"
    UAVCOPTERTYPE = "БПЛА коптерного типа"
    VIDEOTRANSMITTER = "Видеопередатчик"
    PAYLOAD = "Полезная нагрузка (для подвеса)"
    CONTROLPANEL = "Пульт управления"


class SearchParamEnum(Enum):
    """Параметры, необходимые для запуска метода поиска значений в
    тексте (в модуле `pars._get_values`)"""

    def __init__(self, key_words: list[str], units: list[str]) -> None:
        self.key_words = key_words
        self.units = units

    # Battery
    CURRENT_DISCHARGE = (
        ["разряд тока", "разряд", "ток разряда", "выходной ток", "ток выхода"],
        ["ампер", "а", "амп", "a"],
    )
    CAPASITY = (
        ["емкость", "ёмкость", "capacity"],
        ["мач", "ач", "ah", "mah", "мaч", "maч", "mач"],
    )
    SHAPE = (
        ["длина", "ширина", "высота", "размер", "форм фактор", "габариты"],
        ["см", "м", "дм", "cm", "m", "dm", "cм"],
    )
    VOLTAGE = (
        ["напряжение"],
        ["в", "вольт", "v", "volt"],
    )
    
    #Microcontroller
    OPERATING_FREQUENCY = (
        ['частота'],
        ['гц', 'ггц', 'мгц'],
    )
    NUMBER_OF_CHANNELS = (
        ['каналов', "потоков"],
        [],
    )
    OPERATING_CURRENTА = (
        [],
        [],
    )
    WORKING_VOLTAGE = (
        ["напряжение"],
        ["в", "вольт", "v", "volt"],
    )
    TRANSMISSION_POWER = (
        ["мощность"],
        ["дбм"],
    )
    CHANNEL_RESOLUTION = (
        ["канал", "канала"],
        [""],
    )
    WIRELESS_PROTOCOL = (
        [],
        [],
    )

    # ElectricMotor
    MAXIMUM_POWER = (
        ["мощность"],
        ["ватт", "вт"],
    )
    RECOMMENDED_BATTERY = (
        [],
        [],
    )
    NOLOAD_CURRENT = (
        [],
        [],
    )
    PEAK_CURRENT = (
        [],
        [],
    )
    STATOR_LENGTH = (
        [],
        [],
    )
    STATOR_DIAMETER = (
        [],
        [],
    )
    SHAFT_DIAMETER = (
        [],
        [],
    )
    NUMBER_OF_REVOLUTIONS_PER_VOLT = (
        [],
        [],
    )
    RESISTANCE = (
        ["сопротивление"],
        ["ом"],
    )

    # MotorController
    OPERATING_CURRENT = (
        ["ток"],
        ["ампер", "а", "амп", "a"],
    )
    POWER_SUPPORT = (
        [],
        [],
    )

    # FlightController
    PRESENCE_OF_A_BAROMETER = (
        [],
        [],
    )
    PRESENCE_OF_A_BLACK_BOX = (
        [],
        [],
    )
    POWER = (
        ['питание', 'ток'],
        ["в", "вольт", "v", "volt"],
    )
    FIRMWARE = (
        [],
        [],
    )
    PRESENCE_OF_A_USB_CONNECTOR = (
        [],
        [],
    )
    FASTENING = (
        [],
        [],
    )

    # Lidar
    MAX_RANGE = (
        ['дальность', 'расстояние'],
        ['м', 'км', 'метров', 'километров'],
    )
    FREQUENCY = (
        ['частота'],
        ['гц', 'ггц', 'мгц'],
    )
    POWER_SUPPLY = (
        ['питание', 'ток'],
        ["в", "вольт", "v", "volt"],
    )

    # MicroFlightController

    CLOCK_FREQUENCY = (
        ['частота', 'тактовая'],
        ['гц', 'ггц', 'мгц'],
    )
    FLASH_MEMORY_CAPACITY = (
        ['память', 'памяти'],
        ['кб', 'мб', 'кбайт', 'мбайт', 'байт'],
    )
    MOUNTING = (
        ["крепление"],
        ["мм", "см"],
    )
    MIN_INPUT_VOLTAGE = (
        ["минимальное", "входное"],
        ["в", "вольт", "v", "volt"]
    )
    MAX_INPUT_VOLTAGE = (
        ["максимальное", "входное"],
        ["в", "вольт", "v", "volt"]
    )
    UART_PORTS_NUMBER = (
        ["uart"],
        [],
    )

    # Rangefinder

    WAVE_LENGTH = (
        ["волны", "волна"],
        ["нм"],
    )

    # Satellitecommmodule
    BATTERY_LIFE = (
        ["время", "работы"],
        ["мин", "минут", "часов"],
    )
    ACCURACY = (
        ["погрешность", "точность"],
        [],
    )

    # Leashingplatform
    MAX_SPEED = (
        [],
        [],
    )
    FLIGHT_RANGE = (
        [],
        [],
    )
    FLIGHT_ALTITUDE = (
        [],
        [],
    )
    PAYLOAD_WEIGHT = (
        [],
        [],
    )
    FLIGHT_TIME = (
        [],
        [],
    )
    SCREWS_NUMBER = (
        [],
        [],
    )

    # TermalCamera
    RANGE_DETECTION = (
        ["дальность", "обнаружения", "видимости", "сканирования", "видимость"],
        ["м", "км", "см", "к/м", "m", "km", "cm", "k/m", ]
    )
    RANGE_OBSERVATION = (
        ["дистанция наблюдения", "дистанция"],
        ["м", "км", "см", "к/м", "m", "km", "cm", "k/m", ]
    )
    INTERFACE = (
        ["интерфейс"],
        ["удобный", "улучшенный", "пользовательский"]
    )
    BATTERY_AVAILABILITY = (
        ["батарея", "аккумулятор", "аккумуляторная"],
        ["вт/ч", "w/h"]
    )
    FIELD_OF_VIEW = (
        ["поле", "зрения"],
        ["градусов", "гр.", "°"]
    )
    MAGNIFICATION = (
        ["увеличение", "зум", "zoom"],
        ["x", "X"]
    )
    PROTECTION_CLASS = (
        ["защиты", "защита", "класс", "влаги"],
        ["x", "1", "2", "3", "4", "5", "6", "7", "8", "9",]
    )
    WORK_TEMPERATURE = (
        ["рабочая", "температура", "класс", "влаги"],
        ["градусов", "гр.", "°"]

    )
    TYPE_OF_SENSOR = (
        ["тип", "сенсор", "sensor"],
        []
    )

    #UAVCopterType
    MAXIMAL_SPEED = (
        ["максимальная скорость", "макс. скорость", "скорость"],
        ["км/ч"]
    )
    GAINING_SPEED = (
        ["скорость набора"],
        ["км/ч"]
    )
    DECELERATION_SPEED = (
        ["скорость cнижения"],
        ["км/ч"]
    )
    MAXIMAL_RANGE = (
        ["дальность полета", "дальность"],
        ["м", "км", "см", "к/м", "m", "km", "cm", "k/m", ]
    )
    MAXIMUM_FLIGHT_ALTITUDE = (
        ["высота полета", "высота"],
        ["м", "км", "см", "к/м", "m", "km", "cm", "k/m", ]
    )
    POWER_CONSUMPTION = (
        ["энергопотребление", "потребление"],
        ["вт/ч", "w/h"]
    )
    NUMBER_OF_SCREWS = (
        ["число винтов", "винты", "винтов"],
        [""]
    )

    #VideoTransmitter
    WATTAGE = (
        ["мощность"],
        ["мвт", "вт"]
    )

    ANTENNA_CONNECTOR = (
        ["разъем антены", "антена"],
        []
    )

    #Payload
    MATRIX = (
        ["матрица"],
        []
    )
    LENS = (
        ["объектив"],
        []
    )
    NUMBER_OF_MEGAPIXELS = (
        ["число мегапикселей", "мегапикселей"],
        []
    )
    RESOLUTION_TVL = (
        ["разрешение"],
        []
    )
    COMPANION_IMAGE = (
        ["сопровождение"],
        []
    )
    THERMAL_IMAGER_RESOLUTION = (
        ["разрешение", "разрешение тепловизора"],
        []
    )
    RANGEFINDER = (
        ["дальномер"],
        []
    )
    AXES = (
        ["оси стабилизации", "оси", "число осей"],
        []
    )
    
    TANGENT = (
        ["углы стабилизации", "тангаж", "угол стабилизации"],
        []
    )
    ROLL = (
        ["углы стабилизации", "крен"],
        []
    )
    YAW = (
        ["углы стабилизации", "рысканье"],
        []
    )
    CURRENT = (
        ["ток"],
        ["ма", "а"]
    )
    ANTENNA = (
        ["антенна"],
        []
    )
    
    #ControlPanel
    
    RESOLUTION = (
        ["разрешение", "разрешение канала"],
        []
    )
    



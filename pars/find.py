import re
from enum import Enum
import models

class CompFieldType(Enum):
    unit = 1
    range = 2
    boolean = 3


battery_dict = {
    'current_discharge': {
        'keyw': ['разряд тока', 'разряд', 'ток разряда', 'выходной ток', 'ток выхода'],
        'units': ['Ампер', 'А', 'Амп', 'A'],
        'rezValue': '',
        'CompFieldType': CompFieldType.unit
    },
    'capacity': {
        'keyw': ['емкость', 'ёмкость', 'capacity'],
        'units': ['мач', 'ач', 'ah', 'mah', 'мaч', 'maч', 'mач'],
        'rezValue': '',
        'CompFieldType': CompFieldType.unit
    },
    'form_factor': {
        'keyw': ['длина', 'ширина', 'высота', 'размер', 'форм фактор', 'габариты'],
        'units': ['см', 'м', 'дм', 'cm', 'm', 'dm', 'cм'],
        'rezValue': '',
        'CompFieldType': CompFieldType.range
    },
    'voltage': {
        'keyw': ['напряжение', 'voltage'],
        'units': ['в', 'вольт', 'volt', 'v'],
        'rezValue': '',
        'CompFieldType': CompFieldType.unit
    }
}


def ParseUnit(text: str, keywords: list, units: list, localization: int) -> object:
    for kw in keywords:
        idx = text.find(kw)
        if idx == -1:
            continue

        idx_end = idx + localization
        if idx_end > len(text):
            idx_end = len(text)

        target_area = text[idx:idx_end]

        for unit in units:
            index = target_area.find(' ' + unit + ' ')
            if index == -1:
                continue

            nums = re.findall(r'\d*\.\d+|\d+', target_area[:index])
            nums = [float(i) for i in nums]

            return nums[0]


def ClassGenerator(url, image, price, name, objDict):
    if [objDict.keys()] == [battery_dict.keys()]:
        comp_battery = models.CompBattery
        comp_battery.url = url
        comp_battery.image = image
        comp_battery.price = price
        comp_battery.name = name
        comp_battery.current_discharge = objDict['current_discharge']['rezValue']
        comp_battery.capasity = objDict['capacity']['rezValue']
        comp_battery.shape = objDict['form_factor']['rezValue']
        comp_battery.voltage = objDict['voltage']['rezValue']
        return comp_battery
    # if [objDict.keys()]==:
    # if [objDict.keys()]==:
    # if [objDict.keys()]==:


def format_text(text):
    return text.lower().replace("\n", " ").strip().replace(',', '.').replace('<', ' ').replace('>', ' ')


def ParseDict(obj_dict, text, localization=100):
    text = format_text(text)
    all_fields = obj_dict.keys()
    for field in all_fields:
        list_keyw = [format_text(i) for i in obj_dict[field]['keyw']]
        list_unit = [format_text(i) for i in obj_dict[field]['units']]

        if obj_dict[field]['CompFieldType'] == CompFieldType.unit:
            obj_dict[field]['rezValue'] = ParseUnit(text, list_keyw, list_unit, localization)

        if obj_dict[field][''] == CompFieldType.range:
            pass

        if obj_dict[field][''] == CompFieldType.boolean:
            pass

    print(obj_dict)
    return obj_dict


def StartPars(url, image, price, name, comp_type: str, text: str):
    if comp_type == 'CompBattery':
        battery_dict_filled = ParseDict(battery_dict, text)
        battery_object = ClassGenerator(url, image, price, name, battery_dict_filled)
        return battery_object


if __name__ == "__main__":
    txt = """
    
<!DOCTYPE html>
<html lang="ru-RU">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="profile" href="https://gmpg.org/xfn/11">
<link rel="pingback" href="https://aeromotus.ru/xmlrpc.php">
<meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />

<title>Купить Аккумулятор DJI MATRICE 300 TB 60 Intelligent Flight Battery (Part08) - AEROMOTUS</title>
<meta name="description" content="Аккумулятор DJI MATRICE 300 TB 60 Intelligent Flight Battery (Part08) Аккумулятор DJI MATRICE 300 TB60 Intelligent Flight Battery (Part08) для платформы DJI MATRICE 300 RTK (Universal Edition). - AEROMOTUS" />
<link rel="canonical" href="https://aeromotus.ru/product/akkumulyator-dji-matrice-300-tb60-intelligent-flight-battery-part08/" />
<meta property="og:locale" content="ru_RU" />
<meta property="og:type" content="article" />
<meta property="og:title" content="Купить Аккумулятор DJI MATRICE 300 TB 60 Intelligent Flight Battery (Part08) - AEROMOTUS" />
<meta property="og:description" content="Аккумулятор DJI MATRICE 300 TB 60 Intelligent Flight Battery (Part08) Аккумулятор DJI MATRICE 300 TB60 Intelligent Flight Battery (Part08) для платформы DJI MATRICE 300 RTK (Universal Edition). - AEROMOTUS" />
<meta property="og:url" content="https://aeromotus.ru/product/akkumulyator-dji-matrice-300-tb60-intelligent-flight-battery-part08/" />
<meta property="og:site_name" content="AEROMOTUS" />
<meta property="article:publisher" content="https://www.facebook.com/aeromotus.ru/" />
<meta property="article:modified_time" content="2023-02-02T05:20:02+00:00" />
<meta property="og:image" content="http://aeromotus.ru/wp-content/uploads/2020/08/4e2ce5c0ff135c9db66c9655a1fb8dfa.png" />
<meta property="og:image:width" content="600" />
<meta property="og:image:height" content="600" />
<meta property="og:image:type" content="image/png" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:label1" content="Примерное время для чтения" />
<meta name="twitter:data1" content="1 минута" />
<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https://schema.org","@graph":[{"@type":["WebPage","ItemPage"],"@id":"https://aeromotus.ru/product/akkumulyator-dji-matrice-300-tb60-intelligent-flight-battery-part08/","url":"https://aeromotus.ru/product/akkumulyator-dji-matrice-300-tb60-intelligent-flight-battery-part08/","name":"Купить Аккумулятор DJI MATRICE 300 TB 60 Intelligent Flight Battery (Part08) - AEROMOTUS","isPartOf":{"@id":"https://aeromotus.ru/#website"},"primaryImageOfPage":{"@id":"https://aeromotus.ru/product/akkumulyator-dji-matrice-300-tb60-intelligent-flight-battery-part08/#primaryimage"},"image":{"@id":"https://aeromotus.ru/product/akkumulyator-dji-matrice-300-tb60-intelligent-flight-battery-part08/#primaryimage"},"thumbnailUrl":"https://aeromotus.ru/wp-content/uploads/2020/08/4e2ce5c0ff135c9db66c9655a1fb8dfa.png","datePublished":"2020-08-05T18:29:24+00:00","dateModified":"2023-02-02T05:20:02+00:00","description":"Аккумулятор DJI MATRICE 300 TB 60 Intelligent Flight Battery (Part08) Аккумулятор DJI MATRICE 300 TB60 Intelligent Flight Battery (Part08) для платформы DJI MATRICE 300 RTK (Universal Edition). - AEROMOTUS","breadcrumb":{"@id":"https://aeromotus.ru/product/akkumulyator-dji-matrice-300-tb60-intelligent-flight-battery-part08/#breadcrumb"},"inLanguage":"ru-RU","potentialAction":[{"@type":"ReadAction","target":["https://aeromotus.ru/product/akkumulyator-dji-matrice-300-tb60-intelligent-flight-battery-part08/"]}]},{"@type":"ImageObject","inLanguage":"ru-RU","@id":"https://aeromotus.ru/product/akkumulyator-dji-matrice-300-tb60-intelligent-flight-battery-part08/#primaryimage","url":"https://aeromotus.ru/wp-content/uploads/2020/08/4e2ce5c0ff135c9db66c9655a1fb8dfa.png","contentUrl":"https://aeromotus.ru/wp-content/uploads/2020/08/4e2ce5c0ff135c9db66c9655a1fb8dfa.png","width":600,"height":600},{"@type":"BreadcrumbList","@id":"https://aeromotus.ru/product/akkumulyator-dji-matrice-300-tb60-intelligent-flight-battery-part08/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная страница","item":"https://aeromotus.ru/"},{"@type":"ListItem","position":2,"name":"Интернет-магазин квадрокоптеров","item":"https://aeromotus.ru/shop/"},{"@type":"ListItem","position":3,"name":"Аккумулятор DJI MATRICE 300 TB 60 Intelligent Flight Battery (Part08)"}]},{"@type":"WebSite","@id":"https://aeromotus.ru/#website","url":"https://aeromotus.ru/","name":"AEROMOTUS","description":"Магазин профессиональных квадрокоптеров в Москве. Официальный дилер DJI","publisher":{"@id":"https://aeromotus.ru/#organization"},"potentialAction":[{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https://aeromotus.ru/?s={search_term_string}"},"query-input":"required name=search_term_string"}],"inLanguage":"ru-RU"},{"@type":"Organization","@id":"https://aeromotus.ru/#organization","name":"Aeromotus","url":"https://aeromotus.ru/","logo":{"@type":"ImageObject","inLanguage":"ru-RU","@id":"https://aeromotus.ru/#/schema/logo/image/","url":"https://aeromotus.ru/wp-content/uploads/2019/08/original-logos-2016-Dec-1313-584951f41a963-1-300x257.png","contentUrl":"https://aeromotus.ru/wp-content/uploads/2019/08/original-logos-2016-Dec-1313-584951f41a963-1-300x257.png","width":300,"height":257,"caption":"Aeromotus"},"image":{"@id":"https://aeromotus.ru/#/schema/logo/image/"},"sameAs":["https://www.facebook.com/aeromotus.ru/","https://www.instagram.com/aeromotus_ru/","https://www.linkedin.com/company/11315482/admin/","https://www.youtube.com/channel/UCAyu9W59PeY_8qIUeNVXwrg"]}]}</script>

<link rel='dns-prefetch' href='//fonts.googleapis.com' />
<link rel="alternate" type="application/rss+xml" title="AEROMOTUS &raquo; Лента" href="https://aeromotus.ru/feed/" />
<link rel="alternate" type="application/rss+xml" title="AEROMOTUS &raquo; Лента комментариев" href="https://aeromotus.ru/comments/feed/" />
<script type="text/javascript">
window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/14.0.0\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/14.0.0\/svg\/","svgExt":".svg","source":{"concatemoji":"https:\/\/aeromotus.ru\/wp-includes\/js\/wp-emoji-release.min.js?ver=3b71e7425f116479de92df27dcaef655"}};
/*! This file is auto-generated */
!function(e,a,t){var n,r,o,i=a.createElement("canvas"),p=i.getContext&&i.getContext("2d");function s(e,t){var a=String.fromCharCode,e=(p.clearRect(0,0,i.width,i.height),p.fillText(a.apply(this,e),0,0),i.toDataURL());return p.clearRect(0,0,i.width,i.height),p.fillText(a.apply(this,t),0,0),e===i.toDataURL()}function c(e){var t=a.createElement("script");t.src=e,t.defer=t.type="text/javascript",a.getElementsByTagName("head")[0].appendChild(t)}for(o=Array("flag","emoji"),t.supports={everything:!0,everythingExceptFlag:!0},r=0;r<o.length;r++)t.supports[o[r]]=function(e){if(p&&p.fillText)switch(p.textBaseline="top",p.font="600 32px Arial",e){case"flag":return s([127987,65039,8205,9895,65039],[127987,65039,8203,9895,65039])?!1:!s([55356,56826,55356,56819],[55356,56826,8203,55356,56819])&&!s([55356,57332,56128,56423,56128,56418,56128,56421,56128,56430,56128,56423,56128,56447],[55356,57332,8203,56128,56423,8203,56128,56418,8203,56128,56421,8203,56128,56430,8203,56128,56423,8203,56128,56447]);case"emoji":return!s([129777,127995,8205,129778,127999],[129777,127995,8203,129778,127999])}return!1}(o[r]),t.supports.everything=t.supports.everything&&t.supports[o[r]],"flag"!==o[r]&&(t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&t.supports[o[r]]);t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&!t.supports.flag,t.DOMReady=!1,t.readyCallback=function(){t.DOMReady=!0},t.supports.everything||(n=function(){t.readyCallback()},a.addEventListener?(a.addEventListener("DOMContentLoaded",n,!1),e.addEventListener("load",n,!1)):(e.attachEvent("onload",n),a.attachEvent("onreadystatechange",function(){"complete"===a.readyState&&t.readyCallback()})),(e=t.source||{}).concatemoji?c(e.concatemoji):e.wpemoji&&e.twemoji&&(c(e.twemoji),c(e.wpemoji)))}(window,document,window._wpemojiSettings);
</script>
<style type="text/css">
img.wp-smiley,
img.emoji {
	display: inline !important;
	border: none !important;
	box-shadow: none !important;
	height: 1em !important;
	width: 1em !important;
	margin: 0 0.07em !important;
	vertical-align: -0.1em !important;
	background: none !important;
	padding: 0 !important;
}
</style>
<link rel='stylesheet' id='wp-block-library-css' href='https://aeromotus.ru/wp-includes/css/dist/block-library/style.min.css?ver=3b71e7425f116479de92df27dcaef655' type='text/css' media='all' />
<link rel='stylesheet' id='ugb-style-css-v2-css' href='https://aeromotus.ru/wp-content/plugins/stackable-ultimate-gutenberg-blocks/dist/deprecated/frontend_blocks_deprecated_v2.css?ver=3.1.4' type='text/css' media='all' />
<style id='ugb-style-css-v2-inline-css' type='text/css'>
:root {--stk-block-width-default-detected: 1170px;}
:root {
			--content-width: 1170px;
		}
</style>
<link rel='stylesheet' id='wc-blocks-vendors-style-css' href='https://aeromotus.ru/wp-content/plugins/woocommerce/packages/woocommerce-blocks/build/wc-blocks-vendors-style.css?ver=9.6.5' type='text/css' media='all' />
<link rel='stylesheet' id='wc-blocks-style-css' href='https://aeromotus.ru/wp-content/plugins/woocommerce/packages/woocommerce-blocks/build/wc-blocks-style.css?ver=9.6.5' type='text/css' media='all' />
<link rel='stylesheet' id='classic-theme-styles-css' href='https://aeromotus.ru/wp-includes/css/classic-themes.min.css?ver=1' type='text/css' media='all' />
<style id='global-styles-inline-css' type='text/css'>
body{--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgba(6,147,227,1) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgba(252,185,0,1) 0%,rgba(255,105,0,1) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgba(255,105,0,1) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--duotone--dark-grayscale: url('#wp-duotone-dark-grayscale');--wp--preset--duotone--grayscale: url('#wp-duotone-grayscale');--wp--preset--duotone--purple-yellow: url('#wp-duotone-purple-yellow');--wp--preset--duotone--blue-red: url('#wp-duotone-blue-red');--wp--preset--duotone--midnight: url('#wp-duotone-midnight');--wp--preset--duotone--magenta-yellow: url('#wp-duotone-magenta-yellow');--wp--preset--duotone--purple-green: url('#wp-duotone-purple-green');--wp--preset--duotone--blue-orange: url('#wp-duotone-blue-orange');--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;--wp--preset--spacing--20: 0.44rem;--wp--preset--spacing--30: 0.67rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.5rem;--wp--preset--spacing--60: 2.25rem;--wp--preset--spacing--70: 3.38rem;--wp--preset--spacing--80: 5.06rem;}:where(.is-layout-flex){gap: 0.5em;}body .is-layout-flow > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}body .is-layout-flow > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}body .is-layout-flow > .aligncenter{margin-left: auto !important;margin-right: auto !important;}body .is-layout-constrained > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}body .is-layout-constrained > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}body .is-layout-constrained > .aligncenter{margin-left: auto !important;margin-right: auto !important;}body .is-layout-constrained > :where(:not(.alignleft):not(.alignright):not(.alignfull)){max-width: var(--wp--style--global--content-size);margin-left: auto !important;margin-right: auto !important;}body .is-layout-constrained > .alignwide{max-width: var(--wp--style--global--wide-size);}body .is-layout-flex{display: flex;}body .is-layout-flex{flex-wrap: wrap;align-items: center;}body .is-layout-flex > *{margin: 0;}:where(.wp-block-columns.is-layout-flex){gap: 2em;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
.wp-block-navigation a:where(:not(.wp-element-button)){color: inherit;}
:where(.wp-block-columns.is-layout-flex){gap: 2em;}
.wp-block-pullquote{font-size: 1.5em;line-height: 1.6;}
</style>
<style id='extendify-gutenberg-patterns-and-templates-utilities-inline-css' type='text/css'>
.ext-absolute {
  position: absolute !important;
}

.ext-relative {
  position: relative !important;
}

.ext-top-base {
  top: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-top-lg {
  top: var(--extendify--spacing--large, 3rem) !important;
}

.ext--top-base {
  top: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
}

.ext--top-lg {
  top: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
}

.ext-right-base {
  right: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-right-lg {
  right: var(--extendify--spacing--large, 3rem) !important;
}

.ext--right-base {
  right: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
}

.ext--right-lg {
  right: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
}

.ext-bottom-base {
  bottom: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-bottom-lg {
  bottom: var(--extendify--spacing--large, 3rem) !important;
}

.ext--bottom-base {
  bottom: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
}

.ext--bottom-lg {
  bottom: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
}

.ext-left-base {
  left: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-left-lg {
  left: var(--extendify--spacing--large, 3rem) !important;
}

.ext--left-base {
  left: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
}

.ext--left-lg {
  left: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
}

.ext-order-1 {
  order: 1 !important;
}

.ext-order-2 {
  order: 2 !important;
}

.ext-col-auto {
  grid-column: auto !important;
}

.ext-col-span-1 {
  grid-column: span 1 / span 1 !important;
}

.ext-col-span-2 {
  grid-column: span 2 / span 2 !important;
}

.ext-col-span-3 {
  grid-column: span 3 / span 3 !important;
}

.ext-col-span-4 {
  grid-column: span 4 / span 4 !important;
}

.ext-col-span-5 {
  grid-column: span 5 / span 5 !important;
}

.ext-col-span-6 {
  grid-column: span 6 / span 6 !important;
}

.ext-col-span-7 {
  grid-column: span 7 / span 7 !important;
}

.ext-col-span-8 {
  grid-column: span 8 / span 8 !important;
}

.ext-col-span-9 {
  grid-column: span 9 / span 9 !important;
}

.ext-col-span-10 {
  grid-column: span 10 / span 10 !important;
}

.ext-col-span-11 {
  grid-column: span 11 / span 11 !important;
}

.ext-col-span-12 {
  grid-column: span 12 / span 12 !important;
}

.ext-col-span-full {
  grid-column: 1 / -1 !important;
}

.ext-col-start-1 {
  grid-column-start: 1 !important;
}

.ext-col-start-2 {
  grid-column-start: 2 !important;
}

.ext-col-start-3 {
  grid-column-start: 3 !important;
}

.ext-col-start-4 {
  grid-column-start: 4 !important;
}

.ext-col-start-5 {
  grid-column-start: 5 !important;
}

.ext-col-start-6 {
  grid-column-start: 6 !important;
}

.ext-col-start-7 {
  grid-column-start: 7 !important;
}

.ext-col-start-8 {
  grid-column-start: 8 !important;
}

.ext-col-start-9 {
  grid-column-start: 9 !important;
}

.ext-col-start-10 {
  grid-column-start: 10 !important;
}

.ext-col-start-11 {
  grid-column-start: 11 !important;
}

.ext-col-start-12 {
  grid-column-start: 12 !important;
}

.ext-col-start-13 {
  grid-column-start: 13 !important;
}

.ext-col-start-auto {
  grid-column-start: auto !important;
}

.ext-col-end-1 {
  grid-column-end: 1 !important;
}

.ext-col-end-2 {
  grid-column-end: 2 !important;
}

.ext-col-end-3 {
  grid-column-end: 3 !important;
}

.ext-col-end-4 {
  grid-column-end: 4 !important;
}

.ext-col-end-5 {
  grid-column-end: 5 !important;
}

.ext-col-end-6 {
  grid-column-end: 6 !important;
}

.ext-col-end-7 {
  grid-column-end: 7 !important;
}

.ext-col-end-8 {
  grid-column-end: 8 !important;
}

.ext-col-end-9 {
  grid-column-end: 9 !important;
}

.ext-col-end-10 {
  grid-column-end: 10 !important;
}

.ext-col-end-11 {
  grid-column-end: 11 !important;
}

.ext-col-end-12 {
  grid-column-end: 12 !important;
}

.ext-col-end-13 {
  grid-column-end: 13 !important;
}

.ext-col-end-auto {
  grid-column-end: auto !important;
}

.ext-row-auto {
  grid-row: auto !important;
}

.ext-row-span-1 {
  grid-row: span 1 / span 1 !important;
}

.ext-row-span-2 {
  grid-row: span 2 / span 2 !important;
}

.ext-row-span-3 {
  grid-row: span 3 / span 3 !important;
}

.ext-row-span-4 {
  grid-row: span 4 / span 4 !important;
}

.ext-row-span-5 {
  grid-row: span 5 / span 5 !important;
}

.ext-row-span-6 {
  grid-row: span 6 / span 6 !important;
}

.ext-row-span-full {
  grid-row: 1 / -1 !important;
}

.ext-row-start-1 {
  grid-row-start: 1 !important;
}

.ext-row-start-2 {
  grid-row-start: 2 !important;
}

.ext-row-start-3 {
  grid-row-start: 3 !important;
}

.ext-row-start-4 {
  grid-row-start: 4 !important;
}

.ext-row-start-5 {
  grid-row-start: 5 !important;
}

.ext-row-start-6 {
  grid-row-start: 6 !important;
}

.ext-row-start-7 {
  grid-row-start: 7 !important;
}

.ext-row-start-auto {
  grid-row-start: auto !important;
}

.ext-row-end-1 {
  grid-row-end: 1 !important;
}

.ext-row-end-2 {
  grid-row-end: 2 !important;
}

.ext-row-end-3 {
  grid-row-end: 3 !important;
}

.ext-row-end-4 {
  grid-row-end: 4 !important;
}

.ext-row-end-5 {
  grid-row-end: 5 !important;
}

.ext-row-end-6 {
  grid-row-end: 6 !important;
}

.ext-row-end-7 {
  grid-row-end: 7 !important;
}

.ext-row-end-auto {
  grid-row-end: auto !important;
}

.ext-m-0:not([style*="margin"]) {
  margin: 0 !important;
}

.ext-m-auto:not([style*="margin"]) {
  margin: auto !important;
}

.ext-m-base:not([style*="margin"]) {
  margin: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-m-lg:not([style*="margin"]) {
  margin: var(--extendify--spacing--large, 3rem) !important;
}

.ext--m-base:not([style*="margin"]) {
  margin: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
}

.ext--m-lg:not([style*="margin"]) {
  margin: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
}

.ext-mx-0:not([style*="margin"]) {
  margin-left: 0 !important;
  margin-right: 0 !important;
}

.ext-mx-auto:not([style*="margin"]) {
  margin-left: auto !important;
  margin-right: auto !important;
}

.ext-mx-base:not([style*="margin"]) {
  margin-left: var(--wp--style--block-gap, 1.75rem) !important;
  margin-right: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-mx-lg:not([style*="margin"]) {
  margin-left: var(--extendify--spacing--large, 3rem) !important;
  margin-right: var(--extendify--spacing--large, 3rem) !important;
}

.ext--mx-base:not([style*="margin"]) {
  margin-left: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  margin-right: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
}

.ext--mx-lg:not([style*="margin"]) {
  margin-left: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  margin-right: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
}

.ext-my-0:not([style*="margin"]) {
  margin-top: 0 !important;
  margin-bottom: 0 !important;
}

.ext-my-auto:not([style*="margin"]) {
  margin-top: auto !important;
  margin-bottom: auto !important;
}

.ext-my-base:not([style*="margin"]) {
  margin-top: var(--wp--style--block-gap, 1.75rem) !important;
  margin-bottom: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-my-lg:not([style*="margin"]) {
  margin-top: var(--extendify--spacing--large, 3rem) !important;
  margin-bottom: var(--extendify--spacing--large, 3rem) !important;
}

.ext--my-base:not([style*="margin"]) {
  margin-top: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  margin-bottom: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
}

.ext--my-lg:not([style*="margin"]) {
  margin-top: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  margin-bottom: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
}

.ext-mt-0:not([style*="margin"]) {
  margin-top: 0 !important;
}

.ext-mt-auto:not([style*="margin"]) {
  margin-top: auto !important;
}

.ext-mt-base:not([style*="margin"]) {
  margin-top: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-mt-lg:not([style*="margin"]) {
  margin-top: var(--extendify--spacing--large, 3rem) !important;
}

.ext--mt-base:not([style*="margin"]) {
  margin-top: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
}

.ext--mt-lg:not([style*="margin"]) {
  margin-top: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
}

.ext-mr-0:not([style*="margin"]) {
  margin-right: 0 !important;
}

.ext-mr-auto:not([style*="margin"]) {
  margin-right: auto !important;
}

.ext-mr-base:not([style*="margin"]) {
  margin-right: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-mr-lg:not([style*="margin"]) {
  margin-right: var(--extendify--spacing--large, 3rem) !important;
}

.ext--mr-base:not([style*="margin"]) {
  margin-right: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
}

.ext--mr-lg:not([style*="margin"]) {
  margin-right: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
}

.ext-mb-0:not([style*="margin"]) {
  margin-bottom: 0 !important;
}

.ext-mb-auto:not([style*="margin"]) {
  margin-bottom: auto !important;
}

.ext-mb-base:not([style*="margin"]) {
  margin-bottom: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-mb-lg:not([style*="margin"]) {
  margin-bottom: var(--extendify--spacing--large, 3rem) !important;
}

.ext--mb-base:not([style*="margin"]) {
  margin-bottom: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
}

.ext--mb-lg:not([style*="margin"]) {
  margin-bottom: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
}

.ext-ml-0:not([style*="margin"]) {
  margin-left: 0 !important;
}

.ext-ml-auto:not([style*="margin"]) {
  margin-left: auto !important;
}

.ext-ml-base:not([style*="margin"]) {
  margin-left: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-ml-lg:not([style*="margin"]) {
  margin-left: var(--extendify--spacing--large, 3rem) !important;
}

.ext--ml-base:not([style*="margin"]) {
  margin-left: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
}

.ext--ml-lg:not([style*="margin"]) {
  margin-left: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
}

.ext-block {
  display: block !important;
}

.ext-inline-block {
  display: inline-block !important;
}

.ext-inline {
  display: inline !important;
}

.ext-flex {
  display: flex !important;
}

.ext-inline-flex {
  display: inline-flex !important;
}

.ext-grid {
  display: grid !important;
}

.ext-inline-grid {
  display: inline-grid !important;
}

.ext-hidden {
  display: none !important;
}

.ext-w-auto {
  width: auto !important;
}

.ext-w-full {
  width: 100% !important;
}

.ext-max-w-full {
  max-width: 100% !important;
}

.ext-flex-1 {
  flex: 1 1 0% !important;
}

.ext-flex-auto {
  flex: 1 1 auto !important;
}

.ext-flex-initial {
  flex: 0 1 auto !important;
}

.ext-flex-none {
  flex: none !important;
}

.ext-flex-shrink-0 {
  flex-shrink: 0 !important;
}

.ext-flex-shrink {
  flex-shrink: 1 !important;
}

.ext-flex-grow-0 {
  flex-grow: 0 !important;
}

.ext-flex-grow {
  flex-grow: 1 !important;
}

.ext-list-none {
  list-style-type: none !important;
}

.ext-grid-cols-1 {
  grid-template-columns: repeat(1, minmax(0, 1fr)) !important;
}

.ext-grid-cols-2 {
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
}

.ext-grid-cols-3 {
  grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
}

.ext-grid-cols-4 {
  grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
}

.ext-grid-cols-5 {
  grid-template-columns: repeat(5, minmax(0, 1fr)) !important;
}

.ext-grid-cols-6 {
  grid-template-columns: repeat(6, minmax(0, 1fr)) !important;
}

.ext-grid-cols-7 {
  grid-template-columns: repeat(7, minmax(0, 1fr)) !important;
}

.ext-grid-cols-8 {
  grid-template-columns: repeat(8, minmax(0, 1fr)) !important;
}

.ext-grid-cols-9 {
  grid-template-columns: repeat(9, minmax(0, 1fr)) !important;
}

.ext-grid-cols-10 {
  grid-template-columns: repeat(10, minmax(0, 1fr)) !important;
}

.ext-grid-cols-11 {
  grid-template-columns: repeat(11, minmax(0, 1fr)) !important;
}

.ext-grid-cols-12 {
  grid-template-columns: repeat(12, minmax(0, 1fr)) !important;
}

.ext-grid-cols-none {
  grid-template-columns: none !important;
}

.ext-grid-rows-1 {
  grid-template-rows: repeat(1, minmax(0, 1fr)) !important;
}

.ext-grid-rows-2 {
  grid-template-rows: repeat(2, minmax(0, 1fr)) !important;
}

.ext-grid-rows-3 {
  grid-template-rows: repeat(3, minmax(0, 1fr)) !important;
}

.ext-grid-rows-4 {
  grid-template-rows: repeat(4, minmax(0, 1fr)) !important;
}

.ext-grid-rows-5 {
  grid-template-rows: repeat(5, minmax(0, 1fr)) !important;
}

.ext-grid-rows-6 {
  grid-template-rows: repeat(6, minmax(0, 1fr)) !important;
}

.ext-grid-rows-none {
  grid-template-rows: none !important;
}

.ext-flex-row {
  flex-direction: row !important;
}

.ext-flex-row-reverse {
  flex-direction: row-reverse !important;
}

.ext-flex-col {
  flex-direction: column !important;
}

.ext-flex-col-reverse {
  flex-direction: column-reverse !important;
}

.ext-flex-wrap {
  flex-wrap: wrap !important;
}

.ext-flex-wrap-reverse {
  flex-wrap: wrap-reverse !important;
}

.ext-flex-nowrap {
  flex-wrap: nowrap !important;
}

.ext-items-start {
  align-items: flex-start !important;
}

.ext-items-end {
  align-items: flex-end !important;
}

.ext-items-center {
  align-items: center !important;
}

.ext-items-baseline {
  align-items: baseline !important;
}

.ext-items-stretch {
  align-items: stretch !important;
}

.ext-justify-start {
  justify-content: flex-start !important;
}

.ext-justify-end {
  justify-content: flex-end !important;
}

.ext-justify-center {
  justify-content: center !important;
}

.ext-justify-between {
  justify-content: space-between !important;
}

.ext-justify-around {
  justify-content: space-around !important;
}

.ext-justify-evenly {
  justify-content: space-evenly !important;
}

.ext-justify-items-start {
  justify-items: start !important;
}

.ext-justify-items-end {
  justify-items: end !important;
}

.ext-justify-items-center {
  justify-items: center !important;
}

.ext-justify-items-stretch {
  justify-items: stretch !important;
}

.ext-gap-0 {
  gap: 0 !important;
}

.ext-gap-base {
  gap: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-gap-lg {
  gap: var(--extendify--spacing--large, 3rem) !important;
}

.ext-gap-x-0 {
  -moz-column-gap: 0 !important;
       column-gap: 0 !important;
}

.ext-gap-x-base {
  -moz-column-gap: var(--wp--style--block-gap, 1.75rem) !important;
       column-gap: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-gap-x-lg {
  -moz-column-gap: var(--extendify--spacing--large, 3rem) !important;
       column-gap: var(--extendify--spacing--large, 3rem) !important;
}

.ext-gap-y-0 {
  row-gap: 0 !important;
}

.ext-gap-y-base {
  row-gap: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-gap-y-lg {
  row-gap: var(--extendify--spacing--large, 3rem) !important;
}

.ext-justify-self-auto {
  justify-self: auto !important;
}

.ext-justify-self-start {
  justify-self: start !important;
}

.ext-justify-self-end {
  justify-self: end !important;
}

.ext-justify-self-center {
  justify-self: center !important;
}

.ext-justify-self-stretch {
  justify-self: stretch !important;
}

.ext-rounded-none {
  border-radius: 0px !important;
}

.ext-rounded-full {
  border-radius: 9999px !important;
}

.ext-rounded-t-none {
  border-top-left-radius: 0px !important;
  border-top-right-radius: 0px !important;
}

.ext-rounded-t-full {
  border-top-left-radius: 9999px !important;
  border-top-right-radius: 9999px !important;
}

.ext-rounded-r-none {
  border-top-right-radius: 0px !important;
  border-bottom-right-radius: 0px !important;
}

.ext-rounded-r-full {
  border-top-right-radius: 9999px !important;
  border-bottom-right-radius: 9999px !important;
}

.ext-rounded-b-none {
  border-bottom-right-radius: 0px !important;
  border-bottom-left-radius: 0px !important;
}

.ext-rounded-b-full {
  border-bottom-right-radius: 9999px !important;
  border-bottom-left-radius: 9999px !important;
}

.ext-rounded-l-none {
  border-top-left-radius: 0px !important;
  border-bottom-left-radius: 0px !important;
}

.ext-rounded-l-full {
  border-top-left-radius: 9999px !important;
  border-bottom-left-radius: 9999px !important;
}

.ext-rounded-tl-none {
  border-top-left-radius: 0px !important;
}

.ext-rounded-tl-full {
  border-top-left-radius: 9999px !important;
}

.ext-rounded-tr-none {
  border-top-right-radius: 0px !important;
}

.ext-rounded-tr-full {
  border-top-right-radius: 9999px !important;
}

.ext-rounded-br-none {
  border-bottom-right-radius: 0px !important;
}

.ext-rounded-br-full {
  border-bottom-right-radius: 9999px !important;
}

.ext-rounded-bl-none {
  border-bottom-left-radius: 0px !important;
}

.ext-rounded-bl-full {
  border-bottom-left-radius: 9999px !important;
}

.ext-border-0 {
  border-width: 0px !important;
}

.ext-border-t-0 {
  border-top-width: 0px !important;
}

.ext-border-r-0 {
  border-right-width: 0px !important;
}

.ext-border-b-0 {
  border-bottom-width: 0px !important;
}

.ext-border-l-0 {
  border-left-width: 0px !important;
}

.ext-p-0:not([style*="padding"]) {
  padding: 0 !important;
}

.ext-p-base:not([style*="padding"]) {
  padding: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-p-lg:not([style*="padding"]) {
  padding: var(--extendify--spacing--large, 3rem) !important;
}

.ext-px-0:not([style*="padding"]) {
  padding-left: 0 !important;
  padding-right: 0 !important;
}

.ext-px-base:not([style*="padding"]) {
  padding-left: var(--wp--style--block-gap, 1.75rem) !important;
  padding-right: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-px-lg:not([style*="padding"]) {
  padding-left: var(--extendify--spacing--large, 3rem) !important;
  padding-right: var(--extendify--spacing--large, 3rem) !important;
}

.ext-py-0:not([style*="padding"]) {
  padding-top: 0 !important;
  padding-bottom: 0 !important;
}

.ext-py-base:not([style*="padding"]) {
  padding-top: var(--wp--style--block-gap, 1.75rem) !important;
  padding-bottom: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-py-lg:not([style*="padding"]) {
  padding-top: var(--extendify--spacing--large, 3rem) !important;
  padding-bottom: var(--extendify--spacing--large, 3rem) !important;
}

.ext-pt-0:not([style*="padding"]) {
  padding-top: 0 !important;
}

.ext-pt-base:not([style*="padding"]) {
  padding-top: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-pt-lg:not([style*="padding"]) {
  padding-top: var(--extendify--spacing--large, 3rem) !important;
}

.ext-pr-0:not([style*="padding"]) {
  padding-right: 0 !important;
}

.ext-pr-base:not([style*="padding"]) {
  padding-right: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-pr-lg:not([style*="padding"]) {
  padding-right: var(--extendify--spacing--large, 3rem) !important;
}

.ext-pb-0:not([style*="padding"]) {
  padding-bottom: 0 !important;
}

.ext-pb-base:not([style*="padding"]) {
  padding-bottom: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-pb-lg:not([style*="padding"]) {
  padding-bottom: var(--extendify--spacing--large, 3rem) !important;
}

.ext-pl-0:not([style*="padding"]) {
  padding-left: 0 !important;
}

.ext-pl-base:not([style*="padding"]) {
  padding-left: var(--wp--style--block-gap, 1.75rem) !important;
}

.ext-pl-lg:not([style*="padding"]) {
  padding-left: var(--extendify--spacing--large, 3rem) !important;
}

.ext-text-left {
  text-align: left !important;
}

.ext-text-center {
  text-align: center !important;
}

.ext-text-right {
  text-align: right !important;
}

.ext-leading-none {
  line-height: 1 !important;
}

.ext-leading-tight {
  line-height: 1.25 !important;
}

.ext-leading-snug {
  line-height: 1.375 !important;
}

.ext-leading-normal {
  line-height: 1.5 !important;
}

.ext-leading-relaxed {
  line-height: 1.625 !important;
}

.ext-leading-loose {
  line-height: 2 !important;
}

.ext-aspect-square img {
  aspect-ratio: 1 / 1 !important;
  -o-object-fit: cover !important;
     object-fit: cover !important;
}

.ext-aspect-landscape img {
  aspect-ratio: 4 / 3 !important;
  -o-object-fit: cover !important;
     object-fit: cover !important;
}

.ext-aspect-landscape-wide img {
  aspect-ratio: 16 / 9 !important;
  -o-object-fit: cover !important;
     object-fit: cover !important;
}

.ext-aspect-portrait img {
  aspect-ratio: 3 / 4 !important;
  -o-object-fit: cover !important;
     object-fit: cover !important;
}

.ext-aspect-square .components-resizable-box__container,
.ext-aspect-landscape .components-resizable-box__container,
.ext-aspect-landscape-wide .components-resizable-box__container,
.ext-aspect-portrait .components-resizable-box__container {
  height: auto !important;
}

.clip-path--rhombus img {
  -webkit-clip-path: polygon(15% 6%, 80% 29%, 84% 93%, 23% 69%) !important;
          clip-path: polygon(15% 6%, 80% 29%, 84% 93%, 23% 69%) !important;
}

.clip-path--diamond img {
  -webkit-clip-path: polygon(5% 29%, 60% 2%, 91% 64%, 36% 89%) !important;
          clip-path: polygon(5% 29%, 60% 2%, 91% 64%, 36% 89%) !important;
}

.clip-path--rhombus-alt img {
  -webkit-clip-path: polygon(14% 9%, 85% 24%, 91% 89%, 19% 76%) !important;
          clip-path: polygon(14% 9%, 85% 24%, 91% 89%, 19% 76%) !important;
}

/*
The .ext utility is a top-level class that we use to target contents within our patterns.
We use it here to ensure columns blocks display well across themes.
*/

.wp-block-columns[class*="fullwidth-cols"] {
  /* no suggestion */
  margin-bottom: unset !important;
}

.wp-block-column.editor\:pointer-events-none {
  /* no suggestion */
  margin-top: 0 !important;
  margin-bottom: 0 !important;
}

.is-root-container.block-editor-block-list__layout
    > [data-align="full"]:not(:first-of-type)
    > .wp-block-column.editor\:pointer-events-none,
.is-root-container.block-editor-block-list__layout
    > [data-align="wide"]
    > .wp-block-column.editor\:pointer-events-none {
  /* no suggestion */
  margin-top: calc(-1 * var(--wp--style--block-gap, 28px)) !important;
}

.is-root-container.block-editor-block-list__layout
    > [data-align="full"]:not(:first-of-type)
    > .ext-my-0,
.is-root-container.block-editor-block-list__layout
    > [data-align="wide"]
    > .ext-my-0:not([style*="margin"]) {
  /* no suggestion */
  margin-top: calc(-1 * var(--wp--style--block-gap, 28px)) !important;
}

/* Some popular themes use padding instead of core margin for columns; remove it */

.ext .wp-block-columns .wp-block-column[style*="padding"] {
  /* no suggestion */
  padding-left: 0 !important;
  padding-right: 0 !important;
}

/* Some popular themes add double spacing between columns; remove it */

.ext
    .wp-block-columns
    + .wp-block-columns:not([class*="mt-"]):not([class*="my-"]):not([style*="margin"]) {
  /* no suggestion */
  margin-top: 0 !important;
}

[class*="fullwidth-cols"] .wp-block-column:first-child,
[class*="fullwidth-cols"] .wp-block-group:first-child {
  /* no suggestion */
}

[class*="fullwidth-cols"] .wp-block-column:first-child, [class*="fullwidth-cols"] .wp-block-group:first-child {
  margin-top: 0 !important;
}

[class*="fullwidth-cols"] .wp-block-column:last-child,
[class*="fullwidth-cols"] .wp-block-group:last-child {
  /* no suggestion */
}

[class*="fullwidth-cols"] .wp-block-column:last-child, [class*="fullwidth-cols"] .wp-block-group:last-child {
  margin-bottom: 0 !important;
}

[class*="fullwidth-cols"] .wp-block-column:first-child > * {
  /* no suggestion */
  margin-top: 0 !important;
}

[class*="fullwidth-cols"] .wp-block-column > *:first-child {
  /* no suggestion */
  margin-top: 0 !important;
}

[class*="fullwidth-cols"] .wp-block-column > *:last-child {
  /* no suggestion */
  margin-bottom: 0 !important;
}

.ext .is-not-stacked-on-mobile .wp-block-column {
  /* no suggestion */
  margin-bottom: 0 !important;
}

/* Add base margin bottom to all columns */

.wp-block-columns[class*="fullwidth-cols"]:not(.is-not-stacked-on-mobile)
    > .wp-block-column:not(:last-child) {
  /* no suggestion */
  margin-bottom: var(--wp--style--block-gap, 1.75rem) !important;
}

@media (min-width: 782px) {
  .wp-block-columns[class*="fullwidth-cols"]:not(.is-not-stacked-on-mobile)
        > .wp-block-column:not(:last-child) {
    /* no suggestion */
    margin-bottom: 0 !important;
  }
}

/* Remove margin bottom from "not-stacked" columns */

.wp-block-columns[class*="fullwidth-cols"].is-not-stacked-on-mobile
    > .wp-block-column {
  /* no suggestion */
  margin-bottom: 0 !important;
}

@media (min-width: 600px) and (max-width: 781px) {
  .wp-block-columns[class*="fullwidth-cols"]:not(.is-not-stacked-on-mobile)
        > .wp-block-column:nth-child(even) {
    /* no suggestion */
    margin-left: var(--wp--style--block-gap, 2em) !important;
  }
}

/*
    The `tablet:fullwidth-cols` and `desktop:fullwidth-cols` utilities are used
    to counter the core/columns responsive for at our breakpoints.
*/

@media (max-width: 781px) {
  .tablet\:fullwidth-cols.wp-block-columns:not(.is-not-stacked-on-mobile) {
    flex-wrap: wrap !important;
  }

  .tablet\:fullwidth-cols.wp-block-columns:not(.is-not-stacked-on-mobile)
        > .wp-block-column {
    margin-left: 0 !important;
  }

  .tablet\:fullwidth-cols.wp-block-columns:not(.is-not-stacked-on-mobile)
        > .wp-block-column:not([style*="margin"]) {
    /* no suggestion */
    margin-left: 0 !important;
  }

  .tablet\:fullwidth-cols.wp-block-columns:not(.is-not-stacked-on-mobile)
        > .wp-block-column {
    flex-basis: 100% !important; /* Required to negate core/columns flex-basis */
  }
}

@media (max-width: 1079px) {
  .desktop\:fullwidth-cols.wp-block-columns:not(.is-not-stacked-on-mobile) {
    flex-wrap: wrap !important;
  }

  .desktop\:fullwidth-cols.wp-block-columns:not(.is-not-stacked-on-mobile)
        > .wp-block-column {
    margin-left: 0 !important;
  }

  .desktop\:fullwidth-cols.wp-block-columns:not(.is-not-stacked-on-mobile)
        > .wp-block-column:not([style*="margin"]) {
    /* no suggestion */
    margin-left: 0 !important;
  }

  .desktop\:fullwidth-cols.wp-block-columns:not(.is-not-stacked-on-mobile)
        > .wp-block-column {
    flex-basis: 100% !important; /* Required to negate core/columns flex-basis */
  }

  .desktop\:fullwidth-cols.wp-block-columns:not(.is-not-stacked-on-mobile)
        > .wp-block-column:not(:last-child) {
    margin-bottom: var(--wp--style--block-gap, 1.75rem) !important;
  }
}

.direction-rtl {
  direction: rtl !important;
}

.direction-ltr {
  direction: ltr !important;
}

/* Use "is-style-" prefix to support adding this style to the core/list block */

.is-style-inline-list {
  padding-left: 0 !important;
}

.is-style-inline-list li {
  /* no suggestion */
  list-style-type: none !important;
}

@media (min-width: 782px) {
  .is-style-inline-list li {
    margin-right: var(--wp--style--block-gap, 1.75rem) !important;
    display: inline !important;
  }
}

.is-style-inline-list li:first-child {
  /* no suggestion */
}

@media (min-width: 782px) {
  .is-style-inline-list li:first-child {
    margin-left: 0 !important;
  }
}

.is-style-inline-list li:last-child {
  /* no suggestion */
}

@media (min-width: 782px) {
  .is-style-inline-list li:last-child {
    margin-right: 0 !important;
  }
}

.bring-to-front {
  position: relative !important;
  z-index: 10 !important;
}

.text-stroke {
  -webkit-text-stroke-width: var(
        --wp--custom--typography--text-stroke-width,
        2px
    ) !important;
  -webkit-text-stroke-color: var(--wp--preset--color--background) !important;
}

.text-stroke--primary {
  -webkit-text-stroke-width: var(
        --wp--custom--typography--text-stroke-width,
        2px
    ) !important;
  -webkit-text-stroke-color: var(--wp--preset--color--primary) !important;
}

.text-stroke--secondary {
  -webkit-text-stroke-width: var(
        --wp--custom--typography--text-stroke-width,
        2px
    ) !important;
  -webkit-text-stroke-color: var(--wp--preset--color--secondary) !important;
}

.editor\:no-caption .block-editor-rich-text__editable {
  display: none !important;
}

.editor\:no-inserter > .block-list-appender,
.editor\:no-inserter .wp-block-group__inner-container > .block-list-appender {
  display: none !important;
}

.editor\:no-inserter .wp-block-cover__inner-container > .block-list-appender {
  display: none !important;
}

.editor\:no-inserter .wp-block-column:not(.is-selected) > .block-list-appender {
  display: none !important;
}

.editor\:no-resize .components-resizable-box__handle::after,
.editor\:no-resize .components-resizable-box__side-handle::before,
.editor\:no-resize .components-resizable-box__handle {
  display: none !important;
  pointer-events: none !important;
}

.editor\:no-resize .components-resizable-box__container {
  display: block !important;
}

.editor\:pointer-events-none {
  pointer-events: none !important;
}

.is-style-angled {
  /* no suggestion */
  align-items: center !important;
  justify-content: flex-end !important;
}

.ext .is-style-angled > [class*="_inner-container"] {
  align-items: center !important;
}

.is-style-angled .wp-block-cover__image-background,
.is-style-angled .wp-block-cover__video-background {
  /* no suggestion */
  -webkit-clip-path: polygon(0 0, 30% 0%, 50% 100%, 0% 100%) !important;
          clip-path: polygon(0 0, 30% 0%, 50% 100%, 0% 100%) !important;
  z-index: 1 !important;
}

@media (min-width: 782px) {
  .is-style-angled .wp-block-cover__image-background,
    .is-style-angled .wp-block-cover__video-background {
    /* no suggestion */
    -webkit-clip-path: polygon(0 0, 55% 0%, 65% 100%, 0% 100%) !important;
            clip-path: polygon(0 0, 55% 0%, 65% 100%, 0% 100%) !important;
  }
}

.has-foreground-color {
  /* no suggestion */
  color: var(--wp--preset--color--foreground, #000) !important;
}

.has-foreground-background-color {
  /* no suggestion */
  background-color: var(--wp--preset--color--foreground, #000) !important;
}

.has-background-color {
  /* no suggestion */
  color: var(--wp--preset--color--background, #fff) !important;
}

.has-background-background-color {
  /* no suggestion */
  background-color: var(--wp--preset--color--background, #fff) !important;
}

.has-primary-color {
  /* no suggestion */
  color: var(--wp--preset--color--primary, #4b5563) !important;
}

.has-primary-background-color {
  /* no suggestion */
  background-color: var(--wp--preset--color--primary, #4b5563) !important;
}

.has-secondary-color {
  /* no suggestion */
  color: var(--wp--preset--color--secondary, #9ca3af) !important;
}

.has-secondary-background-color {
  /* no suggestion */
  background-color: var(--wp--preset--color--secondary, #9ca3af) !important;
}

/* Ensure themes that target specific elements use the right colors */

.ext.has-text-color p,
.ext.has-text-color h1,
.ext.has-text-color h2,
.ext.has-text-color h3,
.ext.has-text-color h4,
.ext.has-text-color h5,
.ext.has-text-color h6 {
  /* no suggestion */
  color: currentColor !important;
}

.has-white-color {
  /* no suggestion */
  color: var(--wp--preset--color--white, #fff) !important;
}

.has-black-color {
  /* no suggestion */
  color: var(--wp--preset--color--black, #000) !important;
}

.has-ext-foreground-background-color {
  /* no suggestion */
  background-color: var(
        --wp--preset--color--foreground,
        var(--wp--preset--color--black, #000)
    ) !important;
}

.has-ext-primary-background-color {
  /* no suggestion */
  background-color: var(
        --wp--preset--color--primary,
        var(--wp--preset--color--cyan-bluish-gray, #000)
    ) !important;
}

/* Fix button borders with specified background colors */

.wp-block-button__link.has-black-background-color {
  /* no suggestion */
  border-color: var(--wp--preset--color--black, #000) !important;
}

.wp-block-button__link.has-white-background-color {
  /* no suggestion */
  border-color: var(--wp--preset--color--white, #fff) !important;
}

.has-ext-small-font-size {
  /* no suggestion */
  font-size: var(--wp--preset--font-size--ext-small) !important;
}

.has-ext-medium-font-size {
  /* no suggestion */
  font-size: var(--wp--preset--font-size--ext-medium) !important;
}

.has-ext-large-font-size {
  /* no suggestion */
  font-size: var(--wp--preset--font-size--ext-large) !important;
  line-height: 1.2 !important;
}

.has-ext-x-large-font-size {
  /* no suggestion */
  font-size: var(--wp--preset--font-size--ext-x-large) !important;
  line-height: 1 !important;
}

.has-ext-xx-large-font-size {
  /* no suggestion */
  font-size: var(--wp--preset--font-size--ext-xx-large) !important;
  line-height: 1 !important;
}

/* Line height */

.has-ext-x-large-font-size:not([style*="line-height"]) {
  /* no suggestion */
  line-height: 1.1 !important;
}

.has-ext-xx-large-font-size:not([style*="line-height"]) {
  /* no suggestion */
  line-height: 1.1 !important;
}

.ext .wp-block-group > * {
  /* Line height */
  margin-top: 0 !important;
  margin-bottom: 0 !important;
}

.ext .wp-block-group > * + * {
  margin-top: var(--wp--style--block-gap, 1.75rem) !important;
  margin-bottom: 0 !important;
}

.ext h2 {
  margin-top: var(--wp--style--block-gap, 1.75rem) !important;
  margin-bottom: var(--wp--style--block-gap, 1.75rem) !important;
}

.has-ext-x-large-font-size + p,
.has-ext-x-large-font-size + h3 {
  margin-top: 0.5rem !important;
}

.ext .wp-block-buttons > .wp-block-button.wp-block-button__width-25 {
  width: calc(25% - var(--wp--style--block-gap, 0.5em) * 0.75) !important;
  min-width: 12rem !important;
}

/* Classic themes use an inner [class*="_inner-container"] that our utilities cannot directly target, so we need to do so with a few */

.ext .ext-grid > [class*="_inner-container"] {
  /* no suggestion */
  display: grid !important;
}

/* Unhinge grid for container blocks in classic themes, and < 5.9 */

.ext > [class*="_inner-container"] > .ext-grid:not([class*="columns"]),
.ext
    > [class*="_inner-container"]
    > .wp-block
    > .ext-grid:not([class*="columns"]) {
  /* no suggestion */
  display: initial !important;
}

/* Grid Columns */

.ext .ext-grid-cols-1 > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-columns: repeat(1, minmax(0, 1fr)) !important;
}

.ext .ext-grid-cols-2 > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
}

.ext .ext-grid-cols-3 > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
}

.ext .ext-grid-cols-4 > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
}

.ext .ext-grid-cols-5 > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-columns: repeat(5, minmax(0, 1fr)) !important;
}

.ext .ext-grid-cols-6 > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-columns: repeat(6, minmax(0, 1fr)) !important;
}

.ext .ext-grid-cols-7 > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-columns: repeat(7, minmax(0, 1fr)) !important;
}

.ext .ext-grid-cols-8 > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-columns: repeat(8, minmax(0, 1fr)) !important;
}

.ext .ext-grid-cols-9 > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-columns: repeat(9, minmax(0, 1fr)) !important;
}

.ext .ext-grid-cols-10 > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-columns: repeat(10, minmax(0, 1fr)) !important;
}

.ext .ext-grid-cols-11 > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-columns: repeat(11, minmax(0, 1fr)) !important;
}

.ext .ext-grid-cols-12 > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-columns: repeat(12, minmax(0, 1fr)) !important;
}

.ext .ext-grid-cols-13 > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-columns: repeat(13, minmax(0, 1fr)) !important;
}

.ext .ext-grid-cols-none > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-columns: none !important;
}

/* Grid Rows */

.ext .ext-grid-rows-1 > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-rows: repeat(1, minmax(0, 1fr)) !important;
}

.ext .ext-grid-rows-2 > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-rows: repeat(2, minmax(0, 1fr)) !important;
}

.ext .ext-grid-rows-3 > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-rows: repeat(3, minmax(0, 1fr)) !important;
}

.ext .ext-grid-rows-4 > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-rows: repeat(4, minmax(0, 1fr)) !important;
}

.ext .ext-grid-rows-5 > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-rows: repeat(5, minmax(0, 1fr)) !important;
}

.ext .ext-grid-rows-6 > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-rows: repeat(6, minmax(0, 1fr)) !important;
}

.ext .ext-grid-rows-none > [class*="_inner-container"] {
  /* no suggestion */
  grid-template-rows: none !important;
}

/* Align */

.ext .ext-items-start > [class*="_inner-container"] {
  align-items: flex-start !important;
}

.ext .ext-items-end > [class*="_inner-container"] {
  align-items: flex-end !important;
}

.ext .ext-items-center > [class*="_inner-container"] {
  align-items: center !important;
}

.ext .ext-items-baseline > [class*="_inner-container"] {
  align-items: baseline !important;
}

.ext .ext-items-stretch > [class*="_inner-container"] {
  align-items: stretch !important;
}

.ext.wp-block-group > *:last-child {
  /* no suggestion */
  margin-bottom: 0 !important;
}

/* For <5.9 */

.ext .wp-block-group__inner-container {
  /* no suggestion */
  padding: 0 !important;
}

.ext.has-background {
  /* no suggestion */
  padding-left: var(--wp--style--block-gap, 1.75rem) !important;
  padding-right: var(--wp--style--block-gap, 1.75rem) !important;
}

/* Fallback for classic theme group blocks */

.ext *[class*="inner-container"] > .alignwide *[class*="inner-container"],
.ext
    *[class*="inner-container"]
    > [data-align="wide"]
    *[class*="inner-container"] {
  /* no suggestion */
  max-width: var(--responsive--alignwide-width, 120rem) !important;
}

.ext *[class*="inner-container"] > .alignwide *[class*="inner-container"] > *,
.ext
    *[class*="inner-container"]
    > [data-align="wide"]
    *[class*="inner-container"]
    > * {
  /* no suggestion */
}

.ext *[class*="inner-container"] > .alignwide *[class*="inner-container"] > *, .ext
    *[class*="inner-container"]
    > [data-align="wide"]
    *[class*="inner-container"]
    > * {
  max-width: 100% !important;
}

/* Ensure image block display is standardized */

.ext .wp-block-image {
  /* no suggestion */
  position: relative !important;
  text-align: center !important;
}

.ext .wp-block-image img {
  /* no suggestion */
  display: inline-block !important;
  vertical-align: middle !important;
}

body {
  /* no suggestion */
  /* We need to abstract this out of tailwind.config because clamp doesnt translate with negative margins */
  --extendify--spacing--large: var(
        --wp--custom--spacing--large,
        clamp(2em, 8vw, 8em)
    ) !important;
  /* Add pattern preset font sizes */
  --wp--preset--font-size--ext-small: 1rem !important;
  --wp--preset--font-size--ext-medium: 1.125rem !important;
  --wp--preset--font-size--ext-large: clamp(1.65rem, 3.5vw, 2.15rem) !important;
  --wp--preset--font-size--ext-x-large: clamp(3rem, 6vw, 4.75rem) !important;
  --wp--preset--font-size--ext-xx-large: clamp(3.25rem, 7.5vw, 5.75rem) !important;
  /* Fallbacks for pre 5.9 themes */
  --wp--preset--color--black: #000 !important;
  --wp--preset--color--white: #fff !important;
}

.ext * {
  box-sizing: border-box !important;
}

/* Astra: Remove spacer block visuals in the library */

.block-editor-block-preview__content-iframe
    .ext
    [data-type="core/spacer"]
    .components-resizable-box__container {
  /* no suggestion */
  background: transparent !important;
}

.block-editor-block-preview__content-iframe
    .ext
    [data-type="core/spacer"]
    .block-library-spacer__resize-container::before {
  /* no suggestion */
  display: none !important;
}

/* Twenty Twenty adds a lot of margin automatically to blocks. We only want our own margin added to our patterns. */

.ext .wp-block-group__inner-container figure.wp-block-gallery.alignfull {
  /* no suggestion */
  margin-top: unset !important;
  margin-bottom: unset !important;
}

/* Ensure no funky business is assigned to alignwide */

.ext .alignwide {
  /* no suggestion */
  margin-left: auto !important;
  margin-right: auto !important;
}

/* Negate blockGap being inappropriately assigned in the editor */

.is-root-container.block-editor-block-list__layout
    > [data-align="full"]:not(:first-of-type)
    > .ext-my-0,
.is-root-container.block-editor-block-list__layout
    > [data-align="wide"]
    > .ext-my-0:not([style*="margin"]) {
  /* no suggestion */
  margin-top: calc(-1 * var(--wp--style--block-gap, 28px)) !important;
}

/* Ensure vh content in previews looks taller */

.block-editor-block-preview__content-iframe .preview\:min-h-50 {
  /* no suggestion */
  min-height: 50vw !important;
}

.block-editor-block-preview__content-iframe .preview\:min-h-60 {
  /* no suggestion */
  min-height: 60vw !important;
}

.block-editor-block-preview__content-iframe .preview\:min-h-70 {
  /* no suggestion */
  min-height: 70vw !important;
}

.block-editor-block-preview__content-iframe .preview\:min-h-80 {
  /* no suggestion */
  min-height: 80vw !important;
}

.block-editor-block-preview__content-iframe .preview\:min-h-100 {
  /* no suggestion */
  min-height: 100vw !important;
}

/*  Removes excess margin when applied to the alignfull parent div in Block Themes */

.ext-mr-0.alignfull:not([style*="margin"]):not([style*="margin"]) {
  /* no suggestion */
  margin-right: 0 !important;
}

.ext-ml-0:not([style*="margin"]):not([style*="margin"]) {
  /* no suggestion */
  margin-left: 0 !important;
}

/*  Ensures fullwidth blocks display properly in the editor when margin is zeroed out */

.is-root-container
    .wp-block[data-align="full"]
    > .ext-mx-0:not([style*="margin"]):not([style*="margin"]) {
  /* no suggestion */
  margin-right: calc(1 * var(--wp--custom--spacing--outer, 0)) !important;
  margin-left: calc(1 * var(--wp--custom--spacing--outer, 0)) !important;
  overflow: hidden !important;
  width: unset !important;
}

@media (min-width: 782px) {
  .tablet\:ext-absolute {
    position: absolute !important;
  }

  .tablet\:ext-relative {
    position: relative !important;
  }

  .tablet\:ext-top-base {
    top: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .tablet\:ext-top-lg {
    top: var(--extendify--spacing--large, 3rem) !important;
  }

  .tablet\:ext--top-base {
    top: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .tablet\:ext--top-lg {
    top: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .tablet\:ext-right-base {
    right: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .tablet\:ext-right-lg {
    right: var(--extendify--spacing--large, 3rem) !important;
  }

  .tablet\:ext--right-base {
    right: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .tablet\:ext--right-lg {
    right: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .tablet\:ext-bottom-base {
    bottom: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .tablet\:ext-bottom-lg {
    bottom: var(--extendify--spacing--large, 3rem) !important;
  }

  .tablet\:ext--bottom-base {
    bottom: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .tablet\:ext--bottom-lg {
    bottom: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .tablet\:ext-left-base {
    left: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .tablet\:ext-left-lg {
    left: var(--extendify--spacing--large, 3rem) !important;
  }

  .tablet\:ext--left-base {
    left: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .tablet\:ext--left-lg {
    left: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .tablet\:ext-order-1 {
    order: 1 !important;
  }

  .tablet\:ext-order-2 {
    order: 2 !important;
  }

  .tablet\:ext-m-0:not([style*="margin"]) {
    margin: 0 !important;
  }

  .tablet\:ext-m-auto:not([style*="margin"]) {
    margin: auto !important;
  }

  .tablet\:ext-m-base:not([style*="margin"]) {
    margin: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .tablet\:ext-m-lg:not([style*="margin"]) {
    margin: var(--extendify--spacing--large, 3rem) !important;
  }

  .tablet\:ext--m-base:not([style*="margin"]) {
    margin: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .tablet\:ext--m-lg:not([style*="margin"]) {
    margin: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .tablet\:ext-mx-0:not([style*="margin"]) {
    margin-left: 0 !important;
    margin-right: 0 !important;
  }

  .tablet\:ext-mx-auto:not([style*="margin"]) {
    margin-left: auto !important;
    margin-right: auto !important;
  }

  .tablet\:ext-mx-base:not([style*="margin"]) {
    margin-left: var(--wp--style--block-gap, 1.75rem) !important;
    margin-right: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .tablet\:ext-mx-lg:not([style*="margin"]) {
    margin-left: var(--extendify--spacing--large, 3rem) !important;
    margin-right: var(--extendify--spacing--large, 3rem) !important;
  }

  .tablet\:ext--mx-base:not([style*="margin"]) {
    margin-left: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
    margin-right: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .tablet\:ext--mx-lg:not([style*="margin"]) {
    margin-left: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
    margin-right: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .tablet\:ext-my-0:not([style*="margin"]) {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
  }

  .tablet\:ext-my-auto:not([style*="margin"]) {
    margin-top: auto !important;
    margin-bottom: auto !important;
  }

  .tablet\:ext-my-base:not([style*="margin"]) {
    margin-top: var(--wp--style--block-gap, 1.75rem) !important;
    margin-bottom: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .tablet\:ext-my-lg:not([style*="margin"]) {
    margin-top: var(--extendify--spacing--large, 3rem) !important;
    margin-bottom: var(--extendify--spacing--large, 3rem) !important;
  }

  .tablet\:ext--my-base:not([style*="margin"]) {
    margin-top: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
    margin-bottom: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .tablet\:ext--my-lg:not([style*="margin"]) {
    margin-top: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
    margin-bottom: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .tablet\:ext-mt-0:not([style*="margin"]) {
    margin-top: 0 !important;
  }

  .tablet\:ext-mt-auto:not([style*="margin"]) {
    margin-top: auto !important;
  }

  .tablet\:ext-mt-base:not([style*="margin"]) {
    margin-top: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .tablet\:ext-mt-lg:not([style*="margin"]) {
    margin-top: var(--extendify--spacing--large, 3rem) !important;
  }

  .tablet\:ext--mt-base:not([style*="margin"]) {
    margin-top: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .tablet\:ext--mt-lg:not([style*="margin"]) {
    margin-top: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .tablet\:ext-mr-0:not([style*="margin"]) {
    margin-right: 0 !important;
  }

  .tablet\:ext-mr-auto:not([style*="margin"]) {
    margin-right: auto !important;
  }

  .tablet\:ext-mr-base:not([style*="margin"]) {
    margin-right: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .tablet\:ext-mr-lg:not([style*="margin"]) {
    margin-right: var(--extendify--spacing--large, 3rem) !important;
  }

  .tablet\:ext--mr-base:not([style*="margin"]) {
    margin-right: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .tablet\:ext--mr-lg:not([style*="margin"]) {
    margin-right: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .tablet\:ext-mb-0:not([style*="margin"]) {
    margin-bottom: 0 !important;
  }

  .tablet\:ext-mb-auto:not([style*="margin"]) {
    margin-bottom: auto !important;
  }

  .tablet\:ext-mb-base:not([style*="margin"]) {
    margin-bottom: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .tablet\:ext-mb-lg:not([style*="margin"]) {
    margin-bottom: var(--extendify--spacing--large, 3rem) !important;
  }

  .tablet\:ext--mb-base:not([style*="margin"]) {
    margin-bottom: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .tablet\:ext--mb-lg:not([style*="margin"]) {
    margin-bottom: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .tablet\:ext-ml-0:not([style*="margin"]) {
    margin-left: 0 !important;
  }

  .tablet\:ext-ml-auto:not([style*="margin"]) {
    margin-left: auto !important;
  }

  .tablet\:ext-ml-base:not([style*="margin"]) {
    margin-left: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .tablet\:ext-ml-lg:not([style*="margin"]) {
    margin-left: var(--extendify--spacing--large, 3rem) !important;
  }

  .tablet\:ext--ml-base:not([style*="margin"]) {
    margin-left: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .tablet\:ext--ml-lg:not([style*="margin"]) {
    margin-left: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .tablet\:ext-block {
    display: block !important;
  }

  .tablet\:ext-inline-block {
    display: inline-block !important;
  }

  .tablet\:ext-inline {
    display: inline !important;
  }

  .tablet\:ext-flex {
    display: flex !important;
  }

  .tablet\:ext-inline-flex {
    display: inline-flex !important;
  }

  .tablet\:ext-grid {
    display: grid !important;
  }

  .tablet\:ext-inline-grid {
    display: inline-grid !important;
  }

  .tablet\:ext-hidden {
    display: none !important;
  }

  .tablet\:ext-w-auto {
    width: auto !important;
  }

  .tablet\:ext-w-full {
    width: 100% !important;
  }

  .tablet\:ext-max-w-full {
    max-width: 100% !important;
  }

  .tablet\:ext-flex-1 {
    flex: 1 1 0% !important;
  }

  .tablet\:ext-flex-auto {
    flex: 1 1 auto !important;
  }

  .tablet\:ext-flex-initial {
    flex: 0 1 auto !important;
  }

  .tablet\:ext-flex-none {
    flex: none !important;
  }

  .tablet\:ext-flex-shrink-0 {
    flex-shrink: 0 !important;
  }

  .tablet\:ext-flex-shrink {
    flex-shrink: 1 !important;
  }

  .tablet\:ext-flex-grow-0 {
    flex-grow: 0 !important;
  }

  .tablet\:ext-flex-grow {
    flex-grow: 1 !important;
  }

  .tablet\:ext-list-none {
    list-style-type: none !important;
  }

  .tablet\:ext-grid-cols-1 {
    grid-template-columns: repeat(1, minmax(0, 1fr)) !important;
  }

  .tablet\:ext-grid-cols-2 {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  }

  .tablet\:ext-grid-cols-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  }

  .tablet\:ext-grid-cols-4 {
    grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
  }

  .tablet\:ext-grid-cols-5 {
    grid-template-columns: repeat(5, minmax(0, 1fr)) !important;
  }

  .tablet\:ext-grid-cols-6 {
    grid-template-columns: repeat(6, minmax(0, 1fr)) !important;
  }

  .tablet\:ext-grid-cols-7 {
    grid-template-columns: repeat(7, minmax(0, 1fr)) !important;
  }

  .tablet\:ext-grid-cols-8 {
    grid-template-columns: repeat(8, minmax(0, 1fr)) !important;
  }

  .tablet\:ext-grid-cols-9 {
    grid-template-columns: repeat(9, minmax(0, 1fr)) !important;
  }

  .tablet\:ext-grid-cols-10 {
    grid-template-columns: repeat(10, minmax(0, 1fr)) !important;
  }

  .tablet\:ext-grid-cols-11 {
    grid-template-columns: repeat(11, minmax(0, 1fr)) !important;
  }

  .tablet\:ext-grid-cols-12 {
    grid-template-columns: repeat(12, minmax(0, 1fr)) !important;
  }

  .tablet\:ext-grid-cols-none {
    grid-template-columns: none !important;
  }

  .tablet\:ext-flex-row {
    flex-direction: row !important;
  }

  .tablet\:ext-flex-row-reverse {
    flex-direction: row-reverse !important;
  }

  .tablet\:ext-flex-col {
    flex-direction: column !important;
  }

  .tablet\:ext-flex-col-reverse {
    flex-direction: column-reverse !important;
  }

  .tablet\:ext-flex-wrap {
    flex-wrap: wrap !important;
  }

  .tablet\:ext-flex-wrap-reverse {
    flex-wrap: wrap-reverse !important;
  }

  .tablet\:ext-flex-nowrap {
    flex-wrap: nowrap !important;
  }

  .tablet\:ext-items-start {
    align-items: flex-start !important;
  }

  .tablet\:ext-items-end {
    align-items: flex-end !important;
  }

  .tablet\:ext-items-center {
    align-items: center !important;
  }

  .tablet\:ext-items-baseline {
    align-items: baseline !important;
  }

  .tablet\:ext-items-stretch {
    align-items: stretch !important;
  }

  .tablet\:ext-justify-start {
    justify-content: flex-start !important;
  }

  .tablet\:ext-justify-end {
    justify-content: flex-end !important;
  }

  .tablet\:ext-justify-center {
    justify-content: center !important;
  }

  .tablet\:ext-justify-between {
    justify-content: space-between !important;
  }

  .tablet\:ext-justify-around {
    justify-content: space-around !important;
  }

  .tablet\:ext-justify-evenly {
    justify-content: space-evenly !important;
  }

  .tablet\:ext-justify-items-start {
    justify-items: start !important;
  }

  .tablet\:ext-justify-items-end {
    justify-items: end !important;
  }

  .tablet\:ext-justify-items-center {
    justify-items: center !important;
  }

  .tablet\:ext-justify-items-stretch {
    justify-items: stretch !important;
  }

  .tablet\:ext-justify-self-auto {
    justify-self: auto !important;
  }

  .tablet\:ext-justify-self-start {
    justify-self: start !important;
  }

  .tablet\:ext-justify-self-end {
    justify-self: end !important;
  }

  .tablet\:ext-justify-self-center {
    justify-self: center !important;
  }

  .tablet\:ext-justify-self-stretch {
    justify-self: stretch !important;
  }

  .tablet\:ext-p-0:not([style*="padding"]) {
    padding: 0 !important;
  }

  .tablet\:ext-p-base:not([style*="padding"]) {
    padding: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .tablet\:ext-p-lg:not([style*="padding"]) {
    padding: var(--extendify--spacing--large, 3rem) !important;
  }

  .tablet\:ext-px-0:not([style*="padding"]) {
    padding-left: 0 !important;
    padding-right: 0 !important;
  }

  .tablet\:ext-px-base:not([style*="padding"]) {
    padding-left: var(--wp--style--block-gap, 1.75rem) !important;
    padding-right: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .tablet\:ext-px-lg:not([style*="padding"]) {
    padding-left: var(--extendify--spacing--large, 3rem) !important;
    padding-right: var(--extendify--spacing--large, 3rem) !important;
  }

  .tablet\:ext-py-0:not([style*="padding"]) {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
  }

  .tablet\:ext-py-base:not([style*="padding"]) {
    padding-top: var(--wp--style--block-gap, 1.75rem) !important;
    padding-bottom: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .tablet\:ext-py-lg:not([style*="padding"]) {
    padding-top: var(--extendify--spacing--large, 3rem) !important;
    padding-bottom: var(--extendify--spacing--large, 3rem) !important;
  }

  .tablet\:ext-pt-0:not([style*="padding"]) {
    padding-top: 0 !important;
  }

  .tablet\:ext-pt-base:not([style*="padding"]) {
    padding-top: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .tablet\:ext-pt-lg:not([style*="padding"]) {
    padding-top: var(--extendify--spacing--large, 3rem) !important;
  }

  .tablet\:ext-pr-0:not([style*="padding"]) {
    padding-right: 0 !important;
  }

  .tablet\:ext-pr-base:not([style*="padding"]) {
    padding-right: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .tablet\:ext-pr-lg:not([style*="padding"]) {
    padding-right: var(--extendify--spacing--large, 3rem) !important;
  }

  .tablet\:ext-pb-0:not([style*="padding"]) {
    padding-bottom: 0 !important;
  }

  .tablet\:ext-pb-base:not([style*="padding"]) {
    padding-bottom: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .tablet\:ext-pb-lg:not([style*="padding"]) {
    padding-bottom: var(--extendify--spacing--large, 3rem) !important;
  }

  .tablet\:ext-pl-0:not([style*="padding"]) {
    padding-left: 0 !important;
  }

  .tablet\:ext-pl-base:not([style*="padding"]) {
    padding-left: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .tablet\:ext-pl-lg:not([style*="padding"]) {
    padding-left: var(--extendify--spacing--large, 3rem) !important;
  }

  .tablet\:ext-text-left {
    text-align: left !important;
  }

  .tablet\:ext-text-center {
    text-align: center !important;
  }

  .tablet\:ext-text-right {
    text-align: right !important;
  }
}

@media (min-width: 1080px) {
  .desktop\:ext-absolute {
    position: absolute !important;
  }

  .desktop\:ext-relative {
    position: relative !important;
  }

  .desktop\:ext-top-base {
    top: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .desktop\:ext-top-lg {
    top: var(--extendify--spacing--large, 3rem) !important;
  }

  .desktop\:ext--top-base {
    top: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .desktop\:ext--top-lg {
    top: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .desktop\:ext-right-base {
    right: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .desktop\:ext-right-lg {
    right: var(--extendify--spacing--large, 3rem) !important;
  }

  .desktop\:ext--right-base {
    right: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .desktop\:ext--right-lg {
    right: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .desktop\:ext-bottom-base {
    bottom: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .desktop\:ext-bottom-lg {
    bottom: var(--extendify--spacing--large, 3rem) !important;
  }

  .desktop\:ext--bottom-base {
    bottom: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .desktop\:ext--bottom-lg {
    bottom: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .desktop\:ext-left-base {
    left: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .desktop\:ext-left-lg {
    left: var(--extendify--spacing--large, 3rem) !important;
  }

  .desktop\:ext--left-base {
    left: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .desktop\:ext--left-lg {
    left: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .desktop\:ext-order-1 {
    order: 1 !important;
  }

  .desktop\:ext-order-2 {
    order: 2 !important;
  }

  .desktop\:ext-m-0:not([style*="margin"]) {
    margin: 0 !important;
  }

  .desktop\:ext-m-auto:not([style*="margin"]) {
    margin: auto !important;
  }

  .desktop\:ext-m-base:not([style*="margin"]) {
    margin: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .desktop\:ext-m-lg:not([style*="margin"]) {
    margin: var(--extendify--spacing--large, 3rem) !important;
  }

  .desktop\:ext--m-base:not([style*="margin"]) {
    margin: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .desktop\:ext--m-lg:not([style*="margin"]) {
    margin: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .desktop\:ext-mx-0:not([style*="margin"]) {
    margin-left: 0 !important;
    margin-right: 0 !important;
  }

  .desktop\:ext-mx-auto:not([style*="margin"]) {
    margin-left: auto !important;
    margin-right: auto !important;
  }

  .desktop\:ext-mx-base:not([style*="margin"]) {
    margin-left: var(--wp--style--block-gap, 1.75rem) !important;
    margin-right: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .desktop\:ext-mx-lg:not([style*="margin"]) {
    margin-left: var(--extendify--spacing--large, 3rem) !important;
    margin-right: var(--extendify--spacing--large, 3rem) !important;
  }

  .desktop\:ext--mx-base:not([style*="margin"]) {
    margin-left: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
    margin-right: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .desktop\:ext--mx-lg:not([style*="margin"]) {
    margin-left: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
    margin-right: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .desktop\:ext-my-0:not([style*="margin"]) {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
  }

  .desktop\:ext-my-auto:not([style*="margin"]) {
    margin-top: auto !important;
    margin-bottom: auto !important;
  }

  .desktop\:ext-my-base:not([style*="margin"]) {
    margin-top: var(--wp--style--block-gap, 1.75rem) !important;
    margin-bottom: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .desktop\:ext-my-lg:not([style*="margin"]) {
    margin-top: var(--extendify--spacing--large, 3rem) !important;
    margin-bottom: var(--extendify--spacing--large, 3rem) !important;
  }

  .desktop\:ext--my-base:not([style*="margin"]) {
    margin-top: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
    margin-bottom: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .desktop\:ext--my-lg:not([style*="margin"]) {
    margin-top: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
    margin-bottom: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .desktop\:ext-mt-0:not([style*="margin"]) {
    margin-top: 0 !important;
  }

  .desktop\:ext-mt-auto:not([style*="margin"]) {
    margin-top: auto !important;
  }

  .desktop\:ext-mt-base:not([style*="margin"]) {
    margin-top: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .desktop\:ext-mt-lg:not([style*="margin"]) {
    margin-top: var(--extendify--spacing--large, 3rem) !important;
  }

  .desktop\:ext--mt-base:not([style*="margin"]) {
    margin-top: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .desktop\:ext--mt-lg:not([style*="margin"]) {
    margin-top: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .desktop\:ext-mr-0:not([style*="margin"]) {
    margin-right: 0 !important;
  }

  .desktop\:ext-mr-auto:not([style*="margin"]) {
    margin-right: auto !important;
  }

  .desktop\:ext-mr-base:not([style*="margin"]) {
    margin-right: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .desktop\:ext-mr-lg:not([style*="margin"]) {
    margin-right: var(--extendify--spacing--large, 3rem) !important;
  }

  .desktop\:ext--mr-base:not([style*="margin"]) {
    margin-right: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .desktop\:ext--mr-lg:not([style*="margin"]) {
    margin-right: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .desktop\:ext-mb-0:not([style*="margin"]) {
    margin-bottom: 0 !important;
  }

  .desktop\:ext-mb-auto:not([style*="margin"]) {
    margin-bottom: auto !important;
  }

  .desktop\:ext-mb-base:not([style*="margin"]) {
    margin-bottom: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .desktop\:ext-mb-lg:not([style*="margin"]) {
    margin-bottom: var(--extendify--spacing--large, 3rem) !important;
  }

  .desktop\:ext--mb-base:not([style*="margin"]) {
    margin-bottom: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .desktop\:ext--mb-lg:not([style*="margin"]) {
    margin-bottom: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .desktop\:ext-ml-0:not([style*="margin"]) {
    margin-left: 0 !important;
  }

  .desktop\:ext-ml-auto:not([style*="margin"]) {
    margin-left: auto !important;
  }

  .desktop\:ext-ml-base:not([style*="margin"]) {
    margin-left: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .desktop\:ext-ml-lg:not([style*="margin"]) {
    margin-left: var(--extendify--spacing--large, 3rem) !important;
  }

  .desktop\:ext--ml-base:not([style*="margin"]) {
    margin-left: calc(var(--wp--style--block-gap, 1.75rem) * -1) !important;
  }

  .desktop\:ext--ml-lg:not([style*="margin"]) {
    margin-left: calc(var(--extendify--spacing--large, 3rem) * -1) !important;
  }

  .desktop\:ext-block {
    display: block !important;
  }

  .desktop\:ext-inline-block {
    display: inline-block !important;
  }

  .desktop\:ext-inline {
    display: inline !important;
  }

  .desktop\:ext-flex {
    display: flex !important;
  }

  .desktop\:ext-inline-flex {
    display: inline-flex !important;
  }

  .desktop\:ext-grid {
    display: grid !important;
  }

  .desktop\:ext-inline-grid {
    display: inline-grid !important;
  }

  .desktop\:ext-hidden {
    display: none !important;
  }

  .desktop\:ext-w-auto {
    width: auto !important;
  }

  .desktop\:ext-w-full {
    width: 100% !important;
  }

  .desktop\:ext-max-w-full {
    max-width: 100% !important;
  }

  .desktop\:ext-flex-1 {
    flex: 1 1 0% !important;
  }

  .desktop\:ext-flex-auto {
    flex: 1 1 auto !important;
  }

  .desktop\:ext-flex-initial {
    flex: 0 1 auto !important;
  }

  .desktop\:ext-flex-none {
    flex: none !important;
  }

  .desktop\:ext-flex-shrink-0 {
    flex-shrink: 0 !important;
  }

  .desktop\:ext-flex-shrink {
    flex-shrink: 1 !important;
  }

  .desktop\:ext-flex-grow-0 {
    flex-grow: 0 !important;
  }

  .desktop\:ext-flex-grow {
    flex-grow: 1 !important;
  }

  .desktop\:ext-list-none {
    list-style-type: none !important;
  }

  .desktop\:ext-grid-cols-1 {
    grid-template-columns: repeat(1, minmax(0, 1fr)) !important;
  }

  .desktop\:ext-grid-cols-2 {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  }

  .desktop\:ext-grid-cols-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  }

  .desktop\:ext-grid-cols-4 {
    grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
  }

  .desktop\:ext-grid-cols-5 {
    grid-template-columns: repeat(5, minmax(0, 1fr)) !important;
  }

  .desktop\:ext-grid-cols-6 {
    grid-template-columns: repeat(6, minmax(0, 1fr)) !important;
  }

  .desktop\:ext-grid-cols-7 {
    grid-template-columns: repeat(7, minmax(0, 1fr)) !important;
  }

  .desktop\:ext-grid-cols-8 {
    grid-template-columns: repeat(8, minmax(0, 1fr)) !important;
  }

  .desktop\:ext-grid-cols-9 {
    grid-template-columns: repeat(9, minmax(0, 1fr)) !important;
  }

  .desktop\:ext-grid-cols-10 {
    grid-template-columns: repeat(10, minmax(0, 1fr)) !important;
  }

  .desktop\:ext-grid-cols-11 {
    grid-template-columns: repeat(11, minmax(0, 1fr)) !important;
  }

  .desktop\:ext-grid-cols-12 {
    grid-template-columns: repeat(12, minmax(0, 1fr)) !important;
  }

  .desktop\:ext-grid-cols-none {
    grid-template-columns: none !important;
  }

  .desktop\:ext-flex-row {
    flex-direction: row !important;
  }

  .desktop\:ext-flex-row-reverse {
    flex-direction: row-reverse !important;
  }

  .desktop\:ext-flex-col {
    flex-direction: column !important;
  }

  .desktop\:ext-flex-col-reverse {
    flex-direction: column-reverse !important;
  }

  .desktop\:ext-flex-wrap {
    flex-wrap: wrap !important;
  }

  .desktop\:ext-flex-wrap-reverse {
    flex-wrap: wrap-reverse !important;
  }

  .desktop\:ext-flex-nowrap {
    flex-wrap: nowrap !important;
  }

  .desktop\:ext-items-start {
    align-items: flex-start !important;
  }

  .desktop\:ext-items-end {
    align-items: flex-end !important;
  }

  .desktop\:ext-items-center {
    align-items: center !important;
  }

  .desktop\:ext-items-baseline {
    align-items: baseline !important;
  }

  .desktop\:ext-items-stretch {
    align-items: stretch !important;
  }

  .desktop\:ext-justify-start {
    justify-content: flex-start !important;
  }

  .desktop\:ext-justify-end {
    justify-content: flex-end !important;
  }

  .desktop\:ext-justify-center {
    justify-content: center !important;
  }

  .desktop\:ext-justify-between {
    justify-content: space-between !important;
  }

  .desktop\:ext-justify-around {
    justify-content: space-around !important;
  }

  .desktop\:ext-justify-evenly {
    justify-content: space-evenly !important;
  }

  .desktop\:ext-justify-items-start {
    justify-items: start !important;
  }

  .desktop\:ext-justify-items-end {
    justify-items: end !important;
  }

  .desktop\:ext-justify-items-center {
    justify-items: center !important;
  }

  .desktop\:ext-justify-items-stretch {
    justify-items: stretch !important;
  }

  .desktop\:ext-justify-self-auto {
    justify-self: auto !important;
  }

  .desktop\:ext-justify-self-start {
    justify-self: start !important;
  }

  .desktop\:ext-justify-self-end {
    justify-self: end !important;
  }

  .desktop\:ext-justify-self-center {
    justify-self: center !important;
  }

  .desktop\:ext-justify-self-stretch {
    justify-self: stretch !important;
  }

  .desktop\:ext-p-0:not([style*="padding"]) {
    padding: 0 !important;
  }

  .desktop\:ext-p-base:not([style*="padding"]) {
    padding: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .desktop\:ext-p-lg:not([style*="padding"]) {
    padding: var(--extendify--spacing--large, 3rem) !important;
  }

  .desktop\:ext-px-0:not([style*="padding"]) {
    padding-left: 0 !important;
    padding-right: 0 !important;
  }

  .desktop\:ext-px-base:not([style*="padding"]) {
    padding-left: var(--wp--style--block-gap, 1.75rem) !important;
    padding-right: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .desktop\:ext-px-lg:not([style*="padding"]) {
    padding-left: var(--extendify--spacing--large, 3rem) !important;
    padding-right: var(--extendify--spacing--large, 3rem) !important;
  }

  .desktop\:ext-py-0:not([style*="padding"]) {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
  }

  .desktop\:ext-py-base:not([style*="padding"]) {
    padding-top: var(--wp--style--block-gap, 1.75rem) !important;
    padding-bottom: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .desktop\:ext-py-lg:not([style*="padding"]) {
    padding-top: var(--extendify--spacing--large, 3rem) !important;
    padding-bottom: var(--extendify--spacing--large, 3rem) !important;
  }

  .desktop\:ext-pt-0:not([style*="padding"]) {
    padding-top: 0 !important;
  }

  .desktop\:ext-pt-base:not([style*="padding"]) {
    padding-top: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .desktop\:ext-pt-lg:not([style*="padding"]) {
    padding-top: var(--extendify--spacing--large, 3rem) !important;
  }

  .desktop\:ext-pr-0:not([style*="padding"]) {
    padding-right: 0 !important;
  }

  .desktop\:ext-pr-base:not([style*="padding"]) {
    padding-right: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .desktop\:ext-pr-lg:not([style*="padding"]) {
    padding-right: var(--extendify--spacing--large, 3rem) !important;
  }

  .desktop\:ext-pb-0:not([style*="padding"]) {
    padding-bottom: 0 !important;
  }

  .desktop\:ext-pb-base:not([style*="padding"]) {
    padding-bottom: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .desktop\:ext-pb-lg:not([style*="padding"]) {
    padding-bottom: var(--extendify--spacing--large, 3rem) !important;
  }

  .desktop\:ext-pl-0:not([style*="padding"]) {
    padding-left: 0 !important;
  }

  .desktop\:ext-pl-base:not([style*="padding"]) {
    padding-left: var(--wp--style--block-gap, 1.75rem) !important;
  }

  .desktop\:ext-pl-lg:not([style*="padding"]) {
    padding-left: var(--extendify--spacing--large, 3rem) !important;
  }

  .desktop\:ext-text-left {
    text-align: left !important;
  }

  .desktop\:ext-text-center {
    text-align: center !important;
  }

  .desktop\:ext-text-right {
    text-align: right !important;
  }
}

</style>
<link rel='stylesheet' id='contact-form-7-css' href='https://aeromotus.ru/wp-content/plugins/contact-form-7/includes/css/styles.css?ver=5.7.4' type='text/css' media='all' />
<link rel='stylesheet' id='cool-tag-cloud-css' href='https://aeromotus.ru/wp-content/plugins/cool-tag-cloud/inc/cool-tag-cloud.css?ver=2.25' type='text/css' media='all' />
<link rel='stylesheet' id='russia-html5-map-style-css' href='https://aeromotus.ru/wp-content/plugins/russiahtmlmap/static/css/map.css?ver=3b71e7425f116479de92df27dcaef655' type='text/css' media='all' />
<link rel='stylesheet' id='photoswipe-css' href='https://aeromotus.ru/wp-content/plugins/woocommerce/assets/css/photoswipe/photoswipe.min.css?ver=7.5.0' type='text/css' media='all' />
<link rel='stylesheet' id='photoswipe-default-skin-css' href='https://aeromotus.ru/wp-content/plugins/woocommerce/assets/css/photoswipe/default-skin/default-skin.min.css?ver=7.5.0' type='text/css' media='all' />
<style id='woocommerce-inline-inline-css' type='text/css'>
.woocommerce form .form-row .required { visibility: visible; }
</style>
<link rel='stylesheet' id='htbbootstrap-css' href='https://aeromotus.ru/wp-content/plugins/ht-mega-for-elementor/assets/css/htbbootstrap.css?ver=2.1.0' type='text/css' media='all' />
<link rel='stylesheet' id='font-awesome-css' href='https://aeromotus.ru/wp-content/plugins/elementor/assets/lib/font-awesome/css/font-awesome.min.css?ver=4.7.0' type='text/css' media='all' />
<link rel='stylesheet' id='htmega-animation-css' href='https://aeromotus.ru/wp-content/plugins/ht-mega-for-elementor/assets/css/animation.css?ver=2.1.0' type='text/css' media='all' />
<link rel='stylesheet' id='htmega-keyframes-css' href='https://aeromotus.ru/wp-content/plugins/ht-mega-for-elementor/assets/css/htmega-keyframes.css?ver=2.1.0' type='text/css' media='all' />
<link rel='stylesheet' id='electro-fonts-css' href='https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&#038;display=swap' type='text/css' media='all' />
<link rel='stylesheet' id='font-electro-css' href='https://aeromotus.ru/wp-content/themes/electro/assets/css/font-electro.css?ver=3.2.4' type='text/css' media='all' />
<link rel='stylesheet' id='fontawesome-css' href='https://aeromotus.ru/wp-content/themes/electro/assets/vendor/fontawesome/css/all.min.css?ver=3.2.4' type='text/css' media='all' />
<link rel='stylesheet' id='animate-css-css' href='https://aeromotus.ru/wp-content/themes/electro/assets/vendor/animate.css/animate.min.css?ver=3.2.4' type='text/css' media='all' />
<link rel='stylesheet' id='electro-style-css' href='https://aeromotus.ru/wp-content/themes/electro/style.min.css?ver=3.2.4' type='text/css' media='all' />
<link rel='stylesheet' id='dflip-icons-style-css' href='https://aeromotus.ru/wp-content/plugins/3d-flipbook-dflip-lite/assets/css/themify-icons.min.css?ver=1.7.35' type='text/css' media='all' />
<link rel='stylesheet' id='dflip-style-css' href='https://aeromotus.ru/wp-content/plugins/3d-flipbook-dflip-lite/assets/css/dflip.min.css?ver=1.7.35' type='text/css' media='all' />
<link rel='stylesheet' id='elementor-frontend-css' href='https://aeromotus.ru/wp-content/plugins/elementor/assets/css/frontend-lite.min.css?ver=3.11.5' type='text/css' media='all' />
<link rel='stylesheet' id='swiper-css' href='https://aeromotus.ru/wp-content/plugins/elementor/assets/lib/swiper/css/swiper.min.css?ver=5.3.6' type='text/css' media='all' />
<link rel='stylesheet' id='elementor-post-23221-css' href='https://aeromotus.ru/wp-content/uploads/elementor/css/post-23221.css?ver=1678992069' type='text/css' media='all' />
<link rel='stylesheet' id='elementor-pro-css' href='https://aeromotus.ru/wp-content/plugins/elementor-pro/assets/css/frontend-lite.min.css?ver=3.11.6' type='text/css' media='all' />
<link rel='stylesheet' id='font-awesome-5-all-css' href='https://aeromotus.ru/wp-content/plugins/elementor/assets/lib/font-awesome/css/all.min.css?ver=3.11.5' type='text/css' media='all' />
<link rel='stylesheet' id='font-awesome-4-shim-css' href='https://aeromotus.ru/wp-content/plugins/elementor/assets/lib/font-awesome/css/v4-shims.min.css?ver=3.11.5' type='text/css' media='all' />
<link rel='stylesheet' id='elementor-post-34574-css' href='https://aeromotus.ru/wp-content/uploads/elementor/css/post-34574.css?ver=1678992069' type='text/css' media='all' />
<link rel='stylesheet' id='aeromotus-css' href='https://aeromotus.ru/wp-content/themes/electro-child/custom.css' type='text/css' media='screen' />
<link rel='stylesheet' id='google-fonts-1-css' href='https://fonts.googleapis.com/css?family=Roboto%3A100%2C100italic%2C200%2C200italic%2C300%2C300italic%2C400%2C400italic%2C500%2C500italic%2C600%2C600italic%2C700%2C700italic%2C800%2C800italic%2C900%2C900italic%7CRoboto+Slab%3A100%2C100italic%2C200%2C200italic%2C300%2C300italic%2C400%2C400italic%2C500%2C500italic%2C600%2C600italic%2C700%2C700italic%2C800%2C800italic%2C900%2C900italic&#038;display=auto&#038;subset=cyrillic&#038;ver=3b71e7425f116479de92df27dcaef655' type='text/css' media='all' />
<link rel="preconnect" href="https://fonts.gstatic.com/" crossorigin><script type="text/template" id="tmpl-variation-template">
	<div class="woocommerce-variation-description">{{{ data.variation.variation_description }}}</div>
	<div class="woocommerce-variation-price">{{{ data.variation.price_html }}}</div>
	<div class="woocommerce-variation-availability">{{{ data.variation.availability_html }}}</div>
</script>
<script type="text/template" id="tmpl-unavailable-variation-template">
	<p>Этот товар недоступен. Пожалуйста, выберите другую комбинацию.</p>
</script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/wp-yandex-metrika/assets/YmEc.min.js?ver=1.1.7' id='wp-yandex-metrika_YmEc-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-includes/js/jquery/jquery.min.js?ver=3.6.1' id='jquery-core-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.3.2' id='jquery-migrate-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/wp-yandex-metrika/assets/frontend.min.js?ver=1.1.7' id='wp-yandex-metrika_frontend-js'></script>
<script type='text/javascript' id='ugb-block-frontend-js-v2-js-extra'>
/* <![CDATA[ */
var stackable = {"restUrl":"https:\/\/aeromotus.ru\/wp-json\/"};
/* ]]> */
</script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/stackable-ultimate-gutenberg-blocks/dist/deprecated/frontend_blocks_deprecated_v2.js?ver=3.1.4' id='ugb-block-frontend-js-v2-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/russiahtmlmap/static/js/jquery.nicescroll.js?ver=3b71e7425f116479de92df27dcaef655' id='russia-html5-map-nicescroll-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/woocommerce/assets/js/jquery-blockui/jquery.blockUI.min.js?ver=2.7.0-wc.7.5.0' id='jquery-blockui-js'></script>
<script type='text/javascript' id='wc-add-to-cart-js-extra'>
/* <![CDATA[ */
var wc_add_to_cart_params = {"ajax_url":"\/wp-admin\/admin-ajax.php","wc_ajax_url":"\/?wc-ajax=%%endpoint%%&elementor_page_id=11405","i18n_view_cart":"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u043a\u043e\u0440\u0437\u0438\u043d\u044b","cart_url":"https:\/\/aeromotus.ru\/cart\/","is_cart":"","cart_redirect_after_add":"no"};
/* ]]> */
</script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/woocommerce/assets/js/frontend/add-to-cart.min.js?ver=7.5.0' id='wc-add-to-cart-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/js_composer/assets/js/vendors/woocommerce-add-to-cart.js?ver=6.5.0' id='vc_woocommerce-add-to-cart-js-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/elementor/assets/lib/font-awesome/js/v4-shims.min.js?ver=3.11.5' id='font-awesome-4-shim-js'></script>
<link rel="https://api.w.org/" href="https://aeromotus.ru/wp-json/" /><link rel="alternate" type="application/json" href="https://aeromotus.ru/wp-json/wp/v2/product/11405" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://aeromotus.ru/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://aeromotus.ru/wp-includes/wlwmanifest.xml" />
<link rel='shortlink' href='https://aeromotus.ru/?p=11405' />
<link rel="alternate" type="application/json+oembed" href="https://aeromotus.ru/wp-json/oembed/1.0/embed?url=https%3A%2F%2Faeromotus.ru%2Fproduct%2Fakkumulyator-dji-matrice-300-tb60-intelligent-flight-battery-part08%2F" />
<link rel="alternate" type="text/xml+oembed" href="https://aeromotus.ru/wp-json/oembed/1.0/embed?url=https%3A%2F%2Faeromotus.ru%2Fproduct%2Fakkumulyator-dji-matrice-300-tb60-intelligent-flight-battery-part08%2F&#038;format=xml" />
<meta name="generator" content="Redux 4.3.26" /> <script>
			document.documentElement.className = document.documentElement.className.replace( 'no-js', 'js' );
		</script>
<style>
			.no-js img.lazyload { display: none; }
			figure.wp-block-image img.lazyloading { min-width: 150px; }
							.lazyload, .lazyloading { opacity: 0; }
				.lazyloaded {
					opacity: 1;
					transition: opacity 400ms;
					transition-delay: 0ms;
				}
					</style>
<meta name="yandex-verification" content="92548e2e9bbb49a2" /> <noscript><style>.woocommerce-product-gallery{ opacity: 1 !important; }</style></noscript>
<script data-cfasync="false"> var dFlipLocation = "https://aeromotus.ru/wp-content/plugins/3d-flipbook-dflip-lite/assets/"; var dFlipWPGlobal = {"text":{"toggleSound":"Turn on\/off Sound","toggleThumbnails":"Toggle Thumbnails","toggleOutline":"Toggle Outline\/Bookmark","previousPage":"Previous Page","nextPage":"Next Page","toggleFullscreen":"Toggle Fullscreen","zoomIn":"Zoom In","zoomOut":"Zoom Out","toggleHelp":"Toggle Help","singlePageMode":"Single Page Mode","doublePageMode":"Double Page Mode","downloadPDFFile":"Download PDF File","gotoFirstPage":"Goto First Page","gotoLastPage":"Goto Last Page","share":"Share","mailSubject":"I wanted you to see this FlipBook","mailBody":"Check out this site {{url}}","loading":"DearFlip: Loading "},"moreControls":"download,pageMode,startPage,endPage,sound","hideControls":"","scrollWheel":"true","backgroundColor":"#777","backgroundImage":"","height":"auto","paddingLeft":"20","paddingRight":"20","controlsPosition":"bottom","duration":800,"soundEnable":"true","enableDownload":"true","enableAnnotation":"false","enableAnalytics":"false","webgl":"true","hard":"none","maxTextureSize":"1600","rangeChunkSize":"524288","zoomRatio":1.5,"stiffness":3,"pageMode":"0","singlePageMode":"0","pageSize":"0","autoPlay":"false","autoPlayDuration":5000,"autoPlayStart":"false","linkTarget":"2","sharePrefix":"dearflip-"};</script><meta name="generator" content="Elementor 3.11.5; features: e_dom_optimization, e_optimized_assets_loading, e_optimized_css_loading, e_font_icon_svg; settings: css_print_method-external, google_font-enabled, font_display-auto">
<style type="text/css">.recentcomments a{display:inline !important;padding:0 !important;margin:0 !important;}</style><meta name="generator" content="Powered by WPBakery Page Builder - drag and drop page builder for WordPress." />
<style type="text/css">.broken_link, a.broken_link {
	text-decoration: line-through;
}</style> 
<script type="text/javascript">
            (function (m, e, t, r, i, k, a) {
                m[i] = m[i] || function () {
                    (m[i].a = m[i].a || []).push(arguments)
                };
                m[i].l = 1 * new Date();
                k = e.createElement(t), a = e.getElementsByTagName(t)[0], k.async = 1, k.src = r, a.parentNode.insertBefore(k, a)
            })
            (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

            ym("55570990", "init", {
                clickmap: true,
                trackLinks: true,
                accurateTrackBounce: true,
                webvisor: true,
                ecommerce: "dataLayer",
                params: {
                    __ym: {
                        "ymCmsPlugin": {
                            "cms": "wordpress",
                            "cmsVersion":"6.1",
                            "pluginVersion": "1.1.7",
                            "ymCmsRip": "215484077"
                        }
                    }
                }
            });
        </script>

<link rel="icon" href="https://aeromotus.ru/wp-content/uploads/2019/08/original-logos-2016-Dec-1313-584951f41a963-1-300x257-2.png" sizes="32x32" />
<link rel="icon" href="https://aeromotus.ru/wp-content/uploads/2019/08/original-logos-2016-Dec-1313-584951f41a963-1-300x257-2.png" sizes="192x192" />
<link rel="apple-touch-icon" href="https://aeromotus.ru/wp-content/uploads/2019/08/original-logos-2016-Dec-1313-584951f41a963-1-300x257-2.png" />
<meta name="msapplication-TileImage" content="https://aeromotus.ru/wp-content/uploads/2019/08/original-logos-2016-Dec-1313-584951f41a963-1-300x257-2.png" />
<style type="text/css">
        .footer-call-us .call-us-icon i,
        .header-support-info .support-icon i,
        .header-support-inner .support-icon,
        .widget_electro_products_filter .widget_layered_nav li > a:hover::before,
        .widget_electro_products_filter .widget_layered_nav li > a:focus::before,
        .widget_electro_products_filter .widget_product_categories li > a:hover::before,
        .widget_electro_products_filter .widget_product_categories li > a:focus::before,
        .widget_electro_products_filter .widget_layered_nav li.chosen > a::before,
        .widget_electro_products_filter .widget_product_categories li.current-cat > a::before,
        .features-list .media-left i,
        .secondary-nav>.dropdown.open >a::before,
        .secondary-nav>.dropdown.show >a::before,
        p.stars a,
        .top-bar.top-bar-v1 #menu-top-bar-left.nav-inline .menu-item > a i,
        .handheld-footer .handheld-footer-bar .footer-call-us .call-us-text span,
        .footer-v2 .handheld-footer .handheld-footer-bar .footer-call-us .call-us-text span,
        .top-bar .menu-item.customer-support i {
            color: #003a5e;
        }

        .header-logo svg ellipse,
        .footer-logo svg ellipse{
            fill:#003a5e;
        }

        .primary-nav .nav-inline > .menu-item .dropdown-menu,
        .primary-nav-menu .nav-inline > .menu-item .dropdown-menu,
        .navbar-primary .navbar-nav > .menu-item .dropdown-menu,
        .vertical-menu .menu-item-has-children > .dropdown-menu,
        .departments-menu .menu-item-has-children:hover > .dropdown-menu,
        .top-bar .nav-inline > .menu-item .dropdown-menu,
        .secondary-nav>.dropdown .dropdown-menu,
        .header-v6 .vertical-menu .list-group-item > .dropdown-menu,
        .best-selling-menu .nav-item>ul>li.electro-more-menu-item .dropdown-menu,
        .home-v5-slider .tp-tab.selected .tp-tab-title:before,
        .home-v5-slider .tp-tab.selected .tp-tab-title:after,
        .header-v5 .electro-navigation .departments-menu-v2>.dropdown>.dropdown-menu,
        .product-categories-list-with-header.v2 header .caption .section-title:after,
        .primary-nav-menu .nav-inline >.menu-item .dropdown-menu,
        .dropdown-menu-mini-cart,
        .dropdown-menu-user-account,
        .electro-navbar-primary .nav>.menu-item.menu-item-has-children .dropdown-menu,
        .header-v6 .header-logo-area .departments-menu-v2 .departments-menu-v2-title+.dropdown-menu,
        .departments-menu-v2 .departments-menu-v2-title+.dropdown-menu li.menu-item-has-children .dropdown-menu,
        .secondary-nav-v6 .secondary-nav-v6-inner .sub-menu,
        .secondary-nav-v6 .widget_nav_menu .sub-menu {
            border-top-color: #003a5e;
        }

        .columns-6-1 > ul.products > li.product .thumbnails > a:hover,
        .primary-nav .nav-inline .yamm-fw.open > a::before,
        .columns-6-1>ul.products.product-main-6-1 .electro-wc-product-gallery__wrapper .electro-wc-product-gallery__image.flex-active-slide img,
        .single-product .electro-wc-product-gallery .electro-wc-product-gallery__wrapper .electro-wc-product-gallery__image.flex-active-slide img,
        .products-6-1-with-categories-inner .product-main-6-1 .images .thumbnails a:hover,
        .home-v5-slider .tp-tab.selected .tp-tab-title:after,
        .electro-navbar .departments-menu-v2 .departments-menu-v2-title+.dropdown-menu li.menu-item-has-children>.dropdown-menu,
        .product-main-6-1 .thumbnails>a:focus, .product-main-6-1 .thumbnails>a:hover,
        .product-main-6-1 .thumbnails>a:focus, .product-main-6-1 .thumbnails>a:focus,
        .product-main-6-1 .thumbnails>a:focus>img, .product-main-6-1 .thumbnails>a:hover>img,
        .product-main-6-1 .thumbnails>a:focus>img, .product-main-6-1 .thumbnails>a:focus>img {
            border-bottom-color: #003a5e;
        }

        .navbar-primary,
        .footer-newsletter,
        .button:hover::before,
        li.product:hover .button::before,
        li.product:hover .added_to_cart::before,
        .owl-item .product:hover .button::before,
        .owl-item .product:hover .added_to_cart::before,
        .widget_price_filter .ui-slider .ui-slider-handle,
        .woocommerce-pagination ul.page-numbers > li a.current,
        .woocommerce-pagination ul.page-numbers > li span.current,
        .pagination ul.page-numbers > li a.current,
        .pagination ul.page-numbers > li span.current,
        .owl-dots .owl-dot.active,
        .products-carousel-tabs .nav-link.active::before,
        .deal-progress .progress-bar,
        .products-2-1-2 .nav-link.active::before,
        .products-4-1-4 .nav-link.active::before,
        .da .da-action > a::after,
        .header-v1 .navbar-search .input-group .btn,
        .header-v3 .navbar-search .input-group .btn,
        .header-v6 .navbar-search .input-group .btn,
        .header-v8 .navbar-search .input-group .btn,
        .header-v9 .navbar-search .input-group .btn,
        .header-v10 .navbar-search .input-group .btn,
        .header-v11 .navbar-search .input-group-btn .btn,
        .vertical-menu > li:first-child,
        .widget.widget_tag_cloud .tagcloud a:hover,
        .widget.widget_tag_cloud .tagcloud a:focus,
        .navbar-mini-cart .cart-items-count,
        .navbar-compare .count,
        .navbar-wishlist .count,
        .wc-tabs > li.active a::before,
        .ec-tabs > li.active a::before,
        .woocommerce-info,
        .woocommerce-noreviews,
        p.no-comments,
        .products-2-1-2 .nav-link:hover::before,
        .products-4-1-4 .nav-link:hover::before,
        .single_add_to_cart_button,
        .section-onsale-product-carousel .onsale-product-carousel .onsale-product .onsale-product-content .deal-cart-button .button,
        .section-onsale-product-carousel .onsale-product-carousel .onsale-product .onsale-product-content .deal-cart-button .added_to_cart,
        .wpb-accordion .vc_tta.vc_general .vc_tta-panel.vc_active .vc_tta-panel-heading .vc_tta-panel-title > a i,
        ul.products > li.product.list-view:not(.list-view-small) .button:hover,
        ul.products > li.product.list-view:not(.list-view-small) .button:focus,
        ul.products > li.product.list-view:not(.list-view-small) .button:active,
        ul.products > li.product.list-view.list-view-small .button:hover::after,
        ul.products > li.product.list-view.list-view-small .button:focus::after,
        ul.products > li.product.list-view.list-view-small .button:active::after,
        .widget_electro_products_carousel_widget .section-products-carousel .owl-nav .owl-prev:hover,
        .widget_electro_products_carousel_widget .section-products-carousel .owl-nav .owl-next:hover,
        .full-color-background .header-v3,
        .full-color-background .header-v4,
        .full-color-background .top-bar,
        .top-bar-v3,
        .pace .pace-progress,
        .electro-handheld-footer-bar ul li a .count,
        .handheld-navigation-wrapper .stuck .navbar-toggler,
        .handheld-navigation-wrapper .stuck button,
        .handheld-navigation-wrapper.toggled .stuck .navbar-toggler,
        .handheld-navigation-wrapper.toggled .stuck button,
        .da .da-action>a::after,
        .demo_store,
        .header-v5 .header-top,
        .handheld-header-v2,
        .handheld-header-v2.stuck,
        #payment .place-order button[type=submit],
        .single-product .product-images-wrapper .woocommerce-product-gallery.electro-carousel-loaded .flex-control-nav li a.flex-active,
        .single-product .product-images-wrapper .electro-wc-product-gallery .flex-control-nav li a.flex-active,
        .single-product .product-images-wrapper .flex-control-nav li a.flex-active,
        .section-onsale-product .savings,
        .section-onsale-product-carousel .savings,
        .columns-6-1>ul.products.product-main-6-1>li.product .electro-wc-product-gallery .flex-control-nav li a.flex-active,
        .products-carousel-tabs-v5 header ul.nav-inline .nav-link.active,
        .products-carousel-tabs-with-deal header ul.nav-inline .nav-link.active,
        section .deals-carousel-inner-block .onsale-product .onsale-product-content .deal-cart-button .added_to_cart,
        section .deals-carousel-inner-block .onsale-product .onsale-product-content .deal-cart-button .button,
        .header-icon-counter,
        .electro-navbar,
        .departments-menu-v2-title,
        section .deals-carousel-inner-block .onsale-product .onsale-product-content .deal-cart-button .added_to_cart,
        section .deals-carousel-inner-block .onsale-product .onsale-product-content .deal-cart-button .button,
        .deal-products-with-featured header,
        .deal-products-with-featured ul.products > li.product.product-featured .savings,
        .mobile-header-v2,
        .mobile-header-v2.stuck,
        .product-categories-list-with-header.v2 header .caption .section-title,
        .product-categories-list-with-header.v2 header .caption .section-title,
        .home-mobile-v2-features-block,
        .show-nav .nav .nav-item.active .nav-link,
        .header-v5,
        .header-v5 .stuck,
        .electro-navbar-primary,
        .navbar-search-input-group .navbar-search-button,
        .da-block .da-action::after,
        .products-6-1 header.show-nav ul.nav .nav-item.active .nav-link,
        ul.products[data-view=list-view].columns-1>li.product .product-loop-footer .button,
        ul.products[data-view=list-view].columns-2>li.product .product-loop-footer .button,
        ul.products[data-view=list-view].columns-3>li.product .product-loop-footer .button,
        ul.products[data-view=list-view].columns-4>li.product .product-loop-footer .button,
        ul.products[data-view=list-view].columns-5>li.product .product-loop-footer .button,
        ul.products[data-view=list-view].columns-6>li.product .product-loop-footer .button,
        ul.products[data-view=list-view].columns-7>li.product .product-loop-footer .button,
        ul.products[data-view=list-view].columns-8>li.product .product-loop-footer .button,
        ul.products[data-view=list-view]>li.product .product-item__footer .add-to-cart-wrap a,
        .products.show-btn>li.product .added_to_cart,
        .products.show-btn>li.product .button,
        .yith-wcqv-button,
        .header-v7 .masthead,
        .header-v10 .secondary-nav-menu,
        section.category-icons-carousel-v2,
        .category-icons-carousel .category a:hover .category-icon,
        .products-carousel-banner-vertical-tabs .banners-tabs>.nav a.active,
        .products-carousel-with-timer .deal-countdown-timer,
        .section-onsale-product-carousel-v9 .onsale-product .deal-countdown-timer,
        .dokan-elector-style-active.store-v1 .profile-frame + .dokan-store-tabs > ul li.active a:after,
        .dokan-elector-style-active.store-v5 .profile-frame + .dokan-store-tabs > ul li.active a:after,
        .aws-container .aws-search-form .aws-search-clear,
        div.wpforms-container-full .wpforms-form input[type=submit],
        div.wpforms-container-full .wpforms-form button[type=submit],
        div.wpforms-container-full .wpforms-form .wpforms-page-button,
        .electro-dark .full-color-background .masthead .navbar-search .input-group .btn,
        .electro-dark .electro-navbar-primary .nav>.menu-item:hover>a,
        .electro-dark .masthead .navbar-search .input-group .btn {
            background-color: #003a5e;
        }

        .electro-navbar .departments-menu-v2 .departments-menu-v2-title+.dropdown-menu li.menu-item-has-children>.dropdown-menu,
        .products-carousel-banner-vertical-tabs .banners-tabs>.nav a.active::before {
            border-right-color: #003a5e;
        }

        .hero-action-btn:hover {
            background-color: #003556 !important;
        }

        .hero-action-btn,
        #scrollUp,
        .custom .tp-bullet.selected,
        .home-v1-slider .btn-primary,
        .home-v2-slider .btn-primary,
        .home-v3-slider .btn-primary,
        .electro-dark .show-nav .nav .active .nav-link,
        .electro-dark .full-color-background .masthead .header-icon-counter,
        .electro-dark .full-color-background .masthead .navbar-search .input-group .btn,
        .electro-dark .electro-navbar-primary .nav>.menu-item:hover>a,
        .electro-dark .masthead .navbar-search .input-group .btn {
            background-color: #003a5e !important;
        }

        .departments-menu .departments-menu-dropdown,
        .departments-menu .menu-item-has-children > .dropdown-menu,
        .widget_price_filter .ui-slider .ui-slider-handle:last-child,
        section header h1::after,
        section header .h1::after,
        .products-carousel-tabs .nav-link.active::after,
        section.section-product-cards-carousel header ul.nav .active .nav-link,
        section.section-onsale-product,
        section.section-onsale-product-carousel .onsale-product-carousel,
        .products-2-1-2 .nav-link.active::after,
        .products-4-1-4 .nav-link.active::after,
        .products-6-1 header ul.nav .active .nav-link,
        .header-v1 .navbar-search .input-group .form-control,
        .header-v1 .navbar-search .input-group .input-group-addon,
        .header-v1 .navbar-search .input-group .btn,
        .header-v3 .navbar-search .input-group .form-control,
        .header-v3 .navbar-search .input-group .input-group-addon,
        .header-v3 .navbar-search .input-group .btn,
        .header-v6 .navbar-search .input-group .form-control,
        .header-v6 .navbar-search .input-group .input-group-addon,
        .header-v6 .navbar-search .input-group .btn,
        .header-v8 .navbar-search .input-group .form-control,
        .header-v8 .navbar-search .input-group .input-group-addon,
        .header-v8 .navbar-search .input-group .btn,
        .header-v9 .navbar-search .input-group .form-control,
        .header-v9 .navbar-search .input-group .input-group-addon,
        .header-v9 .navbar-search .input-group .btn,
        .header-v10 .navbar-search .input-group .form-control,
        .header-v10 .navbar-search .input-group .input-group-addon,
        .header-v10 .navbar-search .input-group .btn,
        .widget.widget_tag_cloud .tagcloud a:hover,
        .widget.widget_tag_cloud .tagcloud a:focus,
        .navbar-primary .navbar-mini-cart .dropdown-menu-mini-cart,
        .woocommerce-checkout h3::after,
        #customer_login h2::after,
        .customer-login-form h2::after,
        .navbar-primary .navbar-mini-cart .dropdown-menu-mini-cart,
        .woocommerce-edit-address form h3::after,
        .edit-account legend::after,
        .woocommerce-account h2::after,
        .address header.title h3::after,
        .addresses header.title h3::after,
        .woocommerce-order-received h2::after,
        .track-order h2::after,
        .wc-tabs > li.active a::after,
        .ec-tabs > li.active a::after,
        .comments-title::after,
        .comment-reply-title::after,
        .pings-title::after,
        #reviews #comments > h2::after,
        .single-product .woocommerce-tabs ~ div.products > h2::after,
        .single-product .electro-tabs ~ div.products > h2::after,
        .single-product .related>h2::after,
        .single-product .up-sells>h2::after,
        .cart-collaterals h2:not(.woocommerce-loop-product__title)::after,
        .footer-widgets .widget-title:after,
        .sidebar .widget-title::after,
        .sidebar-blog .widget-title::after,
        .contact-page-title::after,
        #reviews:not(.electro-advanced-reviews) #comments > h2::after,
        .cpf-type-range .tm-range-picker .noUi-origin .noUi-handle,
        .widget_electro_products_carousel_widget .section-products-carousel .owl-nav .owl-prev:hover,
        .widget_electro_products_carousel_widget .section-products-carousel .owl-nav .owl-next:hover,
        .wpb-accordion .vc_tta.vc_general .vc_tta-panel.vc_active .vc_tta-panel-heading .vc_tta-panel-title > a i,
        .single-product .woocommerce-tabs+section.products>h2::after,
        #payment .place-order button[type=submit],
        .single-product .electro-tabs+section.products>h2::after,
        .deal-products-carousel .deal-products-carousel-inner .deal-products-timer header .section-title:after,
        .deal-products-carousel .deal-products-carousel-inner .deal-countdown > span,
        .deals-carousel-inner-block .onsale-product .onsale-product-content .deal-countdown > span,
        .home-v5-slider .section-onsale-product-v2 .onsale-product .onsale-product-content .deal-countdown > span,
        .products-with-category-image header ul.nav-inline .active .nav-link,
        .products-6-1-with-categories header ul.nav-inline .active .nav-link,
        .products-carousel-tabs-v5 header ul.nav-inline .nav-link:hover,
        .products-carousel-tabs-with-deal header ul.nav-inline .nav-link:hover,
        section.products-carousel-v5 header .nav-inline .active .nav-link,
        .mobile-header-v1 .site-search .widget.widget_product_search form,
        .mobile-header-v1 .site-search .widget.widget_search form,
        .show-nav .nav .nav-item.active .nav-link,
        .departments-menu-v2 .departments-menu-v2-title+.dropdown-menu,
        .navbar-search-input-group .search-field,
        .navbar-search-input-group .custom-select,
        .products-6-1 header.show-nav ul.nav .nav-item.active .nav-link,
        .header-v1 .aws-container .aws-search-field,
        .header-v3 .aws-container .aws-search-field,
        .header-v6 .aws-container .aws-search-field,
        .header-v8 .aws-container .aws-search-field,
        div.wpforms-container-full .wpforms-form input[type=submit],
        div.wpforms-container-full .wpforms-form button[type=submit],
        div.wpforms-container-full .wpforms-form .wpforms-page-button,
        .electro-dark .electro-navbar .navbar-search .input-group .btn,
        .electro-dark .masthead .navbar-search .input-group .btn {
            border-color: #003a5e;
        }

        @media (min-width: 1480px) {
            .onsale-product-carousel .onsale-product__inner {
        		border-color: #003a5e;
        	}
        }

        .widget_price_filter .price_slider_amount .button,
        .dropdown-menu-mini-cart .wc-forward.checkout,
        table.cart .actions .checkout-button,
        .cart-collaterals .cart_totals .wc-proceed-to-checkout a,
        .customer-login-form .button,
        .btn-primary,
        input[type="submit"],
        input.dokan-btn-theme[type="submit"],
        a.dokan-btn-theme, .dokan-btn-theme,
        .sign-in-button,
        .products-carousel-banner-vertical-tabs .banners-tabs .tab-content-inner>a,
        .dokan-store-support-and-follow-wrap .dokan-btn {
          color: #ffffff;
          background-color: #003a5e;
          border-color: #003a5e;
        }

        .widget_price_filter .price_slider_amount .button:hover,
        .dropdown-menu-mini-cart .wc-forward.checkout:hover,
        table.cart .actions .checkout-button:hover,
        .customer-login-form .button:hover,
        .btn-primary:hover,
        input[type="submit"]:hover,
        input.dokan-btn-theme[type="submit"]:hover,
        a.dokan-btn-theme:hover, .dokan-btn-theme:hover,
        .sign-in-button:hover,
        .products-carousel-banner-vertical-tabs .banners-tabs .tab-content-inner>a:hover,
        .dokan-store-support-and-follow-wrap .dokan-btn:hover {
          color: #fff;
          background-color: #000000;
          border-color: #000000;
        }

        .widget_price_filter .price_slider_amount .button:focus, .widget_price_filter .price_slider_amount .button.focus,
        .dropdown-menu-mini-cart .wc-forward.checkout:focus,
        .dropdown-menu-mini-cart .wc-forward.checkout.focus,
        table.cart .actions .checkout-button:focus,
        table.cart .actions .checkout-button.focus,
        .customer-login-form .button:focus,
        .customer-login-form .button.focus,
        .btn-primary:focus,
        .btn-primary.focus,
        input[type="submit"]:focus,
        input[type="submit"].focus,
        input.dokan-btn-theme[type="submit"]:focus,
        input.dokan-btn-theme[type="submit"].focus,
        a.dokan-btn-theme:focus,
        a.dokan-btn-theme.focus, .dokan-btn-theme:focus, .dokan-btn-theme.focus,
        .sign-in-button:focus,
        .products-carousel-banner-vertical-tabs .banners-tabs .tab-content-inner>a:focus,
        .dokan-store-support-and-follow-wrap .dokan-btn:focus {
          color: #fff;
          background-color: #000000;
          border-color: #000000;
        }

        .widget_price_filter .price_slider_amount .button:active, .widget_price_filter .price_slider_amount .button.active, .open > .widget_price_filter .price_slider_amount .button.dropdown-toggle,
        .dropdown-menu-mini-cart .wc-forward.checkout:active,
        .dropdown-menu-mini-cart .wc-forward.checkout.active, .open >
        .dropdown-menu-mini-cart .wc-forward.checkout.dropdown-toggle,
        table.cart .actions .checkout-button:active,
        table.cart .actions .checkout-button.active, .open >
        table.cart .actions .checkout-button.dropdown-toggle,
        .customer-login-form .button:active,
        .customer-login-form .button.active, .open >
        .customer-login-form .button.dropdown-toggle,
        .btn-primary:active,
        .btn-primary.active, .open >
        .btn-primary.dropdown-toggle,
        input[type="submit"]:active,
        input[type="submit"].active, .open >
        input[type="submit"].dropdown-toggle,
        input.dokan-btn-theme[type="submit"]:active,
        input.dokan-btn-theme[type="submit"].active, .open >
        input.dokan-btn-theme[type="submit"].dropdown-toggle,
        a.dokan-btn-theme:active,
        a.dokan-btn-theme.active, .open >
        a.dokan-btn-theme.dropdown-toggle, .dokan-btn-theme:active, .dokan-btn-theme.active, .open > .dokan-btn-theme.dropdown-toggle {
          color: #ffffff;
          background-color: #000000;
          border-color: #000000;
          background-image: none;
        }

        .widget_price_filter .price_slider_amount .button:active:hover, .widget_price_filter .price_slider_amount .button:active:focus, .widget_price_filter .price_slider_amount .button:active.focus, .widget_price_filter .price_slider_amount .button.active:hover, .widget_price_filter .price_slider_amount .button.active:focus, .widget_price_filter .price_slider_amount .button.active.focus, .open > .widget_price_filter .price_slider_amount .button.dropdown-toggle:hover, .open > .widget_price_filter .price_slider_amount .button.dropdown-toggle:focus, .open > .widget_price_filter .price_slider_amount .button.dropdown-toggle.focus,
        .dropdown-menu-mini-cart .wc-forward.checkout:active:hover,
        .dropdown-menu-mini-cart .wc-forward.checkout:active:focus,
        .dropdown-menu-mini-cart .wc-forward.checkout:active.focus,
        .dropdown-menu-mini-cart .wc-forward.checkout.active:hover,
        .dropdown-menu-mini-cart .wc-forward.checkout.active:focus,
        .dropdown-menu-mini-cart .wc-forward.checkout.active.focus, .open >
        .dropdown-menu-mini-cart .wc-forward.checkout.dropdown-toggle:hover, .open >
        .dropdown-menu-mini-cart .wc-forward.checkout.dropdown-toggle:focus, .open >
        .dropdown-menu-mini-cart .wc-forward.checkout.dropdown-toggle.focus,
        table.cart .actions .checkout-button:active:hover,
        table.cart .actions .checkout-button:active:focus,
        table.cart .actions .checkout-button:active.focus,
        table.cart .actions .checkout-button.active:hover,
        table.cart .actions .checkout-button.active:focus,
        table.cart .actions .checkout-button.active.focus, .open >
        table.cart .actions .checkout-button.dropdown-toggle:hover, .open >
        table.cart .actions .checkout-button.dropdown-toggle:focus, .open >
        table.cart .actions .checkout-button.dropdown-toggle.focus,
        .customer-login-form .button:active:hover,
        .customer-login-form .button:active:focus,
        .customer-login-form .button:active.focus,
        .customer-login-form .button.active:hover,
        .customer-login-form .button.active:focus,
        .customer-login-form .button.active.focus, .open >
        .customer-login-form .button.dropdown-toggle:hover, .open >
        .customer-login-form .button.dropdown-toggle:focus, .open >
        .customer-login-form .button.dropdown-toggle.focus,
        .btn-primary:active:hover,
        .btn-primary:active:focus,
        .btn-primary:active.focus,
        .btn-primary.active:hover,
        .btn-primary.active:focus,
        .btn-primary.active.focus, .open >
        .btn-primary.dropdown-toggle:hover, .open >
        .btn-primary.dropdown-toggle:focus, .open >
        .btn-primary.dropdown-toggle.focus,
        input[type="submit"]:active:hover,
        input[type="submit"]:active:focus,
        input[type="submit"]:active.focus,
        input[type="submit"].active:hover,
        input[type="submit"].active:focus,
        input[type="submit"].active.focus, .open >
        input[type="submit"].dropdown-toggle:hover, .open >
        input[type="submit"].dropdown-toggle:focus, .open >
        input[type="submit"].dropdown-toggle.focus,
        input.dokan-btn-theme[type="submit"]:active:hover,
        input.dokan-btn-theme[type="submit"]:active:focus,
        input.dokan-btn-theme[type="submit"]:active.focus,
        input.dokan-btn-theme[type="submit"].active:hover,
        input.dokan-btn-theme[type="submit"].active:focus,
        input.dokan-btn-theme[type="submit"].active.focus, .open >
        input.dokan-btn-theme[type="submit"].dropdown-toggle:hover, .open >
        input.dokan-btn-theme[type="submit"].dropdown-toggle:focus, .open >
        input.dokan-btn-theme[type="submit"].dropdown-toggle.focus,
        a.dokan-btn-theme:active:hover,
        a.dokan-btn-theme:active:focus,
        a.dokan-btn-theme:active.focus,
        a.dokan-btn-theme.active:hover,
        a.dokan-btn-theme.active:focus,
        a.dokan-btn-theme.active.focus, .open >
        a.dokan-btn-theme.dropdown-toggle:hover, .open >
        a.dokan-btn-theme.dropdown-toggle:focus, .open >
        a.dokan-btn-theme.dropdown-toggle.focus, .dokan-btn-theme:active:hover, .dokan-btn-theme:active:focus, .dokan-btn-theme:active.focus, .dokan-btn-theme.active:hover, .dokan-btn-theme.active:focus, .dokan-btn-theme.active.focus, .open > .dokan-btn-theme.dropdown-toggle:hover, .open > .dokan-btn-theme.dropdown-toggle:focus, .open > .dokan-btn-theme.dropdown-toggle.focus {
          color: #ffffff;
          background-color: #00263e;
          border-color: #001d2f;
        }

        .widget_price_filter .price_slider_amount .button.disabled:focus, .widget_price_filter .price_slider_amount .button.disabled.focus, .widget_price_filter .price_slider_amount .button:disabled:focus, .widget_price_filter .price_slider_amount .button:disabled.focus,
        .dropdown-menu-mini-cart .wc-forward.checkout.disabled:focus,
        .dropdown-menu-mini-cart .wc-forward.checkout.disabled.focus,
        .dropdown-menu-mini-cart .wc-forward.checkout:disabled:focus,
        .dropdown-menu-mini-cart .wc-forward.checkout:disabled.focus,
        table.cart .actions .checkout-button.disabled:focus,
        table.cart .actions .checkout-button.disabled.focus,
        table.cart .actions .checkout-button:disabled:focus,
        table.cart .actions .checkout-button:disabled.focus,
        .customer-login-form .button.disabled:focus,
        .customer-login-form .button.disabled.focus,
        .customer-login-form .button:disabled:focus,
        .customer-login-form .button:disabled.focus,
        .btn-primary.disabled:focus,
        .btn-primary.disabled.focus,
        .btn-primary:disabled:focus,
        .btn-primary:disabled.focus,
        input[type="submit"].disabled:focus,
        input[type="submit"].disabled.focus,
        input[type="submit"]:disabled:focus,
        input[type="submit"]:disabled.focus,
        input.dokan-btn-theme[type="submit"].disabled:focus,
        input.dokan-btn-theme[type="submit"].disabled.focus,
        input.dokan-btn-theme[type="submit"]:disabled:focus,
        input.dokan-btn-theme[type="submit"]:disabled.focus,
        a.dokan-btn-theme.disabled:focus,
        a.dokan-btn-theme.disabled.focus,
        a.dokan-btn-theme:disabled:focus,
        a.dokan-btn-theme:disabled.focus, .dokan-btn-theme.disabled:focus, .dokan-btn-theme.disabled.focus, .dokan-btn-theme:disabled:focus, .dokan-btn-theme:disabled.focus {
          background-color: #003a5e;
          border-color: #003a5e;
        }

        .widget_price_filter .price_slider_amount .button.disabled:hover, .widget_price_filter .price_slider_amount .button:disabled:hover,
        .dropdown-menu-mini-cart .wc-forward.checkout.disabled:hover,
        .dropdown-menu-mini-cart .wc-forward.checkout:disabled:hover,
        table.cart .actions .checkout-button.disabled:hover,
        table.cart .actions .checkout-button:disabled:hover,
        .customer-login-form .button.disabled:hover,
        .customer-login-form .button:disabled:hover,
        .btn-primary.disabled:hover,
        .btn-primary:disabled:hover,
        input[type="submit"].disabled:hover,
        input[type="submit"]:disabled:hover,
        input.dokan-btn-theme[type="submit"].disabled:hover,
        input.dokan-btn-theme[type="submit"]:disabled:hover,
        a.dokan-btn-theme.disabled:hover,
        a.dokan-btn-theme:disabled:hover, .dokan-btn-theme.disabled:hover, .dokan-btn-theme:disabled:hover {
          background-color: #003a5e;
          border-color: #003a5e;
        }

        .navbar-primary .navbar-nav > .menu-item > a:hover,
        .navbar-primary .navbar-nav > .menu-item > a:focus,
        .electro-navbar-primary .nav>.menu-item>a:focus,
        .electro-navbar-primary .nav>.menu-item>a:hover  {
            background-color: #003556;
        }

        .navbar-primary .navbar-nav > .menu-item > a {
            border-color: #003556;
        }

        .full-color-background .navbar-primary,
        .header-v4 .electro-navbar-primary,
        .header-v4 .electro-navbar-primary {
            border-top-color: #003556;
        }

        .full-color-background .top-bar .nav-inline .menu-item+.menu-item:before {
            color: #003556;
        }

        .electro-navbar-primary .nav>.menu-item+.menu-item>a,
        .home-mobile-v2-features-block .features-list .feature+.feature .media {
            border-left-color: #003556;
        }

        .header-v5 .vertical-menu .list-group-item>.dropdown-menu {
            border-top-color: #003a5e;
        }

        .single-product div.thumbnails-all .synced a,
        .woocommerce-product-gallery .flex-control-thumbs li img.flex-active,
        .columns-6-1>ul.products.product-main-6-1 .flex-control-thumbs li img.flex-active,
        .products-2-1-2 .nav-link:hover::after,
        .products-4-1-4 .nav-link:hover::after,
        .section-onsale-product-carousel .onsale-product-carousel .onsale-product .onsale-product-thumbnails .images .thumbnails a.current,
        .dokan-elector-style-active.store-v1 .profile-frame + .dokan-store-tabs > ul li.active a,
        .dokan-elector-style-active.store-v5 .profile-frame + .dokan-store-tabs > ul li.active a {
            border-bottom-color: #003a5e;
        }

        .home-v1-slider .btn-primary:hover,
        .home-v2-slider .btn-primary:hover,
        .home-v3-slider .btn-primary:hover {
            background-color: #003556 !important;
        }


        /*........Dokan.......*/

        .dokan-dashboard .dokan-dash-sidebar ul.dokan-dashboard-menu li.active,
        .dokan-dashboard .dokan-dash-sidebar ul.dokan-dashboard-menu li:hover,
        .dokan-dashboard .dokan-dash-sidebar ul.dokan-dashboard-menu li:focus,
        .dokan-dashboard .dokan-dash-sidebar ul.dokan-dashboard-menu li.dokan-common-links a:hover,
        .dokan-dashboard .dokan-dash-sidebar ul.dokan-dashboard-menu li.dokan-common-links a:focus,
        .dokan-dashboard .dokan-dash-sidebar ul.dokan-dashboard-menu li.dokan-common-links a.active,
        .dokan-store .pagination-wrap ul.pagination > li a.current,
        .dokan-store .pagination-wrap ul.pagination > li span.current,
        .dokan-dashboard .pagination-wrap ul.pagination > li a.current,
        .dokan-dashboard .pagination-wrap ul.pagination > li span.current,
        .dokan-pagination-container ul.dokan-pagination > li.active > a,
        .dokan-coupon-content .code:hover,
        .dokan-report-wrap ul.dokan_tabs > li.active a::before,
        .dokan-dashboard-header h1.entry-title span.dokan-right a.dokan-btn.dokan-btn-sm {
            background-color: #003a5e;
        }

        .dokan-widget-area .widget .widget-title:after,
        .dokan-report-wrap ul.dokan_tabs > li.active a::after,
        .dokan-dashboard-header h1.entry-title span.dokan-right a.dokan-btn.dokan-btn-sm,
        .dokan-store-sidebar .widget-store-owner .widget-title:after {
            border-color: #003a5e;
        }

        .electro-tabs #tab-seller.electro-tab .tab-content ul.list-unstyled li.seller-name span.details a,
        .dokan-dashboard-header h1.entry-title small a,
        .dokan-orders-content .dokan-orders-area .general-details ul.customer-details li a{
            color: #003a5e;
        }

        .dokan-dashboard-header h1.entry-title small a:hover,
        .dokan-dashboard-header h1.entry-title small a:focus {
            color: #003556;
        }

        .dokan-store-support-and-follow-wrap .dokan-btn {
            color: #ffffff!important;
            background-color: #003a5e!important;
        }

        .dokan-store-support-and-follow-wrap .dokan-btn:hover {
            color: #ebebeb!important;
            background-color: #003556!important;
        }

        .header-v1 .navbar-search .input-group .btn,
        .header-v1 .navbar-search .input-group .hero-action-btn,
        .header-v3 .navbar-search .input-group .btn,
        .header-v3 .navbar-search .input-group .hero-action-btn,
        .header-v6 .navbar-search .input-group .btn,
        .header-v8 .navbar-search .input-group .btn,
        .header-v9 .navbar-search .input-group .btn,
        .header-v10 .navbar-search .input-group .btn,
        .navbar-mini-cart .cart-items-count,
        .navbar-compare .count,
        .navbar-wishlist .count,
        .navbar-primary a[data-bs-toggle=dropdown]::after,
        .navbar-primary .navbar-nav .nav-link,
        .vertical-menu>li.list-group-item>a,
        .vertical-menu>li.list-group-item>span,
        .vertical-menu>li.list-group-item.dropdown>a[data-bs-toggle=dropdown-hover],
        .vertical-menu>li.list-group-item.dropdown>a[data-bs-toggle=dropdown],
        .departments-menu>.nav-item .nav-link,
        .customer-login-form .button,
        .dropdown-menu-mini-cart .wc-forward.checkout,
        .widget_price_filter .price_slider_amount .button,
        input[type=submit],
        table.cart .actions .checkout-button,
        .pagination ul.page-numbers>li a.current,
        .pagination ul.page-numbers>li span.current,
        .woocommerce-pagination ul.page-numbers>li a.current,
        .woocommerce-pagination ul.page-numbers>li span.current,
        .footer-newsletter .newsletter-title::before,
        .footer-newsletter .newsletter-marketing-text,
        .footer-newsletter .newsletter-title,
        .top-bar-v3 .nav-inline .menu-item>a,
        .top-bar-v3 .menu-item.customer-support.menu-item>a i,
        .top-bar-v3 .additional-links-label,
        .full-color-background .top-bar .nav-inline .menu-item>a,
        .full-color-background .top-bar .nav-inline .menu-item+.menu-item:before,
        .full-color-background .header-v1 .navbar-nav .nav-link,
        .full-color-background .header-v3 .navbar-nav .nav-link,
        .full-color-background .navbar-primary .navbar-nav>.menu-item>a,
        .full-color-background .navbar-primary .navbar-nav>.menu-item>a:focus,
        .full-color-background .navbar-primary .navbar-nav>.menu-item>a:hover,
        .woocommerce-info,
        .woocommerce-noreviews,
        p.no-comments,
        .woocommerce-info a,
        .woocommerce-info button,
        .woocommerce-noreviews a,
        .woocommerce-noreviews button,
        p.no-comments a,
        p.no-comments button,
        .navbar-primary .navbar-nav > .menu-item >a,
        .navbar-primary .navbar-nav > .menu-item >a:hover,
        .navbar-primary .navbar-nav > .menu-item >a:focus,
        .demo_store,
        .header-v5 .masthead .header-icon>a,
        .header-v4 .masthead .header-icon>a,
        .departments-menu-v2-title,
        .departments-menu-v2-title:focus,
        .departments-menu-v2-title:hover,
        .electro-navbar .header-icon>a,
        .section-onsale-product .savings,
        .section-onsale-product-carousel .savings,
        .electro-navbar-primary .nav>.menu-item>a,
        .header-icon .header-icon-counter,
        .header-v6 .navbar-search .input-group .btn,
        .products-carousel-tabs-v5 header .nav-link.active,
        #payment .place-order .button,
        .deal-products-with-featured header h2,
        .deal-products-with-featured ul.products>li.product.product-featured .savings,
        .deal-products-with-featured header h2:after,
        .deal-products-with-featured header .deal-countdown-timer,
        .deal-products-with-featured header .deal-countdown-timer:before,
        .product-categories-list-with-header.v2 header .caption .section-title,
        .home-mobile-v2-features-block .features-list .media-left i,
        .home-mobile-v2-features-block .features-list .feature,
        .handheld-header-v2 .handheld-header-links .columns-3 a,
        .handheld-header-v2 .off-canvas-navigation-wrapper .navbar-toggler,
        .handheld-header-v2 .off-canvas-navigation-wrapper button,
        .handheld-header-v2 .off-canvas-navigation-wrapper.toggled .navbar-toggler,
        .handheld-header-v2 .off-canvas-navigation-wrapper.toggled button,
        .mobile-header-v2 .handheld-header-links .columns-3 a,
        .mobile-header-v2 .off-canvas-navigation-wrapper .navbar-toggler,
        .mobile-header-v2 .off-canvas-navigation-wrapper button,
        .mobile-header-v2 .off-canvas-navigation-wrapper.toggled .navbar-toggler,
        .mobile-header-v2 .off-canvas-navigation-wrapper.toggled button,
        .mobile-handheld-department ul.nav li a,
        .header-v5 .handheld-header-v2 .handheld-header-links .cart .count,
        .yith-wcqv-button,
        .home-vertical-nav.departments-menu-v2 .vertical-menu-title a,
        .products-carousel-with-timer .deal-countdown-timer,
        .demo_store a,
        div.wpforms-container-full .wpforms-form input[type=submit],
        div.wpforms-container-full .wpforms-form button[type=submit],
        div.wpforms-container-full .wpforms-form .wpforms-page-button,
        .aws-search-form:not(.aws-form-active):not(.aws-processing) .aws-search-clear::after {
            color: #ffffff;
        }

        .woocommerce-info a:focus,
        .woocommerce-info a:hover,
        .woocommerce-info button:focus,
        .woocommerce-info button:hover,
        .woocommerce-noreviews a:focus,
        .woocommerce-noreviews a:hover,
        .woocommerce-noreviews button:focus,
        .woocommerce-noreviews button:hover,
        p.no-comments a:focus,
        p.no-comments a:hover,
        p.no-comments button:focus,
        p.no-comments button:hover,
        .vertical-menu>li.list-group-item.dropdown>a[data-bs-toggle=dropdown-hover]:hover,
        .vertical-menu>li.list-group-item.dropdown>a[data-bs-toggle=dropdown]:hover,
        .vertical-menu>li.list-group-item.dropdown>a[data-bs-toggle=dropdown-hover]:focus,
        .vertical-menu>li.list-group-item.dropdown>a[data-bs-toggle=dropdown]:focus {
            color: #f5f5f5;
        }

        .full-color-background .header-logo path {
            fill:#ffffff;
        }

        .home-v1-slider .btn-primary,
        .home-v2-slider .btn-primary,
        .home-v3-slider .btn-primary,
        .home-v1-slider .btn-primary:hover,
        .home-v2-slider .btn-primary:hover,
        .home-v3-slider .btn-primary:hover,
        .handheld-navigation-wrapper .stuck .navbar-toggler,
        .handheld-navigation-wrapper .stuck button,
        .handheld-navigation-wrapper.toggled .stuck .navbar-toggler,
        .handheld-navigation-wrapper.toggled .stuck button,
        .header-v5 .masthead .header-icon>a:hover,
        .header-v5 .masthead .header-icon>a:focus,
        .header-v5 .masthead .header-logo-area .navbar-toggler,
        .header-v4 .off-canvas-navigation-wrapper .navbar-toggler,
        .header-v4 .off-canvas-navigation-wrapper button,
        .header-v4 .off-canvas-navigation-wrapper.toggled .navbar-toggler,
        .header-v4 .off-canvas-navigation-wrapper.toggled button,
        .products-carousel-tabs-v5 header .nav-link.active,
        .products-carousel-tabs-with-deal header .nav-link.active {
            color: #ffffff !important;
        }

        @media (max-width: 575.98px) {
          .electro-wc-product-gallery .electro-wc-product-gallery__image.flex-active-slide a {
                background-color: #003a5e !important;
            }
        }

        @media (max-width: 767px) {
            .show-nav .nav .nav-item.active .nav-link {
                color: #ffffff;
            }
        }</style> <style type="text/css" id="wp-custom-css">
			@media (max-width:800px) {.cart 
	{text-align: center;}}
.wc-tabs>li {
    margin-right: 20px;}
.wc-tabs>li+li {margin-left: 0px;}
.wc-tabs>li.active a::after {width: 65%;}
.page .entry-header h1 {
	font-size: 2.0em;
}
.footer-social-icons .social-icons a {
	color: #333e48;
	font-size: 2.1em;
}
.tinkoff_credit {
	text-align: center;
	padding-top: 20px;
  padding-bottom: 30px;
}
.tinkoff_credit_submit {
	font-size: 24px;
}
.tinkoff_credit_wrapper {padding-bottom: 20px;}

.entry-title {
	color: #163e50;
}
.h1, .h2, .h3, .h4, .h5, .h6, h1, h2, h3, h4, h5, h6 {
	color: #163e50;
}
.button-menu {
	background-color: #e7e7e7;
}
.wc-tabs {display: inherit;}
.wc-tabs>li a {padding-bottom: 10px;}
.wc-tabs>li {margin-bottom: 10px;}
.wc-tabs li+li {padding-left: 0px;}
.departments-menu-v2-title {
	color: #333e48;
}
.departments-menu-v2-title:focus, .departments-menu-v2-title:hover {
  color: #29323a;	
}
a {
  color: #003a5e;
  font-weight: 600;
}
.alignright {
	float: right;
margin: 0px 0px 20px 20px;}
.woocommerce-notices-wrapper {display: none;}
/*.blog-grid:not(.single-post) article.post {width: 100%}*/
.handheld-footer .handheld-footer-bar {
    background-color: #f2f2f2;
}
.handheld-footer .handheld-footer-bar .footer-call-us .call-us-number, .handheld-footer .handheld-footer-bar .footer-call-us .call-us-number a {
	font-size: 18px;
	color: #333e48;
}
.handheld-footer .handheld-footer-bar .footer-call-us .call-us-text {
	color: #333e48;
}
.owl-item>.product .price, .products>.product .price {
    font-size: 1em;
}
.table-specificatio {
	overflow-y: scroll;
}		</style>

<style>
			</style>

<noscript><style> .wpb_animate_when_almost_visible { opacity: 1; }</style></noscript></head>
<body class="product-template-default single single-product postid-11405 theme-electro woocommerce woocommerce-page woocommerce-no-js group-blog full-width normal wpb-js-composer js-comp-ver-6.5.0 vc_responsive elementor-default elementor-template-full-width elementor-kit-23221 elementor-page-34574">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;"><defs><filter id="wp-duotone-dark-grayscale"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB"><feFuncR type="table" tableValues="0 0.49803921568627" /><feFuncG type="table" tableValues="0 0.49803921568627" /><feFuncB type="table" tableValues="0 0.49803921568627" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;"><defs><filter id="wp-duotone-grayscale"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB"><feFuncR type="table" tableValues="0 1" /><feFuncG type="table" tableValues="0 1" /><feFuncB type="table" tableValues="0 1" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;"><defs><filter id="wp-duotone-purple-yellow"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB"><feFuncR type="table" tableValues="0.54901960784314 0.98823529411765" /><feFuncG type="table" tableValues="0 1" /><feFuncB type="table" tableValues="0.71764705882353 0.25490196078431" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;"><defs><filter id="wp-duotone-blue-red"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB"><feFuncR type="table" tableValues="0 1" /><feFuncG type="table" tableValues="0 0.27843137254902" /><feFuncB type="table" tableValues="0.5921568627451 0.27843137254902" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;"><defs><filter id="wp-duotone-midnight"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB"><feFuncR type="table" tableValues="0 0" /><feFuncG type="table" tableValues="0 0.64705882352941" /><feFuncB type="table" tableValues="0 1" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;"><defs><filter id="wp-duotone-magenta-yellow"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB"><feFuncR type="table" tableValues="0.78039215686275 1" /><feFuncG type="table" tableValues="0 0.94901960784314" /><feFuncB type="table" tableValues="0.35294117647059 0.47058823529412" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;"><defs><filter id="wp-duotone-purple-green"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB"><feFuncR type="table" tableValues="0.65098039215686 0.40392156862745" /><feFuncG type="table" tableValues="0 1" /><feFuncB type="table" tableValues="0.44705882352941 0.4" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;"><defs><filter id="wp-duotone-blue-orange"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB"><feFuncR type="table" tableValues="0.098039215686275 1" /><feFuncG type="table" tableValues="0 0.66274509803922" /><feFuncB type="table" tableValues="0.84705882352941 0.41960784313725" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg> 
<script type="text/javascript">
        (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
            m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
        (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

        ym(55570990, "init", {
            clickmap:true,
            trackLinks:true,
            accurateTrackBounce:true,
            webvisor:true,
            ecommerce:"dataLayer"
        });
    </script>
<noscript><div><img src="https://mc.yandex.ru/watch/55570990" style="position:absolute; left:-9999px;" alt="" /></div></noscript>

<div class="off-canvas-wrapper w-100 position-relative">
<div id="page" class="hfeed site">
<a class="skip-link screen-reader-text visually-hidden" href="#site-navigation">Перейти к навигации</a>
<a class="skip-link screen-reader-text visually-hidden" href="#content">Перейти к содержанию</a>
<header id="masthead" class="site-header header-v5">
<div class="stick-this">
<div class="container hidden-lg-down d-none d-xl-block">
<div class="masthead row align-items-center"><div class="header-logo-area d-flex justify-content-between align-items-center"> <div class="header-site-branding">
<a href="https://aeromotus.ru/" class="header-logo-link">
<img alt="AEROMOTUS" width="269" height="99" data-src="https://aeromotus.ru/wp-content/uploads/2021/11/logo-new.svg" class="img-header-logo lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img  alt="AEROMOTUS"  width="269" height="99" data-src="https://aeromotus.ru/wp-content/uploads/2021/11/logo-new.svg" class="img-header-logo lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img src="https://aeromotus.ru/wp-content/uploads/2021/11/logo-new.svg" alt="AEROMOTUS" class="img-header-logo" width="269" height="99" /></noscript></noscript>
</a>
</div>
<div class="off-canvas-navigation-wrapper ">
<div class="off-canvas-navbar-toggle-buttons clearfix">
<button class="navbar-toggler navbar-toggle-hamburger" type="button">
<i class="ec ec-menu"></i>
</button>
<button class="navbar-toggler navbar-toggle-close" type="button">
<i class="ec ec-close-remove"></i>
</button>
</div>
<div class="off-canvas-navigation">
<ul class="nav nav-inline yamm"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-2538"><a title="Главная" href="https://aeromotus.ru/">Главная</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-2539 dropdown"><a title="Каталог" href="#" data-bs-toggle="dropdown" class="dropdown-toggle" aria-haspopup="true">Каталог</a>
<ul role="menu" class=" dropdown-menu">
<li class="menu-item menu-item-type-post_type_archive menu-item-object-product menu-item-2541"><a title="Все товары" href="https://aeromotus.ru/shop/">Все товары</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_tag menu-item-11358"><a title="УЛЕТНЫЕ ЦЕНЫ" href="https://aeromotus.ru/product-tag/uletnye-czeny/">УЛЕТНЫЕ ЦЕНЫ</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-2542 dropdown-submenu"><a title="БПЛА, Квадрокоптеры" href="#" data-bs-toggle="dropdown" class="dropdown-toggle" aria-haspopup="true">БПЛА, Квадрокоптеры</a>
<ul role="menu" class=" dropdown-menu">
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_tag menu-item-2543"><a title="Все БПЛА" href="https://aeromotus.ru/product-tag/bpla/">Все БПЛА</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-9596"><a title="Parrot" href="https://aeromotus.ru/product-category/parrot/">Parrot</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2544"><a title="DJI Mavic Enterprise" href="https://aeromotus.ru/product-category/dji-mavic/mavic-enterprise/">DJI Mavic Enterprise</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2545"><a title="DJI Inspire" href="https://aeromotus.ru/product-category/inspire/">DJI Inspire</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2546"><a title="DJI Phantom" href="https://aeromotus.ru/product-category/dji-phantom/">DJI Phantom</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat current-product-ancestor current-menu-parent current-product-parent menu-item-2548"><a title="DJI Matrice" href="https://aeromotus.ru/product-category/matrice-seria/">DJI Matrice</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2549"><a title="DJI Agras" href="https://aeromotus.ru/product-category/dji-agras/">DJI Agras</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2547"><a title="DJI Phantom 4 RTK" href="https://aeromotus.ru/product-category/phantom-4-rtk/">DJI Phantom 4 RTK</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2550"><a title="DJI Mavic" href="https://aeromotus.ru/product-category/dji-mavic/">DJI Mavic</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-2552 dropdown-submenu"><a title="Аксессуары и запчасти" href="#" data-bs-toggle="dropdown" class="dropdown-toggle" aria-haspopup="true">Аксессуары и запчасти</a>
<ul role="menu" class=" dropdown-menu">
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat current-product-ancestor menu-item-2553"><a title="Все аксессуары и запчасти" href="https://aeromotus.ru/product-category/aksessuary-i-zapchasti/">Все аксессуары и запчасти</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_tag menu-item-2554"><a title="Аккумуляторы" href="https://aeromotus.ru/product-tag/akkumulyatory/">Аккумуляторы</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-2555 dropdown-submenu"><a title="Подвесы и камеры" href="#" data-bs-toggle="dropdown" class="dropdown-toggle" aria-haspopup="true">Подвесы и камеры</a>
<ul role="menu" class=" dropdown-menu">
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2557"><a title="Все подвесы и камеры" href="https://aeromotus.ru/product-category/podvesy-i-kamery/">Все подвесы и камеры</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-10079"><a title="MicaSense" href="https://aeromotus.ru/product-category/micasense/">MicaSense</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2558"><a title="DJI Zenmuse" href="https://aeromotus.ru/product-category/zenmuse/">DJI Zenmuse</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2559"><a title="Программное обеспечение" href="https://aeromotus.ru/product-category/soft/">Программное обеспечение</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2564"><a title="Специализированные решения" href="https://aeromotus.ru/product-category/individualnye-resheniya/">Специализированные решения</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2566"><a title="Программное обеспечение" href="https://aeromotus.ru/product-category/soft/">Программное обеспечение</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2562"><a title="О НАС" href="https://aeromotus.ru/o-nas/">О НАС</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-43751"><a title="Блог" href="https://aeromotus.ru/home/blog/">Блог</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-40072"><a title="Кейсы" href="https://aeromotus.ru/category/nashi-kejsy/">Кейсы</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-45894"><a title="Обучение" href="https://aeromotus.ru/product-category/obuchenie/">Обучение</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-50103"><a title="Вебинары" href="https://aeromotus.ru/webinar/">Вебинары</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-50104"><a title="Лекции" href="https://aeromotus.ru/obrazovatelnye-vstrechi/">Лекции</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2563"><a title="Контакты" href="https://aeromotus.ru/kontakty/">Контакты</a></li>
<li class="button-menu menu-item menu-item-type-custom menu-item-object-custom menu-item-23930"><a title="Позвоните нам" href="tel:+74999388909">Позвоните нам</a></li>
</ul> </div>
</div>
</div>
<form class="navbar-search col" method="get" action="https://aeromotus.ru/" autocomplete="off">
<label class="sr-only screen-reader-text visually-hidden" for="search">Поиск:</label>
<div class="input-group">
<div class="input-search-field">
<input type="text" id="search" class="form-control search-field product-search-field" dir="ltr" value="" name="s" placeholder="Поиск товара" autocomplete="off" />
</div>
<div class="input-group-btn">
<input type="hidden" id="search-param" name="post_type" value="product" />
<button type="submit" class="btn btn-secondary"><i class="ec ec-search"></i></button>
</div>
</div>
</form>
<div class="aeromotus-header-section">
<div class="aeromotus-header-tagline">
<span>Официальный дилер</span>
<svg width="42" height="24" viewBox="0 0 42 24" xmlns="http://www.w3.org/2000/svg">
<path d="M32.5484163 4.8813551c-.7034221 2.6137997-1.4036831 5.2283432-2.0896266 7.8467915-.3430647 1.3090383-.6798073 2.6190062-1.0747501 3.9142846-.3836003 1.2584617-.8547797 2.6017134-1.5414669 3.7447046-.7162521 1.1928239-1.6437355 2.124212-2.9272995 2.720531-.5132025.2381929-1.0390491.4016367-1.5907417.5185948-.7828198.1658611-1.5691724.2341021-2.3646362.2791003-1.9698794.111008-6.1487607.094459-8.1180823.094459l1.2073274-4.4745306c.9139095 0 1.8276331.0031611 2.7413566-.0221272.8817414-.0245444 1.8519916-.0717739 2.720345-.2770549.9509122-.224991 1.6684659-.6110085 2.296953-1.384717.5725183-.7047237.9574201-1.5840478 1.2727794-2.4133533.5760511-1.5145051 1.1658621-3.6829715 1.5816305-5.2424748.4702497-1.7653422.9222769-3.535147 1.3778371-5.304208zm8.1355423-.0000372l-3.51209 13.0169346h-6.5081884l3.5119041-13.0169346h6.5083743zM19.2211801 0h6.5083744c-.6818527 2.5409101-1.3627757 5.0820061-2.052438 7.6208709-.4806625 1.768689-.957978 3.538122-1.4797339 5.2954686-.2275941.7660848-.4548164 1.5299384-.7530688 2.2737101-.2396805.5974346-.5076242 1.1290455-1.0029762 1.5754944-.3700264.3333957-.7735225.540722-1.2434003.6885467-.6045005.1902196-1.2155089.2599482-1.8400912.3110825-.8982903.0736334-1.7967665.0924136-2.6965444.1069172-2.0693588.0332838-5.8272653.0286352-7.8966242.0197099-.7435858-.0033469-1.4871715-.0078096-2.2307573-.0213834-.5390485-.009669-1.0775392-.0230569-1.615844-.0567126-.3594277-.022685-.7160662-.0528078-1.0712172-.1182597-.240982-.0442544-.4730388-.1037562-.6991454-.2024919-.7447014-.3254001-1.124211-.9758284-1.1463382-1.7679453-.01283-.4533289.0660098-.8850883.15675-1.3235418.1288584-.6210493.2893271-1.2335453.4483083-1.8467851.3034589-1.1716264.8588704-3.3333989 1.2917455-4.4713696.33916-.8917823.7870964-1.7792878 1.6381572-2.3438106.475828-.3155451.9758285-.4832656 1.5271493-.5942736.4087025-.0821867.8194505-.1256974 1.2339172-.156564.694125-.0515061 1.3888078-.0676831 2.0842343-.0799554.9882867-.0172927 1.9765733-.0210115 2.96486-.0239866l2.465301-.003347h2.4651616l-.8780225 3.2541872c-1.4652302 0-2.9300886-.0040908-4.3953189.0044626-.4276687.0026032-.8547796-.0005578-1.2820764.0273336-.1517295.009855-.299926.01971-.446635.0710302-.1930087.0669395-.2883975.1881743-.3731874.3622169-.124024.2547418-.195612.5234293-.2746377.7923028-.120677.410562-.2324287.8235412-.3443663 1.2367064-.1723691.6364826-.3447382 1.2729652-.508368 1.9118651-.0604314.2365194-.1197472.4730389-.1706956.7117896-.035887.1673486-.068241.3341394-.0842321.504835-.0174787.1866867-.022871.4109339.0901823.5842327.1149127.175902.309223.2168094.4905174.2430274.2049091.0299368.4101901.0364448.6162149.0425809.3373004.0102269.674601.0117144 1.0119014.0133879.9228347.0044626 1.8456695.0046486 2.7685042-.0011156.4252515-.0026032.8501311-.0055783 1.2750107-.0226851.2926741-.0117144.5816295-.0217553.869841-.0914839.2190408-.0529937.3902942-.1362962.5384907-.3153592.1002232-.1212348.1656752-.2556715.2255488-.3984757.1487543-.3540353.2526964-.7205288.3611011-1.0868364.4159544-1.4051707.7906294-2.821126 1.1734859-4.235408l1.1434095-4.2441473L19.2211801 0h6.5083744z" fill="#FFF" fill-rule="evenodd" />
</svg>
</div>
<div class="aeromotus-header-phone">
<a href="tel:+74999388909">
<i class="ec ec-support"></i>
<span>+7 (499) 938-89-09</span>
</a>
</div>
</div>
<div class="header-icons col-auto d-flex justify-content-end align-items-center"><div class="header-icon header-icon__cart animate-dropdown dropdown" data-toggle="tooltip" data-placement="top" data-title="Cart">
<a href="https://aeromotus.ru/cart/" data-toggle="dropdown">
<i class="ec ec-shopping-bag"></i>
<span class="cart-items-count count header-icon-counter">0</span>
<span class="cart-items-total-price total-price"><span class="woocommerce-Price-amount amount"><bdi>0&nbsp;<span class="woocommerce-Price-currencySymbol">&#8381;</span></bdi></span></span>
</a>
<ul class="dropdown-menu dropdown-menu-mini-cart">
<li>
<div class="widget_shopping_cart_content">
<div class="woocommerce-mini-cart__empty-message">Нет товаров в корзине.</div>
</div>
</li>
</ul> </div></div></div><div class="electro-navigation-v5">
<div class="container">
<div class="electro-navigation row">
<div class="departments-menu-v2">
<div class="dropdown 
			">
<a href="#" class="departments-menu-v2-title" data-bs-toggle="dropdown">
<span>Меню<i class="departments-menu-v2-icon ec ec-arrow-down-search"></i></span>
</a>
<ul id="menu-menyu-vse-razdely" class="dropdown-menu yamm"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-1740"><a title="Главная" href="https://aeromotus.ru/">Главная</a></li>
<li class="menu-item menu-item-type-post_type_archive menu-item-object-product menu-item-has-children menu-item-2134 dropdown"><a title="Все товары" href="https://aeromotus.ru/shop/" data-bs-toggle="dropdown-hover" class="dropdown-toggle" aria-haspopup="true">Все товары</a>
<ul role="menu" class=" dropdown-menu">
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_tag menu-item-11362"><a title="УЛЕТНЫЕ ЦЕНЫ" href="https://aeromotus.ru/product-tag/uletnye-czeny/">УЛЕТНЫЕ ЦЕНЫ</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_tag menu-item-has-children menu-item-2135 dropdown-submenu"><a title="БПЛА, Квадрокоптеры" href="https://aeromotus.ru/product-tag/bpla/" data-bs-toggle="dropdown-hover" class="dropdown-toggle" aria-haspopup="true">БПЛА, Квадрокоптеры</a>
<ul role="menu" class=" dropdown-menu">
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-9601"><a title="Parrot" href="https://aeromotus.ru/product-category/parrot/">Parrot</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat current-product-ancestor current-menu-parent current-product-parent menu-item-1747"><a title="DJI Matrice" href="https://aeromotus.ru/product-category/matrice-seria/">DJI Matrice</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-1749"><a title="DJI Inspire" href="https://aeromotus.ru/product-category/inspire/">DJI Inspire</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-1751"><a title="DJI Phantom 4 RTK" href="https://aeromotus.ru/product-category/phantom-4-rtk/">DJI Phantom 4 RTK</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-1750"><a title="DJI Phantom" href="https://aeromotus.ru/product-category/dji-phantom/">DJI Phantom</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-1752"><a title="DJI Mavic Enterprise" href="https://aeromotus.ru/product-category/dji-mavic/mavic-enterprise/">DJI Mavic Enterprise</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-1746"><a title="DJI Mavic" href="https://aeromotus.ru/product-category/dji-mavic/">DJI Mavic</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-1748"><a title="DJI Agras" href="https://aeromotus.ru/product-category/dji-agras/">DJI Agras</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat current-product-ancestor menu-item-has-children menu-item-1741 dropdown-submenu"><a title="Аксессуары и Запчасти" href="https://aeromotus.ru/product-category/aksessuary-i-zapchasti/" data-bs-toggle="dropdown-hover" class="dropdown-toggle" aria-haspopup="true">Аксессуары и Запчасти</a>
<ul role="menu" class=" dropdown-menu">
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_tag menu-item-2137"><a title="Аккумуляторы" href="https://aeromotus.ru/product-tag/akkumulyatory/">Аккумуляторы</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-has-children menu-item-1742 dropdown-submenu"><a title="Подвесы и камеры" href="https://aeromotus.ru/product-category/podvesy-i-kamery/" data-bs-toggle="dropdown-hover" class="dropdown-toggle" aria-haspopup="true">Подвесы и камеры</a>
<ul role="menu" class=" dropdown-menu">
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-1745"><a title="DJI Zenmuse" href="https://aeromotus.ru/product-category/zenmuse/">DJI Zenmuse</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_tag menu-item-13582"><a title="Тепловизионные камеры" href="https://aeromotus.ru/product-tag/teplovye-kamery/">Тепловизионные камеры</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_tag menu-item-13584"><a title="Мультиспектральные камеры" href="https://aeromotus.ru/product-tag/multispektralnye-kamery/">Мультиспектральные камеры</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_tag menu-item-13583"><a title="Мониторинг воздуха" href="https://aeromotus.ru/product-tag/monitoring-vozduha/">Мониторинг воздуха</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_tag menu-item-13585"><a title="Лидары" href="https://aeromotus.ru/product-tag/lidary/">Лидары</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_tag menu-item-13586"><a title="Камеры с зумом" href="https://aeromotus.ru/product-tag/kamery-s-zumom/">Камеры с зумом</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_tag menu-item-13587"><a title="Анализаторы воздушного спектра" href="https://aeromotus.ru/product-tag/analizatory-vozdushnogo-spektra/">Анализаторы воздушного спектра</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-13589"><a title="Все товары раздела Подвесы и Камеры" href="https://aeromotus.ru/product-category/podvesy-i-kamery/">Все товары раздела Подвесы и Камеры</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-1744"><a title="Программное обеспечение" href="https://aeromotus.ru/product-category/soft/">Программное обеспечение</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-17955"><a title="Наши услуги" href="https://aeromotus.ru/nashi-uslugi/">Наши услуги</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1738"><a title="Контакты" href="https://aeromotus.ru/kontakty/">Контакты</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1739"><a title="О Нас" href="https://aeromotus.ru/o-nas/">О Нас</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-43750"><a title="Блог" href="https://aeromotus.ru/home/blog/">Блог</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-1754"><a title="Специализированные решения" href="https://aeromotus.ru/product-category/individualnye-resheniya/">Специализированные решения</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-1743"><a title="Профессиональное оборудование" href="https://aeromotus.ru/product-category/professionalnoe-oborudovanie/">Профессиональное оборудование</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2140"><a title="Программное обеспечение" href="https://aeromotus.ru/product-category/soft/">Программное обеспечение</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1737"><a title="Техническое обслуживание БПЛА" href="https://aeromotus.ru/nashi-uslugi/remont-i-obsluzhivanie-bpla/">Техническое обслуживание БПЛА</a></li>
</ul> </div>
</div>
<div class="secondary-nav-menu col electro-animate-dropdown position-relative">
<ul id="menu-menu-2" class="secondary-nav yamm"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-1731"><a title="Главная" href="https://aeromotus.ru/">Главная</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-45892"><a title="Обучение" href="https://aeromotus.ru/product-category/obuchenie/">Обучение</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-1734"><a title="Софт" href="https://aeromotus.ru/product-category/soft/">Софт</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-45418"><a title="Промышленные решения" target="_blank" href="https://enterprise.aeromotus.ru/">Промышленные решения</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-24422"><a title="Вебинары" href="https://aeromotus.ru/webinar/">Вебинары</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2626"><a title="Оплата и Доставка" href="https://aeromotus.ru/dostavka/">Оплата и Доставка</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1730"><a title="О Нас" href="https://aeromotus.ru/o-nas/">О Нас</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-43752"><a title="Блог" href="https://aeromotus.ru/home/blog/">Блог</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-17115"><a title="Вакансии" href="https://aeromotus.ru/vakansii-2/">Вакансии</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1729"><a title="Контакты" href="https://aeromotus.ru/kontakty/">Контакты</a></li>
</ul> </div>
</div>
</div>
</div>
</div>
<div class="handheld-header-wrap container hidden-xl-up d-xl-none">
<div class="handheld-header-v2 row align-items-center handheld-stick-this ">
<div class="off-canvas-navigation-wrapper ">
<div class="off-canvas-navbar-toggle-buttons clearfix">
<button class="navbar-toggler navbar-toggle-hamburger" type="button">
<i class="ec ec-menu"></i>
</button>
<button class="navbar-toggler navbar-toggle-close" type="button">
<i class="ec ec-close-remove"></i>
</button>
</div>
<div class="off-canvas-navigation">
<ul class="nav nav-inline yamm"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-2538"><a title="Главная" href="https://aeromotus.ru/">Главная</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-2539 dropdown"><a title="Каталог" href="#" data-bs-toggle="dropdown" class="dropdown-toggle" aria-haspopup="true">Каталог</a>
<ul role="menu" class=" dropdown-menu">
<li class="menu-item menu-item-type-post_type_archive menu-item-object-product menu-item-2541"><a title="Все товары" href="https://aeromotus.ru/shop/">Все товары</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_tag menu-item-11358"><a title="УЛЕТНЫЕ ЦЕНЫ" href="https://aeromotus.ru/product-tag/uletnye-czeny/">УЛЕТНЫЕ ЦЕНЫ</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-2542 dropdown-submenu"><a title="БПЛА, Квадрокоптеры" href="#" data-bs-toggle="dropdown" class="dropdown-toggle" aria-haspopup="true">БПЛА, Квадрокоптеры</a>
<ul role="menu" class=" dropdown-menu">
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_tag menu-item-2543"><a title="Все БПЛА" href="https://aeromotus.ru/product-tag/bpla/">Все БПЛА</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-9596"><a title="Parrot" href="https://aeromotus.ru/product-category/parrot/">Parrot</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2544"><a title="DJI Mavic Enterprise" href="https://aeromotus.ru/product-category/dji-mavic/mavic-enterprise/">DJI Mavic Enterprise</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2545"><a title="DJI Inspire" href="https://aeromotus.ru/product-category/inspire/">DJI Inspire</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2546"><a title="DJI Phantom" href="https://aeromotus.ru/product-category/dji-phantom/">DJI Phantom</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat current-product-ancestor current-menu-parent current-product-parent menu-item-2548"><a title="DJI Matrice" href="https://aeromotus.ru/product-category/matrice-seria/">DJI Matrice</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2549"><a title="DJI Agras" href="https://aeromotus.ru/product-category/dji-agras/">DJI Agras</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2547"><a title="DJI Phantom 4 RTK" href="https://aeromotus.ru/product-category/phantom-4-rtk/">DJI Phantom 4 RTK</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2550"><a title="DJI Mavic" href="https://aeromotus.ru/product-category/dji-mavic/">DJI Mavic</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-2552 dropdown-submenu"><a title="Аксессуары и запчасти" href="#" data-bs-toggle="dropdown" class="dropdown-toggle" aria-haspopup="true">Аксессуары и запчасти</a>
<ul role="menu" class=" dropdown-menu">
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat current-product-ancestor menu-item-2553"><a title="Все аксессуары и запчасти" href="https://aeromotus.ru/product-category/aksessuary-i-zapchasti/">Все аксессуары и запчасти</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_tag menu-item-2554"><a title="Аккумуляторы" href="https://aeromotus.ru/product-tag/akkumulyatory/">Аккумуляторы</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-2555 dropdown-submenu"><a title="Подвесы и камеры" href="#" data-bs-toggle="dropdown" class="dropdown-toggle" aria-haspopup="true">Подвесы и камеры</a>
<ul role="menu" class=" dropdown-menu">
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2557"><a title="Все подвесы и камеры" href="https://aeromotus.ru/product-category/podvesy-i-kamery/">Все подвесы и камеры</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-10079"><a title="MicaSense" href="https://aeromotus.ru/product-category/micasense/">MicaSense</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2558"><a title="DJI Zenmuse" href="https://aeromotus.ru/product-category/zenmuse/">DJI Zenmuse</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2559"><a title="Программное обеспечение" href="https://aeromotus.ru/product-category/soft/">Программное обеспечение</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2564"><a title="Специализированные решения" href="https://aeromotus.ru/product-category/individualnye-resheniya/">Специализированные решения</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-2566"><a title="Программное обеспечение" href="https://aeromotus.ru/product-category/soft/">Программное обеспечение</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2562"><a title="О НАС" href="https://aeromotus.ru/o-nas/">О НАС</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-43751"><a title="Блог" href="https://aeromotus.ru/home/blog/">Блог</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-40072"><a title="Кейсы" href="https://aeromotus.ru/category/nashi-kejsy/">Кейсы</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-45894"><a title="Обучение" href="https://aeromotus.ru/product-category/obuchenie/">Обучение</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-50103"><a title="Вебинары" href="https://aeromotus.ru/webinar/">Вебинары</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-50104"><a title="Лекции" href="https://aeromotus.ru/obrazovatelnye-vstrechi/">Лекции</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2563"><a title="Контакты" href="https://aeromotus.ru/kontakty/">Контакты</a></li>
<li class="button-menu menu-item menu-item-type-custom menu-item-object-custom menu-item-23930"><a title="Позвоните нам" href="tel:+74999388909">Позвоните нам</a></li>
</ul> </div>
</div>
<div class="header-logo">
<a href="https://aeromotus.ru/" class="header-logo-link">
<img alt="AEROMOTUS" width="269" height="99" data-src="https://aeromotus.ru/wp-content/uploads/2021/11/logo-new.svg" class="img-header-logo lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img  alt="AEROMOTUS"  width="269" height="99" data-src="https://aeromotus.ru/wp-content/uploads/2021/11/logo-new.svg" class="img-header-logo lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img src="https://aeromotus.ru/wp-content/uploads/2021/11/logo-new.svg" alt="AEROMOTUS" class="img-header-logo" width="269" height="99" /></noscript></noscript>
</a>
</div>
<div class="handheld-header-links">
<ul class="columns-4">
<li class="phone">
<a href="tel:+74999388909">
<i class="ec ec-phone"></i>
</a>
</li>
 <li class="search">
<a href="">Поиск</a> <div class="site-search">
<div class="widget woocommerce widget_product_search"><form role="search" method="get" class="woocommerce-product-search" action="https://aeromotus.ru/">
<label class="screen-reader-text" for="woocommerce-product-search-field-0">Искать:</label>
<input type="search" id="woocommerce-product-search-field-0" class="search-field" placeholder="Поиск по товарам&hellip;" value="" name="s" />
<button type="submit" value="Поиск" class="wp-element-button">Поиск</button>
<input type="hidden" name="post_type" value="product" />
</form>
</div> </div>
</li>
<li class="my-account">
<a href="https://aeromotus.ru/my-account/"><i class="ec ec-user"></i></a> </li>
<li class="cart">
<a class="footer-cart-contents" href="https://aeromotus.ru/cart/" title="Просмотреть корзину">
<i class="ec ec-shopping-bag"></i>
<span class="cart-items-count count">0</span>
</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</header>
<div id="content" class="site-content" tabindex="-1">
<div class="container">
<nav class="woocommerce-breadcrumb"><a href="https://aeromotus.ru">Главная</a><span class="delimiter"><i class="fa fa-angle-right"></i></span><a href="https://aeromotus.ru/product-category/aksessuary-i-zapchasti/">Аксессуары и Запчасти</a><span class="delimiter"><i class="fa fa-angle-right"></i></span><a href="https://aeromotus.ru/product-category/aksessuary-i-zapchasti/akkumulyatory-i-zaryadnye-ustrojstva/">Аккумуляторы и зарядные устройства</a><span class="delimiter"><i class="fa fa-angle-right"></i></span>Аккумулятор DJI MATRICE 300 TB 60 Intelligent Flight Battery (Part08)</nav><div class="site-content-inner row"><div class="woocommerce-notices-wrapper"></div> <div data-elementor-type="product" data-elementor-id="34574" class="elementor elementor-34574 elementor-location-single post-11405 product type-product status-publish has-post-thumbnail product_cat-matrice-seria product_cat-akkumulyatory-i-zaryadnye-ustrojstva product_tag-dji-enterprise product_tag-geo first instock sale shipping-taxable purchasable product-type-simple product">
<section class="elementor-section elementor-top-section elementor-element elementor-element-d263967 elementor-section-full_width elementor-section-height-default elementor-section-height-default" data-id="d263967" data-element_type="section">
<div class="elementor-container elementor-column-gap-default">
<div class="elementor-column elementor-col-50 elementor-top-column elementor-element elementor-element-f0c941e" data-id="f0c941e" data-element_type="column">
<div class="elementor-widget-wrap elementor-element-populated">
<div class="elementor-element elementor-element-0f4b85b yes elementor-widget elementor-widget-woocommerce-product-images" data-id="0f4b85b" data-element_type="widget" data-widget_type="woocommerce-product-images.default">
<div class="elementor-widget-container">
<link rel="stylesheet" href="https://aeromotus.ru/wp-content/plugins/elementor-pro/assets/css/widget-woocommerce.min.css">
<span class="onsale">-<span class="percentage">32%</span></span>
<div class="woocommerce-product-gallery woocommerce-product-gallery--with-images woocommerce-product-gallery--columns-5 images" data-columns="5" style="opacity: 0; transition: opacity .25s ease-in-out;">
<figure class="woocommerce-product-gallery__wrapper">
<div data-thumb="https://aeromotus.ru/wp-content/uploads/2020/08/4e2ce5c0ff135c9db66c9655a1fb8dfa-100x100.png" data-thumb-alt="" class="woocommerce-product-gallery__image"><a href="https://aeromotus.ru/wp-content/uploads/2020/08/4e2ce5c0ff135c9db66c9655a1fb8dfa.png"><img width="600" height="600" src="https://aeromotus.ru/wp-content/uploads/2020/08/4e2ce5c0ff135c9db66c9655a1fb8dfa.png" class="wp-post-image" alt="" decoding="async" title="4e2ce5c0ff135c9db66c9655a1fb8dfa" data-caption="" data-src="https://aeromotus.ru/wp-content/uploads/2020/08/4e2ce5c0ff135c9db66c9655a1fb8dfa.png" data-large_image="https://aeromotus.ru/wp-content/uploads/2020/08/4e2ce5c0ff135c9db66c9655a1fb8dfa.png" data-large_image_width="600" data-large_image_height="600" srcset="https://aeromotus.ru/wp-content/uploads/2020/08/4e2ce5c0ff135c9db66c9655a1fb8dfa.png 600w, https://aeromotus.ru/wp-content/uploads/2020/08/4e2ce5c0ff135c9db66c9655a1fb8dfa-300x300.png 300w, https://aeromotus.ru/wp-content/uploads/2020/08/4e2ce5c0ff135c9db66c9655a1fb8dfa-150x150.png 150w, https://aeromotus.ru/wp-content/uploads/2020/08/4e2ce5c0ff135c9db66c9655a1fb8dfa-100x100.png 100w" sizes="(max-width: 600px) 100vw, 600px" /></a></div><div data-thumb="https://aeromotus.ru/wp-content/uploads/2020/08/b7bf90414ade38fb4b436037e97c46ef-100x100.jpg" data-thumb-alt="" class="woocommerce-product-gallery__image"><a href="https://aeromotus.ru/wp-content/uploads/2020/08/b7bf90414ade38fb4b436037e97c46ef.jpg"><img width="600" height="600" src="https://aeromotus.ru/wp-content/uploads/2020/08/b7bf90414ade38fb4b436037e97c46ef.jpg" class="" alt="" decoding="async" title="b7bf90414ade38fb4b436037e97c46ef" data-caption="" data-src="https://aeromotus.ru/wp-content/uploads/2020/08/b7bf90414ade38fb4b436037e97c46ef.jpg" data-large_image="https://aeromotus.ru/wp-content/uploads/2020/08/b7bf90414ade38fb4b436037e97c46ef.jpg" data-large_image_width="600" data-large_image_height="600" srcset="https://aeromotus.ru/wp-content/uploads/2020/08/b7bf90414ade38fb4b436037e97c46ef.jpg 600w, https://aeromotus.ru/wp-content/uploads/2020/08/b7bf90414ade38fb4b436037e97c46ef-300x300.jpg 300w, https://aeromotus.ru/wp-content/uploads/2020/08/b7bf90414ade38fb4b436037e97c46ef-150x150.jpg 150w, https://aeromotus.ru/wp-content/uploads/2020/08/b7bf90414ade38fb4b436037e97c46ef-100x100.jpg 100w" sizes="(max-width: 600px) 100vw, 600px" /></a></div> </figure>
</div>
</div>
</div>
</div>
</div>
<div class="elementor-column elementor-col-50 elementor-top-column elementor-element elementor-element-a8593b1" data-id="a8593b1" data-element_type="column">
<div class="elementor-widget-wrap elementor-element-populated">
<div class="elementor-element elementor-element-5cf24f4 elementor-widget elementor-widget-woocommerce-product-title elementor-page-title elementor-widget-heading" data-id="5cf24f4" data-element_type="widget" data-widget_type="woocommerce-product-title.default">
<div class="elementor-widget-container">
<style>/*! elementor - v3.11.5 - 14-03-2023 */
.elementor-heading-title{padding:0;margin:0;line-height:1}.elementor-widget-heading .elementor-heading-title[class*=elementor-size-]>a{color:inherit;font-size:inherit;line-height:inherit}.elementor-widget-heading .elementor-heading-title.elementor-size-small{font-size:15px}.elementor-widget-heading .elementor-heading-title.elementor-size-medium{font-size:19px}.elementor-widget-heading .elementor-heading-title.elementor-size-large{font-size:29px}.elementor-widget-heading .elementor-heading-title.elementor-size-xl{font-size:39px}.elementor-widget-heading .elementor-heading-title.elementor-size-xxl{font-size:59px}</style><h1 class="product_title entry-title elementor-heading-title elementor-size-default">Аккумулятор DJI MATRICE 300 TB 60 Intelligent Flight Battery (Part08)</h1> </div>
</div>
<div class="elementor-element elementor-element-e5f9b48 elementor-widget-divider--view-line elementor-widget elementor-widget-divider" data-id="e5f9b48" data-element_type="widget" data-widget_type="divider.default">
<div class="elementor-widget-container">
<style>/*! elementor - v3.11.5 - 14-03-2023 */
.elementor-widget-divider{--divider-border-style:none;--divider-border-width:1px;--divider-color:#2c2c2c;--divider-icon-size:20px;--divider-element-spacing:10px;--divider-pattern-height:24px;--divider-pattern-size:20px;--divider-pattern-url:none;--divider-pattern-repeat:repeat-x}.elementor-widget-divider .elementor-divider{display:flex}.elementor-widget-divider .elementor-divider__text{font-size:15px;line-height:1;max-width:95%}.elementor-widget-divider .elementor-divider__element{margin:0 var(--divider-element-spacing);flex-shrink:0}.elementor-widget-divider .elementor-icon{font-size:var(--divider-icon-size)}.elementor-widget-divider .elementor-divider-separator{display:flex;margin:0;direction:ltr}.elementor-widget-divider--view-line_icon .elementor-divider-separator,.elementor-widget-divider--view-line_text .elementor-divider-separator{align-items:center}.elementor-widget-divider--view-line_icon .elementor-divider-separator:after,.elementor-widget-divider--view-line_icon .elementor-divider-separator:before,.elementor-widget-divider--view-line_text .elementor-divider-separator:after,.elementor-widget-divider--view-line_text .elementor-divider-separator:before{display:block;content:"";border-bottom:0;flex-grow:1;border-top:var(--divider-border-width) var(--divider-border-style) var(--divider-color)}.elementor-widget-divider--element-align-left .elementor-divider .elementor-divider-separator>.elementor-divider__svg:first-of-type{flex-grow:0;flex-shrink:100}.elementor-widget-divider--element-align-left .elementor-divider-separator:before{content:none}.elementor-widget-divider--element-align-left .elementor-divider__element{margin-left:0}.elementor-widget-divider--element-align-right .elementor-divider .elementor-divider-separator>.elementor-divider__svg:last-of-type{flex-grow:0;flex-shrink:100}.elementor-widget-divider--element-align-right .elementor-divider-separator:after{content:none}.elementor-widget-divider--element-align-right .elementor-divider__element{margin-right:0}.elementor-widget-divider:not(.elementor-widget-divider--view-line_text):not(.elementor-widget-divider--view-line_icon) .elementor-divider-separator{border-top:var(--divider-border-width) var(--divider-border-style) var(--divider-color)}.elementor-widget-divider--separator-type-pattern{--divider-border-style:none}.elementor-widget-divider--separator-type-pattern.elementor-widget-divider--view-line .elementor-divider-separator,.elementor-widget-divider--separator-type-pattern:not(.elementor-widget-divider--view-line) .elementor-divider-separator:after,.elementor-widget-divider--separator-type-pattern:not(.elementor-widget-divider--view-line) .elementor-divider-separator:before,.elementor-widget-divider--separator-type-pattern:not([class*=elementor-widget-divider--view]) .elementor-divider-separator{width:100%;min-height:var(--divider-pattern-height);-webkit-mask-size:var(--divider-pattern-size) 100%;mask-size:var(--divider-pattern-size) 100%;-webkit-mask-repeat:var(--divider-pattern-repeat);mask-repeat:var(--divider-pattern-repeat);background-color:var(--divider-color);-webkit-mask-image:var(--divider-pattern-url);mask-image:var(--divider-pattern-url)}.elementor-widget-divider--no-spacing{--divider-pattern-size:auto}.elementor-widget-divider--bg-round{--divider-pattern-repeat:round}.rtl .elementor-widget-divider .elementor-divider__text{direction:rtl}.e-con-inner>.elementor-widget-divider,.e-con>.elementor-widget-divider{width:var(--container-widget-width,100%);--flex-grow:var(--container-widget-flex-grow)}</style> <div class="elementor-divider">
<span class="elementor-divider-separator">
</span>
</div>
</div>
</div>
<div class="elementor-element elementor-element-91d61dc elementor-widget elementor-widget-woocommerce-product-short-description" data-id="91d61dc" data-element_type="widget" data-widget_type="woocommerce-product-short-description.default">
<div class="elementor-widget-container">
<div class="woocommerce-product-details__short-description">
<div id="detailText">
<div class="changeDescription">Аккумулятор DJI MATRICE 300 TB60 Intelligent Flight Battery (Part08) для платформы DJI MATRICE 300 RTK (Universal Edition).</div>
</div>
<div class="changePropertiesGroup"></div>
</div>
</div>
</div>
<div class="elementor-element elementor-element-f62c55e elementor-widget elementor-widget-woocommerce-product-price" data-id="f62c55e" data-element_type="widget" data-widget_type="woocommerce-product-price.default">
<div class="elementor-widget-container">
<p class="price"><span class="electro-price"><ins><span class="woocommerce-Price-amount amount"><bdi>87 400&nbsp;<span class="woocommerce-Price-currencySymbol">&#8381;</span></bdi></span></ins> <del><span class="woocommerce-Price-amount amount"><bdi>129 298&nbsp;<span class="woocommerce-Price-currencySymbol">&#8381;</span></bdi></span></del></span></p>
</div>
</div>
<div class="elementor-element elementor-element-afff089 elementor-add-to-cart--layout-auto e-add-to-cart--show-quantity-yes elementor-widget elementor-widget-woocommerce-product-add-to-cart" data-id="afff089" data-element_type="widget" data-widget_type="woocommerce-product-add-to-cart.default">
<div class="elementor-widget-container">
<div class="elementor-add-to-cart elementor-product-simple">
<p class="stock in-stock">В наличии</p>
<form class="cart" action="https://aeromotus.ru/product/akkumulyator-dji-matrice-300-tb60-intelligent-flight-battery-part08/" method="post" enctype='multipart/form-data'>
<div class="e-atc-qty-button-holder">
<div class="quantity hidden hidden-xs-up">
<input type="hidden" id="quantity_641718f53807a" class="qty" name="quantity" value="1" />
</div>
<button type="submit" name="add-to-cart" value="11405" class="single_add_to_cart_button button alt" onclick="ym(55570990, 'reachGoal', 'add_to_cart', {order_price: 87400,currency:'RUB'}); return true;">В корзину</button>
</div>
</form>
</div>
</div>
</div>
</div>
</div>
</div>
</section>
<section class="elementor-section elementor-top-section elementor-element elementor-element-25ef058 elementor-section-full_width elementor-section-height-default elementor-section-height-default" data-id="25ef058" data-element_type="section">
<div class="elementor-container elementor-column-gap-default">
<div class="elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-0821939" data-id="0821939" data-element_type="column">
<div class="elementor-widget-wrap elementor-element-populated">
<div class="elementor-element elementor-element-a2df4b7 elementor-woo-meta--view-inline elementor-widget elementor-widget-woocommerce-product-meta" data-id="a2df4b7" data-element_type="widget" data-widget_type="woocommerce-product-meta.default">
<div class="elementor-widget-container">
<div class="product_meta">
<span class="posted_in detail-container"><span class="detail-label">Категории</span> <span class="detail-content"><a href="https://aeromotus.ru/product-category/matrice-seria/" rel="tag">DJI Matrice</a>, <a href="https://aeromotus.ru/product-category/aksessuary-i-zapchasti/akkumulyatory-i-zaryadnye-ustrojstva/" rel="tag">Аккумуляторы и зарядные устройства</a></span></span>
<span class="tagged_as detail-container"><span class="detail-label">Метки</span> <span class="detail-content"><a href="https://aeromotus.ru/product-tag/dji-enterprise/" rel="tag">DJI Enterprise</a>, <a href="https://aeromotus.ru/product-tag/geo/" rel="tag">Гео</a></span></span>
</div>
</div>
</div>
</div>
</div>
</div>
</section>
<section class="elementor-section elementor-top-section elementor-element elementor-element-d2fe068 elementor-section-full_width elementor-section-stretched elementor-section-height-default elementor-section-height-default" data-id="d2fe068" data-element_type="section" data-settings="{&quot;stretch_section&quot;:&quot;section-stretched&quot;}">
<div class="elementor-container elementor-column-gap-no gx-0">
<div class="elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-4972b9d" data-id="4972b9d" data-element_type="column">
<div class="elementor-widget-wrap elementor-element-populated">
<div class="elementor-element elementor-element-322a8df elementor-widget-mobile__width-inherit elementor-widget elementor-widget-woocommerce-product-data-tabs" data-id="322a8df" data-element_type="widget" data-widget_type="woocommerce-product-data-tabs.default">
<div class="elementor-widget-container">
<div class="woocommerce-tabs wc-tabs-wrapper">
<ul class="tabs wc-tabs" role="tablist">
<li class="description_tab" id="tab-title-description" role="tab" aria-controls="tab-description">
<a href="#tab-description">
Описание </a>
</li>
<li class="oplata_tab" id="tab-title-oplata" role="tab" aria-controls="tab-oplata">
<a href="#tab-oplata">
Оплата </a>
</li>
<li class="dostavka_tab" id="tab-title-dostavka" role="tab" aria-controls="tab-dostavka">
<a href="#tab-dostavka">
Доставка </a>
</li>
</ul>
<div class="woocommerce-Tabs-panel woocommerce-Tabs-panel--description panel entry-content wc-tab" id="tab-description" role="tabpanel" aria-labelledby="tab-title-description">
<div class="electro-description clearfix"> <style type="text/css">
			.am-collapse {overflow: hidden;position: relative;}
			.am-collapse-trigger-wrapper {display: none;text-align: center;padding: 15px 0;}
		</style>
<div data-am-collapse="true">
<div class="am-collapse expanded">
<div id="detailText">
<div class="changeDescription">Аккумулятор DJI MATRICE 300 TB60 Intelligent Flight Battery (Part08) для платформы DJI MATRICE 300 RTK (Universal Edition).</div>
</div>
<div class="changePropertiesGroup"></div>
<table class="stats">
<tbody>
<tr>
<td class="name">Емкость</td>
<td>5935 мАч</td>
</tr>
<tr>
<td class="name">Модель</td>
<td>TB60</td>
</tr>
<tr>
<td class="name">Напряжение</td>
<td>52,8 в</td>
</tr>
<tr>
<td class="name">Тип</td>
<td>Литий-полимерный 12S</td>
</tr>
<tr>
<td class="name">Время зарядки</td>
<td>При использовании зарядной станции для аккумуляторов Intelligent Battery BS60: Входной ток 220 В: 60 минут (полный заряд двух аккумуляторов TB60), 30 минут (заряд двух аккумуляторов TB60 с 20% до 90%); Входной ток 110 В: 70 минут (полный заряд двух аккумуляторов TB60), 40 минут (заряд двух аккумуляторов TB60 с 20% до 90%)</td>
</tr>
<tr>
<td class="name">Вес</td>
<td>Около 1,35 кг</td>
</tr>
<tr>
<td class="name">Энергоемкость</td>
<td>274 Вт·ч</td>
</tr>
<tr>
<td class="name">Диапазон температур зарядки</td>
<td>-20°C…+40°C (Функция самонагревания автоматически активируется при температуре зарядки менее +5°C. Зарядка при низкой температуре воздуха может сократить срок службы аккумулятора.)</td>
</tr>
<tr>
<td class="name">Рабочая температура</td>
<td>-20°C…+50°C</td>
</tr>
<tr>
<td class="name">Температурный диапазон хранения</td>
<td>+22°C&#8230;+30°C</td>
</tr>
</tbody>
</table>
</div>
<div class="am-collapse-trigger-wrapper">
<a href="#" class="button" data-expand="true" data-target=".am-collapse" data-text-more="Показать" data-text-less="Скрыть">Скрыть</a>
</div>
</div>
</div><div class="product_meta">
<span class="posted_in">Категории: <a href="https://aeromotus.ru/product-category/matrice-seria/" rel="tag">DJI Matrice</a>, <a href="https://aeromotus.ru/product-category/aksessuary-i-zapchasti/akkumulyatory-i-zaryadnye-ustrojstva/" rel="tag">Аккумуляторы и зарядные устройства</a></span>
<span class="tagged_as">Метки: <a href="https://aeromotus.ru/product-tag/dji-enterprise/" rel="tag">DJI Enterprise</a>, <a href="https://aeromotus.ru/product-tag/geo/" rel="tag">Гео</a></span>
</div>
</div>
<div class="woocommerce-Tabs-panel woocommerce-Tabs-panel--oplata panel entry-content wc-tab" id="tab-oplata" role="tabpanel" aria-labelledby="tab-title-oplata">
<p>В нашем магазине вы сможете оплатить товар одним из следующих способов:</p>
<p><strong>Наличными</strong></p>
<p>Оплата принимается в российских рублях в наших офисах или курьеру при получении товара после проверки комплектности и внешнего вида изделия. Предоставляется накладная и кассовый чек.</p>
<p><strong>Банковской картой при самовывозе/доставке</strong></p>
<p>При помощи банковской карты вы можете оплатить ваш заказ при получении товара в нашем офисе по адресу: Варшавское шоссе, дом 42. Данный способ расчета не влияет на стоимость товара – комиссия при оплате заказа картой не взимается. Мы принимаем пластиковые карты международных платежных систем МИР, VISA, MasterCard и т.д.</p>
<p><strong>Онлайн оплата через Сбербанк России (VISA, MasterCard, МИР, Apple Pay, Google Pay, SberPay)</strong></p>
<p>Вы можете оплатить свой заказ банковской картой онлайн через Процессинговый центр Сбербанк России, осуществляющий интернет эквайринг. После подтверждения заказа вы будете перенаправлены на защищенную платежную страницу, где вам необходимо ввести данные вашей банковской карты.</p>
<p>Процессинговый центр Сбербанк России защищает данные Вашей банковской карты с использованием технологий, подтвержденных соответствием стандарту безопасности PCI DSS. Данные карты вводятся на защищенной платежной странице, передача информации в Процессинговый центр Сбербанк России происходит с применением надежных алгоритмов шифрования данных.Конфиденциальность сообщаемой персональной информации обеспечивается Сбербанк России. Введенная информация не будет предоставлена третьим лицам за исключением случаев, предусмотренных законодательством РФ. Проведение платежей по банковским картам осуществляется в строгом соответствии с требованиями платежных систем МИР, Visa Int. и MasterCard Europe Sprl.</p>
<p><strong>Оплата банковским переводом<br />
</strong>Вы можете оплатить заказ согласно выставленному счету в любом отделении банка или в онлайн-банке.</p>
<p><strong>Оплата по QR коду или ссылке</strong><br />
После подтверждения наличия товара наш менеджер высылает QR код или ссылку удобным Вам способом.</p>
<p><strong>Кредит или Рассрочка<br />
</strong><br />
В нашем магазине есть возможность приобрести товар в кредит или в рассрочку.Рассрочка это возможность покупки товаров без каких либо переплат равными платежами.</p>
<p>Для этого оформите заказ через корзину и выберите способ оплаты Кредит. Далее следуя инструкциям платежного шлюза Тинькоф кредит вы можете оформить заявку и получить одобрение моментально. Далее вам понадобится встретится с кредитным менеджером для подписания договора.</p>
<p>Подписать кредитный договор можно на встрече с кредитным менеджером или у нас в офисе.</p>
<p><strong>Лизинг</strong><br />
Компания Aeromotus совместно с несколькими лизинговыми компаниями осуществляет программу предоставления продукции на лизинговых условиях. Для того чтобы купить дроны в лизинг юридическому лицу необходимо заполнить заявку и ознакомиться с условиями лизинговой компании.</p>
<p><strong>Юридическим лицам</strong><br />
Оплата производится после заключения договора по выставленному счету. Срок действия счета – 3 рабочих дня.</p>
</div>
<div class="woocommerce-Tabs-panel woocommerce-Tabs-panel--dostavka panel entry-content wc-tab" id="tab-dostavka" role="tabpanel" aria-labelledby="tab-title-dostavka">
<p>Доставку и отправление товаров мы осуществляем следующими способами:</p>
<figure class="wp-block-table">
<table>
<thead>
<tr>
<td><strong>Способ Доставки</strong></td>
<td><strong>Стоимость доставки</strong></td>
</tr>
</thead>
<tbody>
<tr>
<td>Самовывоз<br />
(м. Нагатинская)</td>
<td>0 рублей</td>
</tr>
<tr>
<td>По г. Москва, в пределах МКАД</td>
<td>БЕСПЛАТНО* – до 15 кг.<br />
Больше 15 кг – рассчитывается индивидуально. Стоимость можно уточнить по телефону</td>
</tr>
<tr>
<td>По Московской области</td>
<td>Рассчитывается индивидуально.<br />
Стоимость можно уточнить по телефону</td>
</tr>
<tr>
<td>По России и странам СНГ(Транспортная компания )</td>
<td>Индивидуально, в зависимости от города отправления.</td>
</tr>
</tbody>
</table>
</figure>
<p><strong>Пункт самовывоза находится по адресу:</strong> г. Москва, Варшавское шоссе, дом 42, 6 этаж, офис 6240<br />
<a href="https://yandex.ru/maps/-/CGSpiTjF">Посмотреть на Яндекс.Картах</a><br />
<strong>Для жителей Москвы и ближайшего Подмосковья:</strong><br />
Доставка осуществляется в течение 1-2 дней после заказа. Возможна доставка в день заказа по предварительному согласованию. Менеджер согласовывает время доставки. Водитель совершает предварительный звонок за 1 час.<br />
<strong>Для жителей России и стран СНГ:</strong><br />
Доставка осуществляется транспортными компаниями по согласованию с клиентом. Услуги транспортной компании клиент оплачивает по факту получения товара в своём городе. Работа по полной предоплате или наложенным платежом, срок поставки зависит от удаленности региона от Москвы.</p>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</section>
</div>
</div> </div>
</div>
<footer id="colophon" class="site-footer footer-v2">
<div class="desktop-footer d-none d-lg-block container">
<div class="footer-bottom-widgets">
<div class="container">
<div class="footer-bottom-widgets-inner row">
<div class="footer-contact col-md-5">
<div class="footer-logo">
<img alt="AEROMOTUS" width="600" height="100" data-src="https://aeromotus.ru/wp-content/uploads/2019/08/logo.png" class="lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img  alt="AEROMOTUS" width="600" height="100" data-src="https://aeromotus.ru/wp-content/uploads/2019/08/logo.png" class="lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img src="https://aeromotus.ru/wp-content/uploads/2019/08/logo.png" alt="AEROMOTUS" width="600" height="100" /></noscript></noscript>
</div>
<div class="footer-call-us">
<div class="media d-flex">
<span class="media-left call-us-icon media-middle"><i class="ec ec-support"></i></span>
<div class="media-body">
<span class="call-us-text">Позвоните Нам</span>
<span class="call-us-number">+7 (499) 938-89-09</span>
</div>
</div>
</div>
<div class="footer-address">
<strong class="footer-address-title">Адрес:</strong>
<address>г. Москва, Варшавское шоссе, дом 42, 6 этаж, офис 6240<br />
</address>
</div>
<div class="footer-social-icons">
<ul class="social-icons list-unstyled nav align-items-center">
<li><a class="fab fa-whatsapp mobile" target="_blank" href="https://wa.me/message/NCP5CWXMM3AML1"></a></li><li><a class="fab fa-whatsapp desktop" target="_blank" href="https://wa.me/message/NCP5CWXMM3AML1"></a></li><li><a class="fab fa-youtube" target="_blank" href="https://www.youtube.com/channel/UCAyu9W59PeY_8qIUeNVXwrg"></a></li><li><a class="fab fa-vk" target="_blank" href="https://vk.com/aeromotus"></a></li><li><a class="fab fa-telegram" target="_blank" href="https://t.me/aeromotus_news"></a></li> </ul>
</div>
</div>
<div class="footer-bottom-widgets-menu col-md">
<div class="footer-bottom-widgets-menu-inner row g-0 row-cols-xl-2">
<div class="columns"><aside class="widget clearfix widget_nav_menu"><div class="body"><div class="menu-menu-2-container"><ul id="menu-menu-3" class="menu"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-1731"><a href="https://aeromotus.ru/">Главная</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-45892"><a href="https://aeromotus.ru/product-category/obuchenie/">Обучение</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-1734"><a href="https://aeromotus.ru/product-category/soft/">Софт</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-45418"><a target="_blank" rel="noopener" href="https://enterprise.aeromotus.ru/">Промышленные решения</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-24422"><a href="https://aeromotus.ru/webinar/">Вебинары</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2626"><a href="https://aeromotus.ru/dostavka/">Оплата и Доставка</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1730"><a href="https://aeromotus.ru/o-nas/">О Нас</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-43752"><a href="https://aeromotus.ru/home/blog/">Блог</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-17115"><a href="https://aeromotus.ru/vakansii-2/">Вакансии</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1729"><a href="https://aeromotus.ru/kontakty/">Контакты</a></li>
</ul></div></div></aside></div><div class="columns"><aside class="widget clearfix woocommerce widget_recently_viewed_products"><div class="body"><h4 class="widget-title">Недавно просмотренные товары</h4><ul class="product_list_widget"><li>
<a href="https://aeromotus.ru/product/dji-matrice-300-rtk-combo-2xtb60-zaryadnaya-stancziya-bs60/">
<img width="300" height="300" alt="" decoding="async" data-srcset="https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-300x300.jpg 300w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-150x150.jpg 150w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-768x768.jpg 768w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-600x600.jpg 600w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-100x100.jpg 100w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk.jpg 1000w" data-src="https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-300x300.jpg" data-sizes="(max-width: 300px) 100vw, 300px" class="attachment-woocommerce_thumbnail size-woocommerce_thumbnail lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img width="300" height="300"   alt="" decoding="async" data-srcset="https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-300x300.jpg 300w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-150x150.jpg 150w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-768x768.jpg 768w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-600x600.jpg 600w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-100x100.jpg 100w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk.jpg 1000w"  data-src="https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-300x300.jpg" data-sizes="(max-width: 300px) 100vw, 300px" class="attachment-woocommerce_thumbnail size-woocommerce_thumbnail lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img width="300" height="300" src="https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-300x300.jpg" class="attachment-woocommerce_thumbnail size-woocommerce_thumbnail" alt="" decoding="async" srcset="https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-300x300.jpg 300w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-150x150.jpg 150w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-768x768.jpg 768w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-600x600.jpg 600w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-100x100.jpg 100w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk.jpg 1000w" sizes="(max-width: 300px) 100vw, 300px" /></noscript></noscript> <span class="product-title">DJI Matrice 300 RTK Combo ( 2xTB60, зарядная станция BS60 )</span>
</a>
<span class="electro-price"><ins><span class="woocommerce-Price-amount amount"><bdi>1 299 600&nbsp;<span class="woocommerce-Price-currencySymbol">&#8381;</span></bdi></span></ins> <del><span class="woocommerce-Price-amount amount"><bdi>1 793 502&nbsp;<span class="woocommerce-Price-currencySymbol">&#8381;</span></bdi></span></del></span>
</li>
</ul></div></aside></div><div class="columns"><aside class="widget clearfix widget_block widget_media_image"><div class="body">
<figure class="wp-block-image size-medium"><img decoding="async" width="300" height="34" alt="" data-srcset="https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-300x34.png 300w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-1024x117.png 1024w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-768x87.png 768w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-600x68.png 600w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro.png 1458w" data-src="https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-300x34.png" data-sizes="(max-width: 300px) 100vw, 300px" class="wp-image-23027 lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img decoding="async" width="300" height="34"  alt=""  data-srcset="https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-300x34.png 300w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-1024x117.png 1024w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-768x87.png 768w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-600x68.png 600w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro.png 1458w"  data-src="https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-300x34.png" data-sizes="(max-width: 300px) 100vw, 300px" class="wp-image-23027 lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img decoding="async" width="300" height="34" src="https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-300x34.png" alt="" class="wp-image-23027" srcset="https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-300x34.png 300w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-1024x117.png 1024w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-768x87.png 768w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-600x68.png 600w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro.png 1458w" sizes="(max-width: 300px) 100vw, 300px" /></noscript></noscript><figcaption>Принимаем к оплате</figcaption></figure>
</div></aside></div><div class="columns"><aside class="widget clearfix widget_block widget_media_image"><div class="body">
<figure class="wp-block-image size-full"><img decoding="async" width="1017" height="92" alt="" data-srcset="https://aeromotus.ru/wp-content/uploads/2021/12/dev3.png 1017w, https://aeromotus.ru/wp-content/uploads/2021/12/dev3-300x27.png 300w, https://aeromotus.ru/wp-content/uploads/2021/12/dev3-768x69.png 768w, https://aeromotus.ru/wp-content/uploads/2021/12/dev3-600x54.png 600w" data-src="https://aeromotus.ru/wp-content/uploads/2021/12/dev3.png" data-sizes="(max-width: 1017px) 100vw, 1017px" class="wp-image-24653 lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img decoding="async" width="1017" height="92"  alt=""  data-srcset="https://aeromotus.ru/wp-content/uploads/2021/12/dev3.png 1017w, https://aeromotus.ru/wp-content/uploads/2021/12/dev3-300x27.png 300w, https://aeromotus.ru/wp-content/uploads/2021/12/dev3-768x69.png 768w, https://aeromotus.ru/wp-content/uploads/2021/12/dev3-600x54.png 600w"  data-src="https://aeromotus.ru/wp-content/uploads/2021/12/dev3.png" data-sizes="(max-width: 1017px) 100vw, 1017px" class="wp-image-24653 lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img decoding="async" width="1017" height="92" src="https://aeromotus.ru/wp-content/uploads/2021/12/dev3.png" alt="" class="wp-image-24653" srcset="https://aeromotus.ru/wp-content/uploads/2021/12/dev3.png 1017w, https://aeromotus.ru/wp-content/uploads/2021/12/dev3-300x27.png 300w, https://aeromotus.ru/wp-content/uploads/2021/12/dev3-768x69.png 768w, https://aeromotus.ru/wp-content/uploads/2021/12/dev3-600x54.png 600w" sizes="(max-width: 1017px) 100vw, 1017px" /></noscript></noscript><figcaption>Доставляем</figcaption></figure>
</div></aside></div><div class="columns"><aside class="widget clearfix widget_block"><div class="body"><script>
        (function(w,d,u){
                var s=d.createElement('script');s.async=true;s.src=u+'?'+(Date.now()/60000|0);
                var h=d.getElementsByTagName('script')[0];h.parentNode.insertBefore(s,h);
        })(window,document,'https://cdn-ru.bitrix24.ru/b15766068/crm/site_button/loader_3_rfdb8v.js');
</script></div></aside></div><div class="widget_text columns"><aside class="widget_text widget clearfix widget_custom_html"><div class="widget_text body"><div class="textwidget custom-html-widget">
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-TJGVBST');</script>


<noscript><iframe 
height="0" width="0" style="display:none;visibility:hidden" data-src="https://www.googletagmanager.com/ns.html?id=GTM-TJGVBST" class="lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="></iframe></noscript>
</div></div></aside></div> </div>
</div>
</div>
</div>
</div></div>
<div class="handheld-footer d-lg-none pt-3 v1 "><div class="handheld-widget-menu container">
<div class="columns"><aside class="widget clearfix widget_nav_menu"><div class="body"><div class="menu-menu-2-container"><ul id="menu-menu-4" class="menu"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-1731"><a href="https://aeromotus.ru/">Главная</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-45892"><a href="https://aeromotus.ru/product-category/obuchenie/">Обучение</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-1734"><a href="https://aeromotus.ru/product-category/soft/">Софт</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-45418"><a target="_blank" rel="noopener" href="https://enterprise.aeromotus.ru/">Промышленные решения</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-24422"><a href="https://aeromotus.ru/webinar/">Вебинары</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2626"><a href="https://aeromotus.ru/dostavka/">Оплата и Доставка</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1730"><a href="https://aeromotus.ru/o-nas/">О Нас</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-43752"><a href="https://aeromotus.ru/home/blog/">Блог</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-17115"><a href="https://aeromotus.ru/vakansii-2/">Вакансии</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1729"><a href="https://aeromotus.ru/kontakty/">Контакты</a></li>
</ul></div></div></aside></div><div class="columns"><aside class="widget clearfix woocommerce widget_recently_viewed_products"><div class="body"><h4 class="widget-title">Недавно просмотренные товары</h4><ul class="product_list_widget"><li>
<a href="https://aeromotus.ru/product/dji-matrice-300-rtk-combo-2xtb60-zaryadnaya-stancziya-bs60/">
<img width="300" height="300" alt="" decoding="async" data-srcset="https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-300x300.jpg 300w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-150x150.jpg 150w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-768x768.jpg 768w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-600x600.jpg 600w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-100x100.jpg 100w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk.jpg 1000w" data-src="https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-300x300.jpg" data-sizes="(max-width: 300px) 100vw, 300px" class="attachment-woocommerce_thumbnail size-woocommerce_thumbnail lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img width="300" height="300"   alt="" decoding="async" data-srcset="https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-300x300.jpg 300w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-150x150.jpg 150w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-768x768.jpg 768w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-600x600.jpg 600w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-100x100.jpg 100w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk.jpg 1000w"  data-src="https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-300x300.jpg" data-sizes="(max-width: 300px) 100vw, 300px" class="attachment-woocommerce_thumbnail size-woocommerce_thumbnail lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img width="300" height="300" src="https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-300x300.jpg" class="attachment-woocommerce_thumbnail size-woocommerce_thumbnail" alt="" decoding="async" srcset="https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-300x300.jpg 300w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-150x150.jpg 150w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-768x768.jpg 768w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-600x600.jpg 600w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk-100x100.jpg 100w, https://aeromotus.ru/wp-content/uploads/2020/11/matrice_300_rtk.jpg 1000w" sizes="(max-width: 300px) 100vw, 300px" /></noscript></noscript> <span class="product-title">DJI Matrice 300 RTK Combo ( 2xTB60, зарядная станция BS60 )</span>
</a>
<span class="electro-price"><ins><span class="woocommerce-Price-amount amount"><bdi>1 299 600&nbsp;<span class="woocommerce-Price-currencySymbol">&#8381;</span></bdi></span></ins> <del><span class="woocommerce-Price-amount amount"><bdi>1 793 502&nbsp;<span class="woocommerce-Price-currencySymbol">&#8381;</span></bdi></span></del></span>
</li>
</ul></div></aside></div><div class="columns"><aside class="widget clearfix widget_block widget_media_image"><div class="body">
<figure class="wp-block-image size-medium"><img decoding="async" width="300" height="34" alt="" data-srcset="https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-300x34.png 300w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-1024x117.png 1024w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-768x87.png 768w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-600x68.png 600w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro.png 1458w" data-src="https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-300x34.png" data-sizes="(max-width: 300px) 100vw, 300px" class="wp-image-23027 lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img decoding="async" width="300" height="34"  alt=""  data-srcset="https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-300x34.png 300w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-1024x117.png 1024w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-768x87.png 768w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-600x68.png 600w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro.png 1458w"  data-src="https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-300x34.png" data-sizes="(max-width: 300px) 100vw, 300px" class="wp-image-23027 lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img decoding="async" width="300" height="34" src="https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-300x34.png" alt="" class="wp-image-23027" srcset="https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-300x34.png 300w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-1024x117.png 1024w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-768x87.png 768w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro-600x68.png 600w, https://aeromotus.ru/wp-content/uploads/2021/10/visa-mastercard-mir-maestro.png 1458w" sizes="(max-width: 300px) 100vw, 300px" /></noscript></noscript><figcaption>Принимаем к оплате</figcaption></figure>
</div></aside></div><div class="columns"><aside class="widget clearfix widget_block widget_media_image"><div class="body">
<figure class="wp-block-image size-full"><img decoding="async" width="1017" height="92" alt="" data-srcset="https://aeromotus.ru/wp-content/uploads/2021/12/dev3.png 1017w, https://aeromotus.ru/wp-content/uploads/2021/12/dev3-300x27.png 300w, https://aeromotus.ru/wp-content/uploads/2021/12/dev3-768x69.png 768w, https://aeromotus.ru/wp-content/uploads/2021/12/dev3-600x54.png 600w" data-src="https://aeromotus.ru/wp-content/uploads/2021/12/dev3.png" data-sizes="(max-width: 1017px) 100vw, 1017px" class="wp-image-24653 lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img decoding="async" width="1017" height="92"  alt=""  data-srcset="https://aeromotus.ru/wp-content/uploads/2021/12/dev3.png 1017w, https://aeromotus.ru/wp-content/uploads/2021/12/dev3-300x27.png 300w, https://aeromotus.ru/wp-content/uploads/2021/12/dev3-768x69.png 768w, https://aeromotus.ru/wp-content/uploads/2021/12/dev3-600x54.png 600w"  data-src="https://aeromotus.ru/wp-content/uploads/2021/12/dev3.png" data-sizes="(max-width: 1017px) 100vw, 1017px" class="wp-image-24653 lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img decoding="async" width="1017" height="92" src="https://aeromotus.ru/wp-content/uploads/2021/12/dev3.png" alt="" class="wp-image-24653" srcset="https://aeromotus.ru/wp-content/uploads/2021/12/dev3.png 1017w, https://aeromotus.ru/wp-content/uploads/2021/12/dev3-300x27.png 300w, https://aeromotus.ru/wp-content/uploads/2021/12/dev3-768x69.png 768w, https://aeromotus.ru/wp-content/uploads/2021/12/dev3-600x54.png 600w" sizes="(max-width: 1017px) 100vw, 1017px" /></noscript></noscript><figcaption>Доставляем</figcaption></figure>
</div></aside></div><div class="columns"><aside class="widget clearfix widget_block"><div class="body"><script>
        (function(w,d,u){
                var s=d.createElement('script');s.async=true;s.src=u+'?'+(Date.now()/60000|0);
                var h=d.getElementsByTagName('script')[0];h.parentNode.insertBefore(s,h);
        })(window,document,'https://cdn-ru.bitrix24.ru/b15766068/crm/site_button/loader_3_rfdb8v.js');
</script></div></aside></div><div class="widget_text columns"><aside class="widget_text widget clearfix widget_custom_html"><div class="widget_text body"><div class="textwidget custom-html-widget">
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-TJGVBST');</script>


<noscript><iframe 
height="0" width="0" style="display:none;visibility:hidden" data-src="https://www.googletagmanager.com/ns.html?id=GTM-TJGVBST" class="lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="></iframe></noscript>
</div></div></aside></div></div>
<div class="footer-social-icons container text-center mb-0">
<ul class="social-icons-color nav align-items-center row list-unstyled justify-content-center mb-0">
<li><a class="fab fa-whatsapp mobile" target="_blank" href="https://wa.me/message/NCP5CWXMM3AML1"></a></li><li><a class="fab fa-whatsapp desktop" target="_blank" href="https://wa.me/message/NCP5CWXMM3AML1"></a></li><li><a class="fab fa-youtube" target="_blank" href="https://www.youtube.com/channel/UCAyu9W59PeY_8qIUeNVXwrg"></a></li><li><a class="fab fa-vk" target="_blank" href="https://vk.com/aeromotus"></a></li><li><a class="fab fa-telegram" target="_blank" href="https://t.me/aeromotus_news"></a></li> </ul>
</div>
<div class="handheld-footer-bar">
<div class="handheld-footer-bar-inner">
<div class="footer-logo">
<img alt="AEROMOTUS" width="600" height="100" data-src="https://aeromotus.ru/wp-content/uploads/2019/08/logo.png" class="lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img  alt="AEROMOTUS" width="600" height="100" data-src="https://aeromotus.ru/wp-content/uploads/2019/08/logo.png" class="lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img src="https://aeromotus.ru/wp-content/uploads/2019/08/logo.png" alt="AEROMOTUS" width="600" height="100" /></noscript></noscript>
</div>
<div class="footer-call-us">
<span class="call-us-text">Позвоните Нам</span>
<span class="call-us-number">+7 (499) 938-89-09</span>
</div>
</div>
</div>
</div>
</footer>
</div>
</div>
<div class="back-to-top-wrapper position-absolute bottom-0 pe-none">
<a href="#page" class="btn btn-secondary shadows rounded-cricle d-flex align-items-center justify-content-center p-0 pe-auto position-sticky position-fixed back-to-top-link " aria-label="Scroll to Top"><i class="fa fa-angle-up"></i></a>
</div> <div class="electro-overlay"></div>
<noscript>
                <div>
                    <img src="https://mc.yandex.ru/watch/55570990" style="position:absolute; left:-9999px;" alt=""/>
                </div>
            </noscript>
<script>
        function coolTagCloudToggle( element ) {
            var parent = element.closest('.cool-tag-cloud');
            parent.querySelector('.cool-tag-cloud-inner').classList.toggle('cool-tag-cloud-active');
            parent.querySelector( '.cool-tag-cloud-load-more').classList.toggle('cool-tag-cloud-active');
        }
    </script>
<script>requestAnimationFrame(() => document.body.classList.add( "stk--anim-init" ))</script> <div id="aeromotus-inquire-popup" class="white-popup mfp-hide">
<h4>Узнать цену для <span data-product-title></span></h4>
<div class="wpcf7 no-js" id="wpcf7-f2382-p11405-o1" lang="ru-RU" dir="ltr">
<div class="screen-reader-response"><p role="status" aria-live="polite" aria-atomic="true"></p> <ul></ul></div>
<form action="/product/akkumulyator-dji-matrice-300-tb60-intelligent-flight-battery-part08/#wpcf7-f2382-p11405-o1" method="post" class="wpcf7-form init" aria-label="Контактная форма" novalidate="novalidate" data-status="init">
<div style="display: none;">
<input type="hidden" name="_wpcf7" value="2382" />
<input type="hidden" name="_wpcf7_version" value="5.7.4" />
<input type="hidden" name="_wpcf7_locale" value="ru_RU" />
<input type="hidden" name="_wpcf7_unit_tag" value="wpcf7-f2382-p11405-o1" />
<input type="hidden" name="_wpcf7_container_post" value="11405" />
<input type="hidden" name="_wpcf7_posted_data_hash" value="" />
<input type="hidden" name="_wpcf7_recaptcha_response" value="" />
</div>
<input class="wpcf7-form-control wpcf7-hidden" value="" type="hidden" name="product-id" />
<input class="wpcf7-form-control wpcf7-hidden" value="" type="hidden" name="product-title" />
<input class="wpcf7-form-control wpcf7-hidden" value="" type="hidden" name="product-link" />
<input class="wpcf7-form-control wpcf7-hidden" value="" type="hidden" name="product-variation" />
<p class="field"><span class="wpcf7-form-control-wrap" data-name="customer-name"><input size="40" class="wpcf7-form-control wpcf7-text wpcf7-validates-as-required input-text" aria-required="true" aria-invalid="false" placeholder="Имя:" value="" type="text" name="customer-name" /></span>
</p>
<p class="field"><span class="wpcf7-form-control-wrap" data-name="customer-email"><input size="40" class="wpcf7-form-control wpcf7-text wpcf7-email wpcf7-validates-as-required wpcf7-validates-as-email input-text" aria-required="true" aria-invalid="false" placeholder="E-mail:" value="" type="email" name="customer-email" /></span>
</p>
<p class="field"><span class="wpcf7-form-control-wrap" data-name="customer-phone"><input size="40" class="wpcf7-form-control wpcf7-text input-text" aria-invalid="false" placeholder="Телефон:" value="" type="text" name="customer-phone" /></span>
</p>
<p class="field"><span class="wpcf7-form-control-wrap" data-name="customer-message"><textarea cols="40" rows="10" class="wpcf7-form-control wpcf7-textarea input-text" aria-invalid="false" placeholder="Сообщение:" name="customer-message"></textarea></span>
</p>
<p class="field"><span class="wpcf7-form-control-wrap" data-name="acceptance-986"><span class="wpcf7-form-control wpcf7-acceptance"><span class="wpcf7-list-item"><label><input type="checkbox" name="acceptance-986" value="1" checked="checked" aria-invalid="false" /><span class="wpcf7-list-item-label">Я соглашаюсь с "<a href="https://aeromotus.ru/privacy-policy/" target="_blank">Политика конфиденциальности</a>"</span></label></span></span></span>
</p>
<p class="field"><span class="wpcf7-form-control-wrap" data-name="checkbox-777"><span class="wpcf7-form-control wpcf7-checkbox"><span class="wpcf7-list-item first last"><label><input type="checkbox" name="checkbox-777[]" value="Прислать мне уведомление о поступлении товара" /><span class="wpcf7-list-item-label">Прислать мне уведомление о поступлении товара</span></label></span></span></span>
</p>
<p class="field"><input class="wpcf7-form-control has-spinner wpcf7-submit button alt" type="submit" value="Запросить цену" />
</p><div class="wpcf7-response-output" aria-hidden="true"></div>
</form>
</div>
</div>
<script type="application/ld+json">{"@context":"https:\/\/schema.org\/","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"item":{"name":"\u0413\u043b\u0430\u0432\u043d\u0430\u044f","@id":"https:\/\/aeromotus.ru"}},{"@type":"ListItem","position":2,"item":{"name":"\u0410\u043a\u0441\u0435\u0441\u0441\u0443\u0430\u0440\u044b \u0438 \u0417\u0430\u043f\u0447\u0430\u0441\u0442\u0438","@id":"https:\/\/aeromotus.ru\/product-category\/aksessuary-i-zapchasti\/"}},{"@type":"ListItem","position":3,"item":{"name":"\u0410\u043a\u043a\u0443\u043c\u0443\u043b\u044f\u0442\u043e\u0440\u044b \u0438 \u0437\u0430\u0440\u044f\u0434\u043d\u044b\u0435 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430","@id":"https:\/\/aeromotus.ru\/product-category\/aksessuary-i-zapchasti\/akkumulyatory-i-zaryadnye-ustrojstva\/"}},{"@type":"ListItem","position":4,"item":{"name":"\u0410\u043a\u043a\u0443\u043c\u0443\u043b\u044f\u0442\u043e\u0440 DJI MATRICE 300 TB 60 Intelligent Flight Battery (Part08)","@id":"https:\/\/aeromotus.ru\/product\/akkumulyator-dji-matrice-300-tb60-intelligent-flight-battery-part08\/"}}]}</script>
<div class="pswp" tabindex="-1" role="dialog" aria-hidden="true">
<div class="pswp__bg"></div>
<div class="pswp__scroll-wrap">
<div class="pswp__container">
<div class="pswp__item"></div>
<div class="pswp__item"></div>
<div class="pswp__item"></div>
</div>
<div class="pswp__ui pswp__ui--hidden">
<div class="pswp__top-bar">
<div class="pswp__counter"></div>
<button class="pswp__button pswp__button--close" aria-label="Закрыть (Esc)"></button>
<button class="pswp__button pswp__button--share" aria-label="Поделиться"></button>
<button class="pswp__button pswp__button--fs" aria-label="На весь экран"></button>
<button class="pswp__button pswp__button--zoom" aria-label="Масштаб +/-"></button>
<div class="pswp__preloader">
<div class="pswp__preloader__icn">
<div class="pswp__preloader__cut">
<div class="pswp__preloader__donut"></div>
</div>
</div>
</div>
</div>
<div class="pswp__share-modal pswp__share-modal--hidden pswp__single-tap">
<div class="pswp__share-tooltip"></div>
</div>
<button class="pswp__button pswp__button--arrow--left" aria-label="Пред. (стрелка влево)"></button>
<button class="pswp__button pswp__button--arrow--right" aria-label="След. (стрелка вправо)"></button>
<div class="pswp__caption">
<div class="pswp__caption__center"></div>
</div>
</div>
</div>
</div>
<script type="text/javascript">
		(function () {
			var c = document.body.className;
			c = c.replace(/woocommerce-no-js/, 'woocommerce-js');
			document.body.className = c;
		})();
	</script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/wp-yandex-metrika/assets/woocommerce.min.js?ver=1.1.7' id='wp-yandex-metrika_woocommerce-js'></script>
<script type='text/javascript' id='wp-yandex-metrika_woocommerce-js-after'>
jQuery(document.body).on('wpym_ec_ready', function(){if (typeof wpym !== 'undefined' && wpym.ec) {wpym.ajaxurl = 'https://aeromotus.ru/wp-admin/admin-ajax.php'; wpym.ec.addData({"hasActiveVariation":false,"detailProductId":11405,"products":{"11405":{"id":"product_id_11405","name":"Аккумулятор DJI MATRICE 300 TB 60 Intelligent Flight Battery (Part08)","price":"87400","category":"DJI Matrice"}},"currency":"RUB"});}})
</script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/contact-form-7/includes/swv/js/index.js?ver=5.7.4' id='swv-js'></script>
<script type='text/javascript' id='contact-form-7-js-extra'>
/* <![CDATA[ */
var wpcf7 = {"api":{"root":"https:\/\/aeromotus.ru\/wp-json\/","namespace":"contact-form-7\/v1"}};
/* ]]> */
</script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/contact-form-7/includes/js/index.js?ver=5.7.4' id='contact-form-7-js'></script>
<script type='text/javascript' id='geoip-detect-js-js-extra'>
/* <![CDATA[ */
var geoip_detect = {"options":{"ajaxurl":"https:\/\/aeromotus.ru\/wp-admin\/admin-ajax.php","default_locales":["ru","en"],"do_body_classes":false,"do_shortcodes":true,"cookie_name":"geoip-detect-result","cookie_duration_in_days":1}};
/* ]]> */
</script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/geoip-detect/js/dist/frontend.js?ver=5.2.0' id='geoip-detect-js-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-includes/js/underscore.min.js?ver=1.13.4' id='underscore-js'></script>
<script type='text/javascript' id='wp-util-js-extra'>
/* <![CDATA[ */
var _wpUtilSettings = {"ajax":{"url":"\/wp-admin\/admin-ajax.php"}};
/* ]]> */
</script>
<script type='text/javascript' src='https://aeromotus.ru/wp-includes/js/wp-util.min.js?ver=3b71e7425f116479de92df27dcaef655' id='wp-util-js'></script>
<script type='text/javascript' id='wc-add-to-cart-variation-js-extra'>
/* <![CDATA[ */
var wc_add_to_cart_variation_params = {"wc_ajax_url":"\/?wc-ajax=%%endpoint%%&elementor_page_id=11405","i18n_no_matching_variations_text":"\u0416\u0430\u043b\u044c, \u043d\u043e \u0442\u043e\u0432\u0430\u0440\u043e\u0432, \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0445 \u0432\u0430\u0448\u0435\u043c\u0443 \u0432\u044b\u0431\u043e\u0440\u0443, \u043d\u0435 \u043e\u0431\u043d\u0430\u0440\u0443\u0436\u0435\u043d\u043e. \u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0434\u0440\u0443\u0433\u0443\u044e \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044e.","i18n_make_a_selection_text":"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u043f\u0446\u0438\u0438 \u0442\u043e\u0432\u0430\u0440\u0430 \u043f\u0435\u0440\u0435\u0434 \u0435\u0433\u043e \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435\u043c \u0432 \u0432\u0430\u0448\u0443 \u043a\u043e\u0440\u0437\u0438\u043d\u0443.","i18n_unavailable_text":"\u042d\u0442\u043e\u0442 \u0442\u043e\u0432\u0430\u0440 \u043d\u0435\u0434\u043e\u0441\u0442\u0443\u043f\u0435\u043d. \u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0434\u0440\u0443\u0433\u0443\u044e \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044e."};
/* ]]> */
</script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/woocommerce/assets/js/frontend/add-to-cart-variation.min.js?ver=7.5.0' id='wc-add-to-cart-variation-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/tinkoff-credit/assets/js/tinkoff-scripts.js?ver=1.2.0' id='tinkoff-credit-scripts-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/woocommerce-bitrix24-integration/resources/compiled/theme/js/app.js?id=d0f2b630ba1eb76279ac&#038;ver=3b71e7425f116479de92df27dcaef655' id='wc-bitrix24-theme-js-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/js_composer/assets/lib/bower/flexslider/jquery.flexslider-min.js?ver=6.5.0' id='flexslider-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/woocommerce/assets/js/photoswipe/photoswipe.min.js?ver=4.1.1-wc.7.5.0' id='photoswipe-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/woocommerce/assets/js/photoswipe/photoswipe-ui-default.min.js?ver=4.1.1-wc.7.5.0' id='photoswipe-ui-default-js'></script>
<script type='text/javascript' id='wc-single-product-js-extra'>
/* <![CDATA[ */
var wc_single_product_params = {"i18n_required_rating_text":"\u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u043f\u043e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u043e\u0446\u0435\u043d\u043a\u0443","review_rating_required":"yes","flexslider":{"rtl":false,"animation":"slide","smoothHeight":true,"directionNav":false,"controlNav":"thumbnails","slideshow":false,"animationSpeed":500,"animationLoop":false,"allowOneSlide":false},"zoom_enabled":"","zoom_options":[],"photoswipe_enabled":"1","photoswipe_options":{"shareEl":false,"closeOnScroll":false,"history":false,"hideAnimationDuration":0,"showAnimationDuration":0},"flexslider_enabled":"1"};
/* ]]> */
</script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/woocommerce/assets/js/frontend/single-product.min.js?ver=7.5.0' id='wc-single-product-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/woocommerce/assets/js/js-cookie/js.cookie.min.js?ver=2.1.4-wc.7.5.0' id='js-cookie-js'></script>
<script type='text/javascript' id='woocommerce-js-extra'>
/* <![CDATA[ */
var woocommerce_params = {"ajax_url":"\/wp-admin\/admin-ajax.php","wc_ajax_url":"\/?wc-ajax=%%endpoint%%&elementor_page_id=11405"};
/* ]]> */
</script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/woocommerce/assets/js/frontend/woocommerce.min.js?ver=7.5.0' id='woocommerce-js'></script>
<script type='text/javascript' id='wc-cart-fragments-js-extra'>
/* <![CDATA[ */
var wc_cart_fragments_params = {"ajax_url":"\/wp-admin\/admin-ajax.php","wc_ajax_url":"\/?wc-ajax=%%endpoint%%&elementor_page_id=11405","cart_hash_key":"wc_cart_hash_93f2a6a934a7a3b173a467fa92e7a54c","fragment_name":"wc_fragments_93f2a6a934a7a3b173a467fa92e7a54c","request_timeout":"5000"};
/* ]]> */
</script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/woocommerce/assets/js/frontend/cart-fragments.min.js?ver=7.5.0' id='wc-cart-fragments-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/ht-mega-for-elementor/assets/js/popper.min.js?ver=2.1.0' id='htmega-popper-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/ht-mega-for-elementor/assets/js/htbbootstrap.js?ver=2.1.0' id='htbbootstrap-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/ht-mega-for-elementor/assets/js/waypoints.js?ver=2.1.0' id='waypoints-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/themes/electro/assets/js/bootstrap.bundle.min.js?ver=3.2.4' id='bootstrap-js-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/elementor/assets/lib/waypoints/waypoints.min.js?ver=4.0.2' id='elementor-waypoints-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/themes/electro/assets/js/typeahead.bundle.min.js?ver=3.2.4' id='typeahead-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/themes/electro/assets/js/handlebars.min.js?ver=3.2.4' id='handlebars-js'></script>
<script type='text/javascript' id='electro-js-js-extra'>
/* <![CDATA[ */
var electro_options = {"rtl":"0","ajax_url":"https:\/\/aeromotus.ru\/wp-admin\/admin-ajax.php","ajax_loader_url":"https:\/\/aeromotus.ru\/wp-content\/themes\/electro\/assets\/images\/ajax-loader.gif","enable_sticky_header":"","enable_hh_sticky_header":"","enable_live_search":"1","live_search_limit":"10","live_search_template":"<a href=\"{{url}}\" class=\"media live-search-media\"><img src=\"{{image}}\" class=\"media-left media-object flip float-start\" height=\"60\" width=\"60\"><div class=\"media-body\"><p>{{{value}}}<\/p><\/div><\/a>","live_search_empty_msg":"\u041d\u0435\u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e \u043d\u0430\u0439\u0442\u0438 \u0442\u043e\u0432\u0430\u0440\u044b, \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u0442\u0435\u043a\u0443\u0449\u0435\u043c\u0443 \u0437\u0430\u043f\u0440\u043e\u0441\u0443","deal_countdown_text":{"days_text":"\u0414\u043d\u0438","hours_text":"\u0427\u0430\u0441\u044b","mins_text":"\u041c\u0438\u043d\u0443\u0442\u044b","secs_text":"\u0421\u0435\u043a\u0443\u043d\u0434\u044b"},"typeahead_options":{"hint":false,"highlight":true},"offcanvas_mcs_options":{"axis":"y","theme":"minimal-dark","contentTouchScroll":100,"scrollInertia":1500}};
/* ]]> */
</script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/themes/electro/assets/js/electro.min.js?ver=3.2.4' id='electro-js-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/themes/electro/assets/js/owl.carousel.min.js?ver=3.2.4' id='owl-carousel-js-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/3d-flipbook-dflip-lite/assets/js/dflip.min.js?ver=1.7.35' id='dflip-script-js'></script>
<script type='text/javascript' src='https://www.google.com/recaptcha/api.js?render=6Legvb8UAAAAADub0ByZCSJmQE7epzSY4AcR8gcI&#038;ver=3.0' id='google-recaptcha-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-includes/js/dist/vendor/regenerator-runtime.min.js?ver=0.13.9' id='regenerator-runtime-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-includes/js/dist/vendor/wp-polyfill.min.js?ver=3.15.0' id='wp-polyfill-js'></script>
<script type='text/javascript' id='wpcf7-recaptcha-js-extra'>
/* <![CDATA[ */
var wpcf7_recaptcha = {"sitekey":"6Legvb8UAAAAADub0ByZCSJmQE7epzSY4AcR8gcI","actions":{"homepage":"homepage","contactform":"contactform"}};
/* ]]> */
</script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/contact-form-7/modules/recaptcha/index.js?ver=5.7.4' id='wpcf7-recaptcha-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/wp-smushit/app/assets/js/smush-lazy-load-native.min.js?ver=3.12.6' id='smush-lazy-load-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/aeromotus-core/src/WooCommerce/Front/js/motus.collapse.js' id='motus-collapse-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/elementor-pro/assets/js/webpack-pro.runtime.min.js?ver=3.11.6' id='elementor-pro-webpack-runtime-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/elementor/assets/js/webpack.runtime.min.js?ver=3.11.5' id='elementor-webpack-runtime-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/elementor/assets/js/frontend-modules.min.js?ver=3.11.5' id='elementor-frontend-modules-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-includes/js/dist/hooks.min.js?ver=4169d3cf8e8d95a3d6d5' id='wp-hooks-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-includes/js/dist/i18n.min.js?ver=9e794f35a71bb98672ae' id='wp-i18n-js'></script>
<script type='text/javascript' id='wp-i18n-js-after'>
wp.i18n.setLocaleData( { 'text direction\u0004ltr': [ 'ltr' ] } );
</script>
<script type='text/javascript' id='elementor-pro-frontend-js-before'>
var ElementorProFrontendConfig = {"ajaxurl":"https:\/\/aeromotus.ru\/wp-admin\/admin-ajax.php","nonce":"28795a2ac7","urls":{"assets":"https:\/\/aeromotus.ru\/wp-content\/plugins\/elementor-pro\/assets\/","rest":"https:\/\/aeromotus.ru\/wp-json\/"},"shareButtonsNetworks":{"facebook":{"title":"Facebook","has_counter":true},"twitter":{"title":"Twitter"},"linkedin":{"title":"LinkedIn","has_counter":true},"pinterest":{"title":"Pinterest","has_counter":true},"reddit":{"title":"Reddit","has_counter":true},"vk":{"title":"VK","has_counter":true},"odnoklassniki":{"title":"OK","has_counter":true},"tumblr":{"title":"Tumblr"},"digg":{"title":"Digg"},"skype":{"title":"Skype"},"stumbleupon":{"title":"StumbleUpon","has_counter":true},"mix":{"title":"Mix"},"telegram":{"title":"Telegram"},"pocket":{"title":"Pocket","has_counter":true},"xing":{"title":"XING","has_counter":true},"whatsapp":{"title":"WhatsApp"},"email":{"title":"Email"},"print":{"title":"Print"}},"woocommerce":{"menu_cart":{"cart_page_url":"https:\/\/aeromotus.ru\/cart\/","checkout_page_url":"https:\/\/aeromotus.ru\/checkout\/","fragments_nonce":"7ba76a5e80"}},"facebook_sdk":{"lang":"ru_RU","app_id":""},"lottie":{"defaultAnimationUrl":"https:\/\/aeromotus.ru\/wp-content\/plugins\/elementor-pro\/modules\/lottie\/assets\/animations\/default.json"}};
</script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/elementor-pro/assets/js/frontend.min.js?ver=3.11.6' id='elementor-pro-frontend-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-includes/js/jquery/ui/core.min.js?ver=1.13.2' id='jquery-ui-core-js'></script>
<script type='text/javascript' id='elementor-frontend-js-before'>
var elementorFrontendConfig = {"environmentMode":{"edit":false,"wpPreview":false,"isScriptDebug":false},"i18n":{"shareOnFacebook":"\u041f\u043e\u0434\u0435\u043b\u0438\u0442\u044c\u0441\u044f \u0432 Facebook","shareOnTwitter":"\u041f\u043e\u0434\u0435\u043b\u0438\u0442\u044c\u0441\u044f \u0432 Twitter","pinIt":"\u0417\u0430\u043f\u0438\u043d\u0438\u0442\u044c","download":"\u0421\u043a\u0430\u0447\u0430\u0442\u044c","downloadImage":"\u0421\u043a\u0430\u0447\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435","fullscreen":"\u0412\u043e \u0432\u0435\u0441\u044c \u044d\u043a\u0440\u0430\u043d","zoom":"\u0423\u0432\u0435\u043b\u0438\u0447\u0435\u043d\u0438\u0435","share":"\u041f\u043e\u0434\u0435\u043b\u0438\u0442\u044c\u0441\u044f","playVideo":"\u041f\u0440\u043e\u0438\u0433\u0440\u0430\u0442\u044c \u0432\u0438\u0434\u0435\u043e","previous":"\u041d\u0430\u0437\u0430\u0434","next":"\u0414\u0430\u043b\u0435\u0435","close":"\u0417\u0430\u043a\u0440\u044b\u0442\u044c"},"is_rtl":false,"breakpoints":{"xs":0,"sm":480,"md":768,"lg":1025,"xl":1440,"xxl":1600},"responsive":{"breakpoints":{"mobile":{"label":"\u0422\u0435\u043b\u0435\u0444\u043e\u043d","value":767,"default_value":767,"direction":"max","is_enabled":true},"mobile_extra":{"label":"\u0422\u0435\u043b\u0435\u0444\u043e\u043d \u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435","value":880,"default_value":880,"direction":"max","is_enabled":false},"tablet":{"label":"\u041f\u043b\u0430\u043d\u0448\u0435\u0442","value":1024,"default_value":1024,"direction":"max","is_enabled":true},"tablet_extra":{"label":"\u041f\u043b\u0430\u043d\u0448\u0435\u0442 \u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435","value":1200,"default_value":1200,"direction":"max","is_enabled":false},"laptop":{"label":"\u041d\u043e\u0443\u0442\u0431\u0443\u043a","value":1366,"default_value":1366,"direction":"max","is_enabled":false},"widescreen":{"label":"\u0428\u0438\u0440\u043e\u043a\u043e\u0444\u043e\u0440\u043c\u0430\u0442\u043d\u044b\u0435","value":2400,"default_value":2400,"direction":"min","is_enabled":false}}},"version":"3.11.5","is_static":false,"experimentalFeatures":{"e_dom_optimization":true,"e_optimized_assets_loading":true,"e_optimized_css_loading":true,"e_font_icon_svg":true,"theme_builder_v2":true,"landing-pages":true,"kit-elements-defaults":true,"page-transitions":true,"notes":true,"loop":true,"form-submissions":true,"e_scroll_snap":true},"urls":{"assets":"https:\/\/aeromotus.ru\/wp-content\/plugins\/elementor\/assets\/"},"swiperClass":"swiper-container","settings":{"page":[],"editorPreferences":[]},"kit":{"active_breakpoints":["viewport_mobile","viewport_tablet"],"lightbox_enable_counter":"yes","lightbox_enable_fullscreen":"yes","lightbox_enable_zoom":"yes","lightbox_enable_share":"yes","lightbox_title_src":"title","lightbox_description_src":"description","woocommerce_notices_elements":[]},"post":{"id":11405,"title":"%D0%9A%D1%83%D0%BF%D0%B8%D1%82%D1%8C%20%D0%90%D0%BA%D0%BA%D1%83%D0%BC%D1%83%D0%BB%D1%8F%D1%82%D0%BE%D1%80%20DJI%20MATRICE%20300%20TB%2060%20Intelligent%20Flight%20Battery%20%28Part08%29%20-%20AEROMOTUS","excerpt":"<div id=\"detailText\">\r\n<div class=\"changeDescription\">\u0410\u043a\u043a\u0443\u043c\u0443\u043b\u044f\u0442\u043e\u0440 DJI MATRICE 300 TB60 Intelligent Flight Battery (Part08) \u0434\u043b\u044f \u043f\u043b\u0430\u0442\u0444\u043e\u0440\u043c\u044b DJI MATRICE 300 RTK (Universal Edition).<\/div>\r\n<\/div>\r\n<div class=\"changePropertiesGroup\"><\/div>","featuredImage":"https:\/\/aeromotus.ru\/wp-content\/uploads\/2020\/08\/4e2ce5c0ff135c9db66c9655a1fb8dfa.png"}};
</script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/elementor/assets/js/frontend.min.js?ver=3.11.5' id='elementor-frontend-js'></script>
<script type='text/javascript' src='https://aeromotus.ru/wp-content/plugins/elementor-pro/assets/js/elements-handlers.min.js?ver=3.11.6' id='pro-elements-handlers-js'></script>
</body>
</html>
    """
    rez = StartPars('', '', '', '', 'CompBattery', txt)
    print(rez)
    print(dir(rez))

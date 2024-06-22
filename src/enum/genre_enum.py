from enum import Enum

class GenreEnum(str, Enum):
    Vehicle = "のりもの"
    Weather_Season = "天気・季節"
    Animal = "生き物"
    Prefectures = "都道府県"
    Sports = "スポーツ"
    Symbols = "記号"
    Other = "その他"
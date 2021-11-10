import json
from collections.abc import Iterable

class ColorizeMixin:
    def __repr__(self):
        return f'\033[1;32;40m{self.title} | {self.price} ₽'


class Convert_json_to_srt:
    """ Class convert string to dict"""
    def __init__(self, sometext):
        for el in sometext:
            self.__dict__[el] = sometext[el]

    def __str__(self):
        return str(self.__dict__)


class Advert:
    """Advert без миксина"""
    def __init__(self, somedict):
        for el in somedict:
            print(somedict[el], type(somedict[el]))
            if not isinstance(somedict[el], dict):
                self.__dict__[el] = somedict[el]
            else:
                self.__dict__[el] = Convert_json_to_srt(somedict[el])
        self.price = self._check_price(self.__dict__)

    def _check_price(self, self_dict):
        if 'price' not in self_dict:
            return 0
        if self.__dict__['price'] < 0:
            print('ValueError: price must be >= 0')
        else:
            return self.__dict__['price']

    #без миксина
    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class Advert2(ColorizeMixin):
    """Advert с миксином"""
    def __init__(self, somedict):
        for el in somedict:
            print(somedict[el], type(somedict[el]))
            if not isinstance(somedict[el], dict):
                self.__dict__[el] = somedict[el]
            else:
                self.__dict__[el] = Convert_json_to_srt(somedict[el])
        self.price = self._check_price(self.__dict__)

    def _check_price(self, self_dict):
        if 'price' not in self_dict:
            return 0
        if self.__dict__['price'] < 0:
            print('ValueError: price must be >= 0')
        else:
            return self.__dict__['price']

#Не получилось
class Rec_class:
    """ Try to do Class with recursion """
    def __init__(self, sometext):
        self.traverse(sometext)

    def traverse(self, sometext):
        if isinstance(sometext, dict):
            for value in sometext:
                print(value, sometext[value])
                #self.__dict__[value] = sometext[value]
                self.traverse(sometext[value])

    def __str__(self):
        return str(self.__dict__)


if __name__ == '__main__':

    adv_str = """{
        "title": "iPhone X",
        "price" : 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"],
            "lol" : {
                "lol1" : 100,
                "lol2" : 200
            }
        }
    }"""

    adv_dict = json.loads(adv_str)

    adv = Convert_json_to_srt(adv_dict)
    print('asdasd')
    print(adv.__dict__.keys())
    print('asdasd')


    adv_ad = Advert2(adv_dict)
    print(adv_ad.__dict__.keys())
    print(adv_ad.__dict__)
    print(adv_ad.price)
    print(adv_ad.location.lol)
    print(adv_ad)

    b = Rec_class(adv_dict)
    print(b.__dict__.keys())
    print(b.__dict__)
    print(b.location.address)

    print('asdasd')









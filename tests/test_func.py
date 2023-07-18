import pytest
#import src.item
from src.item import Item
from src.item import InstantiateCSVError
import os


def test_instantiate_from_csv():
    Item.path_to_file = os.path.join(os.path.dirname(__file__), 'ite.csv')
    with pytest.raises(FileNotFoundError, match='Отсутствует файл items.csv'):
        Item.instantiate_from_csv()


def test_instantiate_from_csv_2():
    Item.path_to_file = 'D://electronics-shop-project//src//item_damage.csv'
    with pytest.raises(InstantiateCSVError, match='Файл items.csv поврежден'):
        Item.instantiate_from_csv()


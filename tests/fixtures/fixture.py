import pytest


@pytest.fixture
def auto_data():
    return {'Mark': 'BMW',
            'Country': 'Германия',
            'Body type': 'Седан',
            'Transmission': 'Автомат',
            'Color': 'Черный',
            'Model': 'F90',
            'Price': '5000000',
            'Power': '625'}

import pytest
from Question4 import GetShortestDistanceBetweenCities
testcases =[
    ('Nathiagali',[('Islamabad', 'Murree', 49), ('Murree', 'Nathiagali', 36)]),
    ('Naran',[('Islamabad', 'Murree', 49), ('Murree', 'Nathiagali', 36), ('Nathiagali', 'Abbottabad', 34), ('Abbottabad', 'Mansehra', 23), ('Mansehra', 'Balakot', 37), ('Balakot', 'Kaghan', 59), ('Kaghan', 'Naran', 22)]),
    ('Murree',[('Islamabad', 'Murree', 49)]),
    ('Kaghan',[('Islamabad', 'Murree', 49), ('Murree', 'Nathiagali', 36), ('Nathiagali', 'Abbottabad', 34), ('Abbottabad', 'Mansehra', 23), ('Mansehra', 'Balakot', 37), ('Balakot', 'Kaghan', 59)]),
    ('Hunza',[('Islamabad', 'Murree', 49), ('Murree', 'Nathiagali', 36), ('Nathiagali', 'Abbottabad', 34), ('Abbottabad', 'Mansehra', 23), ('Mansehra', 'Balakot', 37), ('Balakot', 'Kaghan', 59), ('Kaghan', 'Naran', 22), ('Naran', 'Chilas', 113), ('Chilas', 'Hunza', 306)])
]

@pytest.mark.parametrize("i", range(len(testcases)))
def test_GetShortestDistanceBetweenCities(i):
    assert GetShortestDistanceBetweenCities("Islamabad",testcases[i][0]) == testcases[i][1]
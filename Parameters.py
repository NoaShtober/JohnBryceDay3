import pytest

'''
@pytest.mark.parametrize(
    'input, expected_output, desc',
    [
        (10, 20, 'positive numbers'),
        (0, 0, 'zero values'),
        (-5, -10, 'negative values'),
        (2, 6, 'failed values')

    ]

)

def test_Multiple1(input, expected_output, desc):
    print('start test for', desc)
    res = input * 2
    assert res == expected_output, 'Assert found'
'''

@pytest.mark.parametrize(
    'input, expected_output, desc',
    [
        ('Gal', 3, 'Gal'),
        ('Lior', 4, 'Lior'),
        ('Aviel', 4, 'Aviel'),
        ('Noa', 4, 'Noa')

    ]

)

def test_Multiple2(input, expected_output, desc):
    print('start test for', desc)
    res = len(input)
    assert res == expected_output, 'Assert found'

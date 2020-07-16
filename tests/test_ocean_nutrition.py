from ocean_nutrition import __version__

def test_version():
    assert __version__ == '0.1.0'


def test_product_scanner():
	product_id = '7613033538452'
	expected =  'Smarties'
	actual = 
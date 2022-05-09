import minji

data = "data/chocolate.csv"
def test_rangescore():
	test_range = minji.rangeScore(data['Rating'])
	assert isinstance(test_range[0], str)


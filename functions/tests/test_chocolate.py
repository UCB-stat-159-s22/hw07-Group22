import pytest
import pandas as pd
import numpy as np
from collections import Counter
import re
import matplotlib.pyplot as plt
from IPython.display import display_html
from functions.utils import *

data = "data/chocolate.csv"

def test_charac():
    charac_Malaysia = country_common_charac(chocolate, 'Malaysia')
    frequency_output = charac_Malaysia['frequency'].tolist()

    assert isinstance(charac_Malaysia, pd.DataFrame)
    assert len(charac_Malaysia.columns) == 3
    assert type(frequency_output[0]) == int
    
    
def test_rangescore():
	test_range = rangeScore(data['Rating'])
	assert isinstance(test_range[0], str)

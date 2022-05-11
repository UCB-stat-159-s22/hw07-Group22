# Chocolate Bar Analysis

### UC Berkeley Stat 159/259 Reproducible and Collaborative Statistical Data Science
#### Spring 2022 final project 

Binder Link: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-s22/hw07-Group22.git/HEAD?labpath=main.ipynb)

Github Page: https://ucb-stat-159-s22.github.io/hw07-Group22/

*Group members:*

* Lia Chin-Purcell
* Minji Park
* Runting Han
* Jenea Spinks

## Dataset
The dataset used in this analysis contains overall 2,500 plain dark chocolate bars rating.

This can be found at the following link:
http://flavorsofcacao.com/chocolate_database.html

## Project Goals

1. Analyze the difference of cocoa percent in different chocolate bars produced by different companies and analyze whether the cocoa percent in different chocolate bars has changed over years.

2. Analyze the characteristics used to describe different chocolate bars and see if cocoa beans from a specific country of bean origins has a unique, standout characteristic.

3. Analyze the most memorable charactersitics and cocoa percent in chocolate bars by separating review rating ranges. 

4. Analyze high and low average ratings for company locations and see if ingredients used at those locations contribute to those ratings.

5. Regresssion analysis to determine memorable characteristics that have significant inlfuence on ratings.

## Installation and Environment
## Installation
This project can currently only be installed from source, via
```
pip install .
```

## Make
For automization, this project includes a Makefile that has an `env`  target to make an environment with all necessary libraries and an `all`  target that runs all the notebooks.

You can run the `env` target via:
```
make env
```

and the `all` target via:
```
make all
```

## Tests
You can run the project test suite via
```
pytest functions
```

## License
This project is released under the terms of the BSD 3-clause License.



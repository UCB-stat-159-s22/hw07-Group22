#Makefile

.PHONY: env
env: 
	mamba env create -f environment.yml 
	bash -ic 'conda activate chocolate;python -m ipykernel install --user --name chocolate --display-name "IPython - chocolate"'
	
.PHONY : all
all :
	jupyter execute analysis_notebooks/ingredients_analysis.ipynb
	jupyter execute analysis_notebooks/analysis_for_review_ratings.ipynb
	jupyter execute analysis_notebooks/most_memorable_characteristic_regression.ipynb
	jupyter execute analysis_notebooks/Cocoa_percent_change_analysis.ipynb
	jupyter execute analysis_notebooks/common_charac_for_country_analysis.ipynb
	jupyter execute main.ipynb
	

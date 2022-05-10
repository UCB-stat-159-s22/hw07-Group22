#Makefile

.PHONY: env
env: 
	mamba env create -f environment.yml 
	bash -ic 'conda activate chocolate;python -m ipykernel install --user --name chocolate --display-name "IPython - chocolate"'
	
.PHONY : all
all :
	jupyter execute ingredients_analysis.ipynb
	jupyter execute minji.ipynb
	jupyter execute lia_notebook.ipynb
	jupyter execute Cocoa_percent_change_analysis.ipynb
	jupyter execute common_charac_for_country_analysis.ipynb
	jupyter execute main.ipynb
	
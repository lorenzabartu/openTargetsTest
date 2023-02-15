# openTargetsTest
Open Targets Software Developer Technical Test

JSON Dataset Mining: Disease, Targets, Evidence: Eva

## Description

This script works with JSON across three categorized datasets: targets, diseases, and sourceId=eva. 

## Getting Started

This is a python script that depends largely on the python library Pandas, and makes use on Numpy. 
Other modules used in the script are come with python. 

### Dependencies

* Libraries needed before installing program: 
   - Pandas (Installation: https://pandas.pydata.org/docs/getting_started/install.html) 
   - Numpy (Installation: https://numpy.org/install/)


### Installing

To run this program the following need to occur: 
	
  1. Download the targets, diseases, and evidence/sourceId=eva from 
	   http://ftp.ebi.ac.uk/pub/databases/opentargets/platform/21.11/output/etl/
  2. Group all datasets into a folder -- this path will be required to run the script
  3. Download the script from this GitHub repository

### Executing program

Run the program: 
	
  1. Open terminal 
	
  2. Change directory to location of script with a "cd" command (i.e. cd /Users/lorenzabartu/Desktop/)
	
  3. Execute the program: 
		 python combining_data.py path/to/dataset/	
     
     For example, if each dataset folder was held within an overarching folder "datasets" 
     in the directory you're in, then you would run this line: 
     
     python combining_data.py datasets/	
    

### Outputs: 

1. To your set directory a JSON file entitled "output.json" will be created. 
- The file has JSON fields: ‘targetId’, ‘diseaseId’, ‘median’, ‘top3’, ‘approvedSymbol’, ‘name’.
- The file is organized by ascending median score values. 
2. To the command line, a statement will be printed sharing the number of target-target pairs that share a connection to at least two diseases.
## Help

1. Ensure that all three dataset folders are in the same overarching folder. 
2. The script relies on the folder names being consistent with the OpenTargets naming ("targets", "diseases", "sourceId=eva")

## Authors

Contributors names and contact info

Lorenza Bartu
Email: lorenzabartu@gmail.com


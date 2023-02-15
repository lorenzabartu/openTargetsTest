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
    

### Overarching flow of program 

Once the script is called it will: 

	- Parse all json files in each of the three separate folders and merge them all respectively: 
		* i.e. all JSON files from the disease folder are merged
	- Begin with evidence JSON
		- A DataFrame is created 
## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Lorenza Bartu

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)

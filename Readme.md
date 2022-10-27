## Python script is written to get the data from https://datausa.io/api/data?drilldowns=Nation&measures=Population and display the output in the given format.

## Prerequisites:
1. Install python version 3 and above

## Steps to run
1. Open terminal window and run the below command 
 pip3 install -r requirements.txt
2. To run the script run the below commans
  python3 src/main.py

image.png


## Test to run 
1. Change the url parameters to incorrect value to display the error message
2. Exception will be thrown if the getAPI response is not 2XX.
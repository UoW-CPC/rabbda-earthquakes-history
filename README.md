# rabbda-earthquakes-history

## Introduction
This application comes alongs with a series of solutions that aim to demonstrate how Big Data can be used to create complex and real-life Big Data applications.

Specifically, with this application, we present how to acquire historical data from Rest APIs and store them to Hadoop HDFS.

The data source for this demo is related to earthquakes, source: [USGS science for a changing world](https://earthquake.usgs.gov).

USGS provides a [Rest API](https://earthquake.usgs.gov/fdsnws/event/1/) which will be using to request earthquakes data.
Sample request in csv format: [earthquakes](https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=2020-02-18T00:00:00.000Z&endtime=2020-02-19T00:00:00.000)

The steps to store these data to HDFS are the following:
 1. Give as input, years and earthquakes magnitude to be requested. 
 2. For each year, request the data from the Rest API.
 3. Pre-process the data to remove headers and format earthquakes date and time.
 3. Save the data to the host machine.
 4. Upload the data to HDFS.
 
 ## Getting started
 These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
 
 ### Download the repository
 The initial step is to download the repository in your Hadoop machine. To do so, run in terminal the following command:
 ```
 git clone https://github.com/UoW-CPC/rabbda-earthquakes-history.git
 ```
 
 ### Running the application
 Having download the repository you can now run the application.
 First move to the working directory by executing the command:
 ```
 cd rabbda-earthquakes-history
 ``` 
 Now execute the command:
 ```
 ls
 ```
 There you can see a folder and two files:
 * _earthquakes_, folder which contains python scripts used to perform steps 1-5 mentioned in the introduction paragraph. 
 * _requirements.txt_, file used to install packages used by python scripts.
 * _README.md_, project description file.
 
 #### Requirements installation
 
 At this phase __install the requirements__ by running the command:
 
 ```
 pip install -r requirements.txt
 ```
 
 #### Run the Python application
 
 Having install the requirements you can now __run the python application__. 
 
 Move to the earthquakes folder:
 ```
 cd earthquakes
 ```
 To initialise the application you must execute the earthquakes script. 
 The script can take input parameters by using the following options:
  

 ```
 Options:
 
 -p, --hdfs-path=           HDFS path to upload the data [Required]
 -y, --year=                Download earthquakes for a list of years [Required - Option 1]
 -f, --from-year=           Download earthquakes from this year [Required - Option 2]
 -t, --to-year=             Download earthquakes until this year [Required - Option 2]
 -m, --magnitude-over=      Download earthquakes with magnitide-over input value (Default value 0.0) [Optional]
 -o, --overwrite            Instruct the application to download again earthquakes that has been downloaded before [Optional]
 ```
 Initialisation commands:
 
 __Example 1:__ Download all earthquakes for the given years.
 ``` 
 # The program sorts input years and starts the downloading process from year 1980.
 python earthquakes.py -p /user/earthquakes/ -y 2010,2005,1980 
 ```
 __Example 2:__ Download all earthquakes for the given range of years.
 ```
 # The program starts the downloading process for years 2003,2004,2005.
 python earthquakes.py -p /user/earthquakes/ -f 2003 -t 2005 
  ```
 In case you have first run Example 1, the program will download only earthquakes for years 2003 and 2004.
 This is because application stores in its internal database past requests for years and related magnitude
 so to avoid possible data duplication.  
 
 To force downloading also year 2005, you need to pass the _overwrite option_.
 ```
 # The program starts the downloading process for years 2003,2004,2005 with overwrite option active.
 python earthquakes.py -p /user/earthquakes/ -f 2003 -t 2005 -o 
 ```
 __Example 3:__ Download earthquakes for the year 2020 with magnitude over 6.5. 
 ```
 # The program downloads erthquakes for year 2020 with magnitude over 6.5
 python earthquakes.py -p /user/earthquakes/ -y 2020 -m 6.5 
 ```
 
 To see the results open a new terminal and move to the repository directory. There, you can see a new directory, _data_.
 Move into this folder; there you can find files for each input year and requested magnitude. 
 For instance, for _example 3_ the file will be _earthquakes2020mag6.5.csv_.
 
 At this point, we have verified the data in the local machine.
 

 
 #### Uploading the data in HDFS
 
 When the program finish downloading earthquakes for a specific year, it upload the related file
 to HDFS.  
 

 Finally, __go to Ambari Files View__ in the path specified previously and check file availability to HDFS.
 
 ## Architecture
<img width="732" alt="architecture" src="https://user-images.githubusercontent.com/32298274/75445139-bebad500-595c-11ea-830f-9850fa0e7dd0.png">




[Demo video](https://drive.google.com/open?id=1cVJDfO616nggClPJWdOQ2HOVEvEpF7tF)
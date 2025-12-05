# formula1_db
Formula 1 database containing analytical data on drivers, constructors, circuits, races, results, pitstops, driver and constructor standings.


# Data Description
The data in this database is a historical data of numerous formula 1 races and their details. The data was obtained through kaggle.com. The initial dataset contained all the data from the years 1950 to 2017, however, I had to cut most of it out since some tables contained over 25 thousand rows, which made it hard to work with it. This created problems of its own, for example the pitStop table had entries starting from raceId 842, but my race table only contained the first 300 rows. However, most tables worked well with one another and contained a lot of valuable results.

# Execution
All files can be executed easily. After you restore a database dump, you can run all the queries using the ```front_end.py``` script. The only modification needed is changing the password to the password of your local mySQL server.

# Grading
I expect to recieve an A for this assignment because I completed Level 2 schema, Level 2 queries, and a python code and I closely followed the guidelines. I also included the schema, and an ER diagram as well as a screen recording of a test run of my python script. This, according to the rubrick, should allow me to recieve a grade between 90-100.

# Challenges
Apart from the already mentioned piStop issue, I faced two more major challenges. The first one was the issue with special characters in the dataset. Some driver or circuit names contain letters not present in English alphabet and were incorrectly percieved during the import. An example would be a Spanish "é", or Finnish "ä". I had to manually go through the data set and change these letters to their analogies in English alphabet, which took a long time, since they also had to be changed inside wikipedia links. 

The second challenge was also with formating of the data. Many data rows missed specific information which wasn't required. However, where the information was missing, the value wasn't NULL, but an empty string, or just an empty field. That made inserts complicated too, because values like INT explect a NULL and do not accept the given format. Therefore, some variables had to be altered to VARCHARs where the data type did not matter that much. For example the latitude or longitude of racetracks. Even though they are numeric values, in the database they are represented as strings.

# Final Thoughts
This project taught me a lot about the practical experience of creating and managing a database and I got a depper understanding of MySQL language. I hope I was able to demonstrade the required tasks and provide useful data analysis solutions.

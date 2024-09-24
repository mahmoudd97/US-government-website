# US-government-website
we use Python to transform raw data from source into a comprehensive, ready-to-analyze dataset.

Script do:
•	Take a three arguments from the user: 
o	-i: The input files path
o	-o: The output files path
o	-u: optional parameter; if passed the timestamps in data will be kept in UNIX format, if not, convert it to timestamp 
•	Reads JSON file from a directory that the user entered.
•	Extracts the data and cleans and transforms it.
•	Print the number of records of the entered path.
•	Check if the files have any duplicates and remove them.
•	Uses the optional argument "-u" to maintain the UNIX format for the timestamp, otherwise convert it to human readable timestamp format.
•	Prints a message after converting the files with the number of rows transformed and the file's path.
•	Create a CSV file containing the final output in a CSV format, and save the output file in the output path provided by the user.
•	Prints the total execution time.

Introduction
Movie Trailer is a Python program that create an HTML page with a listing of six of my favourite movies.  The page
will display six tiles, with the poster for the movie, the BBFC classification, the name of the movie and my story line
for the movie.

Files included?
In the download you will find the following files
1) coconut_water.py
2) entertainment_centre.py
3) media.py
4) coconut_water.html

Getting Started
1) Download the zipped file MovieTrailer.zip
2) Extract all the files by unzipping the file
3) Execute the entertainment_centre.py file, you will need to have Python 2.7.9 to view the  output

Downloading and installing Python
Go to https://www.python.org/downloads/release/python-279/
follow the download and installation notes on this site

When you execute the entertainment_centre.py file the coconut_water.html file will be overwritten with the last
execution of the program.

coconut_water.py is inspired from fresh_tomatoes.py.  Majority of the work is fresh_tomatoes with some modifications.
- Title name change
- background colour of the web page change
- tile hover behaviour change to include a colour
- classification image is now displayed on the web page
- the duration, story line is also displayed

The design of the program uses Parent and sub-classes in the media file.  This will make further development easier
to implement when TV shows are included.

There are two class variables BBFC_RATING and RATING_URL.


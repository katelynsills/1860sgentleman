1860s Gentleman
==============
>"One should not be simply ill-dressed, but simply well-dressed."

>"At any rate Nature knows best, and no man need be ashamed of showing his manhood in the hair of his face."


A simple Twitter bot written in python that tweets 1860's advice from ["The Gentlemen's Book of Etiquette and Manual of Politeness"](http://www.gutenberg.org/files/39293/39293-h/39293-h.htm).

How to Make Your Own
---------------
Clone the repository.

The key to creating a good twitter bot is choosing the source material. I've found old books to be a fantastic source.

After you've picked your source, download the text file. Eventually, we will be splitting up the text into tweetable chunks, so you'll want to take out anything that you don't want to tweet (titles, chapter titles, gutenburg copywrite statements, etc.) Resave the file to the same folder as the code.

Edit the code
----------
You'll need to change 'gentsguide.txt' in tweetadvice.py to whatever your source file is named. 

Create a twitter account and app.
------

Next, create a twitter account for your tweets, and follow these [6-step instructions](http://iag.me/socialmedia/how-to-create-a-twitter-app-in-8-easy-steps/) for creating a twitter app. Make sure to request read and write privileges and create an access token. Keep your consumer key, consumer secret, access token key and access token secret handy. You'll need them for posting your tweets automatically.

Put in your access credentials
------
(Macs) Create a file called ".env" in the folder and put in your access credentials like so: 

T_CONSUMER_KEY = "insert-here"
T_CONSUMER_SECRET = "insert-here"
T_ACCESS_TOKEN_KEY = "insert-here"
T_ACCESS_TOKEN_SECRET = "insert-here"

Run your app
-------
You can run your app from the terminal by entering "python tweetadvice.py." This will push a tweet to your twitter feed, but will not do it continuously. To make it run continuously, you can schedule it to run on a server or application platform like Heroku. 

Create a free heroku app to run your bot
--------
Create an account with heroku. Then, in the command line, type:

    git add .
    git commit -m "init"
    heroku create
    git push heroku master
    heroku ps:scale web=1

    
This should launch your app. Next, use the free scheduler add-on to run your app at intervals of every 10 minutes, every hour, or every day. 


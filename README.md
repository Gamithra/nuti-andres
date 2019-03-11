# Vargamäe Nuti-Andres

**A twitter bot that generates random sentences based on Anton Hansen Tammsaare's "Tõde ja Õigus" books using the markov chain implementation [markovify](https://github.com/jsvine/markovify) made by jsvine.**

See what the bot's been up to: [Vargamäe Nuti-Andres on Twitter](https://twitter.com/tammsaarebot)

----
## Can i try it?
Yes! Just clone the repository and create a file named config.py, where you specify the following variables:

    project_path = /path/to/repo/ #ends with a slash!

    consumer_token = "your twitter app consumer token"
    consumer_secret = "your twitter app consumer secret"
    token_key = "your twitter app OAuth Access Token"
    token_secret = "your twitter app OAuth Access Token Secret"


###### To generate a new sentence and post it on Twitter, run:
    python3 markov-tammsaare.py

To run the script at a regular interval, check the crontab_entry, specify the path to the repository and add the file to /etc/cron.d/.

###### To generate 15 new sentences and add them to the queue (found at *tode-queue.txt* at the root folder), run:
    python3 fill-queue.py



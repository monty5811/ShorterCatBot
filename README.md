ShorterCatBot
=============

Small Twitter bot to sequentially tweet the Westminster Shorter Catechism daily.

Only requirement is [tweepy](https://github.com/tweepy/tweepy). Install with `pip install tweepy`

Bot is set up to run as a cron job: `0 17 * * * cd ~/shortercatbot/ && python shorter_cat_bot.py`
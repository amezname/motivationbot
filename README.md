# motivationbot
This script sends a daily motivational quote randomly in the day to any phone number using Sendgrid. There are 30,000 different motivational quotes scraped from Twitter.

![quote_small](https://user-images.githubusercontent.com/77634962/152586779-71eee515-c77e-428d-b7c9-319dd324ccd6.jpg)

Steps: 


First create a free Sendgrid account and create an API key:

https://app.sendgrid.com/settings/api_keys

Update config.py with:
	
-Your API key

-Phone number

-Mobile carrier

Run motivational.py script daily at 8 am by scheduling a cron job. This will send the text out randomly during the day between 8 am and 5 pm.

https://gavinwiener.medium.com/how-to-schedule-a-python-script-cron-job-dea6cbf69f4e

https://www.geeksforgeeks.org/how-to-schedule-python-scripts-as-cron-jobs-with-crontab/


To use another users tweets, update twitter_scraper.py: 

	keyword = 'from:username'

Use your own image backgrounds. For reference, I sized all my images to 900x1200



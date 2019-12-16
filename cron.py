import schedule
import time
import os

# Call main Python file
def job():
    os.system('python main.py')

# Run this FOREVER MUAHAHHAHAHAHHAHA
schedule.every().day.at("09:30").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)

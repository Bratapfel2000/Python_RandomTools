#doing task at specific time
import schedule
import time

def task():
    print("Do task now")

schedule.every().day.at("11:15").do(task)

while True:
    schedule.run_pending()
    time.sleep(1)

from utils import scraper

import schedule
import time

def main():
    print("[!] Script started.")

    schedule.every().day.at('15:40').do(lambda: scraper.scrape_websites())

    while True:
        schedule.run_pending()
        time.sleep(10)

    
if __name__ == "__main__":
    main()
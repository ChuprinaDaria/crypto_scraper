import requests
import json
import csv
import time
import re
import pandas as pd
import random
import html as _html

from tqdm import tqdm

from constants.config import FOLDER_ID, GOOGLE_API

from bs4 import BeautifulSoup
from DrissionPage import ChromiumPage
from datetime import datetime

from .decrypt import decrypt_cryptojs_aes_json

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials
from google.oauth2 import service_account

def scrape_websites():

    # CSV INIT
    try:
        print("Scraper started..")
        start = time.time()
        init_csv()
        end = time.time()
        print(f"CSV initialized | Time taken: {(end - start) / 60:.2f} minutes")
    except Exception as e:
        print(f"[-] An unhandled error occured while initialising CSV: {e}")
        pass
    
    # BS4
    try:
        print("[IN PROGRESS] IcoDrops")
        start = time.time()
        icodrops()
        end = time.time()
        print(f"[FINISHED] IcoDrops | Time taken: {(end - start) / 60:.2f} minutes")
    except Exception as e:
        print(f"[-] An unhandled error occured while IcoDrops scraping: {e}")


    # REQUESTS
    try:
        print("[IN PROGRESS] CoinMarketCap")
        start = time.time()
        coinmarketcap()
        end = time.time()
        print(f"[FINISHED] CoinMarketCap | Time taken: {(end - start) / 60:.2f} minutes")
    except Exception as e:
        print(f'[-] An unhandled error occured while CoinMarketCap scraping: {e}')
        pass

    # DRISSION PAGE
    try:
        print("[IN PROGRESS] Coingecko")
        start = time.time()
        coingecko()
        end = time.time()
        print(f"[FINISHED] Coingecko | Time taken: {(end - start) / 60:.2f} minutes")
    except Exception as e:
        print(f"[-] An unhandled error occured while Coingecko scraping: {e}")
        pass
    
    # DRISSION PAGE
    try:   
        print("[IN PROGRESS] IcoLink")
        start = time.time()
        icolink()
        end = time.time()
        print(f"[FINISHED] IcoLink | Time taken: {(end - start) / 60:.2f} minutes")
    except Exception as e:
        print(f"[-] An unhandled error occured while Icolink scraping: {e}")
        pass


    # BS4
    try:
        print("[IN PROGRESS] CryptoRank")
        start = time.time()
        cryptorank()
        end = time.time()
        print(f"[FINISHED] CryptoRank | Time taken: {(end - start) / 60:.2f} minutes")
    except Exception as e:
        print(f"[-] An unhandled error occured while CryptoRank scraping: {e}")
        pass
    
    # BS4
    try:
        print("[IN PROGRESS] Cryptototem")
        start = time.time()
        cryptototem()
        end = time.time()
        print(f"[FINISHED] Cryptototem | Time taken: {(end - start) / 60:.2f} minutes")
    except Exception as e:
        print(f"[-] An unhandled error occured while CryptoRank scraping: {e}")
        pass
    
    
    # BS4
    try:
        print("[IN PROGRESS] Gemfinder")
        start = time.time()
        gemfinder()
        end = time.time()
        print(f"[FINISHED] Gemfinder | Time taken: {(end - start) / 60:.2f} minutes")
    except Exception as e:
        print(f"[-] An unhandled error occured while Gemfinder scraping: {e}")
        pass

    # DRISSION PAGE
    try:
        print("[IN PROGRESS] CoinSniper")
        start = time.time()
        coin_sniper()
        end = time.time()
        print(f"[FINISHED] CoinSniper | Time taken: {(end - start) / 60:.2f} minutes")
    except Exception as e:
        print(f"[-] An unhandled error occured while CoinSniper scraping: {e}")
        pass
    
    # BS4
    try:
        print("[IN PROGRESS] Icomarks")
        start = time.time()
        icomarks()
        end = time.time()
        print(f"[FINISHED] Icomarks | Time taken: {(end - start) / 60:.2f} minutes")
    except Exception as e:
        print(f"[-] An unhandled error occured while IcoMarks scraping: {e}")
        pass
    
    # BS4
    try:
        print("[IN PROGRESS] IcoHolder")
        start = time.time()
        icoholder()
        end = time.time()
        print(f"[FINISHED] IcoHolder | Time taken: {(end - start) / 60:.2f} minutes")
    except Exception as e:
        print(f"[-] An unhandled error occured while Icoholder scraping: {e}")
        pass
    
    # DRISSION PAGE
    try:
        print("[IN PROGRESS] DexTools")
        start = time.time()
        dextools()
        end = time.time()
        print(f"[FINISHED] DexTools | Time taken: {(end - start) / 60:.2f} minutes")    
    except Exception as e:
        print(f"[-] An unhandled error occured while DexTools scraping: {e}")
        pass
    
    # PACKING DATA
    try:
        print("All websites scraped.. Preparing to remove duplicates..")
        remove_duplicates('data.csv')
        pack_to_sheet('data.csv', '1AJXIfme6zgji5IeWrHZOazGtbeQ_gf5V')
        print("Duplicates removed!")
    except Exception as e:
        print(f'An unhandled error occured while packing data: {e}')
        pass


def icodrops():
    cookies = {
        'header_banner': '0',
        'timezone': 'Europe/Chisinau',
        '_ym_uid': '1745310954260032514',
        '_ym_d': '1745310954',
        'csrftoken': 'sHswhWwTR9K7tLjptQsoMJJnPKsIzgha',
        '_ym_isad': '1',
        '_dd_s': 'logs=1&id=a92ffd88-4ca5-4448-a377-9bee404f5f19&created=1745519860399&expire=1745520776361',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'priority': 'u=1, i',
        'referer': 'https://icodrops.com/category/active-ico/',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        # 'cookie': 'header_banner=0; timezone=Europe/Chisinau; _ym_uid=1745310954260032514; _ym_d=1745310954; csrftoken=sHswhWwTR9K7tLjptQsoMJJnPKsIzgha; _ym_isad=1; _dd_s=logs=1&id=a92ffd88-4ca5-4448-a377-9bee404f5f19&created=1745519860399&expire=1745520776361',
    }

    params = {
        'page': '1',
        'paginate': '250',
    }

    response = requests.get('https://icodrops.com/category/active-ico/', params=params, cookies=cookies, headers=headers)
    
    data = response.json()

    soup = BeautifulSoup(data['rendered_html'], 'html.parser')
    
    lists = soup.find_all('li', class_='Tbl-Row Tbl-Row--usual')


    for item in tqdm(lists, total=len(lists)):
        time.sleep(1)

        with open('data.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            project_name = item.find('p', class_='Cll-Project__name').text.strip()
            project_slug = item.find('a', class_='Cll-Project__link').get('href')
            
            project_page = requests.get(f'https://icodrops.com{project_slug}', headers=headers)

            if project_page.status_code == 200:
                soup = BeautifulSoup(project_page.text, 'html.parser')

                links_container = soup.find('ul', class_='Project-Page-Header__links-list')
                links = links_container.find_all('li')

                website = "N/A"
                telegram = "N/A"
                twitter = "N/A"

                for link in links:
                    link_href = link.a['href'] if link.a else "N/A"
                    link_text = link.find('span').text.strip() if link.find('span') else ""

                    if 'Website' in link_text:
                        website = link_href

                        try:
                            website_info = requests.get(website, timeout=10).text
                            website_soup = BeautifulSoup(website_info, 'html.parser')

                            mailtos = list(set(a['href'].replace("mailto:", "") for a in website_soup.find_all('a', href=True) if a['href'].startswith("mailto:")))
                            email = ";".join(email for email in mailtos)

                        except Exception as e:
                            print(f"[icodrops] {e}")
                            pass

                    elif "t.me" in link_href:
                        telegram = link_href
                    elif re.match(r'^https://x\.com/[a-zA-Z0-9_-]+$', link_href):
                        twitter = link_href

                writer.writerow([project_name, website, email, telegram, "telegram admins will be here", twitter, f"https://icodrops.com{project_slug}"])
            else:
                print(f"Failed to fetch project page for {project_name}. Status code: {project_page.status_code}")

def icolink(): 

    driver = ChromiumPage()

    driver.get('https://icolink.com/ico-list/upcoming-ico.html/?start=0')

    driver.scroll.to_bottom()

    coins_container = driver.ele('.uk-child-width-1-1 uk-grid-medium uk-grid-match uk-grid uk-grid-stack')

    for coin in tqdm(coins_container.children()):
        link = coin.ele('tag:a').link
        
        with open('data.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)

            coin_info = requests.get(link)
            soup = BeautifulSoup(coin_info.text, 'html.parser')

            try:
                telegram = soup.find('div', class_='row_telegramlink').span['rel'].replace('tel:', "")
                website = soup.find('div', class_='row_3_website').span['rel']
                twitter = soup.find('div', class_='row_5_twitterlink').span['rel']
                name = soup.find('h1', attrs={'itemprop': 'name'}).text.strip().split(maxsplit=1)[1]

                website_info = requests.get(website, timeout=10).text
                website_soup = BeautifulSoup(website_info, 'html.parser')

                mailtos = list(set(a['href'].replace("mailto:", "") for a in website_soup.find_all('a', href=True) if a['href'].startswith("mailto:")))
                email = ";".join(email for email in mailtos)
            
            except Exception as e:
                print(f"[icolink] {e}")
                continue

            writer.writerow([name, website, email, telegram, "telegram admins will be here", twitter, link])

    driver.close()


def coinmarketcap():
    headers = {
        'x-request-id': 'a0d19b7b0b154acaa7d687b705a5686b',
        'sec-ch-ua-platform': '"macOS"',
        'cache-control': 'no-cache',
        'Referer': 'https://coinmarketcap.com/',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'platform': 'web',
    }

    params = {
        'dataType': '8',
        'limit': '500',
        'start': '1',
    }

    response = requests.get('https://api.coinmarketcap.com/data-api/v3/cryptocurrency/spotlight', params=params, headers=headers)

    data = response.json()

    recently_added = data['data']['recentlyAddedList']

    with open('data.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)

        for item in tqdm(recently_added):

            time.sleep(1)

            name = item['name']
            link = f"https://coinmarketcap.com/currencies/{item['slug']}"

            coin_info = requests.get(link, headers=headers)
                    
            soup = BeautifulSoup(coin_info.text, 'html.parser')
            data_wrapper = soup.find('script', id='__NEXT_DATA__')

            if data_wrapper:
                json_content = data_wrapper.string
                parsed_json = json.loads(json_content)

                try:
                    page_details = parsed_json['props']['pageProps']['detailRes']['detail']
                    website = page_details['urls']['website'][0] if not None else "N/A"
                    telegram = "".join(link for link in page_details['urls']['chat'] if 't.me' in link)
                    twitter = ";".join(link for link in page_details['urls']['twitter'] if link)

                    website_info = requests.get(website, timeout=10).text
                    website_soup = BeautifulSoup(website_info, 'html.parser')

                    mailtos = list(set(a['href'].replace("mailto:", "") for a in website_soup.find_all('a', href=True) if a['href'].startswith("mailto:")))
                    email = ";".join(email for email in mailtos)
    
                except Exception as e:
                    print(f"[coinmarketcap] {e}")
                    pass
            
            writer.writerow([name, website, email, telegram, "telegram admins will be here", twitter, link])


def coingecko():
    
    driver = ChromiumPage()

    for index in tqdm(range(1, 10)):
        driver.get(f'https://www.coingecko.com/en/new-cryptocurrencies?page={index}')

        coin_table = driver.ele('.tw-divide-y tw-divide-gray-200 tw-min-w-full dark:tw-divide-moon-700').children()
        
        for coin in tqdm(coin_table):
            time.sleep(1)

            with open('data.csv', 'a', encoding='utf-8') as file:  
                writer = csv.writer(file)

                name = coin.ele('.tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5').texts()[0].replace('\n', '').strip()
                link = coin.ele('tag:a').link

                try:
                    coin_info = driver.new_tab(url=link)
                except Exception as e:
                    print(f"Error opening link: {link} | Error: {e}")
                    continue
                try:
                    website = [
                        link.attr('href') 
                        for link in coin_info.eles('tag:a') 
                        if link.attr("data-info-type") == "website" and link.attr("href")
                    ][0]

                    telegram = ";".join(link.attr('href') for link in coin_info.eles('tag:a') if link.attr("data-info-type") == "community" and link.attr("href") and 't.me' in link.attr('href'))
                    twitter = ";".join(link.attr('href') for link in coin_info.eles('tag:a') if link.attr("data-info-type") == "community" and link.attr("href") and 'twitter' in link.attr('href'))
                    
                    if website:
                        website_info = requests.get(website, timeout=10).text
                        website_soup = BeautifulSoup(website_info, 'html.parser')

                        mailtos = list(set(a['href'].replace("mailto:", "") for a in website_soup.find_all('a', href=True) if a['href'].startswith("mailto:")))
                        email = ";".join(email for email in mailtos)

                    else:
                        email = "N/A"
                    
                    coin_info.close()

                    writer.writerow([name, website, email, telegram.strip(), "telegram admins will be here", twitter.strip(), link.strip()])

                except Exception as e:
                    print(f'[coingecko] {e}')

    driver.close()       


def cryptorank():
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'content-type': 'application/json',
        'origin': 'https://cryptorank.io',
        'priority': 'u=1, i',
        'referer': 'https://cryptorank.io/',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    }

    json_data = {
        'path': 'round/upcoming',
        'limit': 200,
        'filters': {},
        'skip': 0,
        'status': 'upcoming',
    }

    response = requests.post('https://api.cryptorank.io/v0/round/upcoming', headers=headers, json=json_data)

    if response.status_code not in [200, 201]:
        print(f"Error: {response.status_code}")
        return

    data = response.json()
    
    for item in tqdm(data['data'], total=len(data['data'])):
        time.sleep(1)

        with open('data.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)

            name = item['name']
            slug = item['key']
            link = f"https://cryptorank.io/price/{slug}"

            coin_info = requests.get(f"https://cryptorank.io/_next/data/1745679906999/en/price/{slug}.json?coinKey={slug}", headers=headers)
        
            try:
                links = coin_info.json()['pageProps']['coin']['links']
            except requests.exceptions.JSONDecodeError:
                time.sleep(30)

            website = "N/A"
            telegram = "N/A"
            twitter = "N/A"
            email = "N/A"

            for social_link in links:
                if social_link['type'] == 'web':
                    website = social_link['value']

                    try:
                        website_info = requests.get(website).text
                        website_soup = BeautifulSoup(website_info, 'html.parser')

                        mailtos = list(set(a['href'].replace("mailto:", "") for a in website_soup.find_all('a', href=True) if a['href'].startswith("mailto:")))
                        email = ";".join(email for email in mailtos)

                    except Exception as e:
                        print(f"[cryptorank] {e}")
                        pass
            
                elif social_link['type'] == 'telegram':
                    telegram = social_link['value']
                elif social_link['type'] == 'twitter':
                    twitter = social_link['value']

            writer.writerow([name, website, email, telegram, "telegram admins will be here", twitter, link])



def cryptototem():

    for index in range(1, 4):
        html = requests.get(f'https://cryptototem.com/ajax.php?action=get_ico&page_no={index}&bounty=no&ieo=no&ido=no&status=&industry=&status_type=').text
        soup = BeautifulSoup(html, 'html.parser')

        if not html:
            break

        items = soup.find_all('tr')

        for item in tqdm(items):  
            time.sleep(1)

            with open('data.csv', 'a', encoding='utf-8') as f:
                writer = csv.writer(f)

                link = f"https://cryptototem.com{item.find('a')['href']}"
                
                try:
                    item_info = requests.get(link).text
                    item_soup = BeautifulSoup(item_info, 'html.parser')
                
                    name = item_soup.find('h1', class_='ico-title').text
                    social_links = item_soup.find('div', class_='soc-urls')
                except Exception as e:
                    print(f"[cryptototem] {e}")
                    pass
            
                website = "N/A"
                telegram = "N/A"
                twitter = "N/A"
                email = "N/A"

                for s_link in social_links:
                    
                    href = s_link.get('href')

                    if 'data-u' in s_link.attrs:
                        website = decrypt_cryptojs_aes_json(s_link['data-u'], 'mycrypt')

                        try:
                            website_info = requests.get(website).text
                            website_soup = BeautifulSoup(website_info, 'html.parser')

                            mailtos = list(set(a['href'].replace("mailto:", "") for a in website_soup.find_all('a', href=True) if a['href'].startswith("mailto:")))
                            email = ";".join(email for email in mailtos)
                        except Exception as e:
                            print(f"[cryptototem] {e}")
                            pass
                    
                    elif href and 't.me' in href:
                        telegram = href
                    elif href and 'x.com' in href:
                        twitter = href

                writer.writerow([name, website, email, telegram, "telegram admins will be here", twitter, link])



def gemfinder():

    for index in range(1, 4):
        html = requests.get(f'https://gemfinder.cc/all-time-best-ajax?page={index}').text
        if not html:
            break
    
        soup = BeautifulSoup(html, 'html.parser')

        items = soup.find_all('li')

        for item in tqdm(items): 
            
            time.sleep(1)

            with open('data.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file)

                try:
                    link = item.div['data-href']

                    item_info = requests.get(link).text
                    item_soup = BeautifulSoup(item_info, 'html.parser')

                    item_card = item_soup.find('div', class_='card mb-4 coin_intro')
                    
                    name = item_card.h3.text
                    website = item_card.find('a', class_='btn btn-primary btn-lg mb-3')['href']

                    email = "N/A"
                except Exception as e:
                    print(f'[gemfinder] {e}')
                    continue

                try:            
                    website_info = requests.get(website, timeout=10).text
                    website_soup = BeautifulSoup(website_info, 'html.parser')

                    mailtos = list(set(a['href'].replace("mailto:", "") for a in website_soup.find_all('a', href=True) if a['href'].startswith("mailto:")))
                    email = ";".join(email for email in mailtos)
                    
                except Exception as e:
                    print(f"[gemfinder] {e}")
                    pass
                    
                social_group = item_card.find('div', class_='btn-group')
                social_links = social_group.find_all('a')

                telegram = "N/A"
                twitter = "N/A"

                for social_link in social_links:
                    
                    href = social_link['href']

                    if 't.me' in href:
                        telegram = href
                    elif "twitter.com" in href:
                        twitter = href

                writer.writerow([name, website, email, telegram, "telegram admins will be here", twitter, link])



def dextools():
    driver = ChromiumPage()
    driver.get('https://www.dextools.io/app/en/pairs')

    for _ in range(5):
        time.sleep(0.5)
        driver.scroll.to_bottom()

    datatable = driver.ele('.datatable-scroll ng-star-inserted')
    conts = datatable.eles('.datatable-row-wrapper ng-star-inserted')

    for container in tqdm(conts):
        with open('data.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)

            link = container.ele('tag:a').link
            
            coin_tab = driver.new_tab(link)
            coin_tab.refresh()

            coin_tab.listen.start('https://www.dextools.io/shared/data/pair')

            time.sleep(15)

            data = None
            for packet in coin_tab.listen.steps():
                if packet.response.raw_body:
                    raw = packet.response.raw_body 
                    data = json.loads(raw)
                    break

                else:
                    coin_tab.refresh()
            else:
                print("loop ended")

            try:
                name = data['data'][0]['name']
                telegram = data['data'][0]['token']['links']['telegram']
                website = data['data'][0]['token']['links']['website']
                twitter = data['data'][0]['token']['links']['twitter']
                email = data['data'][0]['token']['info']['email'].strip()

                coin_tab.close()

                writer.writerow([name, website, email, telegram, "telegram admins will be here", twitter, link])

            except Exception as e:
                print(f"[dextools] {e}")
                pass
                
    driver.close()


def coin_sniper():

    driver = ChromiumPage()

    for index in range(1, 4):
        driver.get(f'https://coinsniper.net/new?page={index}')
        
        coin_table = driver.eles('tag:tbody')[1].children()

        for item in tqdm(coin_table):
            if item.attr('class') == "zero-coin":
                continue
            
            time.sleep(random.randint(1, 2))

            with open('data.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file)

                slug = item.attr('data-link')

                link = f"https://coinsniper.net{slug}"

                item_info = driver.new_tab(link)

                name = item_info.ele('.coin-name').texts()[0]

                social_container = item_info.ele('.social-icons scrollable').children()

                telegram = "N/A"
                website = "N/A"
                twitter = "N/A"
                email = "N/A"

                for social in social_container:
                    href = social.ele('tag:a').attr('href')

                    _match = re.search(r"type=([^&]+)&link=([^ ]+)", href)

                    if _match:
                        _type = _match.group(1)
                        _link = _match.group(2)

                        if 't.me' in _link:
                            telegram = _link
                        elif 'x.com' in _link:
                            twitter = _link
                        elif _type == "website":
                            website = _link

                            try:
                                website_info = requests.get(website, timeout=10)
                                website_soup = BeautifulSoup(website_info.text, 'html.parser')
                    
                                mailtos = list(set(a['href'].replace("mailto:", "") for a in website_soup.find_all('a', href=True) if a['href'].startswith("mailto:")))
                                email = ";".join(email for email in mailtos)
                            except Exception as e:
                                print(f"[coinsniper] {e}")
                                pass
                
                item_info.close()

                writer.writerow([name, website, email, telegram, "telegram admins will be here", twitter, link.replace('&s=new', '').strip()])

    driver.close()

def icomarks():
    
    cookies = {
        'PHPSESSID': '5e5508356debd00dbb952de7dab20969',
        '_ga': 'GA1.1.1622364863.1745315853',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_first_add': 'fd%3D2025-04-22%2012%3A57%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Ficomarks.ai%2Ficos%3Fsort%3Dending-desc%7C%7C%7Crf%3D%28none%29',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29',
        'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29',
        'sbjs_udata': 'vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F135.0.0.0%20Safari%2F537.36',
        'XSRF-TOKEN': 'eyJpdiI6IkxRbWZYYTFGeVdiRmNJWDgxaHZld0E9PSIsInZhbHVlIjoiRVpqUVNtVHF2RDQ4R1RhQjd2bUdURWRNTnpEMWZoUkMrcFdyWHdZUHJYMUFnZXVndVdZUG55U3JmQjVvVTlaUUdYWU5aTGU2UHRGUE9iY1Nab0p6aXZqYmVJY25aZDVyUUN6OWhPcHJOWmRubmlYM1pHQm5ZYUpFMmMyRlQweU0iLCJtYWMiOiI3MTgwZDZiMDIwNzRiMmE5NTMwYTNhYzczZWU4ODM4MTdiODM2N2I3ZWIzNjJhOGM5NTM0MmU5YTllOThhZjM5IiwidGFnIjoiIn0%3D',
        'icomarksai_session': 'eyJpdiI6Ik1FallyNjQ5TkFjOC9Tbk5xNXVUVHc9PSIsInZhbHVlIjoib2JBVk9kUi9mQUlNaU51UkI0cldmbXk4a3hubGxNaU1RaEhIdGk4WlUwNExyUDdXejl1cTZ0Z3VaSWxEWWI5eVlkRGFHUXBsZWpBSEZSLzJKVkpKU2FIQ3FwSWU5OFcyVWdjTlVGbFc4anp3Q1lGN2tUdWlhSFVyMWh3VzdOLzUiLCJtYWMiOiIxMTJhM2YwNWM0MjVhNjc2ZmM1ZGM4NWI2Y2ZiZTZjODJhMmFhNDc1YjNkZmE2NTZiMGQwOGE3MWI1ODA5MDYyIiwidGFnIjoiIn0%3D',
        '_ga_0RZJJT4GC2': 'GS1.1.1745933153.2.1.1745933178.0.0.0',
        'sbjs_current_add': 'fd%3D2025-04-29%2016%3A26%3A18%7C%7C%7Cep%3Dhttps%3A%2F%2Ficomarks.ai%2Ficos%3Fsort%3Dending-desc%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
        'sbjs_session': 'pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ficomarks.ai%2Ficos%3Fsort%3Dending-desc',
        '_dd_s': 'logs=1&id=11229dd2-e592-4bbe-9cb6-964cfbf62991&created=1745933153397&expire=1745934087766',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://icomarks.ai',
        'priority': 'u=1, i',
        'referer': 'https://icomarks.ai/icos?sort=ending-desc',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    initial_request = requests.get('https://icomarks.ai/icos?sort=ending-desc', headers=headers, cookies=cookies)
    initial_soup = BeautifulSoup(initial_request.text, 'html.parser')

    try:
        csrf_input = initial_soup.find('input', {'name': '_token'})
        csrf_token = csrf_input['value'] if csrf_input else None
        
        if not csrf_token:
            print("[icomarks] Unable to parse without CSRF token..")
            return
        
    except Exception as e:
        print(f"[icomarks] {e}")
        pass


    data = {
        '_token': csrf_token,
        'offset': '180',
        'sort_field': 'ending',
        'sort_direction': 'desc',
    }

    response = requests.post('https://icomarks.ai/icos/ajax_more', cookies=cookies, headers=headers, data=data).json()

    content = response['content']
    
    normalized = content.encode('utf-8').decode('unicode_escape')
    normalized = _html.unescape(normalized)

    soup = BeautifulSoup(normalized, 'html.parser')

    items = soup.find_all('div', class_='icoListItem')

    for item in tqdm(items):
        time.sleep(random.randint(2, 3))

        with open('data.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)

            try:
                slug = item.find('a')['href']
                link = f"https://icomarks.ai{slug}"

                item_info = requests.get(link).text
                item_soup = BeautifulSoup(item_info, 'html.parser')

                name = item_soup.find('h1').text

                social_links = item_soup.find_all('a', class_='icoinfo-block__view')
            except Exception as e:
                print(f"[icomarks] {e}")
                continue
              
            telegram = "N/A"
            twitter = "N/A"
            website = "N/A"
            email = "N/A"

            for social_link in social_links:
                href = social_link['href']

                if 't.me' in href:
                    telegram = href
                elif 'x.com' in href:
                    twitter = href
                elif 'icomarks' in href:
                    website = href

                    try:
                        website_info = requests.get(website, timeout=10).text
                        website_soup = BeautifulSoup(website_info, 'html.parser')

                        mailtos = list(set(a['href'].replace("mailto:", "") for a in website_soup.find_all('a', href=True) if a['href'].startswith("mailto:")))
                        email = ";".join(email for email in mailtos)
                    except Exception as e:
                        print(f"[icomarks] {e}")
                        pass
            
            writer.writerow([name, website, email, telegram, "telegram admins will be here", twitter, link])


def icoholder():

    cookies = {
        'PHPSESSID': '8tpe8r9jff53etphiplutgjdb5',
        '_ga': 'GA1.2.713790728.1745316478',
        '_fbp': 'fb.1.1745316477903.90802903227796095',
        '_gid': 'GA1.2.154602017.1746013580',
        '_clck': '1v6lkcn%7C2%7Cfvi%7C0%7C1938',
        'cf_clearance': '_X0X_1.R7ou1QcHgCi2L8TBr9PF5liJwv1bNOLSAZ9M-1746013809-1.2.1.1-9VZ3QMhFFBIhygRRDfxs783iPrS40WQ6ECowbdarfGVJ_lIzzUBP5P1am7uYb9N_fwsg.rc6YDFjJWgjgujRrKD5pWOPZZZ_THZ1XWJfOr0nmV2SE703NBisnKUEPXY6VJPjjfWJHfuNW53aOTtoa3aCEJSiySP2tKZhmNm3cB9ScBGMDUk0OvTknaGEJqC2xlP60SynWwi6j_89MGCrjK54cnQFoC8OS4cVmoY.8srfWutccEho7FvUioArmtvhKIQeX4Vog4KKwK.i_i_ORmX2sP.MJTYVwMn9nMIk.JZZdDC5ldoGbO9WGwqiHmuDsqSHw2badvkdMtKyDkU_BSUU6nrGjBLmIvP7zjlZxrU',
        '_ga_SJ7QH52K6S': 'GS1.2.1746013580.2.1.1746013809.60.0.0',
        '_clsk': 'dvs5iu%7C1746016005813%7C10%7C1%7Cl.clarity.ms%2Fcollect',
        '_dd_s': 'logs=1&id=58e0c113-0025-4c48-8e22-bef42d337af4&created=1746013578727&expire=1746017027256',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'infinity': '1',
        'priority': 'u=1, i',
        'referer': 'https://icoholder.com/en/icos/upcoming?isort=r.general&idirection=desc&page=1',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    for index in range(1, 3):
        params = {
            'isort': 'r.general',
            'idirection': 'desc',
            'page': index,
        }

        response = requests.get('https://icoholder.com/en/icos/upcoming', params=params, cookies=cookies, headers=headers).json()['list']

        normalized = response.encode('utf-8').decode('unicode_escape')
        normalized = _html.unescape(normalized)

        soup = BeautifulSoup(normalized, 'html.parser')

        coins = soup.find_all('div', class_='ico-list-row')

        for coin in tqdm(coins):
            time.sleep(1)

            with open('data.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file)

                slug = coin['data-direct']
                link = f'https://icoholder.com{slug}'

                coin_info = requests.get(link).text
                coin_soup = BeautifulSoup(coin_info, 'html.parser')

                name = coin_soup.find('h1').text
                project_links = coin_soup.find('div', class_='links-right')
                social_links = project_links.find_all('a')

                telegram = "N/A"
                website = "N/A"
                twitter = "N/A"
                email = "N/A"

                for social in social_links:
                    title = social.get('data-original-title') or social.get('title')
                    href = social['href']

                    if 'telegram' in title:
                        telegram = href
                    elif 'email' in title:
                        email = href
                    elif 'website' in title:
                        website = href

                        try:
                            website_info = requests.get(website, timeout=10).text
                            website_soup = BeautifulSoup(website_info, 'html.parser')

                            mailtos = list(set(a['href'].replace("mailto:", "") for a in website_soup.find_all('a', href=True) if a['href'].startswith("mailto:")))
                            email = ";".join(email for email in mailtos)

                        except Exception as e:
                            print(f"[icoholder] {e}")
                            pass
                    
                    elif 'twitter' in title:
                        twitter = href

                writer.writerow([name, website, email, telegram, "telegram admins will be here", twitter, link])


def airdropalert():

    cookies = {
        'eoForm_2e2cb988-ddae-11ee-bce6-1f20a4dbde06': 'true',
        'pll_language': 'en',
        'user_country_code': 'bldIYnlyWWlaYitKVWV3cU5iZWROUT09Ojo0YTk4OTg1YTM5ZjMwMDE4ODcxOWYzNGRlNDMxZWQyOA%3D%3D',
        'cookieyes-consent': 'consentid:V01mcFE4SE1WRkFPUVJNdHNuMmJLYk1iRFdMc1NoaXk,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes',
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Language': 'en-US,en;q=0.9',
        'Sec-Fetch-Mode': 'cors',
        'Origin': 'https://airdropalert.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15',
        'Referer': 'https://airdropalert.com/',
        'Sec-Fetch-Dest': 'empty',
        'Priority': 'u=3, i',
    }

    for index in range(1, 4):
        time.sleep(random.randint(2, 3))
        
        data = {
            'action': 'fetch_airdrops',
            'kyc': '',
            'status': '',
            'category': 'new',
            'blockchain': '',
            'sort': '',
            'search_query': '',
            'paged': index,
            '_wpnonce': 'e29b3a7986',
        }

        response = requests.post('https://airdropalert.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)

        soup = BeautifulSoup(response.text, 'html.parser')

        card_container = soup.find('div', class_='airdrop-search-container')
        

        cards = card_container.find_all('div', class_='card-item')

        for card in tqdm(cards):
            
            with open('data.csv', 'a', encoding='utf-8') as f:
                writer = csv.writer(f)

                name = card.find('h4').text.strip()
                link = card.get('data-href')

                card_info = requests.get(link)
                card_soup = BeautifulSoup(card_info.text, 'html.parser')

                card_socials_cont = card_soup.find('div', class_='card-socials')
                
                if not card_socials_cont:
                    continue
                
                card_socials = card_socials_cont.find_all('a')

                telegram = "N/A"
                twitter = "N/A"
                website = "N/A"
                email = "N/A"

                for social in card_socials:
                    href = social.get('href')

                    if 'x.com' in href:
                        twitter = href
                    elif 't.me' in href:
                        telegram = href
                
                website = card_soup.find('a', class_='btn btn-project-website').get('href')

                try:
                    if not website is None:
                        website_info = requests.get(website, timeout=10)
                        website_soup = BeautifulSoup(website_info.text, 'html.parser')

                        mailtos = list(set(a['href'].replace("mailto:", "") for a in website_soup.find_all('a', href=True) if a['href'].startswith("mailto:")))
                        email = ";".join(email for email in mailtos)
                except Exception as e:
                    print(f'[airdropalert] {e}')
                    pass

                writer.writerow([name, website, email, telegram, "telegram admins will be here", twitter, link])



def pack_to_sheet(filename: str):

    creds = service_account.Credentials.from_service_account_file(
        GOOGLE_API,
        scopes=['https://www.googleapis.com/auth/drive']
    )
    
    drive_service = build('drive', 'v3', credentials=creds)

    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    sheet_name = f"Scraped_Data_{now}"

    file_metadata = {
        'name': sheet_name,
        'mimeType': 'application/vnd.google-apps.spreadsheet',
        'parents': [FOLDER_ID]
    }

    media = MediaFileUpload(filename, mimetype='text/csv', resumable=True)
    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    file_id = file.get('id')

    drive_service.permissions().create(
        fileId=file_id,
        body={
            'type': 'anyone',
            'role': 'writer'
        }
    ).execute()


def init_csv():
    with open('data.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Website', 'Email', 'Telegram', 'Telegram Admins', 'Twitter', 'Link'])


def remove_duplicates(filename):
    doc = pd.read_csv(filename)

    doc = doc.drop_duplicates(subset=['Name'], keep='first')

    doc.to_csv(filename, index=False)
    print("Duplicates removed successfully.")


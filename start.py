import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s')

# CSV file path
csv_file_path = 'data_set.csv'

# Check if the file exists, if not create it with header
file_exists = False
try:
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        if any(reader):
            file_exists = True
except FileNotFoundError:
    pass


# Set up the web driver (you need to have the appropriate web driver executable installed)
driver = webdriver.Chrome()

# Navigate to the CNN website
driver.get("https://www.nbcnews.com/archive/articles/2023/december/2")


# Assuming the titles are in h3 tags, adjust this according to the actual HTML structure
main_tag = driver.find_element(By.CLASS_NAME, 'MonthPage')
title_tags = main_tag.find_elements(By.TAG_NAME, 'a')
titles = []
index = 0
for title in title_tags:
    index += 1
    title = {"id": index, "title": title.text, "url": title.get_attribute('href')}
    titles.append(title)

# Append data to the CSV file
with open(csv_file_path, 'a', newline='') as file:

    for title in titles:
        try:
            driver.get(title.get('url'))
            span_tag = driver.find_element(By.CSS_SELECTOR,  'span[data-testid="unibrow-text"]')
            data_tag = driver.find_element(By.CSS_SELECTOR,  'time[data-testid="timestamp__datePublished"]')
            div_tag = driver.find_element(By.CSS_SELECTOR,  'div[data-activity-map="inline-byline-article-top"]')
            title['category'] = span_tag.text
            title['timestamp'] = data_tag.get_attribute('content')
            title['author'] = div_tag.text
            title['hostname'] = 'www.nbcnews.com'
            print(title)

            fieldnames = title.keys()
            logging.info(f"Appended to {csv_file_path}: {title}")
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(title)
        except:
            print("error")
            continue





print(f"Data has been appended to {csv_file_path}.")

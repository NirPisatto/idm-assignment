from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
# Set up the web driver (you need to have the appropriate web driver executable installed)
driver = webdriver.Chrome()

# Navigate to the CNN website
driver.get("https://www.nbcnews.com/archive/articles/2023/december/2")



# Assuming the titles are in h3 tags, adjust this according to the actual HTML structure
main_tag = driver.find_element(By.CLASS_NAME, 'MonthPage')
title_tags = main_tag.find_elements(By.TAG_NAME, 'a')

print(len(title_tags))  # This should be 40
# stream-item-category-label
# Loop through the titles and extract the information


titles = []
index = 0
for title in title_tags:
    index += 1
    title = {"id": index, "title": title.text, "url": title.get_attribute('href')}
    titles.append(title)


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
    except:
        print("error")
        continue

    



# print(titles)
# # Close the browser window
# driver.quit()


# # # wriete to csv
# csv_file_path = "output.csv"

# # # Extracting field names from the first dictionary in the array
# field_names = titles[0].keys()

# # # Write the data to the CSV file
# with open(csv_file_path, mode='w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=field_names)
    
#     # Write the header
#     writer.writeheader()
    
#     # Write the data
#     writer.writerows(titles)

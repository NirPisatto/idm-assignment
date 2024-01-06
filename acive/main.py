from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import logging

logging.basicConfig(filename='example.log', level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s')


# Set up the web driver (you need to have the appropriate web driver executable installed)
driver = webdriver.Chrome()


# Navigate to the CNN website
driver.get("https://news.yahoo.com/world/")

for i in range(10):
    print(i)
    time.sleep(1)

# for i in range(1):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(5)


# Assuming the titles are in h3 tags, adjust this according to the actual HTML structure
titles = driver.find_elements(By.CSS_SELECTOR, 'h3[data-test-locator="stream-item-title"]')
print(titles)  # This should be 40
print(len(titles))  # This should be 40
# stream-item-category-label
# Loop through the titles and extract the information


resutls = []

for title in titles:
    a_tag = title.find_element(By.TAG_NAME, 'a')
    url = a_tag.get_attribute('href')
    title_text = a_tag.text

    previous_sibling = title.find_element(By.XPATH, 'preceding-sibling::*')
    category_tag = previous_sibling.find_element(By.TAG_NAME, 'strong')
    publisher_tag = previous_sibling.find_element(By.CSS_SELECTOR, 'span[data-test-locator="stream-item-publisher"]')

    publisher = publisher_tag.text
    category =  category_tag.text  # Adjust as needed
    hostname = "www.cnn.com"  # Adjust as needed
    timestamp = "CurrentTimestamp"  # You might need to find this information on the page

    resutls.append({'title': title_text, 'url': url, 'publisher': publisher, 'category': category, 'hostname': hostname, 'timestamp': timestamp})


print(resutls)  
# Close the browser window
driver.quit()


# wriete to csv
csv_file_path = "output.csv"

# Extracting field names from the first dictionary in the array
field_names = resutls[0].keys()

# Write the data to the CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    
    # Write the header
    writer.writeheader()
    
    # Write the data
    writer.writerows(resutls)

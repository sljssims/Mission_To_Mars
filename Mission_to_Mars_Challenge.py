
# Import Splinter and BeautifulSoup
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as soup
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager

# Set the executable path and initialize a browswe
# Set up Splinter

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

#Scraping code

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Set up parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# Srape the articles title
slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
# For finding one Use find_all() for all summaries
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
# Note the indexing, references the second button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# Find the relative image url
# Use the .get function becuase the src will change 
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

df.to_html()


################### Hemishperes############################

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

########################################################################################################################
###############3. Write code to retrieve the image urls and titles for each hemisphere#################################
########################################################################################################################

#########################
# Cereberus
#########################
# Visit the URL 
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)
url = "https://marshemispheres.com/"
browser.visit(url)

# Click the link
browser.find_link_by_partial_text('Cerberus Hemisphere Enhanced').click()

# Parse Resluts
html = browser.html
soup = bs(html, 'html.parser')

# Cereberus_title and url
Cereberus_url = soup.find('div', class_ = 'downloads').a["href"]
Cereberus_title = soup.find("h2", class_="title").text

# Add the list to a dictionary
Cereberus = {
    "title": Cereberus_title,
    "img_url": Cereberus_url
}
hemisphere_image_urls.append(Cereberus)
Cereberus

#########################
# Schiaparelli
#########################
# Visit the URL
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)
url = "https://marshemispheres.com/"
browser.visit(url)

# Click the link
browser.find_link_by_partial_text('Schiaparelli Hemisphere Enhanced').click()

# Parse Resluts
html = browser.html
soup = bs(html, 'html.parser')

# Schiaparelli_title and url
schiaparelli_url = soup.find('div', class_ = 'downloads').a["href"]
schiaparelli_title = soup.find("h2", class_="title").text

# Add list to dictionary
schiaparelli = {
    "title": schiaparelli_title,
    "img_url": schiaparelli_url
}
hemisphere_image_urls.append(schiaparelli)
schiaparelli

#########################
# Syrtis
#########################
# Visit the url
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)
url = "https://marshemispheres.com/"
browser.visit(url)

# Click the link
browser.find_link_by_partial_text('Syrtis Major Hemisphere Enhanced').click()

# Parse Resluts
html = browser.html
soup = bs(html, 'html.parser')

# Syrtis_title and url
Syrtis_url = soup.find('div', class_ = 'downloads').a["href"]
Syrtis_title = soup.find("h2", class_="title").text

# Add the list to a dictionary 
Syrtis = {
    "title": Syrtis_title,
    "img_url": Syrtis_url
}
hemisphere_image_urls.append(Syrtis)
Syrtis

#########################
# Valles
#########################
# Visit the url
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)
url = "https://marshemispheres.com/"
browser.visit(url)

# Click the link
browser.find_link_by_partial_text('Valles Marineris Hemisphere Enhanced').click()

# Parse Resluts
html = browser.html
soup = bs(html, 'html.parser')

# Valles_title and url
Valles_url = soup.find('div', class_ = 'downloads').a["href"]
Valles_title = soup.find("h2", class_="title").text

# Add the list to a dictionary 
Valles = {
    "title": Valles_title,
    "img_url": Valles_url
}
hemisphere_image_urls.append(Valles)
Valles

##########################################################################
# 4. Print the list that holds the dictionary of each image url and title.
##########################################################################
hemisphere_image_urls

# 5. Quit the browser
browser.quit()




# Desktop Notifier for COVID-19
# Importing the necessary libraries 
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as BS
from win10toast import ToastNotifier 
import datetime

def covid_updates_notification():
    # User agent for avoiding 403 error
    header = {'User-Agent' : 'Mozilla'}
    
    # Requesting the webpage
    request = Request('https://www.worldometers.info/coronavirus/country/india/', headers = header)
    
    # Opening the url
    html = urlopen(request)
    
    # Parsing the html
    soup = BS(html, 'html.parser')
    
    # Finding the new cases and new deaths
    new_cases = soup.find('li', {'class' : 'news_li'}).strong.text.split()[0]
    new_deaths = list(soup.find('li', {'class' : 'news_li'}).strong.next_siblings)[1].text.split()[0]
    
    # Notifier for Desktop
    notifier = ToastNotifier()
    message = f"New cases     - {new_cases}\nNew Deaths   - {new_deaths}"
    # Showing the message on Desktop
    time = datetime.datetime.now().strftime("%x")
    notifier.show_toast(title = f'COVID-19 Update   {time}', msg = message, duration = 15, icon_path = r'covid.ico')
    
if __name__ == '__main__':
    covid_updates_notification()











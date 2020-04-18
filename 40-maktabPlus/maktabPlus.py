from bs4 import BeautifulSoup
import requests

plusRes = requests.get('https://maktabkhooneh.org/plus/')
soup = BeautifulSoup(plusRes.text, 'html.parser')

courseUniversity = soup.find_all('div', attrs = {'class': 'course-card__uni-title'})
courseTitle      = soup.find_all('div', attrs = {'class': 'course-card__title'})

for i in range(len(courseUniversity)):
    if(courseUniversity[i].text == 'مکتب‌خونه'):
        print(courseTitle[i].text, )
    #print( courseTitle[i].text, ',', courseUniversity[i].text)
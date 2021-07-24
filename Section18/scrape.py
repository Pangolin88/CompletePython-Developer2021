import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        link = links[index].get('href')
        vote = subtext[index].select('.score')
        if (len(vote)):
            points = int(vote[0].getText().replace(' points', ''))
            if (points > 99):
                hn.append({'title': title, 'link': link, 'votes': points})
    return sorted(hn, key=lambda k: k['votes'], reverse=True)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))

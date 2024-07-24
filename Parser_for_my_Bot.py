import requests
from bs4 import BeautifulSoup


link1 = 'https://dronus.ru/news'
link2 = 'https://dronus.ru/official'
link3 = 'https://rostec.ru/search/?q=%D0%B0%D0%B2%D0%B8%D0%BE%D0%BD%D0%B8%D0%BA%D0%B0'
link4 = 'https://bastechnology.ru/news/'
bez_povtorov = []


sp_titles = open('Список.txt', 'a+')
bez_dublicatov = set()


def fixing_symbols(stroka):
    stroka = stroka.replace('\u2212', '-')
    stroka = stroka.replace(':', '.')
    return stroka


def check_string_in_file(filename, search_string):
    with open(filename, 'r') as file:
        for line in file:
            if search_string in line:
                return True
    return False

def parcing():
    site1 = requests.get(link1).text
    soup1 = BeautifulSoup(site1, 'lxml')
    block1 = soup1.find('div', id='primary')
    articles1 = block1.find_all('a')
    for i in articles1:
        if i['href'] != 'https://dronus.ru/news':
            article_link = i['href']
            article_site = requests.get(article_link).text
            soup_article = BeautifulSoup(article_site, 'lxml')
            article_title = soup_article.find('h1').text.strip()
            article_title = fixing_symbols(article_title)
            if not check_string_in_file('Список.txt', article_title) and article_title.find('Рубрика') == -1 and article_title != '':
                f = open(article_title + '.txt', 'w', encoding='utf-8')
                f.write(article_title + '. Cсылка на статью: ' + article_link + '\n')
                for n in soup_article.find_all('p'):
                    f.write(n.text + '\n')
                f.close()
                bez_dublicatov.add(article_title)

    site2 = requests.get(link2).text
    soup2 = BeautifulSoup(site2, 'lxml')
    block2 = soup2.find('div', id='primary')
    articles2 = block2.find_all('a')
    for i in articles2:
        if i['href'] != 'https://dronus.ru/official':
            article_link = i['href']
            article_site = requests.get(article_link).text
            soup_article = BeautifulSoup(article_site, 'lxml')
            article_title = soup_article.find('h1').text.strip()
            article_title = fixing_symbols(article_title)
            if not check_string_in_file('Список.txt', article_title) and article_title.find('Рубрика') == -1 and article_title != '':
                f = open(article_title + '.txt', 'w', encoding='utf-8')
                f.write(article_title + '. Cсылка на статью: ' + article_link + '\n')
                for n in soup_article.find_all('p'):
                    f.write(n.text + '\n')
                f.close()
                bez_dublicatov.add(article_title)

    site3 = requests.get(link3).text
    soup3 = BeautifulSoup(site3, 'lxml')
    block3 = soup3.find('div', id='search-results')
    articles3 = block3.find_all('a')
    for i in articles3:
        article_link = i['href']
        if 'tags' not in article_link and article_link != '/news/section/aviatsiya/' and article_link != '/news/section/subject/':
            article_site = requests.get('https://rostec.ru' + article_link).text
            article_soup = BeautifulSoup(article_site, 'lxml')
            article_title = article_soup.find('h1').text
            article_title = fixing_symbols(article_title)
            if not check_string_in_file('Список.txt', article_title) and article_title.find('Рубрика') == -1 and article_title != '':
                f = open(article_title + '.txt', 'w', encoding='utf-8')
                f.write(article_title + '. Ссылка на статью: https://rostec.ru' + article_link + '\n')
                for k in article_soup.find_all('p'):
                    if k is not None:
                        f.write(k.text.strip() + '\n')
                f.close()
                bez_dublicatov.add(article_title)

    site4 = requests.get(link4).text
    soup4 = BeautifulSoup(site4, 'lxml')
    block4 = soup4.find('section')
    articles4 = block4.find_all('a')
    for i in articles4:
        if i['href'] != 'https://bastechnology.ru/news/page/2/' and i['href'] != 'https://bastechnology.ru/news/page/3/':
            if i['href'] != 'https://bastechnology.ru/news/page/54/' and i['href'] not in bez_povtorov:
                article_link = i['href']
                article_site = requests.get(i['href']).text
                article_soup = BeautifulSoup(article_site, 'lxml')
                article_title = article_soup.find('h1').text
                article_text = article_soup.find('article').find_all('p')
                if not check_string_in_file('Список.txt', article_title):
                    sp_titles.write(article_title + '\n')
                    f = open(article_title + '.txt', 'w', encoding='utf-8')
                    f.write(article_title + '. Cсылка на статью: ' + article_link + '\n')
                    for stroka in article_text:
                        f.write(stroka.text.strip() + '\n')
                    for n in article_soup.find('article').find_all('ul'):
                        f.write(n.text.strip() + '\n')
        bez_povtorov.append(i['href'])

    sp5 = open('Военные дроны.txt', 'w')
    link5 = 'https://topwar.ru/armament/drones/'
    site5 = requests.get(link5).text
    soup5 = BeautifulSoup(site5, 'lxml')
    block5 = soup5.find_all('h2')
    for i in block5:
        article_title = i.find('a').text.strip()
        article_link = i.find('a')['href']
        sp5.write(article_title + '. Ссылка на статью: ' + article_link + '\n')

    sp5.close()

    for i in bez_dublicatov:
        sp_titles.write(i + '\n')

    sp_titles.close()


#бот выдает только ссылки на статьи
#сельскохозяйственные дроны, военные дроны, строительные
#патенты
#частота обновления два раза в день

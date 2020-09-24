import requests
from bs4 import BeautifulSoup


def whatimax(bot, update):
    url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200904'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')

    if(imax):
        imax = imax.find_parent('div' , class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id=update.message.chat_id, text=title + 'IMAX 영화상영이 있습니다')
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text='IMAX 영화상영은 없습니다.')



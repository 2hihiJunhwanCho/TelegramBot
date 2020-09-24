from bs4 import BeautifulSoup
import requests


def top(self, update):
    session = requests.Session()
    addr = 'https://www.naver.com/'
    self.addr = addr
    req = session.get(self.addr)
    soup = BeautifulSoup(req.text, 'html.parser')

    table = soup.find(class_='ah_l')
    t_ary = list(table.stripped_strings)
    update.message.reply_text('실시간 네이버 인기검색어\n'
                              + t_ary[0] + '위: ' + t_ary[1] + '\n'
                              + t_ary[2] + '위: ' + t_ary[3] + '\n'
                              + t_ary[4] + '위: ' + t_ary[5] + '\n'
                              + t_ary[6] + '위: ' + t_ary[7] + '\n'
                              + t_ary[8] + '위: ' + t_ary[9] + '\n'
                              )

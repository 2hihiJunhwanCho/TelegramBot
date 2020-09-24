from bs4 import BeautifulSoup
import requests



def show_ranklist(self, update): #네이버 영화 상영 순위
    session = requests.Session()
    addr = 'http://movie.naver.com/movie/running/current.nhn'

    self.addr = addr
    req = session.get(self.addr)
    soup = BeautifulSoup(req.text, "html.parser")
    titles = soup.find_all('dl', class_='lst_dsc')

    rank = 1
    for title in titles:
        update.message.reply_text(str(rank) + '위: ' + title.find('a').text + "\n"
                                  + "Link : " + addr + title.find('a')['href'] + "\n"
                                  )
        rank += 1
        if (rank == 6):
            break

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,)
import logging
from modules.movie import show_ranklist
from modules.navertopsearch import top
from modules.moviecraw import whatimax
from modules.melon_rank import show_music_rank
from bs4 import BeautifulSoup
import requests

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
#My bot token from BotFather
token = '#Your Token'

# define command handlers

def ver(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text="ver : 1.0")

def test(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="test")

def start(bot, update):
   bot.send_message(chat_id=update.message.chat_id, text="반갑습니다 :)")

# 정해진 커맨드가 아닌 다른 명령을 받았을 때 출력할 메시지
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="아직은 배우지 않은 명령어 같네요 :/")

# main문을 정의하고
def main():
    # Create Updater object and attach dispatcher to it
    updater = Updater(token)
    dp = updater.dispatcher
    print("Bot started")

    # Start the bot #여기에서 추가할 기능의 명령어를 추가하여 주세요
    updater.start_polling()
    dp.add_handler(CommandHandler('hello', start))
    dp.add_handler(CommandHandler('test', test))
    dp.add_handler(CommandHandler('ver', ver))
    dp.add_handler(CommandHandler('music', show_music_rank))
    dp.add_handler(CommandHandler('movie', show_ranklist))
    dp.add_handler(CommandHandler('naver', top))
    dp.add_handler(CommandHandler('whatimax', whatimax))
    dp.add_handler(MessageHandler(Filters.command, unknown))


    # Run the bot until you press Ctrl-C
    updater.idle()
    updater.stop()

#모듈연동이 안될경우에는 밑에 칸에서 봇에 추가할 기능소스 입력하세요

def show_music_rank(bot, update):
    if __name__ == "__main__":
        RANK = 10  ## 멜론 차트 순위가 1 ~ 10위까지 있음(Rank = n n은 수정이 되므로 n을 수정하여 n순위출력 조정가능)

        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
        req = requests.get('https://www.melon.com/chart/week/index.htm', headers=header)  ## 주간 차트를 크롤링 할 것임
        html = req.text
        parse = BeautifulSoup(html, 'html.parser')


        titles = parse.find_all("div", {"class": "ellipsis rank01"})
        singers = parse.find_all("div", {"class": "ellipsis rank02"})
        albums = parse.find_all("div", {"class": "ellipsis rank03"})

        title = []
        singer = []
        album = []

        for t in titles:
            title.append(t.find('a').text)

        for s in singers:
            singer.append(s.find('span', {"class": "checkEllipsis"}).text)

        for a in albums:
            album.append(a.find('a').text)

        for i in range(RANK):
            bot.send_message(chat_id=update.message.chat_id, text='%3d위: %s [ %s ] - %s' % (i + 1, title[i], album[i], singer[i]))






#여기 밑으로는 왠만해선 건드리지 맙시다 여기 Line 안에서만 아무거나 하세요 (Enter로 Space는 늘릴수 있어요)
if __name__ == '__main__':
    main()


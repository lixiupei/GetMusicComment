import pymysql
import requests
import time
import random
import socket
import datetime
import send_email
import http.client
import read_city
from bs4 import BeautifulSoup


#
def get_content(url, data=None):
    header = {
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    timeout = random.choice(range(80, 180))
    while True:
        try:
            rep = requests.get(url, headers=header, timeout=timeout)
            rep.encoding = 'utf-8'
            break
        except socket.timeout as e:
            print('3:', e)
            time.sleep(random.choice(range(8, 15)))

        except socket.error as e:
            print('4:', e)
            time.sleep(random.choice(range(20, 60)))

        except http.client.BadStatusLine as e:
            print('5:', e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            print('6:', e)
            time.sleep(random.choice(range(5, 15)))
    return rep.text


def get_data(html_text):
    final = []
    bs = BeautifulSoup(html_text, "html.parser")  # 创建BS对象
    body = bs.body
    data = body.find('div', attrs={'id': '7d'})
    # data = body.find('div',{'div':'7d'})
    print(type(data))
    ul = data.find('ul')
    li = ul.find_all('li')
    for day in li:
        temp = []
        date = day.find('h1').string
        temp.append(date)
        inf = day.find_all('p')
        temp.append(inf[0].string)
        temperature_lowest = inf[1].find('i').string
        if inf[1].find('span') is None:
            temperature_highest = temperature_lowest.replace('℃', '')
        else:
            temperature_highest = inf[1].find('span').string
            temperature_highestm = temperature_highest.replace("℃", "")
        temperature_lowest = temperature_lowest.replace('℃', '')
        temp.append(temperature_highest.replace("℃", ""))
        temp.append(temperature_lowest)
        final.append(temp)
    return final



if __name__ == '__main__':
    temp = []
    all_save_data = []
    read_city.delete_table()  # 先将表中数据清楚
    get_code = read_city.read_database()
    num = len(get_code)
    s = 0
    today = datetime.date.today()
    while s < num:
        print(get_code[s])
        url = 'http://www.weather.com.cn/weather/' + get_code[s] + '.shtml'
        html = get_content(url)
        result = get_data(html)
        formatted_today = today.strftime('%Y%m%d')
        i = 0
        get_city = read_city.get_city(get_code[s])
        for weather in result:
            now = datetime.datetime.now()
            date = now + datetime.timedelta(days=i)
            week = date.weekday() + 1
            all_save_data.append((date, weather[1], weather[2], weather[3], get_city, get_code[s], week))

            i += 1
        temp.append(get_city)
        s += 1
    read_city.save_database(all_save_data)


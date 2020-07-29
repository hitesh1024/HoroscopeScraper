import requests
from bs4 import BeautifulSoup

LIST_SIGN = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn',
             'aquarius', 'pisces']


class Horoscope:
    Horoscope = None
    Session = None
    Stars = {}
    Matches = {}

    def star_ratings(self):
        r = requests.get(self.URL_STAR_RATING)

        soup = BeautifulSoup(r.content, 'html5lib')

        main_horoscope = soup.find('main')

        stars = main_horoscope.div.findAll('h3')
        messages = main_horoscope.div.findAll('p')

        # Loops over 4 moods
        for i in range(len(stars)):
            # Loops over to count the number of stars
            star = stars[i]
            message = messages[i]

            # print(star.text, end=': ')
            # print(len(star.findAll('i', attrs={'class': 'highlight'})))
            # print(message.text)
            # print()

            self.Stars[star.text.split(' ')[0]] = {
                "rating": len(star.findAll('i', attrs={'class': 'highlight'}))*20,
                "message": message.text
            }

        return self.Stars

    # Working Snippet with only stars
    # def star_ratings(self):
    #     if not self.Session:
    #         r = requests.get(self.URL_HOROSCOPE)
    #         self.Session = BeautifulSoup(r.content, 'html5lib')
    #
    #     stars = self.Session.find('div', attrs={'class': 'ratings'})
    #     for i in stars.findAll("h4"):
    #         self.Stars[i.text] = len(i.parent.findAll('i', attrs={'class': 'highlight'}))
    #
    #     return self.Stars

    def horoscope(self):
        if not self.Session:
            r = requests.get(self.URL_HOROSCOPE)
            self.Session = BeautifulSoup(r.content, 'html5lib')

        self.Horoscope = self.Session.find('div', attrs={'class': 'main-horoscope'}).p.text
        # print(self.Horoscope)

        return self.Horoscope

    def matches(self):
        if not self.Session:
            r = requests.get(self.URL_HOROSCOPE)
            self.Session = BeautifulSoup(r.content, 'html5lib')

        self.Matches['Love'] = self.Session.find(id='src-horo-matchlove').p.text.lower()
        self.Matches['Friendship'] = self.Session.find(id='src-horo-matchfriend').p.text.lower()
        self.Matches['Career'] = self.Session.find(id='src-horo-matchcareer').p.text.lower()
        # print(self.Matches)

        return self.Matches

    def __init__(self, p):
        self.id = LIST_SIGN.index(p) + 1
        print(self.id)
        self.sign = p
        print(self.sign)
        self.URL_HOROSCOPE = f'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={self.id}'
        self.URL_STAR_RATING = f'https://www.horoscope.com/star-ratings/today/{self.sign}'
        print(self.URL_HOROSCOPE)
        print(self.URL_STAR_RATING)

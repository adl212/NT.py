from utils import format_number as fn
from requests import get
import re, json
import date
from cars import cars
from countries import countries
class Racer:
    def __init__(self, racer=None):
        if racer == None:
            self.success = False
            return

        newdata = {}
        newdata = json.loads('{'+re.search(r'RACER_INFO: \{\"(.*)\}', get(f'https://www.nitrotype.com/racer/{racer}').text.strip()).group()+'}')['RACER_INFO']
        #print(newdata)
        if newdata == {}:
            self.success = False
            return

        if not newdata['tag']:
            self.tag = ''
        else:
            self.tag = f"[{newdata['tag']}] "
        self.userid = newdata['userID']
        '''
        userid = newdata['userID']
        #print(userid)
        newdata = loads(get(f'https://test.nitrotype.com/api/players/{str(userid)}').text)['data']
        self.newdata = loads(get(f'https://test.nitrotype.com/api/players/{str(userid)}').text)['data']
        '''
        self.success = True
        if self.success:
            self.carIDs = []
            for elem in newdata['cars']:
                if elem[1] == 'owned':
                    self.carIDs.append(elem[0])

            self.username = newdata['username'].title()

            display_name = newdata['displayName'] or self.username
            self.name = display_name



            try:
                self.racelogs = newdata['raceLogs']
            except:
                pass
            self.tag_and_name = f'[{self.tag}{display_name}\n"{newdata["title"].title()}"](https://nitrotype.com/racer/{racer})'

            self.membership = newdata['membership']

            if newdata['carHueAngle'] == 0:
                self.car = f'https://www.nitrotype.com/cars/{newdata["carID"]}_large_1.png'
            else:
                self.car = f'https://www.nitrotype.com/cars/painted/{newdata["carID"]}_large_1_{newdata["carHueAngle"]}.png'
            
            self.level = fn(newdata['level'])
            self.experience = fn(newdata['experience'])
            self.points = fn(newdata['achievementPoints'])
            self.country = countries.get(newdata['country'], 'Unknown')
            if self.country != 'Unknown':
                self.country += f' :flag_{newdata["country"].lower()}: '
            self.views = fn(newdata['profileViews'])
            self.created = date.fromtimestamp(newdata['createdStamp']).strftime('%d %B %Y')

            self.cars_owned = 0
            self.cars_sold = 0
            self.cars_total = 0
            for car in newdata['cars']:
                if car[1] == 'owned':
                    self.cars_owned += 1
                elif car[1] == 'sold':
                    self.cars_sold += 1
                self.cars_total += 1
            self.cars_owned = fn(self.cars_owned)
            self.cars_sold = fn(self.cars_sold)
            self.cars_total = fn(self.cars_total)
            self.current_car = cars.get(newdata['carID'])
            self.carid = newdata['carID']

            self.nitros = newdata['nitros']
            self.nitros_used = newdata['nitrosUsed']
            self.nitros_total = self.nitros + self.nitros_used
            self.nitros = fn(self.nitros)
            self.nitros_used = fn(self.nitros_used)
            self.nitros_total = fn(self.nitros_total)

            self.races = newdata['racesPlayed']
            self.first = newdata['placed1']
            self.second = newdata['placed2']
            self.third = newdata['placed3']
            try:
                self.first_perc = round((self.first/self.races)*100, 2)
            except ZeroDivisionError:
                self.first_perc = 0
            try:
                self.second_perc = round((self.second/self.races)*100, 2)
            except ZeroDivisionError:
                self.second_perc = 0
            try:
                self.third_perc = round((self.third/self.races)*100, 2)
            except ZeroDivisionError:
                self.third_perc = 0
            self.races = fn(self.races)
            self.first = fn(self.first)
            self.second = fn(self.second)
            self.third = fn(self.third)

            self.wpm_average = fn(newdata['avgSpeed'])
            self.wpm_high = fn(newdata['highestSpeed'])
            '''
            self.money = newdata['money']
            self.money_spent = newdata['moneySpent']
            self.money_total = self.money + self.money_spent
            self.money = fn(self.money)
            self.money_spent = fn(self.money_spent)
            self.money_total = fn(self.money_total)
            '''
            try:
                self.boards = newdata['racingStats']
                self.daily_pre = self.boards[1]
                self.daily_races = self.daily_pre['played']
                self.daily_speed = int(self.daily_pre['typed'])/5/float(self.daily_pre['secs'])*60
                self.daily_accuracy = 100-((int(self.daily_pre['errs'])/int(self.daily_pre['typed']))*100)
                self.daily_points = (self.daily_races*(100+(self.daily_speed/2))*self.daily_accuracy/100)
            except:
                pass
            try:
                self.season_pre = self.boards[0]
                self.season_races = self.season_pre['played']
                self.season_speed = int(self.season_pre['typed'])/5/float(self.season_pre['secs'])*60
                self.season_accuracy = 100-((int(self.season_pre['errs'])/int(self.season_pre['typed']))*100)
                self.season_points = (self.season_races*(100+(self.season_speed/2))*self.season_accuracy/100)
            except:
                pass
            self.friend_reqs_allowed = ':white_check_mark: ' if newdata['allowFriendRequests'] == 1 else ':negative_squared_cross_mark:'
            self.looking_for_team = ':white_check_mark: ' if newdata['lookingForTeam'] == 1 else ':negative_squared_cross_mark:'
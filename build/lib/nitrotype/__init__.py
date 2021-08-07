import re, json, os
from datetime import date
import cloudscraper, jsonpickle, random
with open(os.path.join(os.path.dirname(__file__), 'scrapers.json')) as f:
    scrapers = json.load(f)['scrapers']
#cars of nitrotype
cars = {
    1 : 'Lamborgotti Mephisto SS',
    2 : 'Lamborgotti Mephisto',
    3 : 'Jeepers Rubicorn',
    4 : 'Portch Picante',
    5 : 'Bantly Super Sport',
    6 : 'The Rolls',
    7 : 'Winston Citroen',
    8 : 'Winston Agile',
    9 : 'Rental Car',
    10 : 'Mission Accomplished',
    11 : 'Buggani Vyrus SS',
    13 : 'Auttie B9',
    14 : 'Nitsua Lance 722',
    15 : 'Misoux Lion',
    16 : 'Misoux Toad',
    17 : 'Minnie the Cooper',
    18 : 'Nizza 350x',
    19 : 'One Ace',
    20 : 'Cougar Ace',
    21 : 'Rand Rover R/T',
    22 : 'B-Team Van',
    23 : 'Mercedex Bens V-20',
    24 : 'Mercedex Bens C-64',
    25 : 'Portch Spyder',
    26 : 'Auttie Roadster',
    27 : 'Bimmer M2.0',
    28 : 'Bimmer 9.0t',
    29 : 'Thunder Cougarbird',
    30 : 'Rat Rod Skully',
    31 : 'Outtie R11',
    33 : 'The Flamerod',
    34 : 'Valent Performo',
    35 : 'Portch GT3 RS',
    36 : 'Ponce de Leon',
    37 : '\'67 Shellback GT-500',
    38 : 'Road Warrior',
    39 : 'Linux Elise',
    40 : '\'69 Shellback RT-500',
    42 : 'The Gator',
    43 : 'Bastok Suprillia',
    44 : 'The Judge',
    45 : 'The Stallion',
    46 : 'The Macro',
    47 : 'The Fastback',
    48 : 'The Covenant',
    49 : 'The Trifecta',
    50 : '8 Bit Racer',
    51 : 'Mini Sherman',
    52 : 'Typiano Pizza Car',
    53 : 'Rocket Man',
    54 : 'All Terrain Vehicle',
    55 : 'MP 427',
    56 : 'Wambulance',
    57 : 'Hotdog Mobile',
    58 : 'F-35 JSF',
    59 : 'NASA Shuttle',
    60 : 'Caterham Racer',
    61 : 'Mack Daddy',
    62 : 'Big Hauler',
    63 : 'Big Blue  ',
    64 : 'Fort GT40',
    65 : 'Dom Vipper GST-R',
    66 : 'Alpha Romero 8Ω',
    67 : 'Blazing Buggy',
    68 : 'F4U Corsair',
    69 : 'Rocket Sleigh',
    70 : 'XMaxx Tree Racer',
    71 : 'Shadow Xmaxx Tree',
    72 : 'Party Sleigh',
    73 : 'Zonday Tricolore',
    74 : 'The Monster',
    75 : 'Flux Capacitor',
    76 : 'The Gotham',
    77 : 'The Pirc',
    78 : 'Suziki GXRS 1200',
    79 : 'EZ Rider',
    80 : 'Lamborgotti AdventX',
    81 : 'Summer Classic',
    82 : 'Hang Ten',
    83 : '\'41 Woodie Deluxx',
    84 : 'Hang Eleven',
    85 : '\'41 Woodie Sunshine',
    86 : 'The Xcelsior V12',
    87 : '\'68 Roadtripper',
    88 : 'Hang Fifteen',
    89 : 'Wach 6',
    90 : 'Fort F-125',
    91 : 'Wisker Electric',
    92 : '\'67 Vette',
    93 : 'MSG 01',
    94 : 'Fort Stallion',
    95 : 'Police Bimmer',
    96 : 'Auttie R-8.1',
    97 : 'Wampus',
    98 : 'Pumpkin Hauler',
    99 : 'Wreath Racer',
    100 : 'Santa\'s Buggy',
    101 : 'Travis\' Car',
    102 : 'Dark Elf',
    103 : 'The Golden Gift',
    104 : 'Corndog\'s Car',
    105 : '\'14 Mantaray',
    106 : 'Ferreti Samsher 458',
    107 : 'Lacan Hypersport',
    109 : 'Sun Buggie',
    110 : 'Hammer Wheels',
    111 : 'Kringle 4000',
    112 : 'Buddy\'s Snowmobile',
    113 : 'Kringle 4000 XL',
    114 : 'Buddy\'s Snowmorocket',
    115 : 'Six Four',
    116 : 'Six Four Plus Three',
    117 : 'The Midnight Hauler',
    118 : 'The Candy Hauler',
    119 : 'Kringle 5000',
    120 : 'Wrapped Wracer',
    121 : 'Wrapped Wracer GT',
    122 : 'Holiday Hero',
    123 : 'Kringle 5000 L.T.',
    124 : 'Mercedex McLaro SLR',
    125 : 'Floaty Blue',
    126 : 'B.O.A.T.',
    127 : 'I\'m Spicy!',
    128 : 'Y.A.C.H.T.',
    129 : 'Mercedex McLaro SLR 12.5',
    130 : 'Nitr-o\'-Lantern',
    131 : 'Nitr-o\'-the-Wisp',
    132 : 'Xmaxx Xxpress',
    133 : 'XMaxx Xxpress XXL',
    134 : 'Gilded Xxpress',
    135 : 'Lamborgotti Xmaxx LT',
    136 : 'Lamborgotti Xmaxx LT-C',
    137 : 'Mercedex McLaro SHS 15.0',
    138 : 'Strykist 1300',
    139 : 'Range Runner',
    140 : 'Strykist 1300 XT-LR',
    141 : 'Track-o\'-Lantern',
    142 : 'Gingerbread Racer',
    143 : 'Gingerbread Racer H&T',
    144 : 'Missile Toe',
    145 : 'Missile Toe H&T',
    146 : 'The Dark Chocolate Knight',
    149 : 'Teggsla',
    150 : 'Egg Beater',
    151 : 'Eggcedes',
    152 : 'Egg Hauler',
    153 : 'Mercedex GT 20.0',
    154 : 'Rocky Roo',
    155 : 'NitroPAC',
    156 : 'Matchbox',
    157 : 'Lucky Number 7',
    158 : 'Easy Breezy',
    159 : 'HoverJet 5000 Mk. 3',
    160 : 'Golden Breeze',
    161 : 'B.U.S.',
    162 : 'S\'cool B.U.S.',
    163 : 'AU-79',
    164 : 'The Underachiever',
    165 : 'The Overachiever',
    166 : 'The Wildflower',
    167 : 'Jolly RS',
    168 : 'Jolly GTX LG',
    169 : 'The Goldray',
    170 : 'can hav nt g0ld plx?',
    171 : 'The Wraptor',
    172 : 'Travis\' Truck',
    173 : 'The Wraptor GG',
    174 : 'The Silent Knight',
    175 : 'NT Gold',
    176 : 'Lamborgotti Tiesto',
    177 : 'Portch Cobalt',
    178 : 'Alpha Romero 123Ω',
    179 : 'Travis\' Big Truck',
    180 : 'Bright Idea',
    181 : 'Sandstorm',
    182 : 'The Jury',
    183 : 'The Goldfish',
    184 : 'Shock Value',
    185 : 'Gold Standard',
    186 : 'Solar Roller',
    187 : 'H2GO',
    188 : 'The DevasTater',
    189 : 'Creepy Crawler',
    190 : 'The Goblin',
    191 : 'Something Wicked',
    192 : 'Frosted Roller',
    193 : 'Gingerbread GT',
    194 : 'Holiday Heat',
    195 : 'Cold Snap',
    196 : 'The Snowy Knight',
    197 : 'The Rocket Klaus',
    198 : 'Golden Ticket',
    199 : 'Wavebreaker',
    200 : 'Broadwing',
    201 : 'Bimmer Prism i20',
    202 : 'Heartbreaker',
    203 : 'The Danger 9',
    204 : 'The Wild 500',
    205 : 'Tigreen',
    206 : 'X1 Eclipse',
    207 : 'Error 500',
    208 : 'Vapor',
    209 : '9 Bit Racer',
    210 : 'Chompus\' Wild Ride',
    211 : 'Whiplash XS',
    212 : 'The Hydro Planer',
    213 : 'Timber Speeder',
    214 : 'Wampus\' Waffle Wagon',
    215 : 'Webmobile Spider',
    216 : 'Rand Rover Evar',
    217 : 'SpaceZ Crew Draco',
    218 : 'MacLaro Sienna',
    219 : 'Calculatron',
    220 : 'Screw Tank',
    221 : 'Hoverbike',
    222 : 'Jet Bicycle'
}
#countries in nitrotype
countries = {
	'AD': 'Andorra',
	'AE': 'United Arab Emirates',
	'AF': 'Afghanistan',
	'AG': 'Antigua & Barbuda',
	'AI': 'Anguilla',
	'AL': 'Albania',
	'AM': 'Armenia',
	'AN': 'Netherlands Antilles',
	'AO': 'Angola',
	'AQ': 'Antarctica',
	'AR': 'Argentina',
	'AS': 'American Samoa',
	'AT': 'Austria',
	'AU': 'Australia',
	'AW': 'Aruba',
	'AZ': 'Azerbaijan',
	'BA': 'Bosnia and Herzegovina',
	'BB': 'Barbados',
	'BD': 'Bangladesh',
	'BE': 'Belgium',
	'BF': 'Burkina Faso',
	'BG': 'Bulgaria',
	'BH': 'Bahrain',
	'BI': 'Burundi',
	'BJ': 'Benin',
	'BM': 'Bermuda',
	'BN': 'Brunei Darussalam',
	'BO': 'Bolivia',
	'BR': 'Brazil',
	'BS': 'Bahama',
	'BT': 'Bhutan',
	'BV': 'Bouvet Island',
	'BW': 'Botswana',
	'BY': 'Belarus',
	'BZ': 'Belize',
	'CA': 'Canada',
	'CC': 'Cocos (Keeling) Islands',
	'CF': 'Central African Republic',
	'CG': 'Congo',
	'CH': 'Switzerland',
	'CI': 'Côte D\'ivoire (Ivory Coast)',
	'CK': 'Cook Iislands',
	'CL': 'Chile',
	'CM': 'Cameroon',
	'CN': 'China',
	'CO': 'Colombia',
	'CR': 'Costa Rica',
	'CU': 'Cuba',
	'CV': 'Cape Verde',
	'CX': 'Christmas Island',
	'CY': 'Cyprus',
	'CZ': 'Czech Republic',
	'DE': 'Germany',
	'DJ': 'Djibouti',
	'DK': 'Denmark',
	'DM': 'Dominica',
	'DO': 'Dominican Republic',
	'DZ': 'Algeria',
	'EC': 'Ecuador',
	'EE': 'Estonia',
	'EG': 'Egypt',
	'EH': 'Western Sahara',
	'ER': 'Eritrea',
	'ES': 'Spain',
	'ET': 'Ethiopia',
	'FI': 'Finland',
	'FJ': 'Fiji',
	'FK': 'Falkland Islands (Malvinas)',
	'FM': 'Micronesia',
	'FO': 'Faroe Islands',
	'FR': 'France',
	'FX': 'France, Metropolitan',
	'GA': 'Gabon',
	'GB': 'United Kingdom (Great Britain)',
	'GD': 'Grenada',
	'GE': 'Georgia',
	'GF': 'French Guiana',
	'GH': 'Ghana',
	'GI': 'Gibraltar',
	'GL': 'Greenland',
	'GM': 'Gambia',
	'GN': 'Guinea',
	'GP': 'Guadeloupe',
	'GQ': 'Equatorial Guinea',
	'GR': 'Greece',
	'GS': 'South Georgia and the South Sandwich Islands',
	'GT': 'Guatemala',
	'GU': 'Guam',
	'GW': 'Guinea-Bissau',
	'GY': 'Guyana',
	'HK': 'Hong Kong',
	'HM': 'Heard & McDonald Islands',
	'HN': 'Honduras',
	'HR': 'Croatia',
	'HT': 'Haiti',
	'HU': 'Hungary',
	'ID': 'Indonesia',
	'IE': 'Ireland',
	'IL': 'Israel',
	'IN': 'India',
	'IO': 'British Indian Ocean Territory',
	'IQ': 'Iraq',
	'IR': 'Islamic Republic of Iran',
	'IS': 'Iceland',
	'IT': 'Italy',
	'JM': 'Jamaica',
	'JO': 'Jordan',
	'JP': 'Japan',
	'KE': 'Kenya',
	'KG': 'Kyrgyzstan',
	'KH': 'Cambodia',
	'KI': 'Kiribati',
	'KM': 'Comoros',
	'KN': 'St. Kitts and Nevis',
	'KP': 'Korea, Democratic People\'s Republic of',
	'KR': 'Korea, Republic of',
	'KW': 'Kuwait',
	'KY': 'Cayman Islands',
	'KZ': 'Kazakhstan',
	'LA': 'Lao People\'s Democratic Republic',
	'LB': 'Lebanon',
	'LC': 'Saint Lucia',
	'LI': 'Liechtenstein',
	'LK': 'Sri Lanka',
	'LR': 'Liberia',
	'LS': 'Lesotho',
	'LT': 'Lithuania',
	'LU': 'Luxembourg',
	'LV': 'Latvia',
	'LY': 'Libyan Arab Jamahiriya',
	'MA': 'Morocco',
	'MC': 'Monaco',
	'MD': 'Moldova, Republic of',
	'MG': 'Madagascar',
	'MH': 'Marshall Islands',
	'ML': 'Mali',
	'MN': 'Mongolia',
	'MM': 'Myanmar',
	'MO': 'Macau',
	'MP': 'Northern Mariana Islands',
	'MQ': 'Martinique',
	'MR': 'Mauritania',
	'MS': 'Monserrat',
	'MT': 'Malta',
	'MU': 'Mauritius',
	'MV': 'Maldives',
	'MW': 'Malawi',
	'MX': 'Mexico',
	'MY': 'Malaysia',
	'MZ': 'Mozambique',
	'NA': 'Namibia',
	'NC': 'New Caledonia',
	'NE': 'Niger',
	'NF': 'Norfolk Island',
	'NG': 'Nigeria',
	'NI': 'Nicaragua',
	'NL': 'Netherlands',
	'NO': 'Norway',
	'NP': 'Nepal',
	'NR': 'Nauru',
	'NU': 'Niue',
	'NZ': 'New Zealand',
	'OM': 'Oman',
	'PA': 'Panama',
	'PE': 'Peru',
	'PF': 'French Polynesia',
	'PG': 'Papua New Guinea',
	'PH': 'Philippines',
	'PK': 'Pakistan',
	'PL': 'Poland',
	'PM': 'St. Pierre & Miquelon',
	'PN': 'Pitcairn',
	'PR': 'Puerto Rico',
	'PT': 'Portugal',
	'PW': 'Palau',
	'PY': 'Paraguay',
	'QA': 'Qatar',
	'RE': 'Réunion',
	'RO': 'Romania',
	'RU': 'Russian Federation',
	'RW': 'Rwanda',
	'SA': 'Saudi Arabia',
	'SB': 'Solomon Islands',
	'SC': 'Seychelles',
	'SD': 'Sudan',
	'SE': 'Sweden',
	'SG': 'Singapore',
	'SH': 'St. Helena',
	'SI': 'Slovenia',
	'SJ': 'Svalbard & Jan Mayen Islands',
	'SK': 'Slovakia',
	'SL': 'Sierra Leone',
	'SM': 'San Marino',
	'SN': 'Senegal',
	'SO': 'Somalia',
	'SR': 'Suriname',
	'ST': 'Sao Tome & Principe',
	'SV': 'El Salvador',
	'SY': 'Syrian Arab Republic',
	'SZ': 'Swaziland',
	'TC': 'Turks & Caicos Islands',
	'TD': 'Chad',
	'TF': 'French Southern Territories',
	'TG': 'Togo',
	'TH': 'Thailand',
	'TJ': 'Tajikistan',
	'TK': 'Tokelau',
	'TM': 'Turkmenistan',
	'TN': 'Tunisia',
	'TO': 'Tonga',
	'TP': 'East Timor',
	'TR': 'Turkey',
	'TT': 'Trinidad & Tobago',
	'TV': 'Tuvalu',
	'TW': 'Taiwan, Province of China',
	'TZ': 'Tanzania, United Republic of',
	'UA': 'Ukraine',
	'UG': 'Uganda',
	'UM': 'United States Minor Outlying Islands',
	'US': 'United States of America',
	'UY': 'Uruguay',
	'UZ': 'Uzbekistan',
	'VA': 'Vatican City State (Holy See)',
	'VC': 'St. Vincent & the Grenadines',
	'VE': 'Venezuela',
	'VG': 'British Virgin Islands',
	'VI': 'United States Virgin Islands',
	'VN': 'Viet Nam',
	'VU': 'Vanuatu',
	'WF': 'Wallis & Futuna Islands',
	'WS': 'Samoa',
	'YE': 'Yemen',
	'YT': 'Mayotte',
	'YU': 'Yugoslavia',
	'ZA': 'South Africa',
	'ZM': 'Zambia',
	'ZR': 'Zaire',
	'ZW': 'Zimbabwe'
}


class Racer:
    def __init__(self, racer=None, scraper=None):
        self.requests = jsonpickle.decode(random.choice(scrapers))
        if scraper:
            self.requests = scraper
        def get(*args, **kwargs):
            return self.requests.get(headers=self.requests.headers, *args, **kwargs)
        if racer == None:
            self.success = False
            return

        newdata = {}
        newdata = json.loads('{"'+re.search(r'RACER_INFO: \{\"(.*)\}', get(f'https://www.nitrotype.com/racer/{racer}').text.strip()).group(1)+'}')
        
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
            self.newdata = newdata
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
            self.level = (newdata['level'])
            self.experience = (newdata['experience'])
            #self.points = (newdata['achievementPoints'])
            '''
            self.country = countries.get(newdata['country'], 'Unknown')
            if self.country != 'Unknown':
                self.country += f'{newdata["country"].lower()}'
            '''
            self.views = (newdata['profileViews'])
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
            self.cars_owned = (self.cars_owned)
            self.cars_sold = (self.cars_sold)
            self.cars_total = (self.cars_total)
            self.current_car = cars.get(newdata['carID'])
            self.carid = newdata['carID']

            self.nitros = newdata['nitros']
            self.nitros_used = newdata['nitrosUsed']
            self.nitros_total = self.nitros + self.nitros_used
            self.nitros = (self.nitros)
            self.nitros_used = (self.nitros_used)
            self.nitros_total = (self.nitros_total)

            self.races = newdata['racesPlayed']
            '''self.first = newdata['placed1']
            self.second = newdata['placed2']
            self.third = newdata['placed3']'''
            '''try:
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
                self.third_perc = 0'''
            self.races = (self.races)
            '''self.first = (self.first)
            self.second = (self.second)
            self.third = (self.third)'''

            self.wpm_average = (newdata['avgSpeed'])
            self.wpm_high = (newdata['highestSpeed'])
            '''
            self.money = newdata['money']
            self.money_spent = newdata['moneySpent']
            self.money_total = self.money + self.money_spent
            self.money = (self.money)
            self.money_spent = (self.money_spent)
            self.money_total = (self.money_total)
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
            self.friend_reqs_allowed = True if newdata['allowFriendRequests'] == 1 else False
            self.looking_for_team = True if newdata['lookingForTeam'] == 1 else False
class Team:
    def __init__(self, team, scraper=None):
        self.requests = jsonpickle.decode(random.choice(scrapers))
        if scraper:
            self.requests = scraper
        def get(*args, **kwargs):
            return self.requests.get(headers=self.requests.headers, *args, **kwargs)
        try:
            def api_get(path): return get(f'https://www.nitrotype.com/api/{path}')
            self.data = json.loads(api_get(f'teams/{team}').content)
            self.success = True
            if self.data['success'] == False:
                self.success = False
                self.data = {}
                return
        except Exception:
            self.data = {}
        else:
            self.data = self.data['data']
            self.info = self.data["info"]
        stats = self.data['stats']
        for stat in stats:
            if stat['board'] == 'daily':
                self.daily_pre = stat
                self.daily_races = self.daily_pre['played']
                self.daily_speed = int(self.daily_pre['typed'])/5/self.daily_pre['secs']*60
                self.daily_accuracy = 100-((int(self.daily_pre['errs'])/int(self.daily_pre['typed']))*100)
                self.daily_points = (self.daily_races*(100+(self.daily_speed/2))*self.daily_accuracy/100)
            if stat['board'] == 'season':
                self.season_pre = stat
                self.season_races = self.season_pre['played']
                self.season_speed = int(self.season_pre['typed'])/5/self.season_pre['secs']*60
                self.season_accuracy = 100-((int(self.season_pre['errs'])/int(self.season_pre['typed']))*100)
                self.season_points = (self.season_races*(100+(self.season_speed/2))*self.season_accuracy/100)
            if stat['board'] == 'alltime':
                self.alltime_pre = stat
                self.alltime_races = self.alltime_pre['played']
                self.alltime_speed = int(self.alltime_pre['typed'])/5/self.alltime_pre['secs']*60
                self.alltime_accuracy = 100-((int(self.alltime_pre['errs'])/int(self.alltime_pre['typed']))*100)
                self.alltime_points = (self.alltime_races*(100+(self.alltime_speed/2))*self.alltime_accuracy/100)


            self.leaders = []
            self.captain = (self.info['username'], self.info['displayName'])
            for elem in self.data['members']:
                if elem['role'] == "officer" and elem['username'] != self.captain[0]:
                    self.leaders.append((elem['username'], elem['displayName']))


            self.tag_and_name = f'[ [{self.info["tag"].upper()}] {self.info["name"]} ](https://www.nitrotype.com/team/{self.info["tag"].upper()})'


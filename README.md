# NT.py
## What is this?
* gets racer stats
* gets team stats
* access the nitrotype api
## Racer Class
Get the stats of a racer.
### Arguments
* username

How to use it:
```python
import nitrotype
racer = nitrotype.Racer('adl212')
print(racer.username)
```
This will print out adl212
You can see all the attributes of the Racer class [here](#racer-attributes)

## Team Class
Get the stats of a team.
### Arguments
* team tag

How to use it:
```python
import nitrotype
team = nitrotype.Team('NTA')
print(team.leaders)
```
This will print out officers by type tuple (**username**, **displayname**)
You can see all the attributes of the Team class [here](#team-attributes)

# Racer Attributes
Here are the attributes of the Racer class:
* `success` - returns a boolean of **True** or **False**
    * If **False**, then other attributes will not exist
* `tag` - The racer's current team's tag
* `userid` - The userid of the racer
* `carIDs` - A list of cars in nitrotype's car ids
* `username` - The username of the racer
* `name` - Current display name of the racer
* `tag_and_name` - The user's team tag and display name put together
    * If not in team, will only be the display name
* `membership` - Gold or regular membership
* `car` - *link* to current car image
* `level` - Current level of racer
* `experience` - Amount of XP achieved
* `points` - Amount of achievement points achieved
* `views` - Player profile views
* `created` - Account creation time
* `cars_owned` - Amount of cars owned
* `cars_sold` - Amount of cars sold
* `cars_total` - Amount of cars owned and owned before
* `current_car` - The name of the current car equipped
* `carid` - The id of the current car equipped
* `nitros` - The nitros owned by a Racer
* `nitros_used` - Amount of nitros used by the Racer
* `nitros_total` - Amount of nitros owned and used by the racer
* `races` - Amount of races the racer has finished
* `wpm_average` - The racer's current wpm average
* `wpm_high` - The racer's current highest wpm
*Note: These stats might return an error as the racer may have not raced in the last 24 hours, in the season, or in the entire length of their account*
* `boards` - The racer's stats in json
* `daily_pre` - The racer's daily stats in json
* `daily_races` - Amount of races in the last 24 hours
* `daily_speed` - Average speed in the last 24 hours
* `daily_accuracy` - Average accuracy in the last 24 hours
* `daily_points` - Points accumulated from the last 24 hours
* `season_pre` - The racer's season stats in json
* `season_races` - Amount of races in the current season
* `season_speed` - Average speed in the current season
* `season_accuracy` - Average accuracy in the current season
* `season_points` - Points accumulated from the current season
* `friend_reqs_allowed` - returns **True** if racer accepts friend requests, else it returns **False**
* `looking_for_team` - returns **True** if racer accepts team invites, else it returns **False**
# Team Attributes
Here are the attributes of the Team class:
* `data` - json data received from the nitrotype api
* `success` - returns a boolean of **True** or **False**
    * If **False**, then other attributes will not exist
* `info` - team info like name and the tag
*Note: These stats might return an error as the team may have not raced in the last 24 hours, in the season, or in the lifetime of the team*
* `daily_pre` - daily stats of team in json
* `daily_races` - team races in the last 24 hours
* `daily_speed` - average speed of team in the last 24 hours
* `daily_accuracy` - average accuracy of team in the last 24 hours
* `daily_points` - amount of points accumulated in the last 24 hours
* `season_pre` - seasonal stats of team in json
* `season_races` - team races in the current season
* `season_speed` - average speed of team in the current season
* `season_accuracy` - average accuracy of team in the current season
* `season_points` - amount of points accumulated in the current season
* `alltime_pre` - alltime stats of team in json
* `alltime_races` - team races in alltime
* `alltime_speed` - average speed of team in alltime
* `alltime_accuracy` - average accuracy of team in alltime
* `alltime_points` - amount of points accumulated in alltime
* `leaders` - officers by type tuple (**username**, **displayname**)
* `captain` - captain by type tuple (**username**, **displayname**)
* `tag_and_name` - The tag and name of a team put together
    * For example, `[NTA]*Ambassadors*`
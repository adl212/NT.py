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
This will print out officers and the captain by type tuple (**username**, **displayname**)
You can see all the attributes of the Team class [here](#team-attributes)

# Racer Attributes

# Team Attributes
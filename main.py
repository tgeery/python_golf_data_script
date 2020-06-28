import requests
import json
import sys

if len(sys.argv) < 2:
    print("Missing tournament ID (e.g. 320)")
    exit(1)
tid = sys.argv[1]
url='https://api.sportsdata.io/golf/v2/json/Leaderboard/' + tid + '?key=d9b5d28013b841f2bdca8ac7a73c75d2'
r = requests.get(url)
data = r.json()
out = open('result.csv', 'w')
#f = open('output.json', 'r')
#raw = f.read()
#data = json.loads(raw)
start = data['Tournament']['StartDate']
end = data['Tournament']['EndDate']
year = start.split('-')[0]
name = data['Tournament']['Name']
location = data['Tournament']['Location']
venue = data['Tournament']['Venue']
#print(name)
#print(venue)
#print(location)
#print(start)
#print(end)
out.write('Tournament Name,Venue,City,State,Start,End,Player,Country,Round 1 Score,Round 2 Score,Round 3 Score,Round 4 Score\n')
for player in data['Players']:
    player_name = player['Name']
    country = player['Country']
    rnd = [0,0,0,0]
    i = 0
    for r in player['Rounds']:
        rnd[i] = r['Score']
        i += 1
        if i == 4:
            break
    if player_name and country:
        out.write(name + "," + venue + "," + location + "," + start + "," + end + "," + player_name + "," + country + "," + str(rnd[0]) + "," + str(rnd[1]) + "," + str(rnd[2]) + "," + str(rnd[3]) + "\n")

from modules import nflTeam


Ravens = nflTeam.NFLTeam("Baltimore","Ravens",39.2778962,-76.6245498)
Bills = nflTeam.NFLTeam("Buffalo","Bills",42.7737546,-78.789161)
Bengals = nflTeam.NFLTeam("Cincinnati","Bengals",39.0954576,-84.5182464)
Browns = nflTeam.NFLTeam("Cleveland","Browns",41.5060535,-81.7017368)
Broncos = nflTeam.NFLTeam("Denver","Broncos",39.7438895,-105.0222981)
Texans = nflTeam.NFLTeam("Houston","Texans",29.6847219,-95.4128961)
Colts = nflTeam.NFLTeam("Indianapolis","Colts",39.7601007,-86.1660764)
Jaguars = nflTeam.NFLTeam("Jacksonville","Jaguars",30.323972,-81.639478)
Chiefs = nflTeam.NFLTeam("Kansas City","Chiefs",39.0489391,-94.4861044)
Chargers = nflTeam.NFLTeam("San Diego","Chargers",32.7831122,-117.1217603)
Dolphins = nflTeam.NFLTeam("Miami","Dolphins",25.9579665,-80.2410491)
Patriots = nflTeam.NFLTeam("New England","Patriots",42.0909458,-71.2665352)
Jets = nflTeam.NFLTeam("New York","Jets",40.8128397,-74.0763978)
Raiders = nflTeam.NFLTeam("Oakland","Raiders",37.7515946,-122.2027345)
Steelers = nflTeam.NFLTeam("Pittsburgh","Steelers",40.4467648,-80.017949)
Titans = nflTeam.NFLTeam("Tennessee","Titans",36.166479,-86.7734785)
Cardinals = nflTeam.NFLTeam("Arizona","Cardinals",33.5276247,-112.264748)
Falcons = nflTeam.NFLTeam("Atlanta","Falcons",33.758,-84.401)
Panthers = nflTeam.NFLTeam("Carolina","Panthers",35.2258296,-80.8550261)
Bears = nflTeam.NFLTeam("Chicago","Bears",41.8623132,-87.6188771)
Cowboys = nflTeam.NFLTeam("Dallas","Cowboys",32.7472844,-97.0966826)
Lions = nflTeam.NFLTeam("Detroit","Lions",42.3400064,-83.0477917)
Packers = nflTeam.NFLTeam("Green Bay","Packers",44.5013406,-88.064397)
Rams = nflTeam.NFLTeam("St. Louis","Rams",38.6328232,-90.1906955)
Vikings = nflTeam.NFLTeam("Minnesota","Vikings",44.973889,-93.258056)
Saints = nflTeam.NFLTeam("New Orleans","Saints",29.951061,-90.0834329)
Giants = nflTeam.NFLTeam("New York","Giants",40.8128397,-74.0763978)
Eagles= nflTeam.NFLTeam("Philadelphia","Eagles",39.9007674,-75.1696522)
FortyNiners = nflTeam.NFLTeam("San Francisco","FortyNiners",37.7343181,-122.429401)
Seahawks = nflTeam.NFLTeam("Seattle","Seahawks",47.5951518,-122.3338281)
Buccaneers = nflTeam.NFLTeam("Tampa Bay","Buccaneers",27.9758691,-82.5055231)
Redskins = nflTeam.NFLTeam("Washington","Redskins",38.9076433,-76.8667341)

nflTeams = [Ravens,Bills,Bengals,Browns,Broncos,Texans,Colts,Jaguars,Chiefs,Chargers,Dolphins,Patriots,Jets,Raiders,Steelers,Titans,Cardinals,Falcons,Panthers,Bears,Cowboys,Lions,Packers,Rams,Vikings,Saints,Giants,Eagles,FortyNiners,Seahawks,Buccaneers,Redskins]

def assignment(teamStr):
    if teamStr == 'San Francisco 49ers':
        teamStr = 'San Francisco FortyNiners'
    for team in nflTeams:
        if teamStr.split()[-1] == team.mascot:
            return team

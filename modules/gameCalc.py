def sol1(filePath,pd,tm):
    from geopy.distance import geodesic
    df = pd.read_excel(filePath, sheet_name='Sheet1')
    for index, row in df.iterrows():
        teamHome = tm.assignment(row['teamHome'])
        teamAway = tm.assignment(row['teamAway'])
        gameLoc = [teamHome.latitude,teamHome.longitude]
        awayLoc = [teamAway.latitude,teamAway.longitude]
        distance = geodesic(gameLoc, awayLoc )



        projWinner = row['projWinner']
        projMargin = row['projMargin']
        projTot = row['projTot']

        scoreHome = row['scoreHome']
        scoreAway = row['scoreAway']
        actWinner = row['actualWinner']
        actMargin = int(scoreHome) - int(scoreAway)
        actTot = row['actTot']


        awayPerformance = actMargin/projMargin

        return[distance,awayPerformance]


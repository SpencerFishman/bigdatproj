def sol1(filePath,pd,tm):
    from geopy.distance import geodesic
    df = pd.read_excel(filePath, sheet_name='Sheet1')
    bigList = []
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
        actMargin = int(scoreAway) - int(scoreHome)
        actTot = row['actTot']
        midNum = projTot/2
        if projWinner == teamAway.fullName:
                projMargin = -projMargin
                projAwayTeam = midNum + projMargin/2
                projHomeTeam = midNum - projMargin/2
        elif projWinner == teamHome.fullName:
                projAwayTeam = midNum + projMargin/2
                projHomeTeam = midNum - projMargin/2      
        else:
                projAwayTeam = midNum
                projHomeTeam = midNum
        actMidNum= actTot/2
        if actWinner == teamAway.fullName:
                actAwayTeam = actMidNum + actMargin/2
                actHomeTeam = actMidNum - actMargin/2
        elif projWinner == teamHome.fullName:
                actAwayTeam = actMidNum + actMargin/2
                actHomeTeam = actMidNum - actMargin/2 
        else:
                actAwayTeam = actMidNum
                actHomeTeam = actMidNum
        dfRow = [distance, teamAway.fullName, teamHome.fullName, projWinner, projMargin,actWinner,actMargin]
        bigList.append(dfRow)
    myDf=pd.DataFrame(bigList,columns=['Travel Distance','Away Team','Home Team','Projected Winner','Projected Margin of Victory','Actual Winner', 'Actual Margin of Victory'])
    print(myDf)
    return myDf
    
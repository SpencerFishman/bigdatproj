def sol1(filePath,pd,tm):
    from geopy.distance import geodesic
    df = pd.read_excel(filePath, sheet_name='Sheet1')
    #retDf = pd.DataFrame(columns=['Travel Distance','Home Team','Away Team','Projected Winner','Projected Margin of Victory','Projected % Margin','Actual Winner', 'Actual Margin of Victory', 'Actual % Margin,' 'Away Team Performance'])
    header = ['Travel Distance','Away Team','Home Team','Projected Winner','Projected Margin of Victory','Projected % Margin','Actual Winner', 'Actual Margin of Victory', 'Actual % Margin,' 'Away Team Performance']
    #header = ['Travel Distance','Away Team','Home Team','Projected Winner','Expected Margin','Projection % Margin','Actual Winner', 'Actual Margin of Victory', 'Actual % Margin,' 'Away Team Performance']
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
        #awayPerformance = actMargin/projMargin

        #print(projWinner)
        #print('hometeam', teamHome.fullName)
        #print(teamHome.fullName==projWinner)
        #print('awayteam', teamAway.fullName)
        #print(teamAway.fullName==projWinner)
        #print("projMargin" , projMargin)
        #print("projTot", projTot)


        midNum = projTot/2

        if projWinner == teamAway.fullName: # if the away team is projected to win
                projMargin = -projMargin #this makes the margin positive so represents how much away team will win by.
                print(projMargin,"Away team margin")
                projAwayTeam = midNum + projMargin/2
                projHomeTeam = midNum - projMargin/2
        elif projWinner == teamHome.fullName:
                print('Hometeam win')
                projAwayTeam = midNum + projMargin/2
                projHomeTeam = midNum - projMargin/2      
        else:
                print("This is a tie")
                projAwayTeam = midNum
                projHomeTeam = midNum
        

        actMidNum= actTot/2
        if actWinner == teamAway.fullName: # if the away team is projected to win
                #projMargin = -projMargin #this makes the margin positive so represents how much away team will win by.
                print(actMargin,"Away team margin")
                actAwayTeam = actMidNum + actMargin/2
                actHomeTeam = actMidNum - actMargin/2
        elif projWinner == teamHome.fullName:
                print('Hometeam win')
                actAwayTeam = actMidNum + actMargin/2
                actHomeTeam = actMidNum - actMargin/2 
        else:
                print("This is a tie")
                actAwayTeam = actMidNum
                actHomeTeam = actMidNum
        
        #% away team will lose/win by based on projected points
        print(row["Season"],row["Week"])
        print(teamHome.fullName,projHomeTeam,actHomeTeam)
        print(teamAway.fullName,projAwayTeam,actAwayTeam)
        projPerformance = ((projAwayTeam/projHomeTeam)-1)*100
        actPerformance = ((actAwayTeam/actHomeTeam)-1)*100
        overallPerformance = (actPerformance/projPerformance)*100
        dfRow = [distance, teamAway.fullName, teamHome.fullName, projWinner, projMargin, projPerformance,actWinner,actMargin,actPerformance,overallPerformance]
        print(dfRow)
        bigList.append(dfRow)

        #header = ['Travel Distance','Away Team','Home Team','Projected Winner','Projected Margin of Victory','Projected % Margin','Actual Winner', 'Actual Margin of Victory', 'Actual % Margin,' 'Away Team Performance']
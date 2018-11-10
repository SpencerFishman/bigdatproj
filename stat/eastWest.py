import pandas as pd
#myDf=pd.DataFrame(bigList,columns=['Travel Distance','Away Team','Away Latitude','Away Longitude', 'Home Team','Home Latitude', 
# 'Home Longitude','Projected Winner','Projected Away Score', 'Projected Home Score','Projected Over Under',
# Projected Margin v. Home Team','Actual Winner', 'Actual Away Score','Actual Home Score','Actual Over Under','Actual Margin v. Home Team',
# 'Performance (Margin Comp)','Performance (Scaled Margin Comp)',])
myFile = r"C:\Users\Jonathan Lu\Desktop\isye2028\Big Data Project\bigdatproj\outputnew.xlsx"

xl = pd.ExcelFile(myFile)
df = xl.parse("Sheet1")
homeWin = 0
awayWin = 0
for index, row in df.iterrows():
    homeTeam = str(row['Home Team'])
    awayTeam = str(row['Away Team'])
    if str(row['Actual Winner']) == homeTeam:
        homeWin += 1
    elif str(row['Actual Winner']) == awayTeam:
        awayWin += 1
    elif str(row['Actual Winner']) == 'Tie':
        winningTeam = "None"
    else:
        break
print(homeWin)
print(awayWin)
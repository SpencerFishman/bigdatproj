def main():
    dataPath = sys.path[0] + r'\dataset\nflDataset.xlsx'
    df = pd.read_excel(dataPath, sheetname='Sheet1')
    print(df['Season'])



if __name__ == '__main__':
    import sys
    import pandas as pd
    from lib import teams
    main()
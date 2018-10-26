def main():
    dataPath = sys.path[0] + r'\dataset\nflDataset.xlsx'
    gc.sol1(dataPath,pd,tm)



if __name__ == '__main__':
    import sys
    import pandas as pd
    from modules import teams as tm
    from modules import gameCalc as gc
    main()
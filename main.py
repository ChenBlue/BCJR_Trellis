from BCJR import BCJR
import csv
import pandas as pd
import numpy as np

def main(filename):
	print("Hello world!")
	df = pd.read_csv(filename, header=None)
	print(df)
	
	bc = BCJR(1,2)

if __name__ == '__main__':
    main('file2.csv')
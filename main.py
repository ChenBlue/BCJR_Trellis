from BCJR import BCJR

def main(filename):
	print("Hello world!")

	#x = 3
	#y = 6
	#print(x^y)
	
	
	bcjr = BCJR(filename)
	print("length:", bcjr.get_len())
	print("dimension:", bcjr.get_dim())
	print("bit:", bcjr.get_bit())

	bcjr.build()

	bcjr.plot_section(0,bcjr.get_len())

if __name__ == '__main__':
    main('file3.csv')
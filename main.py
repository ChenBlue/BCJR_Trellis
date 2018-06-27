from BCJR import BCJR

def main(filename):
	print("Hello world!")
	
	
	bcjr = BCJR(filename)
	print("length:", bcjr.get_len())
	print("dimension:", bcjr.get_dim())
	print("bit:", bcjr.get_bit())

	bcjr.build()

	bcjr.plot_section(0,5)

if __name__ == '__main__':
    main('file1.csv')
from parser import *
from random import *
from solver import *

def main():
	
	print('Case Valid Input :')
	for i in range(10):
		j = uniform(-1000, 1000)
		l = uniform(-1000, 1000)
		cmd = f"{j}*X^0 = {l}*X^0"
		print(cmd)
		parser = Parser(cmd)
		solver = Solver(parser.left_member, parser.right_member)
		solver.solve()
		print('\n')

	print('\n')
	for i in range(10):
		j = uniform(-1000, 1000)
		l = uniform(-1000, 1000)
		g = uniform(-1000, 1000)
		h = uniform(-1000, 1000)
		cmd = f"{j}*X^0 + {g}*X^1 = {l}*X^0 + {h}*X^1"
		print(cmd)
		parser = Parser(cmd)
		solver = Solver(parser.left_member, parser.right_member)
		solver.solve()
		print('\n')

	
	print('\n')
	for i in range(10):
		j = uniform(-1000, 1000)
		l = uniform(-1000, 1000)
		g = uniform(-1000, 1000)
		h = uniform(-1000, 1000)
		k = uniform(-1000, 1000)
		m = uniform(-1000, 1000)
		cmd = f"{j}*X^0 + {g}*X^1 + {k}*X^2 = {l}*X^0 + {h}*X^1 + {m}*X^2"
		print(cmd)
		parser = Parser(cmd)
		solver = Solver(parser.left_member, parser.right_member)
		solver.solve()
		print('\n')

	print('Case Invalid input:\n')
	dont = False
	cmd = f"1*X^0 + 0*X^0 + 1*X^2 = 2*X^0 + 2*X^1 + 3*X^2"
	print(cmd)
	parser = Parser(cmd)
	if parser.check_factors() == 0:
		print('Error : bad factors.')
		dont = True
	if parser.check_powers() == 0:
		print('Error : bad exponent.')
		dont = True
	if dont == False:
		solver = Solver(parser.left_member, parser.right_member)
		solver.solve()
	print('\n')

	dont = False
	cmd = f"2**X^0 + 3**X^1 + 2**X^2 = 2*X^0 + 3*X^1 + 2*X^2"
	print(cmd)
	parser = Parser(cmd)
	if parser.check_factors() == 0:
		print('Error : bad factors.')
		dont = True
	if parser.check_powers() == 0:
		print('Error : bad exponent.')
		dont = True
	if dont == False:
		solver = Solver(parser.left_member, parser.right_member)
		solver.solve()
	print('\n')

	dont = False
	cmd = f"2*X^^0 + 2*X^1 + 2*X^2 = 2*X^0 + 2*X^1 + 2*X^2"
	print(cmd)
	parser = Parser(cmd)
	if parser.check_factors() == 0:
		print('Error : bad factors.')
		dont = True
	if parser.check_powers() == 0:
		print('Error : bad exponent.')
		dont = True
	if dont == False:
		solver = Solver(parser.left_member, parser.right_member)
		solver.solve()
	print('\n')

	dont = False
	cmd = f"2mù*X^0 = 2*X^0 + 3*X^1 + 2*X^2"
	print(cmd)
	parser = Parser(cmd)
	if parser.check_factors() == 0:
		print('Error : bad factors.')
		dont = True
	if parser.check_powers() == 0:
		print('Error : bad exponent.')
		dont = True
	if dont == False:
		solver = Solver(parser.left_member, parser.right_member)
		solver.solve()

	dont = False
	cmd = f"2*X^0  == 3*X^0"
	print(cmd)
	parser = Parser(cmd)	
	if parser.check_factors() == 0:
		print('Error : bad factors.')
		dont = True
	if parser.check_powers() == 0:
		print('Error : bad exponent.')
		dont = True
	if dont == False:
		solver = Solver(parser.left_member, parser.right_member)
		solver.solve()
	print('\n')

	dont = False
	cmd = f"2*X^1 + 3*X^2 = 3*X^0 + 4*X^1 + 4*X^2"
	print(cmd)
	parser = Parser(cmd)
	if parser.check_factors() == 0:
		print('Error : bad factors.')
		dont = True
	if parser.check_powers() == 0:
		print('Error : bad exponent.')
		dont = True
	if dont == False:
		solver = Solver(parser.left_member, parser.right_member)
		solver.solve()
	
	dont = False
	print('\n')
	cmd = f"3*X^0 + 4*X^1 =    "
	print(cmd)
	parser = Parser(cmd)
	if parser.check_factors() == 0:
		print('Error : bad factors.')
		dont = True
	if parser.check_powers() == 0:
		print('Error : bad exponent.')
		dont = True
	if dont == False:
		solver = Solver(parser.left_member, parser.right_member)
		solver.solve()
	print('\n')
	
	dont = False
	cmd = f"2*XX^0 + 3*X^1 = 3*X^0 + 4*X^1 + 4*X^2"
	print(cmd)
	parser = Parser(cmd)
	if parser.check_factors() == 0:
		print('Error : bad factors.')
		dont = True
	if parser.check_powers() == 0:
		print('Error : bad exponent.')
		dont = True
	if dont == False:
		solver = Solver(parser.left_member, parser.right_member)
		solver.solve()

	dont = False
	cmd = f"2*X^0 + 3*X^2 = 3*X^0 + 4*X^1 + 4*X^2"
	print(cmd)
	parser = Parser(cmd)
	if parser.check_factors() == 0:
		print('Error : bad factors.')
		dont = True
	if parser.check_powers() == 0:
		print('Error : bad exponent.')
		dont = True
	if dont == False:
		solver = Solver(parser.left_member, parser.right_member)
		solver.solve()

	dont = False
	cmd = f"2*X^$0 + 3*X^1 = 3*X^0 + 4*X^1 + 4*X^2"
	print(cmd)
	parser = Parser(cmd)
	if parser.check_factors() == 0:
		print('Error : bad factors.')
		dont = True
		quit()
	if parser.check_powers() == 0:
		print('Error : bad exponent.')
		dont = True
		quit()
	if dont == False:
		solver = Solver(parser.left_member, parser.right_member)
		solver.solve()

	dont = False
	cmd = f"2*X^ + 3*X^1 = 3*X^0 + 4*X^1 + 4*X^2"
	print(cmd)
	parser = Parser(cmd)
	if parser.check_factors() == 0:
		print('Error : bad factors.')
		dont = True
		quit()
	if parser.check_powers() == 0:
		print('Error : bad exponent.')
		dont = True
		quit()	
	solver = Solver(parser.left_member, parser.right_member)
	solver.solve()

	dont = False
	cmd = f"2*X^0 + 3 = 3*X^0 + 4*X^1 + 4*X^2"
	print(cmd)
	parser = Parser(cmd)
	if parser.check_factors() == 0:
		print('Error : bad factors.')
		dont = True
	if parser.check_powers() == 0:
		print('Error : bad exponent.')
		dont = True
	if dont == False:
		solver = Solver(parser.left_member, parser.right_member)
		solver.solve()

	dont = False
	cmd = f"2*X^0 + 3..3*X^1 = 3*X^0 + 4*X^1 + 4*X^2"
	print(cmd)
	parser = Parser(cmd)
	if parser.check_factors() == 0:
		print('Error : bad factors.')
		dont = True
	if parser.check_powers() == 0:
		print('Error : bad exponent.')
		dont = True
	if dont == False:
		solver = Solver(parser.left_member, parser.right_member)
		solver.solve()

	dont = False
	cmd = f"2*X^0 + 3*X^1 = 3      *X^0 + 4   *X^1 +4   *X^2"
	print(cmd)
	parser = Parser(cmd)
	if parser.check_factors() == 0:
		print('Error : bad factors.')
		dont = True
	if parser.check_powers() == 0:
		print('Error : bad exponent.')
		dont = True
	if dont == False:
		solver = Solver(parser.left_member, parser.right_member)
		solver.solve()
	
if __name__ == '__main__':
    main()
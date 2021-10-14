# ########################################################################## #
#                                                                            #
#                                                        :::      ::::::::   #
#   computorV1.py                                      :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: glecler <glecler@student.42.fr>            +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2021/11/10 by glecler                    #+#    #+#             #
#   Updated: 2021/11/10 by glecler                   ###   ########.fr       #
#                                                                            #
# ########################################################################## #

#!/usr/bin/python3

import sys
from parser import *
from solver import *

def main():
	
	if (len(sys.argv) != 2):
		print('Wrong number of arguments!')
		quit()
	
	input = sys.argv[1]

	if (sum(1 for i in input if (i > '9' or i < '0') and i not in ('=', 'X', '^', '-', '+', '*', ' ', '.'))):
		print('Wrong character.')
		quit()
	if (sum(1 for i in input if i == '=')) != 1:
		print('Missing or added \'=\'')
		quit()
	
	parser = Parser(input)
	
	if parser.check_factors() == 0:
		print('Error : bad factors.')
		quit()
	if parser.check_powers() == 0:
		print('Error : bad exponent.')
		quit()
	
	solver = Solver(parser.left_member, parser.right_member)
	solver.solve()

if __name__ == '__main__':
	main()
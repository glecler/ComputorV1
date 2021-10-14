# ########################################################################## #
#                                                                            #
#                                                        :::      ::::::::   #
#   parser.py                                          :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: glecler <glecler@student.42.fr>            +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2021/11/10 by glecler                    #+#    #+#             #
#   Updated: 2021/11/10 by glecler                   ###   ########.fr       #
#                                                                            #
# ########################################################################## #

class Member:
	def __init__(self, factors, powers):
		self.factors = factors
		self.powers = powers
	
	def __str__(self):
		ret = ''
		sign = ''
		if self.factors == 0 and self.powers == 0:
			return "0"
		for i in range(len(self.factors)):
			if float(self.factors[i]) > 0 and i != 0:
				sign = '+'
			else:
				sign = ''
			ret += f'{sign} {self.factors[i]} * X^{self.powers[i]}'
		return ret

class Parser:
	def __init__(self, input):
		left = self.parse(input.split('=')[0].strip())
		right = self.parse(input.split('=')[1].strip())
		self.left_member = Member(left[0], left[1])
		self.right_member = Member(right[0], right[1])

	def __str__(self):
		return f'{str(self.left_member)} = {str(self.right_member)}'

	def parse(self, input):
		input = input.split('*')
		input = [i.split()[j] for i in input for j in range(len(i.split()))]
		input = [i.strip() for i in input]
		factors, powers = [], []
		if len(input) == 0:
			print('Error : Empty input.')
			return 0, 0
		last_string = 'sign'
		sign = ''
		for i in input:
			if i == '-' or i == '+':
				sign = i
				last_string = 'sign'
			elif self.is_num(i) and last_string == 'sign':
				factors.append((sign + i).strip('+'))
				last_string = 'factor'
			elif '^' in i:
				if self.is_num(i.split('^')[1]):
					powers.append(i.split('^')[1])
				else:
					print('Error: bad exponent.')
				last_string = 'power'
		if len(factors) != len(powers):
			print('Error : Invalid input.')
			return 0, 0
		return factors, powers

	
	def check_factors(self):
		if self.right_member.factors == 0 or self.left_member.factors == 0:
			return 0

	def check_powers(self):
		if self.right_member.powers == 0 or self.left_member.powers == 0:
			return 0
		for powers in [self.right_member.powers, self.left_member.powers]:
			for x in range(len(powers)):
				if powers[x] != str(x):
					return 0
		return 1

	@staticmethod
	def is_num(string):
		num = True
		dot = 0
		for i in range(len(string)):
			if string[i] == '.':
				dot += 1
			if string[i] == '-' and i == 0:
				continue
			if '9' < string[i] or string[i] < '0' and string[i] != '.':
				num = False
		if dot > 1:
			num = False
		return num
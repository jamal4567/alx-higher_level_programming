#!/usr/bin/python3
if __name__ == "__main__":
	import sys
	counter = len(sys.argv)-1
	if counter != 3:
		sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
		sys.exit(1)
	else:
		from calculator_1 import add, sub, mul, div
		if sys.argv[2] == "+":
			print("{} + {} = {}".format(int(sys.argv[1]), int(sys.argv[3]), add(int(sys.argv[1]), int(sys.argv[3]))))
		elif sys.argv[2] == "-":
			print("{} - {} = {}".format(int(sys.argv[1]), int(sys.argv[3]), sub(int(sys.argv[1]), int(sys.argv[3]))))
		elif sys.argv[2] == "*":
			print("{} * {} = {}".format(int(sys.argv[1]), int(sys.argv[3]), mul(int(sys.argv[1]), int(sys.argv[3]))))
		elif sys.argv[2] == "/":
			print("{} / {} = {}".format(int(sys.argv[1]), int(sys.argv[3]), div(int(sys.argv[1]), int(sys.argv[3]))))
		else:
			sys.stderr.write("Unknown operator. Available operators: +, -, * and /\n")
			sys.exit(1)

from random import seed,randint
from ctypes import *
import sys

def get_values():
	stat = []
	for i in xrange(4):
		stat.append(randint(1,6))
	return sorted(stat)

def sum_three(stats):
	return sum(stats[1:])

def rnd_seed():
	while True:
		try:
			a = raw_input('Type a seed to determine randoms:  ')
			if a == "":
				continue
			break
		except TypeError:
			print 'type a fuckin hashable object ya dink'
	seed(a)

def my_seed(x):
	seed(str(x))

def roll_stats():
	rnd_seed()
	stat_list = []
	for i in xrange(6):
		s = stat_list.append(sum_three(get_values()))

	return sorted(stat_list, reverse=True)

def main():
	windll.Kernel32.GetStdHandle.restype = c_ulong
	h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))

	while True:
		s = roll_stats()
		su = sum(s)
		sys.stdout.write('\n\tStat point sum: ')
		if su >= 96:
			windll.Kernel32.SetConsoleTextAttribute(h, 14)
		elif su >= 88:
			windll.Kernel32.SetConsoleTextAttribute(h, 10)
		elif su >= 78:
			windll.Kernel32.SetConsoleTextAttribute(h, 11)
		elif su <= 63:
			windll.Kernel32.SetConsoleTextAttribute(h, 12)
		sys.stdout.write('%s' % str(su))
		windll.Kernel32.SetConsoleTextAttribute(h, 15)

		sys.stdout.write('\n\tStats: [')
		for i,item in enumerate(s):
			if item == 18:
				windll.Kernel32.SetConsoleTextAttribute(h, 14)
			elif item >= 16:
				windll.Kernel32.SetConsoleTextAttribute(h, 10)
			elif item >= 14:
				windll.Kernel32.SetConsoleTextAttribute(h, 11)
			elif item <= 9:
				windll.Kernel32.SetConsoleTextAttribute(h, 12)
			sys.stdout.write('%s' % str(item))
			windll.Kernel32.SetConsoleTextAttribute(h, 15)
			if i == 5:
				sys.stdout.write(']\n\n')
			else:
				sys.stdout.write(', ')
		br = raw_input('')


if __name__ == '__main__':
	main()

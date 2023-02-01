#!/usr/bin/env python3


if __name__ == '__main__':
	
	for arg in sys.argv:
		if arg == '-help' or arg == '-h':
			print('help needed')
			sys.exit(0)

	iter_argv = iter(sys.argv)
	flag1 = next(iter_argv)
	flag2 = next(iter_argv)
	flag3 = next(iter_argv)

	if flag1:
		print('flag1 is on')

	if flag2:
		print('flag2 is on')

	if flag3:
		print('flag3 is on')

	option1 = next(iter_argv)
	print('option1 is set to', option1)
	option2 = next(iter_argv)
	print('option2 is set to', option2)
	option3 = next(iter_argv)
	print('option3 is set to', option3)

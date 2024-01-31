import sys

args = sys.argv[1:]
if args[1]:
    if args[1] == 'en':
        print('hello,' + args[0] + '!')
else:
    print('你好，' + args[0] + '!')
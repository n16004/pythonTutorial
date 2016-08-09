import sys
print(sys.argv)

print('hello python')
print('open logfile...')

sys.stderr.write('warning: log file not found starting a new one\n')

print('finish')

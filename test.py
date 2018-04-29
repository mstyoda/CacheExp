import os


f = '.'
fs = os.listdir('.')

for f1 in fs:
	tmp_path = os.path.join(f,f1)
	if 'trace.gz' in tmp_path:
		print tmp_path


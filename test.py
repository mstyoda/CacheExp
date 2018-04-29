import os


sh = ''
f = '.'
fs = os.listdir('.')

for f1 in fs:
	tmp_path = os.path.join(f,f1)
	if 'trace.gz' in tmp_path:
		tmp_id = tmp_path[2:5] + '.stats'
		tmp_path = '.' + tmp_path
		sh += '../bin/CMPsim.usertrace.64 -threads 1 -t '+ tmp_path + ' -o ' + tmp_id + '0 -cache UL3:1024:64:16 -LLCrepl 0\n'
		sh += '../bin/CMPsim.usertrace.64 -threads 1 -t '+ tmp_path + ' -o ' + tmp_id + '1 -cache UL3:1024:64:16 -LLCrepl 1\n'
		sh += '../bin/CMPsim.usertrace.64 -threads 1 -t '+ tmp_path + ' -o ' + tmp_id + '2 -cache UL3:1024:64:16 -LLCrepl 2\n'
		break
open('runs/do_run.sh','w').write(sh)

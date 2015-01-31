import os
import sys

config = {}

#read config
def read_config():
	#configfile = sys.argv[1]
	configfile = 'pipe2config'
	f = open(configfile, 'r')
	for line in f:
		if '#' not in line and len(line) > 2:
			line = line.strip().split(':')
			config[line[0]] = line[1]
	f.closed
	
#interpret config
def interpret_cufflinks():
	option = ''
	try:
		if config['cufflinks_assembly'] == 'strict':
			option += '-G %s ' %(config['cufflinks_annote'])
		elif config['cufflinks_assembly'] == 'guided':
			option += '-g %s ' %(config['cufflinks_annote'])
		else:
			print 'invalid assembly option'	
			
		if config['cufflinks_bias'] == 'Y':
			option += '-b %s ' %(config['cufflinks_bias_genome'])
		elif config['cufflinks_bias'] == 'N':
			option = option
		else:
			print 'invalid cufflinks bias config'
		
		if config['cufflinks_init'] == 'Y':
			option += '-u '
		elif config['cufflinks_init'] == 'N':
			option = option
		else:
			print 'invalid cufflinks init config'
		
		if config['cufflinks_lib_type'] in ['fr-unstranded', 'fr-firststrand', 'fr-secondstrand']:
			option += '--library-type %s ' %(config['cufflinks_lib_type'])
		elif config['cufflinks_lib_type'] == '':
			option = option
		else:
			print 'invalid library type'
		
		return option
		
	except KeyError:
		print 'invalid configuration'
		
#interpret config
def interpret_cuffdiff():
	option = ''
	try:
		if config['cuffdiff_cond'] != '':
			option += '-L %s ' %(config['cuffdiff_cond'])
	
		if config['cuffdiff_time'] == 'Y':
			option += '-T '
			
		if config['cuffdiff_bias'] == 'Y':
			option += '-b %s ' %(config['cuffdiff_bias_genome'])
		elif config['cuffdiff_bias'] == 'N':
			option = option
		else:
			print 'invalid cuffdiff bias config'
		
		if config['cuffdiff_init'] == 'Y':
			option += '-u '
		elif config['cuffdiff_init'] == 'N':
			option = option
		else:
			print 'invalid cuffdiff init config'
		
		if config['cuffdiff_lib_type'] in ['fr-unstranded', 'fr-firststrand', 'fr-secondstrand']:
			option += '--library-type %s ' %(config['cuffdiff_lib_type'])
		elif config['cuffdiff_lib_type'] == '':
			option = option
		else:
			print 'invalid library type'
		
		if config['cuffdiff_annote'] != '':
			option += '%s ' %(config['cuffdiff_annote'])
		
		return option
		
	except KeyError:
		print 'invalid configuration'		
		

#quantify transcript
def cufflinks():
	option = interpret_cufflinks()
	try:
		cmd1 = 'cufflinks -o %s %s %s' %(config['cufflinks_out_folder'], option,  config['cufflinks_bam'])
		print cmd1
		os.system(cmd1)
	except KeyError:
		print 'invalid configuration'		

#differential expression
def cuffdiff():
	option = interpret_cuffdiff()		
	try:
		cmd1 = 'cuffdiff -o %s %s %s' %(config['cuffdiff_out_folder'], option,  config['cuffdiff_bam'])
		print cmd1
		os.system(cmd1)
	except KeyError:
		print 'invalid configuration'
		
							
def run():
	read_config()
	cufflinks()
	cuffdiff()
	
run()
	


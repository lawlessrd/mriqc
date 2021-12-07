#!/usr/bin/env python

## Check for dataset_description file in BIDS folder

import os,glob,json,sys,getopt

def dataset_description_file(in_dir, project, subject):
    """
    Build BIDS dataset description json file
    :param BIDS_PROJ_DIR: Project BIDS directory
    :param XNAT: XNAT interface
    :param project: XNAT Project
    """
    BIDSVERSION = "1.0.1"
    dataset_description = dict()
    dataset_description['BIDSVersion'] = BIDSVERSION
    dataset_description['Name'] = project
    dataset_description['Subject'] = subject
    dataset_description['Author'] = "No Author defined on XNAT"
    with open(os.path.join(in_dir, 'dataset_description.json'), 'w') as f:
        json.dump(dataset_description, f, indent=2)

def main(argv):
	in_dir = ''
	project = ''
	subject = ''
	try:
		opts, args = getopt.getopt(argv, "hi:p:s:",["in_dir=","project=","subject="])
	except getopt.GetoptError:
		print('dataset_description_check.py -i <folder> -p <project> -s <subject>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('dataset_description_check.py -i <folder>')
			sys.exit()
		elif opt in ("-i", "--in_dir"):
			in_dir = arg
		elif opt in ("-p","--project"):
			project = arg
		elif opt in ("-s","--subject"):
			subject = arg

	dataset_json = glob.glob(in_dir + '/dataset_description.json')

	print('Checking for dataset_description.json')
	if dataset_json:
		print('File found. Proceeding to MRIQC processing.')
	else:
		print('File not found. Creating dataset_description.json')
		dataset_description_file(in_dir, project, subject)
		print('Creation complete. Proceeding to MRIQC processing.')

if __name__ == '__main__':
	main(sys.argv[1:])
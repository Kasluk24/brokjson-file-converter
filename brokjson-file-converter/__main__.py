import argparse
import json
import brokjson
from pathlib import Path

# Convert GeoJSON to BrokJSON
def toBrok(infile, outfile):
	geo = json.loads(open(infile, 'r').read())
	brok = brokjson.geo2brok(geo)
	
	outfile.parents[0].mkdir(exist_ok=True)
	
	with open(outfile, 'w') as file:
		file.write(json.dumps(brok))
	

# Convert BrokJSON to GeoJSON
def toGeo(infile, outfile):
	brok = json.loads(open(infile, 'r').read())
	geo = brokjson.brok2geo(brok)
	
	outfile.parents[0].mkdir(exist_ok=True)
	
	with open(outfile, 'w') as file:
		file.write(json.dumps(geo))
	

if __name__ == '__main__':
	# Argument parser
	parser = argparse.ArgumentParser(description='Convert GeoJSON files to BrokJSON files and vice versa from command line')
	parser.add_argument('function', choices=['g2b', 'b2g'])
	parser.add_argument('infile', metavar='I', type=str, nargs=1, help='GeoJSON or brokJSON file to convert')
	parser.add_argument('outfile', metavar='O', type=str, nargs='*', help='Converted file')
	args = parser.parse_args()
	
	# File path
	infile = Path(args.infile[0])
	outfile = Path()
	
	if args.outfile:
		outfile = Path(args.outfile[0])
	else:
		outfile = (infile.parents[0] / args.function / infile.name)

	# Select function
	if args.function == 'g2b':
		toBrok(infile, outfile)
		
	if args.function == 'b2g':
		toGeo(infile, outfile)
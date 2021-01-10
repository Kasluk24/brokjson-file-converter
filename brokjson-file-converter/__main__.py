import argparse
import json
import brokjson
from pathlib import Path


# Convert GeoJSON to BrokJSON (single file)
def toBrok(infile, outfile=None):
    # Specifie outfile if not given and create directory
    if not outfile:
        outfile = Path(infile.parents[0] / 'brokjson' / infile.name)

    outfile.parents[0].mkdir(exist_ok=True)

    # Read geojson object from file and create brokjson object
    geo = json.loads(open(infile, 'r').read())
    brok = brokjson.geo2brok(geo)

    # Write file
    with open(outfile, 'w') as file:
        file.write(json.dumps(brok))


# Convert BrokJSON to GeoJSON (single file)
def toGeo(infile, outfile=None):
    # Specifie outfile if not given and create directory
    if not outfile:
        outfile = Path(infile.parents[0] / 'geojson' / infile.name)

    outfile.parents[0].mkdir(exist_ok=True)

    # Read brokjson object from file and create geojson object
    brok = json.loads(open(infile, 'r').read())
    geo = brokjson.brok2geo(brok)

    # Write file
    with open(outfile, 'w') as file:
        file.write(json.dumps(geo))


# Convert GeoJSON to BrokJSON (directory)
def toBrokMass(indir, outdir=None):
    # Specifie output directory if not given and create it
    if not outdir:
        outdir = Path(indir / 'brokjson')

    outdir.mkdir(parents=True, exist_ok=True)

    # Load all json files
    infiles = indir.glob('*.json')
    for file in infiles:
        # Read geojson object from file and create brokjson object
        geo = json.loads(open(file, 'r').read())
        brok = brokjson.geo2brok(geo)

        # Write file
        with open((outdir / file.name), 'w') as writefile:
            writefile.write(json.dumps(brok))


# Convert BrokJSON to GeoJSON (directory)
def toGeoMass(indir, outdir=None):
    # Specifie output directory if not given and create it
    if not outdir:
        outdir = Path(indir / 'geojson')

    outdir.mkdir(parents=True, exist_ok=True)

    # Load all json files
    infiles = indir.glob('*.json')
    for file in infiles:
        # Read brokjson object from file and create geojson object
        brok = json.loads(open(file, 'r').read())
        geo = brokjson.brok2geo(brok)

        # Write file
        with open((outdir / file.name), 'w') as writefile:
            writefile.write(json.dumps(geo))


if __name__ == '__main__':
    # Argument parser
    parser = argparse.ArgumentParser(description='Convert GeoJSON files to BrokJSON files and vice versa from command line')
    parser.add_argument('function', choices=['geo2brok', 'brok2geo'], help='Direction of conversion: geo2brok = GeoJSON to BrokJSON, brok2geo = BrokJSON to GeoJSON')
    parser.add_argument('inpath', metavar='I', type=str, nargs=1, help='GeoJSON or BrokJSON file or directory to convert')
    parser.add_argument('outpath', metavar='O', type=str, nargs='*', help='Converted file or output directory')
    args = parser.parse_args()

    # File path
    inpath = Path(args.inpath[0])
    outpath = Path()
    try:
	    outpath = Path(args.outpath[0])
    except IndexError:
	    outpath = None

    # Select function
    if args.function == 'geo2brok':
        if inpath.is_dir():
            toBrokMass(inpath, outpath)
        else:
            toBrok(inpath, outpath)

    if args.function == 'brok2geo':
        if inpath.is_dir():
            toGeoMass(inpath, outpath)
        else:
            toGeo(inpath, outpath)

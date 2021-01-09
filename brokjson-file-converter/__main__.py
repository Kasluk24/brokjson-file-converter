import argparse
import json
import brokjson
from pathlib import Path


# Convert GeoJSON to BrokJSON (single file)
def toBrok(infile, outfile):
    geo = json.loads(open(infile, 'r').read())
    brok = brokjson.geo2brok(geo)

    outfile.parents[0].mkdir(exist_ok=True)

    with open(outfile, 'w') as file:
        file.write(json.dumps(brok))


# Convert BrokJSON to GeoJSON (single file)
def toGeo(infile, outfile):
    brok = json.loads(open(infile, 'r').read())
    geo = brokjson.brok2geo(brok)

    outfile.parents[0].mkdir(exist_ok=True)

    with open(outfile, 'w') as file:
        file.write(json.dumps(geo))


# Convert GeoJSON to BrokJSON (directory)
def toBrokMass(infile, outfile):
    outfile.mkdir(exist_ok=True)

    infiles = infile.glob('/*.json')
    for file in infiles:
        geo = json.loads(open(file, 'r').read())
        brok = brokjson.geo2brok(geo)

        with open((outfile / file.name), 'w') as writefile:
            writefile.write(json.dumps(brok))


# Convert BrokJSON to GeoJSON (directory)
def toGeoMass(infile, outfile):
    outfile.mkdir(exist_ok=True)

    infiles = infile.glob('*.json')
    for file in infiles:
        brok = json.loads(open(file, 'r').read())
        geo = brokjson.brok2geo(brok)

        with open((outfile / file.name), 'w') as writefile:
            writefile.write(json.dumps(geo))


if __name__ == '__main__':
    # Argument parser
    parser = argparse.ArgumentParser(description='Convert GeoJSON files to BrokJSON files and vice versa from command line')
    parser.add_argument('function', choices=['geo2brok', 'brok2geo'], help='Direction of conversion: geo2brok = GeoJSON to BrokJSON, brok2geo = BrokJSON to GeoJSON')
    parser.add_argument('infile', metavar='I', type=str, nargs=1, help='GeoJSON or BrokJSON file to convert')
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
    if args.function == 'geo2brok':
        if infile.is_file():
            toBrok(infile, outfile)
        else:
            toBrokMass(infile, outfile)

        if args.function == 'brok2geo':
            if infile.is_file():
                toGeo(infile, outfile)
            else:
                toGeoMass(infile, outfile)

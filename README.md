# brokjson file converter

Python command line application to convert BrokJSON files to GeoJSON files and vice versa

What is [BrokJSON](https://www.brokjson.dev/)?

## Installation
### Get directly from GitHub and install with pip
- Execute the following command in the command line <br>
`pip install git+https://github.com/Kasluk24/brokjson-file-converter.git#egg=brokjson-file-converter`

### Manual download and install with pip
- Download the zip file from GitHub and save it in a directory of your choice
- Install from the zip file with the following command (replace <brokjson-file-converter.zip> with the path to the downloaded file) <br>
`pip install <brokjson-file-converter.zip>`

### Manual ussage
- Download the zip file from GitHub and save it in a directory of your choice
- Navigate to the file **__main__.py**
- Open the console and run with<br>
`python __main__.py <function> <inpath> <outpath>`

## Ussage
- The converter can convert BrokJSON files to GeoJSON files and also GeoJSON files to BrokJSON files. The first argument defines the direction.<br>
geo2brok = from GeoJSON to BrokJSON, brok2geo = BrokJSON to GeoJSON

### Convert single file
- The second argument defines the file to be converted.
- The third argument is optional and specifies the converted file. If this file is not specified, the converter creates a subfolder (geo2brok or brok2geo depending on the selected direction) and saves the converted file with the original filename in it.

### Mass conversion
- To convert all files in a directory with the ending "\*.json", just specifie the directory instead of the filename.
- If no export directory is specified, the files are written to a subfolder named "geojson" or "brokjson" depending on the direction.

## Examples
- Convert the GeoJSON file "GeoJSON.json" to the BrokJSON file BrokJSON.json<br>
`python -m brokjson-file-converter geo2brok GeoJSON.json BrokJSON.json`
- Convert the brokJSON file "BrokJSON.json" to the GeoJSON file GeoJSON.json<br>
`python -m brokjson-file-converter brok2geo BrokJSON.json GeoJSON.json`
- Convert all "\*.json" files inside the directory "brokfiles" to GeoJSON files into the directory "geofiles"
`python -m brokjson-file-converter brok2geo brokfiles geofiles`


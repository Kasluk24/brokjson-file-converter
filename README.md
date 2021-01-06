# brokjson file converter

Python command line application to convert brokJSON files to geoJSON files and vice versa

What is [brokJSON](https://www.brokjson.dev/)?


## Installation with pip
### Direct from GitHub
- Execute the following command in the command line <br>
`pip install git+https://github.com/Kasluk24/brokjson-file-converter.git#egg=brokjson-file-converter`

### Manual download
- Download the zip file from GitHub and save it in a directory of your choice
- Install from the zip file with the following command (replace <brokjson-file-converter.zip> with the path to the downloaded file) <br>
`pip install <brokjson-file-converter.zip>`

## Ussage
- The converter can convert brokJSON files to geoJSON files and geoJSON files to brokJSON files. The first argument defines the direction.<br>
geo2brok = from geoJSON to brokJSON, brok2geo = brokJSON to geoJSON
- The second argument defines the file to be converted.
- The third argument is optional and specifies the converted file. If this file is not specified, the converter creates a subfolder (geo2brok or brok2geo depending on the selected direction) and saves the converted file with the original filename in it.

### Examples
- Convert the geoJSON file "GeoJSON.json" to the brokJSON file BrokJSON.json<br>
`python brokjson-file-converter geo2brok GeoJSON.json BrokJSON.json`
- Convert the brokJSON file "BrokJSON.json" to the geoJSON file GeoJSON.json<br>
`python brokjson-file-converter brok2geo BrokJSON.json GeoJSON.json`

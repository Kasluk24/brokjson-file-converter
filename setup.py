import os
from setuptools import setup

# The directory containing this file
HERE = os.path.dirname(__file__)

# The text of the README file
README = open(os.path.join(HERE, "README.md"), 'r').read()

# This call to setup() does all the work
setup(
    name="brokjson-file-converter",
    version="1.0.0",
    description="Convert GeoJSON files to BrokJSON files and vice versa from command line",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Kasluk24/brokjson-file-converter",
    author="Lukas Gafner",
    author_email="gafner.lukas@gmx.ch",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["brokjson-file-converter"],
    include_package_data=True,
    python_requires='>=3.4',
    install_requires=['brokjson']
)

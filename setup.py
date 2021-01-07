import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="brokjson-file-converter",
    version="0.0.1",
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
    install_requires=['brokjson']
)

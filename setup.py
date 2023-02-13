from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0'
DESCRIPTION = 'multiply a number by the given multiplier'

# Setting up
setup(
    name="multiplier_test_specter",
    version=VERSION,
    author="Specter",
    author_email="<sigurd.thornes@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'multiply'],
    classifiers=[
        "Development Status :: done",
        "Intended Audience :: teacher",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
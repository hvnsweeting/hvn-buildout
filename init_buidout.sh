#!/bin/sh
# Download file
curl -O http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py

# Run file
python bootstrap.py

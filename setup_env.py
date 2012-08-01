#!/bin/sh
# Download file
echo "Downloading bootstrap.py..."
curl -O http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py

# Run file
echo "Running bootstrap.py..."
python bootstrap.py

echo "init buildout..."
# Init buildout
bin/buildout

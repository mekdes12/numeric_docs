#!/bin/bash
sphinx-build -vvv -N -b latex . _build
cd _build;make;cd ..

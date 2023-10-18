#!/bin/bash
cd monodikit || exit
pdoc -o ../docs/ --html ./
cd ..

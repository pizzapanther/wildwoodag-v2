#!/usr/bin/env bash

rm static/web.*
parcel build
hugo -b /
python3 prepare_native_app.py
rm -rf public/pimg/
cap sync $1
cap open $1

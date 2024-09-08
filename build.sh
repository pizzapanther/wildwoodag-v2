#!/usr/bin/env bash

export CAPACITOR_ANDROID_STUDIO_PATH=/snap/android-studio/163/bin/studio.sh

rm static/web.*
parcel build
hugo -b /
python3 prepare_native_app.py
rm -rf public/pimg/
cap sync $1
cap open $1

#!/usr/bin/env bash

tag=$1

if [[ $tag = v* ]]
then
  tag="${tag:1}"
fi

hugo -b /
python3 prepare_native_app.py
rm -rf public/pimg/
capgo bundle zip --bundle $tag

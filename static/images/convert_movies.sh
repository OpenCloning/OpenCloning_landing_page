#! /bin/bash

for file in *.mov; do
    ffmpeg -y -i ${file} -vf "setpts=0.66*PTS,fps=10,scale=1000:-1:flags=lanczos" "${file%.*}.gif"
done

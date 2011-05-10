#!/bin/bash

pdf=$(echo $1|sed 's/.pdf//g')

convert \
-density 150 \
-geometry 800x600 \
+antialias \
-rotate 90 \
-type GrayScale \
${pdf}.pdf image_%02d.jpg

zip ${pdf}.zip image_*.jpg
rm image_*.jpg

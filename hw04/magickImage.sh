TMP_FILE=/tmp/img.png

convert boris.png -background white -font Times-Roman -pointsize 264 \
	label:'Boris the Beagle' \
	-gravity Center -append $TMP_FILE

sudo fbi -noverbose -T 1 -a $TMP_FILE 

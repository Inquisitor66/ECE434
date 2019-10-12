TMP_FILE=/tmp/myName.png

convert -background Khaki -fill blue -font Times-Roman -pointsize 32 \
	-size 240x320 \
	label:'ImageMagick\nMy name is\nDalton\nStichtenoth' \
	$TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE

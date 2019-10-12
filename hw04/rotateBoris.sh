TMP_FILE=/tmp/img.png

convert -rotate "90" boris.png $TMP_FILE

sudo fbi -noverbose -T 1 -a $TMP_FILE

for YR in {2017..2023}; do
	echo Starting $YR
        [ -d $YR ] || mkdir $YR;
        find . -maxdepth 1 -regextype posix-extended -regex "^.+[^[:digit:]]$YR.+[-_]+.*" -exec mv {} ./$YR/ \;
	echo Finished $YR
done


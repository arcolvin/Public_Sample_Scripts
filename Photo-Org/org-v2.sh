for YR in {2017..2023}; do # Set date range for search
        [ -d $YR ] || mkdir $YR; # Make DIR if no exist
        
        # maxdepth 1 makes this non-recursive
        find . -maxdepth 1 -regextype posix-extended -regex "^.+[^[:digit:]]$YR.+[-_]+.*" -exec mv {} ./$YR/ \;
done



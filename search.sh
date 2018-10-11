#!/bin/bash
keyword=$1
echo $keyword

/usr/bin/python /data/gitsearch/coding.net.py $keyword >log
#/usr/bin/python /data/gitsearch/gitee.py $keyword >>log
#/usr/bin/python /data/gitsearch/giteecode.py $keyword >>log
/usr/bin/python /data/gitsearch/gitlab.py $keyword >>log


 

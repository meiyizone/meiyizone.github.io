#!/bin/bash

count=1
DATE=$(date -I)
PREFIX="/home/ren/play/meiyizone.github.io/_posts/"
echo $DATE
for img in $(cat imgs.txt)
do
	echo $img
	filename=${PREFIX}/${DATE}-ornament-${count}.markdown
	echo -n > $filename
	echo --- >> $filename
	echo layout: post >> $filename
	echo title:  "美艺空间手工饰品 ${DATE}-${count}" >> $filename
	echo description: 美艺空间手工饰品 >> $filename
	echo date: $DATE >> $filename
	echo img: $img >> $filename
	echo author: Xiaomeng >> $filename
	echo --- >> $filename
	count=$(($count + 1))
done

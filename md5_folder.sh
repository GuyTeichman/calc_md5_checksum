#! /bin/bash
# Run MD5 on all files in current folder
for file in *
do 
    md5sum $file
done
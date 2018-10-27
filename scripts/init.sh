#!/bin/bash
if [ ! -d "/root/.aws" ]; then mkdir "/root/.aws"; fi;

cp -r "/home/imagenamer/.aws" "/root"
aws configure
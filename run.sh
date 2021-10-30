#!/bin/bash
echo $1 $2 $3

PY=python3

if [ $1 = 'r' ]; then
  $PY main.py
elif [ $1 = 'x' ]; then
  echo ""
else
  echo "Arg did not match!"
fi

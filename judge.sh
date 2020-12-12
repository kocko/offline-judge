#!/bin/bash

JUDGE_HOME=/mnt/d/dev/offline-judge
ARGS=$@

if [[ $1 = 'parse' ]]
then
  python3 $JUDGE_HOME/parse-contest.py $2 $3
elif [[ $1 = 'test' ]]
then
  python3 $JUDGE_HOME/test-solution.py
elif [[ $1 = 'add-test' ]]
then
  python3 $JUDGE_HOME/add-test.py
fi

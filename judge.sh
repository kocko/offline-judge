#!/usr/bin/env bash

JUDGE_HOME=
ARGS=$@

if [[ $1 = 'parse' ]]
then
  python parse-contest.py $2 $3
elif [[ $1 = 'test' ]]
then
  python ../../test-solution.py
elif [[ $1 = 'add-test' ]]
then
  python ../../add-test.py
fi

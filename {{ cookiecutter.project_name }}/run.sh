#!/bin/bash
export PYTHONPATH=$PYTHONPATH:$(pwd)

easypy {{ cookiecutter.project_name }}_job.py  \
  -configuration easypy_config.yaml  \
  -html_log . \
  -testbed_file testbeds/default.yaml \
  "$@" \
  --print-timestamp

EASYPY_EXIT_CODE=$?
# if all tests succeed, easypy exits with code 0
# set an environment variable to determine whether notifications will fire
if [ $EASYPY_EXIT_CODE -eq 0 ]; then
    export RESULT="Passed"
else
    export RESULT="Failed"
fi
echo "Test Result: $RESULT"
exit $EASYPY_EXIT_CODE

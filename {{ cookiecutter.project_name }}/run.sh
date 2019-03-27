#!/bin/bash
export PYTHONPATH=$PYTHONPATH:$(pwd)

pyats run job {{ cookiecutter.project_name }}_job.py -configuration easypy_config.yaml --html-logs . --testbed-file testbeds/default.yaml

# if all tests succeed, easypy exits with code 0
# set an environment variable to determine whether notifications will fire
if [ $? -eq 0 ]; then
    export RESULT="Passed"
else
    export RESULT="Failed"
fi
echo "Test Result: $RESULT"

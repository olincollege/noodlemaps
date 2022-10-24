#!/usr/bin/env bash

#runs at level of noodlemaps folder

#add tests to run here

python3 -m pytest "testing/unit_tests/test_dummy.py"
python3 -m pytest "testing/unit_tests/test_exp_api_work.py"

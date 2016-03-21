# Motivation

## Description:

Build up testing cases for Moat including: 

1. Basic Ad searching;
2. Checking the Search Try These list:
   a. randomly click one of the three Ads in Try These list;
   b. check the three Ads in Try These list are generating randomly;
3. Checking the Recent Seen Ads are no more than half an hour old;
4. Checking Ad search result count:
   a. check Ad count if results are in a single page (not greater than 100);
   b. check Ad count even results are more than 100;
5. Check the "Share this Ad" feature.

Structure: 

1. Base test action + UiMap + Constants dictionary for common use in other modules;
2. Page objects for each page, and page common configuration;
3. Test directory including modules for each test scenarios.

## Installation

pip install -U selenium
pip install nose

Setting up python - Selenium environment: http://selenium-python.readthedocs.org/installation.html

After downloading the codes, please setup PATHONPATH. Example:

	export PYTHONPATH=/Users/RonnyWang/Workspace/Moativation_python

## Tests

1. nosetests   --  for running all test cases;
2. nosetests moat_*****_test.py   --  for running a specific test module;
3. nosetests --nocapture   --  for running along with logging information displayed on console

## Contributors

Ronny Wang
ronny.wang.r9@gmail.com 

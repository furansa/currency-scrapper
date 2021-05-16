#!/usr/bin/env bash
#
# Git hook to be called by pre-commit and trigger the tests
#
# Exit immediately if a command exits with a non-zero status
set -e

# Only run under the virtual environment to make sure the dependencies are met
[ ${VIRTUAL_ENV} ] || {
    echo "ERROR: Make sure the virtual environment is active."
    exit 1
}

# Runs unit tests, disable reports generation for now
# python3 -m pytest --cov=. --html=./tests/unit/report.html -v
cd app && python3 -m pytest -v tests/unit/

# Generate HTML coverage test report, disabled for now, needs better configuration
# coverage run -m pytest tests/*/*_test.py
# coverage report
# coverage html -d ./tests/unit/coverage

# Runs system tests and generates test report, disabled for now since is unstable
# robot -d ./tests/system/output ./tests/system

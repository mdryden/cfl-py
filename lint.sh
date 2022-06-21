#!/bin/sh

echo "flake8 errors:"
flake8 src test --count --show-source --statistics
echo "isort results:"
isort --check src --profile black
isort --check test
echo "mypy results:"
mypy src
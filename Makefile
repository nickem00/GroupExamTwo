#!/usr/bin/env make

# Change this to be your variant of the python command
PYTHON ?= python

# Define the path to the virtual environment and source directory
VENV := .venv
SRC := src
TESTS := $(SRC)/game/tests

# Print out colored action message
define MESSAGE
	@printf "\033[32;01m---> $(1)\033[0m\n"
endef

all: version venv install test

# ---------------------------------------------------------
# Setup a venv and install packages.
#
version:
	@$(MESSAGE) "Currently using executable: $(PYTHON)"
	@which $(PYTHON)
	@$(PYTHON) --version

venv:
	@test -d $(VENV) || $(PYTHON) -m venv $(VENV)
	@$(MESSAGE) "Now activate the Python virtual environment with 'source $(VENV)/bin/activate'"

install:
	@$(VENV)/Scripts/pip install -r requirements.txt

installed:
	@$(VENV)/bin/pip list

# ---------------------------------------------------------
# Cleanup generated and installed files.
#
clean:
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@rm -rf .coverage htmlcov

clean-all: clean
	@rm -rf $(VENV)

# ---------------------------------------------------------
# Test all the code at once.
#
lint:
	@$(VENV)/Scripts/flake8 $(SRC)
	@$(VENV)/Scripts/pylint $(SRC)

test:
	@$(MESSAGE) "Running tests with coverage..."
	@$(VENV)/Scripts/coverage run -m pytest $(TESTS)
	@$(VENV)/Scripts/coverage report -m
	@$(VENV)/Scripts/coverage html
# @$(VENV)/Scripts/pytest $(TESTS)

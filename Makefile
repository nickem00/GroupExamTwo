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

format:
	@$(VENV)/Scripts/black $(SRC)

test:
	@$(MESSAGE) "Running tests with coverage..."
	@$(VENV)/Scripts/coverage run -m pytest $(TESTS)
	@$(VENV)/Scripts/coverage report -m
	@$(VENV)/Scripts/coverage html
# @$(VENV)/Scripts/pytest $(TESTS)

# ---------------------------------------------------------
# Build Sphinx HTML documentation.
#
html:
	@$(MESSAGE) "Building Sphinx HTML documentation..."
	@test -d docs || mkdir docs
	@cd docs; sphinx-build -b html . _build/html

# ---------------------------------------------------------
# Generate UML diagrams in PlantUML format.
# PlantUML files are generated in the doc/uml directory.
# Add the modules to be included in the UML diagram in the pyreverse command.
#
uml:
	@$(MESSAGE) "Generating PlantUML diagrams..."
	pyreverse -o puml -p DiceGame src/game/player.py src/game/developer.py src/game/dice.py src/game/exceptions.py src/game/highscore.py src/game/histogram.py src/game/intelligence.py src/game/main.py src/game/playerVsComputer.py src/game/playerVsPlayer.py src/game/rules.py src/game/settingsClass.py src/game/tools.py
	mkdir -p doc/uml
	mv *.puml doc/uml/
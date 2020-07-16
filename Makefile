#/bin/make

SHELL ?= /bin/bash
OCEAN_NUTRITION_NAME ?= "$(shell python src/setup.py --name)"
OCEAN_NUTRITION_VERSION ?= "$(shell python src/setup.py --version)"
OCEAN_NUTRITION_DESCRIPTION ?= "$(shell python src/setup.py --description)"
ENV ?= local

include config/.env.$(ENV)
export

.DEFAULT_GOAL := help
.PHONY: help #: Display a list of command and exit.
help:
	@awk 'BEGIN {FS = " ?#?: "; print ""$(OCEAN_NUTRITION_NAME)" "$(OCEAN_NUTRITION_VERSION)"\n"$(OCEAN_NUTRITION_DESCRIPTION)"\n\nUsage: make \033[36m<command>\033[0m\n\nCommands:"} /^.PHONY: ?[a-zA-Z_-]/ { printf "  \033[36m%-10s\033[0m %s\n", $$2, $$3 }' $(MAKEFILE_LIST)

.PHONY: docs
docs:
	@$(OPEN) http://localhost:8000
	@$(MKDOCS) serve -f docs/mkdocs.yml

.PHONY: notebooks
notebooks:
	@$(JUPYTER) lab

.PHONY: lint
lint:
	@${FLAKE8} src tests

.PHONY: tests
tests:
	@$(PYTEST) tests

.PHONY: run
run:
	@$(OPEN) http://localhost:5000
	@$(FLASK) run

.PHONY: clean #: Delete build files.
clean:
	@[[ -z "${FORCE}" ]] || rm -r .venv
	@find . -name .ipynb_checkpoints -type d -not -path .venv -print0 | xargs -0 rm -r
	@find . -name __pycache__ -type d -not -path .venv -print0 | xargs -0 rm -r
	@find . -name *.pytest_cache -type d -not -path .venv -print0 | xargs -0 rm -r
	@find . -name *.egg-info -type d -not -path .venv -print0 | xargs -0 rm -r

%:
	@$(SHELL) scripts/$(*).sh
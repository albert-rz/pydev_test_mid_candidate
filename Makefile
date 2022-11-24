.PHONY: help venv clean clean-pyc clean-out lint tests cov format
.DEFAULT_GOAL := help

.SILENT: clean clean-pyc clean-out

PYTHON=python3
env=

PR=pydev_test_mid_candidate

define PRINT_HELP_PYSCRIPT
import re, sys

targets = []
for line in sys.stdin:
	match = re.match(r'^([a-zA-Z0-9_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		targets.append((target, help))

targets = sorted(targets, key=lambda x: x[0])
for target, help in targets:
    print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON) -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-pyc clean-out ## Clean pycs artifacts and out data
	rm -rf $(PR)

clean-out: ## Remove files within out/
	find out -type f \( ! -name ".gitkeep" \) -exec rm -f {} +
	find out -type d \( ! -wholename "out" \) -exec rm -fr {} +

lint: ## Check style with pylint and flake8
	pylint --exit-zero nvs_ex${env}

pre-commit: clean ## Run pre-commit without attempting a commit
	pre-commit run --all-files

format: ## Apply formatters
	black -l 100 nvs_ex${env}
	isort --profile black -l 100 nvs_ex${env}
	docformatter -r -i --wrap-summaries 100 --wrap-descriptions 90 nvs_ex${env}

serve:
	flask --app nvs_ex${env}.ex_4 run

ex: clean
	rm -rf $(PR)
	mkdir $(PR)
	cp -r .devcontainer_no_proxy $(PR)/.devcontainer
	cp -r .vscode assets images nvs_ex out $(PR)
	cp .dockerignore .editorconfig .gitignore .pre-commit-config.yaml .pylintrc $(PR)
	cp EXERCISE.md $(PR)/README.md
	cp LICENSE Makefile openapi.yml poetry.lock poetry.toml pydev_test_mid.code-workspace pyproject.toml $(PR)

repository =

clean:
	find . -name '__pycache__' | xargs rm -rf


build:
	( \
	. .venv/bin/activate; \
	python3 -m pip install build; \
	python3 -m build; \
	tar -tvf dist/*.tar.gz; \
	)


format:
	( \
	. .venv/bin/activate; \
	python3 -m black src/downloadurl tests; \
	python3 -m isort src/downloadurl tests; \
	)


install:
	( \
	. .venv/bin/activate; \
	python3 -m pip install -e .; \
	)


publish:
	@echo 'Use the following commands to publish:'
	@echo '. .venv/bin/activate'
	@echo 'python3 -m pip install build twine'
	@echo 'python3 -m build'
	@echo 'twine upload dist/*'



venv:
	( \
	python3 -m venv .venv; \
	. .venv/bin/activate; \
	python3 -m pip install -U pip; \
	python3 -m pip install pip-tools; \
	pip-compile --extra=dev --output-file=requirements.txt pyproject.toml; \
	python3 -m pip install -r requirements.txt; \
	rm requirements.txt; \
	)

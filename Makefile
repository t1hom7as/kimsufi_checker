PACKAGE = kimsufi-checker


# Default python: 3.6
PY = py36


.PHONY: isort
isort:
	@tox -e isort


.PHONY: lint
lint:
	@tox -e lint


# prompt_example> make bumpversion OPTIONS="-- --allow-dirty patch"
.PHONY: bumpversion
bumpversion:
	@tox -e bumpversion $(OPTIONS)


.PHONY: find_todo
find_todo:
	@grep --color=always -PnRe "(#|\"|\').*TODO" src/ || true


.PHONY: find_fixme
find_fixme:
	@grep --color=always -nRe "#.*FIXME" src/ || true


.PHONY: find_xxx
find_xxx:
	@grep --color=always -nRe "#.*XXX" src/ || true


.PHONY: count
count: clean
	@# @find src/ -type f \( -name "*.py" -o -name "*.rst" \) | xargs wc -l
	@echo "Lines of documentation:"
	@find docs/source/ -type f -name "*.rst" | xargs wc -l
	@echo "Lines of code:"
	@find src/ tests/ -type f -name "*.py" | xargs wc -l


.PHONY: clean
clean:
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' | xargs rm -rf
	@find . -type d -name '*.ropeproject' | xargs rm -rf
	@rm -rf build/
	@rm -rf dist/
	@rm -f src/*.egg
	@rm -f src/*.eggs
	@rm -rf src/*.egg-info/
	@rm -f MANIFEST
	@rm -rf docs/build/
	@rm -rf htmlcov/
	@rm -f .coverage
	@rm -f .coverage.*
	@rm -rf .cache/
	@rm -f coverage.xml
	@rm -f *.cover
	@rm -rf .pytest_cache/
	@rm -f debian/files
	@rm -f debian/debhelper-build-stamp
	@rm -f debian/$(PACKAGE).debhelper.log
	@rm -f debian/$(PACKAGE).*.debhelper
	@rm -f debian/$(PACKAGE).substvars
	@rm -rf debian/.debhelper
	@rm -rf debian/$(PACKAGE)/



.PHONY: install-dev
install-dev:
	@pip install -e .


##### Build #####

.PHONY: build-python-source
build-python-source:
	@python setup.py sdist


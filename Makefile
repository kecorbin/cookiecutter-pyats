test:
	rm -rf awesome_pyats && cookiecutter . && cd awesome_pyats && make test && cd ..

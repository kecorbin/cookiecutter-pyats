test:
	rm -rf awesome_pyats && \
	  echo "\n\n\n\n\n\n\n" | cookiecutter . && \
	 	cd awesome_pyats && \
		docker build -t test . && \
		docker run --rm test
		cd ..

awesome_pyats:

docker-test:
	rm -rf awesome_pyats && \
	  echo "\n\n\n\n\n\n\n\n\n\n\n\n" | cookiecutter . && \
	 	cd awesome_pyats && \
		docker build -t test . && \
		docker run --rm test
		cd ..

test:
	rm -rf awesome_pyats && \
		echo "\n\n\n\n\n\n\n\n\n\n\n\n" | cookiecutter . && \
		cd awesome_pyats && \
		./run.sh
		cd ..

test-global:
	rm -rf awesome_pyats && \
		echo "\n\n\n\n\n\n\n\n\n\n\n\n" | cookiecutter . && \
		cd awesome_pyats && \
		./run.sh --only-global
		cd ..

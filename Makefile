.phony: test

test:
	python -m unittest discover -p "*_test.py" -v
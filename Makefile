
# find python3
PYTHON=`which python3`

# our testing targets
.PHONY: tests flake black isort all

all: isort black flake tests

tests:
	${PYTHON} -m pytest  tests

flake:
	${PYTHON} -m flake8 api tests

black:
	${PYTHON} -m black -t py37 api tests

isort:
	${PYTHON} -m isort --atomic api tests

# end

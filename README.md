> Python Boot Camp (SoftServe, Dec 2017)
# Home work

## Dey 1: 

#### Task 1 - Build Vagrant
For starting vagrant:
```
vagrant up
```
For entry
```
vagrant ssh
```
or
```
ssh vagrant@192.168.33.10 # password: vagrant
```
[Link to Vagrantfile](https://github.com/shitikovkirill/pbc-PythonBootCamp/blob/master/Vagrantfile)

#### Task 2 - Fibonacci

Ran
```
python project/pbc_app/fibonacci.py
```

[Link to fibonacci.py](https://github.com/shitikovkirill/pbc-PythonBootCamp/blob/master/pbc_app/fibonacci.py)

#### Task 3 - Numbers pairs

Ran
```
python project/pbc_app/numbers_pairs.py
```

[Link to numbers_pairs.py](https://github.com/shitikovkirill/pbc-PythonBootCamp/blob/master/pbc_app/numbers_pairs.py)

## Dey 2: 

#### Task 1 - Prepare virtual environment

[Install pip, virtualenv and virtualenvwrapper](https://github.com/shitikovkirill/pbc-PythonBootCamp/blob/master/bootstrap/python.sh)

[Create virtualenv](https://github.com/shitikovkirill/pbc-PythonBootCamp/blob/master/bootstrap/virtualenvwrapper.sh)

[Run](https://github.com/shitikovkirill/pbc-PythonBootCamp/blob/master/bootstrap/run.sh)

#### Task 2 - Simple unit tests

Run tests:
```
cd project
workon PythonBootCamp
pytest
```
List of tests:

[test_fibonachi.py](https://github.com/shitikovkirill/pbc-PythonBootCamp/blob/master/tests/test_fibonacci.py)

[test_numbers_pairs.py](https://github.com/shitikovkirill/pbc-PythonBootCamp/blob/master/tests/test_numbers_pairs.py)

#### Task 3 Install Java on VM

[java.sh](https://github.com/shitikovkirill/pbc-PythonBootCamp/blob/master/bootstrap/java.sh)

## Dey 3:
#### Task 1 Structurize project

```
.
├── bootstrap
│   ├── common.sh
│   ├── java.sh
│   ├── python.sh
│   ├── run.sh
│   └── virtualenvwrapper.sh
├── pbc_app
│   ├── fibonacci.py
│   ├── __init__.py
│   ├── numbers_pairs.py
├── README.md
├── requirements.txt
├── tests
│   ├── __init__.py
│   ├── test_fibonacci.py
│   └── test_numbers_pairs.py
└── Vagrantfile
```

#### Task 2 Use 'parametrize'

[See pull request](https://github.com/shitikovkirill/pbc-PythonBootCamp/pull/13)

#### Task 3 Configure markers

Run marked tests

```
cd project
workon PythonBootCamp
pytest -v -m fibonacci_generator
```

[See pull request](https://github.com/shitikovkirill/pbc-PythonBootCamp/pull/14)

#### Task 4 Configure markers
Run CLI script
```
cd project
workon PythonBootCamp

python pbc_app/numbers_pairs.py -n 3 4 5 6 1 3 9 4 7 3

python pbc_app/fibonacci.py -n 7
```

## Dey 7:
#### Task 3 Test a grid config

[See pull request](https://github.com/shitikovkirill/pbc-PythonBootCamp/pull/30)

## Dey 8:
#### Task 1 Test a grid config

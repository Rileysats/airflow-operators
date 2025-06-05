# README.md

# My Airflow Operators

This project contains custom Airflow operators and hooks designed to extend the functionality of Apache Airflow.

## Installation

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage

### Custom Operators

The custom operators can be found in the `src/operators` directory. You can import and use them in your Airflow DAGs as follows:

```python
from operators.custom_operators import CustomOperator
```

### Custom Hooks

The custom hooks are located in the `src/hooks` directory. You can import and use them in your tasks as follows:

```python
from hooks.custom_hooks import CustomHook
```

## Running Tests

To run the tests for the custom operators and hooks, use the following command:

```bash
python -m unittest discover -s tests
```

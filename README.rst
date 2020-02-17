# PigLatin.py

A simple example project containing a PigLatin module, skeleton documentation
and PyTest based tests.

## Install the Dependencies

Create a new virtualenv, activate it and then install the required modules.

```
$ python3 -m venv my_venv
$ source my_venv/bin/activate
$ pip install -r requirements.py
```

(On Windows, the second step above should be, `my_venv\Scripts\activate`.)

## Run the Tests

```
$ pytest tests
```

## Build the Docs

```
$ cd docs
$ make html
```

The docs will be built in the `_build/html` directory. Just point your browser
at the `index.html` page in there.

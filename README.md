# cine-smith

App to automatically generate short format content

## Setup

- Install `python`, `pip` and `pipenv` if not already present locally.

- Run the following to install dependencies first

```
pipenv install
```

- Then execute the main.py script

```
pipenv run python main.py
```

- For adding a new dependency make sure to use

```
pipenv install <dependency>
```

So that the `Pipfile` remains updated

For API calls, create a `.env` file under the root directory,
and add the values in the file:

```
GCS_DEVELOPER_KEY = "<YOUR_GCS_DEVELOPER_KEY>"
GCS_CX = "<YOUR_GCS_CX>"

OPENAI_API_KEY = "<YOUR_OPENAI_API_KEY>"
```

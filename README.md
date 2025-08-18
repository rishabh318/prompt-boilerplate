.

## Prerequisites

- [Python](https://www.python.org/) (^v3.10)
- [Poetry](https://python-poetry.org/) (latest)
- [Pre-commit](https://pre-commit.com/) (latest)
- [Docker](https://www.docker.com/) (^v17.12)
- [Docker Compose](https://docs.docker.com/compose/) (^v1.18)
- [Git](https://git-scm.com/) (^v2.15)
- OS: Linux, macOS or Windows 10/11 with WSL2

## Setup and Installation

Follow the instructions below to setup your local development environment.

1. Install prerequisites

    ```bash
    # macOS
    $ brew install python3.10 libpq

    # Linux / WSL2
    $ sudo apt-get install python3.10 libpq-dev
    ```

    After installing python3.10, make sure to set it as default python version

    ```bash
    # Install Poetry
    $ curl -sSL https://install.python-poetry.org | python3.10 -

    # Install Pre-commit
    $ python3.10 -m pip install pre-commit
    ```

2. Clone the repository

    ```bash
    $ git clone git@gitlab.kjshvjkdfhjkcfd.git
    ```

3. Install dependencies and setup pre-commit

    ```bash
    $ cd <foldername>
    $ pre-commit install
    $ poetry install
    $ poetry self add poetry-plugin-export
    $ git switch development
    # create a new branch from development branch to work on a new feature and task assigned to you
    ```

4. Running the project

    Setting environment variables:
    ```bash
    $ cd <foldername>
    $ cp .env.example .env
    # Edit .env file to set environment variables
    ```

    Running the app using docker-compose:
    ```bash
    $ cd <foldername>
    $ docker compose up --build
    # Give it a few minutes to build and start the app

    # Use the command below to run any command inside the app container
    $ docker compose exec -it common_apis flash shell
    ```

    Open the API in browser: [http://localhost:8091/](http://localhost:8080/api/v1/)

5. Opening project in VSCode

    ```bash
    $ cd <foldername>
    $ code . # or any other code editor of your choice
    ```

    Setting Python interpreter:

    ```bash
    $ poetry env info -p
    # Copy the printed path to the Python interpreter, for example:
    # e.g: /Users/vinay/Library/Caches/pypoetry/virtualenvs/<foldername>-87UHZHXZ-py3.10
    ```

    - Open Command Palette (Ctrl+Shift+P / Cmd+Shift+P)
    - Select Python: Select Interpreter
    - Select "+ Enter interpreter path"
    - Paste the copied path + `/bin/python` then hit Enter/Return
    - Full path should look like: `/Users/vinay/Library/Caches/pypoetry/virtualenvs/<foldername>-87UHZHXZ-py3.10/bin/python`

6. Generating requirements.txt files

    Requirement files gets generated automatically using pre-commit hook just before comming the changes. However, you can also generate them manually using the following commands:

    ```bash
    $ cd <foldername>
    $ poetry export -f requirements.txt -o requirements.txt --without-hashes
    $ poetry export -f requirements.txt -o requirements.dev.txt --without-hashes --with dev
    ```

    Commit the generated files to the repository.

## Contributing

Follow the instructions below to contribute to the project.

- Clone the repository
- Create a new branch from `development` branch
- Make changes and commit them
- Fix any linting errors and commit again
- Push changes to remote
- Create a pull request to merge changes to `development` branch after code review

### Acknowledgments

- [**Python**](https://www.python.org/)
- [**Flask**](https://flask.palletsprojects.com/en/2.3.x/)
- [**Flask Migrate**](https://flask-migrate.readthedocs.io/en/latest/)
- [**Docker and Docker Compose**](https://www.docker.com/)
- [**PostgreSQL**](https://www.postgresql.org/)
- [**Redis**](https://redis.io/)
- [**Poetry**](https://python-poetry.org/)
- [**Pre-commit**](https://pre-commit.com/)
- [**Pytest**](https://docs.pytest.org/en/stable/)
- [**Ruff**](https://beta.ruff.rs/docs/)
- [**Black**](https://black.readthedocs.io/en/stable/)
- [**Flake8**](https://flake8.pycqa.org/en/latest/)
- [**Sentry**](https://sentry.io/)


### Steps to Move code From Common repo to Common api repo

1. go to development branch
    - git checkout development

2. take latest pull
    - git pull origin development

3. create new branch from development and switch to new branch
    - git checkout -b branch-name

4. commit all your changes on new branch
    - git add .
    - git commit -m "<commit messgae>"

5. push new branch to origin
    - git push origin branch-name

6. raise PR for merging new branch changes to development branch

7. once PR is merged checkout to development branch and take latest pull
    - git checkout development
    - git pull origin development

8. Switch to branch - chore/vinay/micro-to-mono-architecture
    - git fetch origin chore/vinay/micro-to-mono-architecture
    - git checkout chore/vinay/micro-to-mono-architecture

9. merge new changes from development to chore/vinay/micro-to-mono-architecture branch
    - git merge development

10. resolve conflicts
    - git add .
    ## commit without message
    - git commit

11. set new_origin for pushing code to Common API REPO
    - git remote add new_origin git@gitlab.cdhl.in:cdhl/<foldername>/<foldername>.git
    - git remote -v

12. Push changes to Common API Repo and Common Repo
    ## for Common API Repo
    - git push new_origin chore/vinay/micro-to-mono-architecture

    ## for Common Repo
    - git push origin chore/vinay/micro-to-mono-architecture

13. once changes are pushed go to https://gitlab.cdhl.in/cdhl/<foldername>/<foldername> and create new PR


## Localisation

We strongly follows the [Languages of India](https://en.wikipedia.org/wiki/Languages_of_India) standard for language codes. We have used the same language codes in our APIs.

All the tables/ORM will have a column named `language_code` which will be used to store max 3 chars long the language code of the record.

Each translated entry row will self reference to the original row using `parent_id` column.

### Language codes

| Language | Language Code |
| --- | --- |
| English | en |
| Hindi | hi |
| Marathi | mr |
| Gujarati | gu |
| Bengali | bn |
| Tamil | ta |
| Telugu | te |
| Kannada | kn |
| Malayalam | ml |

### Example

| id | parent_id | language_code | name |
| --- | --- | --- | --- |
| 1 | null | en | English |
| 2 | 1 | hi | हिंदी |
| 3 | 1 | mr | मराठी |
| 4 | 1 | gu | ગુજરાતી |
| 5 | 1 | bn | বাংলা |
| 6 | 1 | ta | தமிழ் |
| 7 | 1 | te | తెలుగు |
| 8 | 1 | kn | ಕನ್ನಡ |
| 9 | 1 | ml | മലയാളം |

### Designing the ORM

While designing the ORM, add `language_code` and `parent_id` columns to the table. Where `parent_id` will be the foreign key to the same table and `language_code` will be the language code of the record with default to `en`.

```python
class Example(db.Model):
    __tablename__ = 'example_table'
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('example_table.id'))
    language_code = db.Column(db.String(3), default='en', nullable=False)
    title = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text, nullable=False)
```

### Querying translated records

While querying the English version must always be selected along with selected language.

For example if user has set his preferred language as Hindi then English version will always be selected as per requirements to send main field to mixpanel or any other trackinganalytics tools.

### Changes to old querying codes

Also all the existing querying code be modified to only fetch records in English to avoid any breaking changes.

```sql
-- Get all records in English
SELECT * FROM example_table WHERE language_code = 'en';

-- Get all records in Hindi
SELECT * FROM example_table WHERE language_code = 'hi';
```

```python
# Get all records in English
Example.query.filter_by(language_code='en').all()
```

### How to fetch consilidated translated records

To fetch all the translated records in a single query, we can use the following query.

Asumming user has set his preferred language as Hindi.

```sql
SELECT * FROM example_table WHERE language_code in ('en', 'hi');
-- Or in case user has not set his preferred language
SELECT * FROM example_table WHERE language_code in ('en', 'en');
```

```python
# Get all records in Hindi
Example.query.filter_by(language_code=['en', 'hi']).all()
```

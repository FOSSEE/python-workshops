# Python testing with `pytest`

This is a very simple outline of this workshop:

- General introduction to testing and Test Driven Development (TDD)

- Start with a very simple example, `gcd`.

- Show how to do the simplest TDD using `pytest`.

- Basic `pytest` features:
  - Testing cases where an exception should be raised
  - Testing floating point numbers with `pytest.approx`
  - Grouping tests in classes.

- Next take a more complex problem:
  - Find all the git repositories recursively inside a given directory.
  - Write tests for this.
  - General approach on how to do this.
  - Use TDD.

- Writing fixtures:
  - Previous example as motivation for this.
  - Creating simple fixtures.
  - Fixture cleanup.
  - Fixture with data.
  - Fixtures using other fixtures.
  - Fixture scope and other ways to use fixtures with `pytest.mark`

- Some pointers on how to write better tests.
  - Link to useful articles.

- Interlude, travis-ci
  - Push code to github
  - Setup travis-ci
  - .travis.yml
  - Run tests.
  - Show updates and PRs.
  - Add badge to README.

- Coverage and improving tests.
  - Look at coverage
  - Show simple reports
  - HTML reports.

- Setup codecov.
  - See how codecov shows the reports and tracks coverage
  - Explore codecov.io

- More on testing with pytest
    - Using tmpdir.
    - Using capsys.
    - Using monkeypatch/mock.

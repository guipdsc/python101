# Tests

How to install pytest

```python
python3 -m pip install pytest
```

Logic behind tests:

- Arrange - set up environment in which the test is going to be executed (variables, files, etc)
- Act - run function or method to be tested
- Assert - Verify if expected conditions are met

Example from our code:

```python
def test_artifacts_with_dynamic_conf(foo_package, tmp_path):
    """
    Ensure that dynamic_conf package artifacts were found
    """
    dynamic_conf = {"REQUIRED_ARTIFACTS": {tmp_path: ["dynamic_conf_file.txt"]}}
    (tmp_path / "dynamic_conf_file.txt").touch()
    foo_package.update(dynamic_conf)
    assert foo_package.get_artifacts() == {
        tmp_path: {
            "file_example.txt",
            "dir_example/file_example_2.txt",
            "dynamic_conf_file.txt",
        },
        tmp_path / "additional": {"additional_original.txt"},
    }
```

Assert keyword

```python
def test_uppercase():
		assert "loud noises".upper() == "LOUD NOISES"
```

Fixture

```python
import pytest

@pytest.fixture
def example_fixture():
    return 1

def test_with_fixture(example_fixture):
    assert example_fixture == 1
```

Special Fixture

- tmp_path

more at [https://docs.pytest.org/en/6.2.x/fixture.html](https://docs.pytest.org/en/6.2.x/fixture.html)

Parametrization

```python
@pytest.mark.parametrize(
    "number,result", [(6, True), (7, False), (496, True), (8, False)]
)
def test_check_perfect(number, result):
    assert exercises.check_perfect(number) == result
```

Catch exceptions in pytest

```python
def test_invalid_close_tag():
    with pytest.raises(ValueError, match=r"Invalid XML:"):
        apinext.lib.manifest_file.ApinextManifestFile(INVALID_CLOSE_TAG)

```

Test driven development -TDD
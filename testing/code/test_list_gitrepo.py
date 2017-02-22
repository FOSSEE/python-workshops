import tempfile
import os
import shutil
import pytest


def is_git_repo(path):
    git_dir = os.path.join(path, '.git')
    return os.path.isdir(git_dir)


def find_all_git_repos(path):
    pass


@pytest.fixture
def git_repo():
    tmp_dir = tempfile.mkdtemp()
    git_repo = os.path.join(tmp_dir, '.git')
    if not os.path.exists(git_repo):
        os.makedirs(git_repo)

    yield tmp_dir

    shutil.rmtree(tmp_dir)


def test_is_git_repo_should_detect_git_repo(git_repo):
    # Given
    dir = git_repo

    # When
    result = is_git_repo(dir)

    # Then
    assert result == True


def test_is_git_repo_should_not_detect_non_git_repo():
    tmp_dir = tempfile.mkdtemp()
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    try:
        assert is_git_repo(tmp_dir) == False
    finally:
        shutil.rmtree(tmp_dir)

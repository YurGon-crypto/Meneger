
import pytest
import os
from my_context_manager import FileManager

@pytest.fixture
def file_obj():

    with FileManager('test_file.txt') as file:
        file.write('Hello, World!')
        file.flush()
        yield file


def pytest_fixture_post_finalizer(fixturedef, request):
    file_obj = request.getfixturevalue('file_obj')
    if file_obj:
        file_obj.close()
        if os.path.exists(file_obj.name):
            os.remove(file_obj.name)

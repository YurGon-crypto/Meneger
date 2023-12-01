import unittest
import tempfile
import os

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.flush()  # Ensure changes are flushed to the file
            self.file.close()
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print("File removed")  # Add this line for debugging


class TestFileManager(unittest.TestCase):
    def test_file_manager_success(self):
        # Positive test case when everything works as expected
        with FileManager('test_file.txt') as file:
            file.write('Hello, World!')
            file.flush()  # Ensure changes are flushed to the file
        self.assertTrue(os.path.exists('test_file.txt'))
        with open('test_file.txt', 'r') as file:
            content = file.read()
        self.assertEqual(content, 'Hello, World!')

    def test_file_manager_error_handling(self):
        # Test case when an error occurs within the context manager
        with self.assertRaises(ValueError):
            with FileManager('test_file.txt') as file:
                file.write('Hello, World!')
                raise ValueError("Something went wrong")

        # Ensure the file is not created or remains empty
        self.assertFalse(os.path.exists('test_file.txt'))

    def test_file_manager_file_not_found(self):
        # Test case when the file to be opened does not exist
        with self.assertRaises(FileNotFoundError):
            with FileManager('nonexistent_file.txt') as file:
                file.write('Hello, World!')

        # Ensure the file is not created
        self.assertFalse(os.path.exists('nonexistent_file.txt'))

    def test_file_manager_runtime_error(self):
        # Test case when a runtime error occurs outside the context manager
        with self.assertRaises(RuntimeError):
            with FileManager('test_file.txt') as file:
                file.write('Hello, World!')
            # Simulate a runtime error after exiting the context manager
            raise RuntimeError("Runtime error outside the context manager")

        # Ensure the file is not created or remains empty
        self.assertFalse(os.path.exists('test_file.txt'))


if __name__ == '__main__':
    unittest.main()

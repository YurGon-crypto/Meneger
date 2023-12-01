import logging

class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.counter = 0

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            self.counter += 1
            logging.info(f"File '{self.filename}' opened. Counter: {self.counter}")
            return self.file
        except Exception as e:
            logging.error(f"Error opening file '{self.filename}': {str(e)}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            self.counter -= 1
            logging.info(f"File '{self.filename}' closed. Counter: {self.counter}")
        if exc_type is not None:
            logging.error(f"Exception {exc_type.__name__}: {str(exc_value)}")
        return False

with FileContextManager("test_task_1.txt", "w") as file:
    file.write("Task 1: Testing FileContextManager")

with FileContextManager("test_task_1.txt", "r") as file:
    content = file.read()
    assert content == "Task 1: Testing FileContextManager"


logging.basicConfig(level=logging.INFO)

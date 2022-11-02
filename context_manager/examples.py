from contextlib import contextmanager

class CustomContextManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("entering")
        self.f=open(f"{ self.filename }","w")
        return self.f

    def __exit__(self, exc_type, exc_value, traceback):
        print("exiting")
        self.f.close()


@contextmanager
def managed_resource(filename):
    print("entering")
    f = open(f"{ filename }","w")
    try:
        yield f
    finally:
        print("exiting")
        f.close()

with CustomContextManager("context-class.txt") as f:
    f.write("foo")

with managed_resource("context-function.txt") as f:
    f.write("foo")
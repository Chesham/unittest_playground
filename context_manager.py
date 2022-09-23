from unittest.mock import Mock


def foo(self):
    return self


db = Mock()
db.__enter__ = foo
db.__exit__ = Mock()

print(f"{db!r}")
with db as f:
    print(f"{f!r}")

db.__enter__ = Mock(return_value=None)

with db as f:
    print(f"{f!r}")

from unittest.mock import MagicMock


class BrythonMock:
    style = MagicMock(name="STYLE")

    def __getitem__(self, item):
        self.DIV = self
        return self

    def __call__(self, *args, **kwargs):
        return self

    def __le__(self, other):
        return True

    def __lt__(self, other):
        return True
document = BrythonMock()
html = BrythonMock()
html.DIV = BrythonMock()
html.DIV.__le__ = MagicMock(name="DIVAPP")
html.IMG = MagicMock()
window = MagicMock()

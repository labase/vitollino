from unittest.mock import MagicMock


class BrythonMock:

    def __init__(self, *_, **__):
        self.onclick = lambda: None
        self.text = None
        self.elt = self
        self.style = MagicMock()
        self.head = MagicMock()
        a, b = MagicMock(), MagicMock()
        a.__le__, b.__le__, self.head.__le__ = MagicMock(), MagicMock(), MagicMock()

        self.STYLE = self.H2 = self.H1 = self.A = a

        self.IMG = b

    def __getitem__(self, item):
        return self

    def __call__(self, *args, **kwargs):
        return self

    def set_header(self, *_, **__):
        return self

    def open(self, *_, **__):
        return self

    def bind(self, *_, **__):
        return self

    def send(self, *_, **__):
        return self

    def __le__(self, other):
        return True

    def __lt__(self, other):
        return True


document = BrythonMock()
html = BrythonMock()
html.DIV = BrythonMock
# html.DIV.__le__ = MagicMock(name="DIVAPP")
# html.IMG = MagicMock()
window = MagicMock()
ajax = BrythonMock()

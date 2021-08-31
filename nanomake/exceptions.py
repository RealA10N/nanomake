import typing
from .printer import NanomakePrinter as Printer


class NanomakeError(Exception):

    def __init__(self, *msg: str):
        self.msg = msg

    def print(self,) -> None:
        Printer.error('\n'.join(self.msg))


class NanomakeConfigError(NanomakeError):
    """ Raised when there is an error in the nanomake setup configuration
    file. """

    def __init__(self, filename: str, fieldpath: typing.List[str], msg: str):
        super().__init__(
            f'*configuration error* in {filename!r}:',
            f'Under field {fieldpath!r}: {msg}',
        )


class NanomakeParsingError(NanomakeError):
    """ Raised when the configuration file doesn't follow the TOML syntax
    specification and it can't be parsed correctly. """

    def __init__(self, filename: str, msg: str):
        super().__init__(
            f'*parsing error* in {filename!r}:',
            msg
        )

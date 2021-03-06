# Stubs for fabric.io (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def output_loop(*args, **kwargs): ...

class OutputLooper:
    chan = ...  # type: Any
    stream = ...  # type: Any
    capture = ...  # type: Any
    timeout = ...  # type: Any
    read_func = ...  # type: Any
    prefix = ...  # type: Any
    printing = ...  # type: Any
    linewise = ...  # type: Any
    reprompt = ...  # type: bool
    read_size = ...  # type: int
    write_buffer = ...  # type: Any
    def __init__(self, chan, attr, stream, capture, timeout) -> None: ...
    def loop(self): ...
    def prompt(self): ...
    def try_again(self): ...

def input_loop(chan, using_pty): ...

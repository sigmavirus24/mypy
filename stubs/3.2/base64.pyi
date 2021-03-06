# Stubs for base64

# Based on http://docs.python.org/3.2/library/base64.html

from typing import IO

def b64encode(s: bytes, altchars: bytes = None) -> bytes: ...
def b64decode(s: bytes, altchars: bytes = None,
              validate: bool = False) -> bytes: ...
def standard_b64encode(s: bytes) -> bytes: ...
def standard_b64decode(s: bytes) -> bytes: ...
def urlsafe_b64encode(s: bytes) -> bytes: ...
def urlsafe_b64decode(s: bytes) -> bytes: ...
def b32encode(s: bytes) -> bytes: ...
def b32decode(s: bytes, casefold: bool = False,
              map01: bytes = None) -> bytes: ...
def b16encode(s: bytes) -> bytes: ...
def b16decode(s: bytes, casefold: bool = False) -> bytes: ...

def decode(input: IO[bytes], output: IO[bytes]) -> None: ...
def decodebytes(s: bytes) -> bytes: ...
def decodestring(s: bytes) -> bytes: ...
def encode(input: IO[bytes], output: IO[bytes]) -> None: ...
def encodebytes(s: bytes) -> bytes: ...
def encodestring(s: bytes) -> bytes: ...

from string import digits
from typing import Generator

from Enum import *


# Tokenizer class accepts the code strings
class Tokenizer:
    def __init__(self, code: str) -> None:
        self.code = code
        self.ptr: int = 0

    def next_token(self) -> Token:
        while self.ptr < len(self.code) and self.code[self.ptr] == " ":
            self.ptr += 1

        if self.ptr == len(self.code):
            return Token(TokenType.EOF)

        char = self.code[self.ptr]
        self.ptr += 1
        if char == "+":
            return Token(TokenType.PLUS)
        elif char == "-":
            return Token(TokenType.MINUS)
        elif char in digits:
            return Token(TokenType.INT, int(char))
        else:
            raise RuntimeError(f"Can't tokenize {char!r}.")

    # Making the tokenizer iterable
    def __iter__(self) -> Generator[Token, None, None]:
        while (token := self.next_token()).type != TokenType.EOF:
            yield token  # yield of the next token
        yield token  # yield of the EOF token(End Of Stream)


if __name__ == "__main__":
    code = "1 + 2 + 3 + 4 - 5 - 6 + 7 - 8"
    tokenizer = Tokenizer(code)
    print(code)
    for tok in tokenizer:
        print(f"\t{tok.type}, {tok.value}")

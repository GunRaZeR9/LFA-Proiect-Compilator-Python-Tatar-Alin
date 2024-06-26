from Parser import *
from Tokenizer import *


class BytecodeType(StrEnum):
    BINOP = auto()
    PUSH = auto()


@dataclass
class Bytecode:
    type: BytecodeType
    value: Any = None


class Compiler:
    def __init__(self, tree: BinOp) -> None:
        self.tree = tree

    def compile(self) -> Generator[Bytecode, None, None]:
        left = self.tree.left
        yield Bytecode(BytecodeType.PUSH, left.value)

        right = self.tree.right
        yield Bytecode(BytecodeType.PUSH, right.value)

        yield Bytecode(BytecodeType.BINOP, self.tree.op)


if __name__ == "__main__":

    compiler = Compiler(Parser(list(Tokenizer("3 + 5"))).parse())
    for bc in compiler.compile():
        print(bc)

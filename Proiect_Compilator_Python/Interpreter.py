from Compiler import *
from Stack import *


class Interpreter:
    def __init__(self, bytecode: list[Bytecode]) -> None:
        self.stack = Stack()
        self.bytecode = bytecode
        self.ptr: int = 0

    def interpret(self) -> None:
        for bc in self.bytecode:
            # Interpret this bytecode operator.
            if bc.type == BytecodeType.PUSH:
                self.stack.push(bc.value)
            elif bc.type == BytecodeType.BINOP:
                right = self.stack.pop()
                left = self.stack.pop()
                if bc.value == "+":
                    result = left + right
                elif bc.value == "-":
                    result = left - right
                else:
                    raise RuntimeError(f"Unknown operator {bc.value}.")
                self.stack.push(result)

        print("Done!")
        print(self.stack)

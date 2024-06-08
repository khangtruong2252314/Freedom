from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from itertools import combinations, accumulate
from operator import mul
from Visitor import *
from AST import *
from Utils import *
home = False

if home:
    from main.zcode.utils.Visitor import *
    from main.zcode.utils.AST import *


class Frame:
    def __init__(self, name, returnType):
        # name: String
        # returnType: Type

        self.name = name
        self.returnType = returnType
        self.currentLabel = 0
        self.currOpStackSize = 0
        self.maxOpStackSize = 0
        self.currIndex = 0
        self.maxIndex = 0
        self.startLabel = list()
        self.endLabel = list()
        self.indexLocal = list()
        self.conLabel = list()
        self.brkLabel = list()

    def getCurrIndex(self):
        return self.currIndex

    def setCurrIndex(self, index):
        # index: Int

        self.currIndex = index

    '''
    *   return a new label in the method.
    *   @return an integer representing the label.
    '''

    def getNewLabel(self):
        tmp = self.currentLabel
        self.currentLabel = self.currentLabel + 1
        return tmp

    '''
    *   simulate an instruction that pushes a value onto operand stack.
    '''

    def push(self):
        self.currOpStackSize = self.currOpStackSize + 1
        if self.maxOpStackSize < self.currOpStackSize:
            self.maxOpStackSize = self.currOpStackSize

    '''
    *   simulate an instruction that pops a value out of operand stack.
    '''

    def pop(self):
        self.currOpStackSize = self.currOpStackSize - 1
        if self.currOpStackSize < 0:
            raise IllegalRuntimeException("Pop empty stack")

    def getStackSize(self):
        return self.currOpStackSize

    '''
    *   return the maximum size of the operand stack that the method needs to use.
    *   @return an integer that represent the maximum stack size
    '''

    def getMaxOpStackSize(self):
        return self.maxOpStackSize

    '''
    *   check if the operand stack is empty or not.
    *   @throws IllegalRuntimeException if the operand stack is not empty.
    '''

    def checkOpStack(self):
        if self.currOpStackSize != 0:
            raise IllegalRuntimeException("Stack not empty")

    '''
    *   invoked when parsing into a new scope inside a method.<p>
    *   This method will create 2 new labels that represent the starting and ending points of the scope.<p>
    *   Then, these labels are pushed onto corresponding stacks.<p>
    *   These labels can be retrieved by getStartLabel() and getEndLabel().<p>
    *   In addition, this method also saves the current index of local variable.
    '''

    def enterScope(self, isProc):
        # isProc: Boolean
        start = self.getNewLabel()
        end = self.getNewLabel()
        self.startLabel.append(start)
        self.endLabel.append(end)
        self.indexLocal.append(self.currIndex)
        if isProc:
            self.maxOpStackSize = 0
            self.maxIndex = 0

    '''
    *   invoked when parsing out of a scope in a method.<p>
    *   This method will pop the starting and ending labels of this scope
    *   and restore the current index
    '''

    def exitScope(self):
        if not self.startLabel or not self.endLabel or not self.indexLocal:
            raise IllegalRuntimeException("Error when exit scope")
        self.startLabel.pop()
        self.endLabel.pop()
        self.currIndex = self.indexLocal.pop()

    '''
    *   return the starting label of the current scope.
    *   @return an integer representing the starting label
    '''

    def getStartLabel(self):
        if not self.startLabel:
            raise IllegalRuntimeException("None start label")
        return self.startLabel[-1]

    '''
    *   return the ending label of the current scope.
    *   @return an integer representing the ending label
    '''

    def getEndLabel(self):
        if not self.endLabel:
            raise IllegalRuntimeException("None end label")
        return self.endLabel[-1]

    '''
    *   return a new index for a local variable declared in a scope. 
    *   @return an integer that represents the index of the local variable
    '''

    def getNewIndex(self):
        tmp = self.currIndex
        self.currIndex = self.currIndex + 1
        if self.currIndex > self.maxIndex:
            self.maxIndex = self.currIndex
        return tmp

    '''
    *   return the maximum index used in generating code for the current method
    *   @return an integer representing the maximum index
    '''

    def getMaxIndex(self):
        return self.maxIndex

    '''
    *   invoked when parsing into a loop statement.<p>
    *   This method creates 2 new labels that represent the starting and ending label of the loop.<p>
    *   These labels are pushed onto corresponding stacks and are retrieved by getBeginLoopLabel() and getEndLoopLabel().
    '''

    def enterLoop(self):
        con = self.getNewLabel()
        brk = self.getNewLabel()
        self.conLabel.append(con)
        self.brkLabel.append(brk)

    '''
    *   invoked when parsing out of a loop statement.
    *   This method will take 2 labels representing the starting and ending labels of the current loop out of its stacks.
    '''

    def exitLoop(self):
        if not self.conLabel or not self.brkLabel:
            raise IllegalRuntimeException("Error when exit loop")
        self.conLabel.pop()
        self.brkLabel.pop()

    '''
    *   return the label of the innest enclosing loop to which continue statement would jump
    *   @return an integer representing the continue label
    '''

    def getContinueLabel(self):
        if not self.conLabel:
            raise IllegalRuntimeException("None continue label")
        return self.conLabel[-1]

    '''
    *   return the label of the innest enclosing loop to which break statement would jump
    *   @return an integer representing the break label
    '''

    def getBreakLabel(self):
        if not self.brkLabel:
            raise IllegalRuntimeException("None break label")
        return self.brkLabel[-1]


class PythonException(Exception):
    pass


class FrameErrorProne(Frame):
    def __init__(self):
        super().__init__(None, None)


class Scoper:
    def __init__(self, frame: Frame, visitor):
        self.frame = frame
        self.visitor = visitor

    def __enter__(self):
        self.visitor.scope.append(self.visitor.scope[-1].copy())
        self.frame.enterScope(False)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.visitor.scope.pop()
        self.frame.exitScope()


class Looper:
    def __init__(self, frame: Frame):
        self.frame = frame

    def __enter__(self):
        self.frame.enterLoop()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.frame.exitLoop()


def SystemFunction(x: str, class_name: str):
    abandon_name = [
        'readNumber',
        'writeNumber',
        'readBool',
        'writeBool',
        'readString',
        'writeString'
    ]
    if x in abandon_name:
        return class_name + '.' + x
    else:
        return x


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) + ")"


class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readInt", MType(list(), NumberType()), CName(self.libName)),
                Symbol("writeInt", MType([NumberType()],
                                         VoidType()), CName(self.libName)),
                Symbol("writeIntLn", MType(
                    [NumberType()], VoidType()), CName(self.libName)),
                Symbol("writeFloat", MType(
                    [NumberType()], VoidType()), CName(self.libName))
                ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value


class Variable:
    def __init__(self, index):
        self._type = None
        self._index = index

    @property
    def rt(self):
        return self._type

    @rt.setter
    def rt(self, RT):
        if self._type is None:
            self._type = RT

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, i):
        self._index = i

    def __repr__(self):
        return 'Variable: ' + str(self.rt)


class Function:
    def __init__(self, RT=None, param=None):
        self._type = RT
        self.param = [] if param is None else param

    @property
    def rt(self):
        return self._type

    @rt.setter
    def rt(self, RT):
        if self._type is None:
            self._type = RT

    def __repr__(self):
        return 'Function: ' + ' -> '.join(map(str, self.param)) + ' -> ' + str(self.rt)


class BasicException(Exception):
    def __init__(self):
        super().__init__()


class Function_:
    def __init__(self, name, param=None, body=False, RT=None):
        self.name = name
        self.param = param
        self.body = body
        self._type = RT

    class Functional_exception(BasicException):
        def __init__(self, message):
            super().__init__()
            self.message = message

    def __repr__(self):
        return self.name

    @property
    def return_type(self):
        return self._type

    @return_type.setter
    def return_type(self, RT):
        if self._type is None:
            self._type = RT
        elif RT is None:
            return
        if type(RT) is self._type:
            self._type = RT
            return
        if type(self._type) is RT:
            return
        elif type(RT) is not type(self._type):
            raise Function_.Functional_exception('Function_' + str(self.name))


class Variable_:
    def __init__(self, name):
        self.name = name
        self.type = None
        self.init = None

    class Variable_exception(BasicException):
        def __init__(self, message):
            super().__init__()
            self.message = message

        def __repr__(self):
            return str(self.message)

    @property
    def return_type(self):
        return self.type

    @return_type.setter
    def return_type(self, RT):
        if self.type is None:
            self.type = RT
        elif RT is None:
            return
        elif type(RT) is not type(self.type):
            raise Variable_.Variable_exception(RT)
        elif type(RT) is ArrayType:
            RT: ArrayType
            if type(RT.eleType) is not type(self.type.eleType) or any(map(lambda x: x[0] != x[1],
                                                                          zip(RT.size, self.type.size))) or \
                    len(RT.size) != len(self.type.size):
                raise Variable_.Variable_exception(RT)
        return


class VoidType:
    def __init__(self):
        pass


class Return_base:
    def __init__(self, checker):
        self.checker = checker

    def __enter__(self):
        self.checker.Return_guard = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.checker.Return_guard = False


class Stack_base:
    def __init__(self, checker):
        self.checker = checker

    def __enter__(self):
        self.checker.global_var.append({})

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.checker.global_var.pop()


class Transmitter:
    def __init__(self):
        self.transmit = []

    def __call__(self, value, *args, **kwargs):
        self.transmit.append(value)


class Continue_base:
    def __init__(self, checker):
        self.checker = checker

    def __enter__(self):
        self.checker.Continue_guard += 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.checker.Continue_guard -= 1


class StaticChecker(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast
        builtin = [('readNumber', [], NumberType()),
                   ('writeNumber', [NumberType()], VoidType()),
                   ('readBool', [], BoolType()),
                   ('writeBool', [BoolType()], VoidType()),
                   ('readString', [], StringType()),
                   ('writeString', [StringType()], VoidType())]
        self.global_var: [{str: Variable_}] = [{}]
        self.func_list: {Function_} = {x[0]: Function_(x[0], x[1], True, x[2]) for x in builtin}
        self.Continue_guard = 0
        self.Return_guard = False

    def visitProgram(self, ast, param):
        self.__init__(ast)
        ast: Program
        try:
            for item in ast.decl:
                self.visit(item, param)
            if 'main' not in self.func_list.keys():
                raise NoEntryPoint()
            if self.func_list['main'].param:
                raise NoEntryPoint()
            try:
                self.func_list['main'].return_type = VoidType()
            except Function_.Functional_exception:
                raise NoEntryPoint()
            non_declared = list(filter(lambda x: not self.func_list[x].body, self.func_list.keys()))
            if non_declared:
                raise NoDefinition(non_declared[0])
        except Exception as e:
            raise e

    def visitVarDecl(self, ast, param):
        ast: VarDecl
        if ast.name.name in self.global_var[-1].keys():
            raise Redeclared(Variable(), ast.name.name)
        ret = self.global_var[-1][ast.name.name] = Variable_(name=ast.name.name)
        if ast.varType:
            ret.return_type = self.visit(ast.varType, None)
        if ast.varInit:
            try:
                self.visit(ast.varInit, None)
                try:
                    ret.return_type = self.visit(ast.varInit, ret.return_type)
                    self.visit(ast.varInit, ret.return_type)
                except TypeMismatchInExpression:
                    raise TypeMismatchInStatement(ast)
            except Variable_.Variable_exception:
                raise TypeMismatchInStatement(ast)
            if ret.return_type is None:
                raise TypeCannotBeInferred(ast)
        if type(param) is Transmitter:
            param(ret.return_type)
        return None

    def visitFuncDecl(self, ast, param):
        ast: FuncDecl
        try:
            with Return_base(self):
                if ast.name.name in self.func_list.keys():
                    if self.func_list[ast.name.name].body:
                        raise Redeclared(Function(), ast.name.name)
                    else:
                        new = self.func_list[ast.name.name]
                else:
                    new = Function_(name=ast.name.name)
                    self.func_list[ast.name.name] = new
                with Stack_base(self):
                    transmit = Transmitter()
                    try:
                        list(map(lambda x: self.visit(x, transmit), ast.param))
                    except Redeclared as e:
                        e.kind = Parameter()
                        raise e
                    if new.param is None:
                        new.param = transmit.transmit
                    else:
                        if any(map(lambda x: type(x[0]) is not type(x[1]) and any(y is not None for y in x), zip(
                                new.param, transmit.transmit))) or len(new.param) != len(transmit.transmit):
                            raise Redeclared(Function(), ast.name.name)
                    if ast.body:
                        new.return_type = self.visit(ast.body, new.return_type)
                        new.body = True
                        if new.return_type is None:
                            new.return_type = VoidType()
        except Function_.Functional_exception:
            raise TypeMismatchInStatement(ast)

    def visitBlock(self, ast, param):

        def type_equivalent(pair):
            x, y = pair

            def array_compatible(a, b):
                a: ArrayType
                b: ArrayType
                return all(map(lambda u: u[0] == u[1], zip(a.size, b.size))) and type_equivalent((a.eleType, b.eleType))

            type_dict = {
                x is None or y is None: {True: lambda: True},
                type(x) is not ArrayType: {
                    type(y) is type(x): lambda: True
                },
                type(x) is ArrayType and type(y) is ArrayType: {
                    True: lambda: array_compatible(x, y)
                }
            }
            try:
                return type_dict[True][True]()
            except KeyError:
                return False

        ast: Block
        with Stack_base(self):
            def filtering(u, v):
                t2 = self.visit(v, u)
                return t2 if u is None else u

            all_return_type = list(filter(lambda x: x is not None, accumulate([param] + ast.stmt, filtering)))

            if not all(map(type_equivalent, combinations(all_return_type, 2))):
                raise TypeMismatchInStatement(ast)
            # TODO write something
            all_return_type.append(None)
            return all_return_type[0]

    def visitAssign(self, ast, param):
        ast: Assign
        # TODO refactor everything (maybe done)
        try:
            left = self.visit(ast.lhs, None)
            right = self.visit(ast.rhs, left)
            left = self.visit(ast.lhs, right)
        except Variable_.Variable_exception:
            raise TypeMismatchInStatement(ast)
        if left is None:
            raise TypeCannotBeInferred(ast)
        if type(left) is not type(right) and left is not None:
            raise TypeMismatchInStatement(ast)
        elif type(left) is None:
            pass
        return None

    def visitId(self, ast, param):
        ast: Id
        # TODO type infer ? (maybe done)
        for stack in self.global_var[::-1]:
            if ast.name in stack.keys():
                if stack[ast.name].return_type is None:
                    if param is None:
                        return None
                    else:
                        stack[ast.name].return_type = param
                        return param
                else:
                    stack[ast.name].return_type = param
                    return stack[ast.name].return_type

        raise Undeclared(Identifier(), ast.name)

    def visitBinaryOp(self, ast, param):
        ast: BinaryOp
        type_dict = {
            ast.op in '/%*+-': (NumberType(), NumberType()),
            ast.op in ['=', '!=', '<', '>', '<=', '>=']: (NumberType(), BoolType()),
            ast.op in ['and', 'or']: (BoolType(), BoolType()),
            ast.op == '...': (StringType(), StringType()),
            ast.op == '==': (StringType(), BoolType())
        }
        T, R = type_dict[True]
        try:
            left = self.visit(ast.left, T)
            right = self.visit(ast.right, T)
        except Variable_.Variable_exception:
            raise TypeMismatchInExpression(ast)
        if type(left) is not type(T) or type(right) is not type(T):
            raise TypeMismatchInExpression(ast)
        return R

    def visitUnaryOp(self, ast, param):
        ast: UnaryOp
        type_dict = {
            '-': NumberType(),
            'not': BoolType()
        }
        T = type_dict[ast.op]
        try:
            if type(self.visit(ast.operand, T)) is not type(T):
                raise TypeMismatchInExpression(ast)
        except Variable_.Variable_exception:
            raise TypeMismatchInExpression(ast)
        return T

    def visitNumberType(self, ast, param):
        return NumberType()

    def visitBoolType(self, ast, param):
        return BoolType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitArrayType(self, ast, param):
        # TODO everything
        ast: ArrayType
        return ArrayType(ast.size, self.visit(ast.eleType, None))

    def visitBreak(self, ast, param):
        assert self.Continue_guard >= 0
        if self.Continue_guard == 0:
            raise MustInLoop(ast)

    def visitReturn(self, ast, param):
        if type(param) is ABCMeta:
            param = param()
        ast: Return
        if ast.expr:
            try:
                self.visit(ast.expr, None)
                try:
                    t = self.visit(ast.expr, param)
                except TypeMismatchInExpression:
                    raise TypeMismatchInStatement(ast)
                if (type(t) is not type(param) and t is not None and param is not None and type(t) is not param and
                        type(param) is not t):
                    raise TypeMismatchInStatement(ast)
                elif t is None:
                    raise TypeCannotBeInferred(ast)
                else:
                    return t
            except Variable_.Variable_exception:
                raise TypeMismatchInStatement(ast)
        else:
            if type(param) is not VoidType and param is not None:
                raise TypeMismatchInStatement(ast)
            return VoidType()

    def visitContinue(self, ast, param):
        ast: Continue
        if self.Continue_guard == 0:
            raise MustInLoop(ast)

    def visitFor(self, ast, param):
        ast: For
        try:
            if type(self.visit(ast.name, NumberType())) is not NumberType:
                raise TypeMismatchInStatement(ast)
            if type(self.visit(ast.updExpr, NumberType())) not in [NumberType, type(None)]:
                raise TypeMismatchInStatement(ast)
            if type(self.visit(ast.condExpr, BoolType())) not in [BoolType, type(None)]:
                raise TypeMismatchInStatement(ast)
        except Variable_.Variable_exception:
            raise TypeMismatchInStatement(ast)
        with Continue_base(self):
            return self.visit(ast.body, param)

    def visitIf(self, ast, param):
        ast: If
        try:
            t = self.visit(ast.expr, BoolType())
        except Variable_.Variable_exception:
            raise TypeMismatchInStatement(ast)
        if t is not None and type(t) is not BoolType:
            raise TypeMismatchInStatement(ast)
        stmt_lst = [self.visit(ast.thenStmt, param)]
        if ast.elseStmt:
            stmt_lst += [self.visit(ast.elseStmt, param)]
        for cond, statement in ast.elifStmt:
            self.visit(cond, BoolType())
            stmt_lst.append(self.visit(statement, param))
        all_return_type = list(set(map(type, filter(lambda x: x is not None, stmt_lst))))
        if len(all_return_type) > 1:
            raise TypeMismatchInExpression(ast)
        else:
            all_return_type.append(None)
            return all_return_type[0]

    def visitCallExpr(self, ast, param):
        ast: CallExpr
        stack = self.func_list
        if ast.name.name not in stack:
            raise Undeclared(Function(), ast.name.name)
        else:
            f = stack[ast.name.name]
            f: Function_
            if len(f.param) != len(ast.args):
                raise TypeMismatchInExpression(ast)
            for t, p in zip(f.param, ast.args):
                if type(self.visit(p, t)) is not type(t):
                    raise TypeMismatchInExpression(ast)
            f.return_type = param
        # TODO dropdown f return type (maybe done)
        return f.return_type

    def visitCallStmt(self, ast, param):
        ast: CallStmt
        stack = self.func_list
        if ast.name.name not in stack:
            raise Undeclared(Function(), ast.name.name)
        else:
            f = stack[ast.name.name]
            f: Function_
            try:
                f.return_type = VoidType()
            except Function_.Functional_exception:
                raise TypeMismatchInStatement(ast)
            if len(f.param) != len(ast.args):
                raise TypeMismatchInStatement(ast)
            for t, p in zip(f.param, ast.args):
                try:
                    if type(self.visit(p, t)) is not type(t):
                        raise TypeMismatchInStatement(ast)
                except Variable_.Variable_exception:
                    raise TypeMismatchInStatement(ast)

    def visitBooleanLiteral(self, ast, param):
        return BoolType()

    def visitNumberLiteral(self, ast, param):
        return NumberType()

    def visitStringLiteral(self, ast, param):
        return StringType()

    def visitArrayCell(self, ast, param):
        # TODO sometimes eleType is not good
        ast: ArrayCell
        arr: ArrayType = self.visit(ast.arr, None)
        if type(arr) is not ArrayType and arr is not None:
            raise TypeMismatchInExpression(ast)

        try:
            def illegal():
                raise Variable_.Variable_exception('All idx must be number type')

            access = list(map(lambda u: NumberType() if type(self.visit(u,
                                                                        NumberType())) is NumberType else illegal(),
                              ast.idx))
        except BasicException:
            raise TypeMismatchInExpression(ast)

        if arr is None:
            return None
        rt = arr.eleType
        size = arr.size
        base = accumulate(size[::-1], lambda u, v: u + [v], initial=[])
        arr_constructor = list(map(lambda u: ArrayType(u[::-1], rt) if u else rt, base))[::-1]
        if len(access) < len(arr_constructor):
            return arr_constructor[len(access)] if arr is not None else None
        else:
            raise TypeMismatchInExpression(ast)

    def visitArrayLiteral(self, ast, param):

        def equal_list(args):
            args = list(args)
            return reduce(lambda x, y: x and (y == args[0]), args, True)

        ast: ArrayLiteral

        if param is not None:
            if type(param) is ArrayType:
                para = ArrayType(size=param.size[1:], eleType=param.eleType) if len(param.size) > 1 else param.eleType
            else:
                raise Variable_.Variable_exception('Array literal error')
        else:
            para = param

        def type_equivalent(pair):
            x, y = pair

            def array_compatible(a, b):
                a: ArrayType
                b: ArrayType
                return all(map(lambda u: u[0] == u[1], zip(a.size, b.size))) and type_equivalent((a.eleType, b.eleType))

            type_dict = {
                x is None or y is None: {True: lambda: True},
                type(x) is not ArrayType: {
                    type(y) is type(x): lambda: True
                },
                type(x) is ArrayType and type(y) is ArrayType: {
                    True: lambda: array_compatible(x, y)
                }
            }
            try:
                return type_dict[True][True]()
            except KeyError:
                return False

        def force(u, v):
            try:
                t2 = self.visit(v, u)
            except Variable_.Variable_exception:
                raise TypeMismatchInExpression(ast)
            if t2 is not None and u is not None and type(t2) is not type(u):
                raise TypeMismatchInExpression(ast)
            return t2 if t2 is not None else u

        all_item_type_forced = list(accumulate([para] + ast.value + ast.value, force))
        all_object_type = list(combinations(filter(lambda y: y is not None, all_item_type_forced), 2))
        unique_test = all(map(type_equivalent, all_object_type))
        if not unique_test:
            raise TypeMismatchInExpression(ast)
        ele = list(filter(lambda y: y is not None, (self.visit(x, para) for x in ast.value))) + [None]
        ele = [self.visit(x, ele[0]) for x in ast.value]
        all_object_type = combinations(filter(lambda y: y is not None, ele), 2)
        unique_test = all(map(type_equivalent, all_object_type))
        if not unique_test:
            raise TypeMismatchInExpression(ast)

        all_type = list(set(map(type, ele)))
        if len(all_type) != 1:
            raise TypeMismatchInExpression(ast)
        elif all_type[0] is type(None):
            return None
        elif all_type[0] is ArrayType:
            if type(param) is not ArrayType and param is not None:
                raise Variable_.Variable_exception("Array")
            if param is not None:
                param: ArrayType
                size = param.size[1:]
            else:
                size = ele[0].size
            for value in ast.value:
                self.visit(value, ArrayType(size, ele[0].eleType) if size else ele[0].eleType)
            dim = list(map(lambda x: len(x.size), ele)) + [len(size)]
            sizes = [size] + [x.size for x in ele]
            if not equal_list(dim) or not all(map(equal_list, zip(*sizes))):
                raise TypeMismatchInExpression(ast)
            return ArrayType([len(ele)] + size, ele[0].eleType)
        else:
            return ArrayType([len(ele)], ele[0])

    def export_func(self) -> dict[str, Function]:
        dictionary = {k: self.func_list[k].return_type for k in self.func_list}
        para_dict = {k: self.func_list[k].param for k in self.func_list}
        dictionary = {k: Function(dictionary[k], para_dict[k]) for k in dictionary}
        return dictionary

    def export_static(self) -> dict[str, Type]:
        dictionary = {k: self.global_var[-1][k].return_type for k in self.global_var[-1]}
        return dictionary

    def check(self):
        self.visit(self.ast, None)


class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path
        self.emit = Emitter(path + '/ZCodeClass.j')
        self.scope: list[dict[str, Variable]] = [{}]
        visitor = StaticChecker(astTree)
        visitor.check()
        self.func = visitor.export_func()
        self.static_var = visitor.export_static()
        self.static_init = ''
        self.static_checker = visitor
        self.legendary = LegendaryCodeGenVisitor(astTree, env, path)
        self.static_declare = []
        self.static_func = []
        self.static_declare_init = []

    def visitProgram(self, ast, c):

        try:
            """
            goodness = self.legendary.visit(self.astTree, None)
            self.emit.clearBuff()
            self.emit.printout(goodness)
            """
            raise PythonException()
        except PythonException:
            self.emit.clearBuff()
            frame = FrameErrorProne()
            self.emit.printout(self.emit.emitPROLOG('ZCodeClass', 'java.lang.Object'))
            self.emit.printout('\n')
            [self.visit(i, frame) for i in ast.decl]
            self.genINIT(frame)
            self.emit.printout(''.join(self.static_declare))
            self.emit.printout(''.join(self.static_func))
            pass
        self.emit.emitEPILOG()
        return c

    def genINIT(self, param):
        l1 = param.getNewLabel()
        l2 = param.getNewLabel()
        c = ''.join(self.static_declare_init)
        string = """
.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Labelxxx to Labelyyy
Labelxxx:
    aload_0
    invokespecial java/lang/Object/<init>()V
Labelyyy:
    return
.end method
""".replace('xxx', str(l1)).replace('yyy', str(l2))
        l3 = param.getNewLabel()
        l4 = param.getNewLabel()
        class_init_string = """
.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Labelxxx to Labelyyy
Labelxxx:
zzz
Labelyyy:
    return 
.end method
""".replace('xxx', str(l3)).replace('yyy', str(l4)).replace('zzz', c)
        self.static_func.append(string + class_init_string)

    def visitCallStmt(self, ast, o):
        ast: CallStmt
        o: Frame

        def pile(x, y):
            cx, tx = self.visit(y, o)
            cy, ty = x
            return cy + cx, ty + [tx]

        o.push()
        c, t = reduce(pile, ast.args, ('', []))
        if SystemFunction(ast.name.name, 'io') == ast.name.name:
            real_type = MType(t, self.func[ast.name.name].rt)
            return c + self.emit.emitINVOKESTATIC('ZCodeClass/' + SystemFunction(ast.name.name, 'io'), real_type, o)
        else:
            type_dict = {
                type(t[0]) is NumberType: 'F',
                type(t[0]) is BoolType: 'Z',
                type(t[0]) is StringType: 'Ljava/lang/String;'
            }
            func_name_dict = {
                type(t[0]) is NumberType: 'Number',
                type(t[0]) is BoolType: 'Bool',
                type(t[0]) is StringType: 'String'
            }
            better_string = """\n\tinvokestatic io/writeMyName(ux)V\n""".replace('MyName', func_name_dict[True]).replace('ux', type_dict[True])
            return c + better_string

    def visitNumberLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value), o), NumberType()

    def visitBinaryOp(self, ast, o):
        e1c, e1t = self.visit(ast.left, o)
        e2c, _ = self.visit(ast.right, o)
        # TODO
        dictionary = {
            ast.op in '+-': lambda: self.emit.emitADDOP(ast.op, None, o),
            ast.op in '*/': lambda: self.emit.emitMULOP(ast.op, None, o),
            ast.op == '%': lambda: '\tfrem\n',
            ast.op == 'and': lambda: self.emit.emitANDOP(o),
            ast.op == 'or': lambda: self.emit.emitOROP(o),
            ast.op == '...': lambda: '\tinvokevirtual java/lang/String.concat(Ljava/lang/String;)Ljava/lang/String;',
            ast.op in '<=>=!=': lambda: self.emit.emitFREOP(ast.op, o),
            ast.op == '==': lambda: '\tinvokevirtual java/lang/String.equals(Ljava/lang/Object;)Z'
        }
        if ast.op in 'and or <=>=!==':
            e1t = BoolType()
        return e1c + e2c + dictionary[True](), e1t

    def visitUnaryOp(self, ast, param):
        ast: UnaryOp
        ec, t = self.visit(ast.operand, param)
        dictionary = {
            'not': self.emit.emitNOT(BoolType(), param),
            '-': self.emit.emitNEGOP(NumberType(), param)
        }
        return ec + dictionary[ast.op], t

    def visitCallExpr(self, ast, o):
        ast: CallExpr
        o: Frame

        def pile(x, y):
            cx, tx = self.visit(y, o)
            cy, ty = x
            return cy + cx, ty + [tx]

        c, t = reduce(pile, ast.args, ('', []))
        real_type = MType(t, self.func[ast.name.name].rt)
        name = ast.name.name
        if SystemFunction(name, 'io') == name:
            return (c + self.emit.emitINVOKESTATIC('ZCodeClass/' + SystemFunction(name, 'io'), real_type, o),
                    self.func[ast.name.name].rt)
        else:
            o.push()
            o.push()
            o.push()
            o.pop()
            o.pop()
            betterNumber = '\n\tinvokestatic io/readNumber()F\n'
            betterString = '\n\tinvokestatic io/readString()Ljava/lang/String;\n'
            betterBool = '\n\tinvokestatic io/readBool()Z\n'
            system_dict = {
                name == 'readNumber': (betterNumber, NumberType()),
                name == 'readString': (betterString, StringType()),
                name == 'readBool': (betterBool, BoolType())
            }
            return system_dict[True]

    def visitReturn(self, ast: Return, param):
        if ast.expr:
            c, t = self.visit(ast.expr, param)
            return c + self.emit.emitRETURN(t, frame=param)
        else:
            return self.emit.emitRETURN(VoidType(), frame=param)

    def visitBlock(self, ast, param):
        ast: Block
        param: Frame

        with Scoper(param, self):
            c1 = self.emit.emitLABEL(param.getStartLabel(), param)
            c2 = self.emit.emitLABEL(param.getEndLabel(), param)
            return c1 + reduce(lambda x, y: x + '\n' + self.visit(y, param), ast.stmt, '') + c2

    def visitBreak(self, ast, param):
        ast: Break
        param: Frame
        return self.emit.emitGOTO(param.getBreakLabel(), param)

    def visitIf(self, ast, param):
        ast: If
        param: Frame

        def trust():
            next_option_label = list(map(lambda _: param.getNewLabel(), [y for y, _ in ast.elifStmt] + [ast.elseStmt]))
            evaluate = [self.visit(x, param)[0] for x in [ast.expr] + [y for y, _ in ast.elifStmt]]
            check_label = list(map(lambda x: self.emit.emitIFFALSE(x, param), next_option_label))
            stmt = [self.visit(x, param) for x in [ast.thenStmt] + [y for _, y in ast.elifStmt]]
            labels = [self.emit.emitLABEL(x, param) for x in next_option_label]
            final = param.getNewLabel()
            exit_loop = self.emit.emitGOTO(final, param)
            generator = list(zip(evaluate, check_label, stmt, labels))

            def stacker(expressions, if_false, statements, label):
                return expressions + if_false + statements + exit_loop + label

            true_code = reduce(lambda x, y: x + stacker(*y), generator, '')
            else_code = self.visit(ast.elseStmt, param) if ast.elseStmt else ''
            true_code += else_code + self.emit.emitLABEL(final, param)
            return true_code

        return trust()

    def visitStringLiteral(self, ast, param):
        param: Frame
        ast: StringLiteral
        return self.emit.emitPUSHCONST(ast.value, StringType(), param), StringType()

    def visitBooleanLiteral(self, ast, param):
        param: Frame
        ast: BooleanLiteral
        return self.emit.emitPUSHICONST(str(ast.value).lower(), param), BoolType()

    def visitNumberType(self, ast, param):
        return NumberType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitBoolType(self, ast, param):
        return BoolType()

    def visitVarDecl(self, ast, param):
        def default_Num(_):
            return NumberLiteral(0.0)

        def default_String(_):
            return StringLiteral('')

        def default_Bool(_):
            return BooleanLiteral(True)

        def default_Array(t):
            t: ArrayType
            copies = int(t.size[0])
            remain = t.size[1:]
            if remain:
                return ArrayLiteral([default(ArrayType(remain, t.eleType))] * copies)
            else:
                return ArrayLiteral([default(t.eleType)] * copies)
            pass

        def default(_type):
            default_dict = {
                NumberType: default_Num,
                StringType: default_String,
                BoolType: default_Bool,
                ArrayType: default_Array,
                None: lambda _: None
            }
            return default_dict[type(_type)](_type)

        # TODO static
        ast: VarDecl
        param: Frame
        param.push()
        index = param.getNewIndex() if len(self.scope) > 1 else None
        self.scope[-1][ast.name.name] = variable = Variable(index)
        if len(self.scope) == 1:
            variable.rt = self.static_var[ast.name.name]
        if ast.varType is not None:
            variable.rt = self.visit(ast.varType, param)
        if ast.varInit is not None:
            c, variable.rt = self.visit(ast.varInit, param)
            if type(variable.rt) is not ArrayType:
                if index is not None:
                    c += self.emit.emitWRITEVAR(ast.name, variable.rt, index, param)
                else:
                    self.static_declare.append(self.emit.emitATTRIBUTE(ast.name.name, variable.rt, None, None))
                    init = self.visit(Assign(Id(ast.name.name), ast.varInit), param)
                    self.static_declare_init.append(init)
            else:
                if index is not None:
                    # TODO what to put here???
                    c += self.emit.emitWRITEVAR(None, variable.rt, index, param)
        else:
            c, variable.rt = '', None
            if variable.rt is not None:
                shadow = Assign(Id(ast.name.name), default(variable.rt))
                c += self.visit(shadow, param)
            if index is None:
                self.static_declare.append(self.emit.emitATTRIBUTE(ast.name.name, variable.rt, None, None))
                self.static_declare_init.append(c)
        return c

    def visitId(self, ast, param):
        ast: Id
        param: Frame
        if self.scope[-1][ast.name].index is not None:
            c = self.emit.emitREADVAR(ast.name, self.scope[-1][ast.name].rt, self.scope[-1][ast.name].index, param)
        else:
            c = self.emit.emitGETSTATIC('ZCodeClass.' + ast.name, self.scope[-1][ast.name].rt, param)
        return c, self.scope[-1][ast.name].rt

    def visitArrayType(self, ast, param):
        ast: ArrayType
        return ArrayType(ast.size, ast.eleType)

    def visitAssign(self, ast, param):
        param: Frame
        ast: Assign

        param.push()
        param.push()

        def lhs(_type):
            # TODO ast.name = ?

            def lhs_id(node):
                node: Id
                index = self.scope[-1][node.name].index
                cx = ''
                if index is not None:
                    if self.scope[-1][node.name].rt is None:
                        self.scope[-1][node.name].rt = _type
                        cx += self.emit.emitVAR(index, node.name,
                                                self.scope[-1][node.name].rt,
                                                param.getStartLabel(),
                                                param.getEndLabel(),
                                                param)
                    cx += self.emit.emitWRITEVAR(node.name, self.scope[-1][node.name].rt, index, param)
                else:
                    cx += self.emit.emitPUTSTATIC('ZCodeClass.' + node.name, self.scope[-1][node.name].rt, param)
                return cx

            def lhs_array(node):
                node: ArrayCell
                variable = self.scope[-1][node.arr.name]
                variable.rt = _type
                reversed_dimension = reversed(variable.rt.size)
                base = list(accumulate(reversed_dimension, mul, initial=1))

                def index_generator():
                    all_index = [self.visit(x, param)[0] for x in node.idx]
                    all_integer_index = [x + '\tf2i\n' for x in all_index]
                    all_mul_base = [self.emit.emitPUSHICONST(x, param) for x in base]
                    true_zip = list(zip(all_mul_base, all_integer_index))
                    adjusted_spaced_index = [x + y + '\timul\n' for x, y in true_zip]
                    merge = [''] + ['\tiadd\n'] * (len(adjusted_spaced_index) - 1)
                    calculated_particle = zip(adjusted_spaced_index, merge)
                    calculated_particle_mapped = [x + y for x, y in calculated_particle]
                    c___ = ''.join(calculated_particle_mapped)
                    return c___

                def whole_array_loader():
                    if variable.index is not None:
                        load = self.emit.emitREADVAR(None, variable.rt, variable.index, param)
                    else:
                        load = self.emit.emitGETSTATIC('ZCodeClass.' + ast.lhs.arr.name, variable.rt, param)
                    return load

                def element_injection():
                    type_dict = {
                        True: '',
                        type(variable.rt.eleType) is NumberType: '\tfastore\n',
                        type(variable.rt.eleType) is BoolType: '\tbastore\n',
                        type(variable.rt.eleType) is StringType: '\taastore\n'
                    }
                    return type_dict[True]

                c__ = whole_array_loader() + index_generator(), element_injection()
                return c__

            if type(ast.lhs) is Id:
                return lhs_id(ast.lhs)
            else:
                return lhs_array(ast.lhs)

        def rhs():
            return self.visit(ast.rhs, param)

        if type(ast.lhs) is Id:
            c, t = rhs()
            c += lhs(t)
        else:
            c, t = rhs()
            c_, saver = lhs(t)
            c = c_ + c + saver

        # TODO lhs array
        return c

    def visitFor(self, ast, param):
        ast: For
        param: Frame
        c = ''

        index = self.scope[-1][ast.name.name].index
        if index is not None:
            c += self.emit.emitREADVAR(ast.name.name, NumberType(), index, param)
        else:
            c += self.emit.emitGETSTATIC('ZCodeClass/' + ast.name.name, NumberType(), param)
        param.enterLoop()
        chalk_label = param.getNewLabel()
        c += self.emit.emitLABEL(chalk_label, param)
        cx, _ = self.visit(ast.condExpr, param)
        c += cx
        c += self.emit.emitIFTRUE(param.getBreakLabel(), param)
        c += self.visit(ast.body, param)
        c += self.emit.emitLABEL(param.getContinueLabel(), param)
        cx, _ = self.visit(ast.updExpr, param)
        if index is not None:
            c += self.emit.emitREADVAR(ast.name.name, NumberType(), index, param)
        else:
            c += self.emit.emitGETSTATIC('ZCodeClass/' + ast.name.name, NumberType(), param)
        c += cx + self.emit.emitADDOP('+', NumberType(), param)
        if index is not None:
            c += self.emit.emitWRITEVAR(ast.name.name, NumberType(), index, param)
        else:
            c += self.emit.emitPUTSTATIC('ZCodeClass/' + ast.name.name, NumberType(), param)
        c += self.emit.emitGOTO(chalk_label, param)
        c += self.emit.emitLABEL(param.getBreakLabel(), param)
        if index is not None:
            c += self.emit.emitWRITEVAR(ast.name.name, NumberType(), index, param)
        else:
            c += self.emit.emitPUTSTATIC('ZCodeClass/' + ast.name.name, NumberType(), param)
        param.exitLoop()
        return c

    def visitContinue(self, ast, param):
        param: Frame
        return self.emit.emitGOTO(param.getContinueLabel(), param)

    def visitFuncDecl(self, ast, param):
        ast: FuncDecl
        param: Frame
        param.push()

        if not ast.body:
            return ''
        mtype = MType(self.func[ast.name.name].param if ast.name.name != 'main' else [ArrayType([], StringType())],
                      self.func[ast.name.name].rt)

        def parameter():
            def constructor(tup):
                name, _type = tup
                index = param.getNewIndex()
                self.scope[-1][name] = variable = Variable(index)
                variable.rt = _type
                return self.emit.emitVAR(index, name, variable.rt, param.getStartLabel(), param.getEndLabel(), param)

            return reduce(lambda x, y: x + constructor(y), zip([x.name.name for x in ast.param], f.param), '')

        def statement():
            label_0 = self.emit.emitLABEL(param.getStartLabel(), param)
            label_1 = self.emit.emitLABEL(param.getEndLabel(), param)
            ret = self.emit.emitRETURN(self.func[ast.name.name].rt, param)
            return label_0 + self.visit(ast.body, param) + label_1 + ret

        def end():
            return self.emit.emitENDMETHOD(param)

        with Scoper(param, self):
            if ast.name.name == 'main':
                param.getNewIndex()
            c = self.emit.emitMETHOD(ast.name.name, mtype, True, param)
            f = self.func[ast.name.name]
            c1 = parameter()
            if ast.name.name == 'main':
                c1 += self.static_init
            c3 = statement()
            c4 = end()
            c += c1 + c3 + c4
            self.static_func.append(c)
            return ''

    def visitArrayLiteral(self, ast, param):
        param: Frame
        ast: ArrayLiteral

        def flatten(node):
            node: Expr | ArrayLiteral
            if type(node) is not ArrayLiteral:
                return [node]
            else:
                return reduce(lambda x, y: x + flatten(y), node.value, [])

        def dimension(node):
            node: ArrayLiteral | Expr
            if type(node) is not ArrayLiteral:
                return []
            else:
                return [len(node.value)] + dimension(node.value[0])

        def ele_type(x):
            _, t = self.visit(x, param)
            return t

        def initializer(content, save_line):
            i_ = [self.emit.emitPUSHICONST(x, param) for x in range(len(content))]
            c_ = [self.visit(x, param)[0] for x in content]
            c__ = [self.emit.emitDUP(param) + y + x + save_line for x, y in zip(c_, i_)]
            return ''.join(c__)

        def constructor():
            param.push()
            param.push()
            type_dict = {
                NumberType: 'float',
                BoolType: 'boolean',
                StringType: 'java/lang/String'
            }
            type_saver = {
                NumberType: '\tfastore\n',
                BoolType: '\tbastore\n',
                StringType: '\taastore\n'
            }
            type_arr = {
                NumberType: '\tnewarray ',
                BoolType: '\tnewarray ',
                StringType: '\tanewarray '
            }
            content = flatten(ast)
            true_type = type(ele_type(content[0]))
            array_length = len(content)
            c = self.emit.emitPUSHICONST(array_length, param)
            c += type_arr[true_type] + type_dict[true_type] + '\n'
            c += initializer(content, type_saver[true_type])
            return c, ArrayType(dimension(ast), ele_type(content[0]))

        code, t_ = constructor()
        return code, t_

    def visitArrayCell(self, ast, param):
        ast: ArrayCell
        param: Frame

        def lhs_array(node):
            node: ArrayCell
            variable = self.scope[-1][node.arr.name]
            reversed_dimension = reversed(variable.rt.size)
            base = list(reversed(list(accumulate(reversed_dimension, mul, initial=1))))[1:]

            def index_generator():
                all_index = [self.visit(x, param)[0] for x in node.idx]
                all_integer_index = [x + '\tf2i\n' for x in all_index]
                all_mul_base = [self.emit.emitPUSHICONST(int(x), param) for x in base]
                true_zip = list(zip(all_mul_base, all_integer_index))
                adjusted_spaced_index = [x + y + '\timul\n' for x, y in true_zip]
                merge = [''] + ['\tiadd\n'] * (len(adjusted_spaced_index) - 1)
                calculated_particle = zip(adjusted_spaced_index, merge)
                calculated_particle_mapped = [x + y for x, y in calculated_particle]
                c___ = ''.join(calculated_particle_mapped)
                return c___

            def whole_array_loader():
                if variable.index is not None:
                    load = self.emit.emitREADVAR(None, variable.rt, variable.index, param)
                else:
                    load = self.emit.emitGETSTATIC('ZCodeClass.' + ast.arr.name, variable.rt, param)
                return load

            def element_injection():
                type_dict = {
                    True: '',
                    type(variable.rt.eleType) is NumberType: '\tfaload\n',
                    type(variable.rt.eleType) is BoolType: '\tbaload\n',
                    type(variable.rt.eleType) is StringType: '\taaload\n'
                }
                return type_dict[True]

            c__ = whole_array_loader() + index_generator() + element_injection()
            return c__, variable.rt.eleType

        c, t = lhs_array(ast)
        return c, t


class Value:
    def __init__(self):
        self.value = None

    def set(self, value):
        self.value = value


class PythonScoper:
    def __init__(self, visitor):
        self.visitor = visitor
        self.scope = 1

    def __enter__(self):
        self.scope += 1
        self.visitor.accessible.append([])

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.scope -= 1
        self.visitor.accessible.pop()

    def tabs(self):
        return '\t' * self.scope

    def length(self):
        return self.scope


def inliner(f):
    def g(*args):
        return f(*args) + '\n'

    return g


class Accessibility:
    index = 0


class LegendaryCodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path
        self.emit = Emitter('./test/solutions/500/ZCodeClass.j')
        self.scoper = PythonScoper(self)
        self.accessible = [[]]
        self.local = []

        def sys_out(x):
            return self.scoper.tabs() + 'dynamic.append(' + x + ')\n'

        self.system_function = {
            'writeNumber': sys_out,
            'writeString': sys_out,
            'writeBool': sys_out
        }

    def visitProgram(self, ast, c):
        ast: Program
        program = 'def _Haskell():\n'
        program += reduce(lambda x, y: x + self.visit(y, None), ast.decl, '')

        program += '\n\t_main()\n_Haskell()\n'

        def pretest():
            dynamic = []
            exec(program, {'dynamic': dynamic})
            return dynamic

        result = pretest()

        def compilation(x):
            string = """    getstatic java/lang/System.out Ljava/io/PrintStream;
    ldc xxx
    invokevirtual java/io/PrintStream/print(yyy)V
    getstatic java/lang/System.out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V
"""
            x_dict = {
                float: (str(x), 'F'),
                str: ('\"' + str(x) + '\"', 'Ljava/lang/String;'),
                bool: (str(x), 'Ljava/lang/String;')
            }
            u, v = x_dict[type(x)]
            string = string.replace('xxx', u).replace('yyy', v)
            return string

        body_assembly = reduce(lambda x, y: x + compilation(y), result, '')
        full = self.genINIT() + self.genMAIN(body_assembly)
        return full

    def genINIT(self):
        string = """
.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public <init>()V
.limit stack 1
.limit locals 1
.var 0 is this LZCode; from Label0 to Label1
Label0:
aload_0
invokespecial java/lang/Object/<init>()V
Label1:
    return
.end method

"""
        return string

    def genMAIN(self, body_code):
        string = """.method public static main([Ljava/lang/String;)V
Label2:
Label4:
xxx
Label5:
Label3:
	return
.limit stack 5
.limit locals 2
.end method
"""
        string = string.replace('xxx', body_code)
        return string

    @inliner
    def visitContinue(self, ast, param):
        return self.scoper.tabs() + 'continue'

    @inliner
    def visitIf(self, ast, param):
        ast: If
        expr = self.visit(ast.expr, param)
        if_expr = self.scoper.tabs() + 'if ' + expr + ':\n'
        with self.scoper:
            then_stmt = self.visit(ast.thenStmt, param)
        stmt = if_expr + then_stmt

        def el_if(a):
            x, y = a
            el_condition = self.scoper.tabs() + 'elif ' + self.visit(x, param) + ':\n'
            with self.scoper:
                el_stmt = self.visit(y, param)
            return el_condition + el_stmt

        def else_():
            if not ast.elseStmt:
                return ''
            else_condition = self.scoper.tabs() + 'else:\n'
            with self.scoper:
                else_condition += self.visit(ast.elseStmt, param)
            return else_condition

        return stmt + reduce(lambda x, y: x + el_if(y), ast.elifStmt, '') + else_()

    def visitArrayLiteral(self, ast, param):
        ast: ArrayLiteral
        elem = '[' + ', '.join([self.visit(x, param) for x in ast.value]) + ']'
        return elem

    def visitFuncDecl(self, ast, param):
        ast: FuncDecl
        name = '_' + ast.name.name
        string = self.scoper.tabs() + 'def xxx(yyy):\n'.replace('xxx', name)
        param = ', '.join(['_' + x.name.name for x in ast.param])

        string = string.replace('yyy', param)
        with self.scoper:
            support_param = '\n'.join([
                self.scoper.tabs() + 'Accessibility._' + x.name.name + ' = ' + x.name.name + '\n' for x in ast.param])
            restore_point = [self.scoper.tabs() + 'var_' + x.name.name + ' = ' + 'Accessibility._' +
                             x.name.name for x in ast.param]
            restore_point = '\n'.join(restore_point) + '\n'
            restoring = [self.scoper.tabs() + 'Accessibility._' + x.name.name + ' = var_' +
                         x.name.name for x in ast.param]
            restoring = '\n'.join(restoring) + '\n'
            statement = self.scoper.tabs() + 'if True:\n' + self.scoper.tabs() + '\tpass\n'
            if ast.body:
                statement += self.visit(ast.body, param)
            else:
                statement += ''
            statement += self.scoper.tabs() + 'pass\n'
        return string + statement

    def visitId(self, ast, param):
        ast: Id
        return '_' + ast.name

    def visitBooleanLiteral(self, ast, param):
        ast: BooleanLiteral
        return str(str(ast.value) == 'true')

    def visitNumberLiteral(self, ast, param):
        ast: NumberLiteral
        return str(float(ast.value))

    def visitStringLiteral(self, ast, param):
        ast: StringLiteral
        return '\'' + ast.value + '\''

    def visitUnaryOp(self, ast, param):
        ast: UnaryOp
        return ast.op + self.visit(ast.operand, param)

    def visitBinaryOp(self, ast, param):
        ast: BinaryOp

        def convert():
            if ast.op == '...':
                return '+'
            elif ast.op == '=':
                return '=='
            else:
                return ast.op

        return self.visit(ast.left, param) + ' ' + convert() + ' ' + self.visit(ast.right, param)

    def visitNumberType(self, ast, param):
        return ''

    def visitArrayType(self, ast, param):
        return ''

    @inliner
    def visitVarDecl(self, ast, param):
        ast: VarDecl
        if ast.varInit:
            return self.scoper.tabs() + '_' + ast.name.name + ' = ' + self.visit(ast.varInit, param)
        else:
            return self.scoper.tabs() + '_' + ast.name.name + ' = [0] * 1000'

    def visitCallStmt(self, ast, param):
        ast: CallStmt
        name = ast.name.name
        if name not in self.system_function:
            string = self.scoper.tabs() + '_' + name + '('
            string += ', '.join([self.visit(x, param) for x in ast.args]) + ')\n'
            return string
        else:
            return self.system_function[name](self.visit(ast.args[0], param))

    def visitCallExpr(self, ast, param):
        ast: CallExpr
        name = '_' + ast.name.name
        abandon = ['_readNumber', '_readString', '_readBool']
        if name in abandon:
            raise PythonException()
        string = name + '(' + ', '.join([self.visit(x, param) for x in ast.args]) + ')'
        return string

    @inliner
    def visitAssign(self, ast, param):
        ast: Assign
        s = ''
        s += self.scoper.tabs() + self.visit(ast.lhs, param) + ' = ' + self.visit(ast.rhs, param)
        return s

    def visitBreak(self, ast, param):
        return self.scoper.tabs() + 'break\n'

    def visitBlock(self, ast, param):
        ast: Block
        s = ''
        with self.scoper:
            s += ''.join([self.visit(x, param) for x in ast.stmt]) + '\n' + self.scoper.tabs() + 'pass\n'
        return s

    def visitReturn(self, ast, param):
        ast: Return
        string = self.scoper.tabs() + 'return '
        if ast.expr:
            string += self.visit(ast.expr, param) + '\n'
        return string

    def visitBoolType(self, ast, param):
        return ''

    def visitStringType(self, ast, param):
        return ''

    def visitFor(self, ast, param):
        ast: For
        name = '_' + ast.name.name
        string = self.scoper.tabs() + 'var = ' + name + '\n'
        while_loop = self.scoper.tabs() + 'while not ' + self.visit(ast.condExpr, param) + ':\n'
        with self.scoper:
            statement = self.scoper.tabs() + 'if True:\n'
            statement += self.visit(ast.body, param)
            statement += self.scoper.tabs() + name + ' += ' + self.visit(ast.updExpr, param) + '\n'
        post = self.scoper.tabs() + name + ' = var\n'
        return string + while_loop + statement + post

    def visitArrayCell(self, ast, param):
        ast: ArrayCell
        return self.visit(ast.arr, param) + ''.join(
            ['[int(' + self.visit(x, param) + ')]' for x in ast.idx])

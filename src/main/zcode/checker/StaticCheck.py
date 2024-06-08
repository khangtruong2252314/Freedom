from Visitor import *
from StaticError import *
from itertools import accumulate, combinations
from functools import reduce

home = False

if home:
    from main.zcode.utils.AST import *
    from main.zcode.utils.Utils import Utils
    from main.zcode.utils.Visitor import BaseVisitor
else:
    from AST import *
    from Utils import Utils
    from Visitor import BaseVisitor


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


class StaticChecker(BaseVisitor, Utils):
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
        stmt_lst = []
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

    def check(self):
        self.visit(self.ast, None)

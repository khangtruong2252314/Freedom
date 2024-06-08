from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(self.visitNot_nullable_declaration(ctx.not_nullable_declaration()))

    def visitNot_nullable_declaration(self, ctx: ZCodeParser.Not_nullable_declarationContext):
        if ctx.function_declaration():
            a = ctx.function_declaration()
            A = self.visitFunction_declaration(a)
        elif ctx.var_statement():
            a = ctx.var_statement()
            A = self.visitVar_statement(a)
        else:
            a = ctx.type_statement()
            A = self.visitType_statement(a)
        if ctx.not_nullable_declaration():
            b = ctx.not_nullable_declaration()
            B = self.visitNot_nullable_declaration(b)
            return [A] + B
        else:
            return [A]

    def visitContinue_statement(self, ctx: ZCodeParser.Continue_statementContext):
        return Continue()

    def visitBreak_statement(self, ctx: ZCodeParser.Break_statementContext):
        return Break()

    def visitIndex_expression(self, ctx: ZCodeParser.Index_expressionContext):
        if ctx.index_expression():
            a = self.visitIndex_expression(ctx.index_expression())
            b = self.visitArithmetic(ctx.arithmetic())
            if type(a) is list:
                return a + [b]
            else:
                return [a, b]
        else:
            return [self.visitArithmetic(ctx.arithmetic())]

    def visitAtom(self, ctx: ZCodeParser.AtomContext):
        if ctx.NUMBER_TOKEN():
            return NumberLiteral(float(ctx.NUMBER_TOKEN().getText()))
        elif ctx.STRING_TOKEN():
            return StringLiteral(ctx.STRING_TOKEN().getText())
        elif ctx.element_expression():
            return self.visitElement_expression(ctx.element_expression())
        elif ctx.function_expression():
            return self.visitFunction_expression(ctx.function_expression())

    def visitAtomic(self, ctx: ZCodeParser.AtomicContext):
        if ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.STRING_TOKEN():
            return StringLiteral(ctx.STRING_TOKEN().getText())
        elif ctx.list_arithmetic():
            return self.visitList_arithmetic(ctx.list_arithmetic())
        elif ctx.atom():
            return self.visitAtom(ctx.atom())

    def visitMath(self, ctx: ZCodeParser.MathContext):
        return self.visitArithmetic(ctx.arithmetic())

    def visitString_arithmetic(self, ctx: ZCodeParser.String_arithmeticContext):
        if ctx.compare_arithmetic(1):
            a = ctx.compare_arithmetic(0)
            b = ctx.compare_arithmetic(1)
            o = ctx.ETC_OP()
            A = self.visitCompare_arithmetic(a)
            B = self.visitCompare_arithmetic(b)
            return BinaryOp(o.getText(), A, B)
        else:
            return self.visitCompare_arithmetic(ctx.compare_arithmetic(0))

    def visitCompare_arithmetic(self, ctx: ZCodeParser.Compare_arithmeticContext):
        if ctx.logical_arithmetic(1):
            op = None
            if ctx.GE_OP():
                op = ctx.GE_OP()
            elif ctx.LE_OP():
                op = ctx.LE_OP()
            elif ctx.L_OP():
                op = ctx.L_OP()
            elif ctx.G_OP():
                op = ctx.G_OP()
            elif ctx.SINGLE_EQUAL_OP():
                op = ctx.SINGLE_EQUAL_OP()
            elif ctx.DOUBLE_EQUAL_OP():
                op = ctx.DOUBLE_EQUAL_OP()
            elif ctx.NE_OP():
                op = ctx.NE_OP()
            assert op is not None
            a = ctx.logical_arithmetic(0)
            b = ctx.logical_arithmetic(1)
            A = self.visitLogical_arithmetic(a)
            B = self.visitLogical_arithmetic(b)
            return BinaryOp(op.getText(), A, B)
        else:
            return self.visitLogical_arithmetic(ctx.logical_arithmetic(0))

    def visitLogical_arithmetic(self, ctx: ZCodeParser.Logical_arithmeticContext):
        if ctx.logical_arithmetic(1):
            a = ctx.logical_arithmetic(0)
            b = ctx.logical_arithmetic(1)
            o = None
            if ctx.AND():
                o = ctx.AND()
            elif ctx.OR():
                o = ctx.OR()
            assert o is not None
            A = self.visitLogical_arithmetic(a)
            B = self.visitLogical_arithmetic(b)
            return BinaryOp(o.getText(), A, B)
        else:
            return self.visitAdding_arithmetic(ctx.adding_arithmetic())

    def visitAdding_arithmetic(self, ctx: ZCodeParser.Adding_arithmeticContext):
        if ctx.multiplying_arithmetic():
            return self.visitMultiplying_arithmetic(ctx.multiplying_arithmetic())
        else:
            a = ctx.adding_arithmetic(0)
            b = ctx.adding_arithmetic(1)
            o = None
            if ctx.SUB_OP():
                o = ctx.SUB_OP()
            if ctx.ADD_OP():
                o = ctx.ADD_OP()
            assert o is not None
            A = self.visitAdding_arithmetic(a)
            B = self.visitAdding_arithmetic(b)
            return BinaryOp(o.getText(), A, B)

    def visitMultiplying_arithmetic(self, ctx: ZCodeParser.Multiplying_arithmeticContext):
        if ctx.multiplying_arithmetic():
            a = ctx.multiplying_arithmetic(0)
            b = ctx.multiplying_arithmetic(1)
            o = None
            if ctx.MULT_OP():
                o = ctx.MULT_OP()
            elif ctx.DIV_OP():
                o = ctx.DIV_OP()
            elif ctx.MOD_OP():
                o = ctx.MOD_OP()
            assert o is not None
            A = self.visitMultiplying_arithmetic(a)
            B = self.visitMultiplying_arithmetic(b)
            return BinaryOp(o.getText(), A, B)
        else:
            return self.visitNot_arithmetic(ctx.not_arithmetic())

    def visitNot_arithmetic(self, ctx: ZCodeParser.Not_arithmeticContext):
        if ctx.not_arithmetic():
            o = ctx.NOT()
            a = ctx.not_arithmetic()
            A = self.visitNot_arithmetic(a)
            return UnaryOp(o.getText(), A)
        else:
            return self.visitSign_arithmetic(ctx.sign_arithmetic())

    def visitSign_arithmetic(self, ctx: ZCodeParser.Sign_arithmeticContext):
        if ctx.bracket_arithmetic():
            return self.visitBracket_arithmetic(ctx.bracket_arithmetic())
        else:
            o = ctx.SUB_OP()
            a = ctx.sign_arithmetic()
            A = self.visitSign_arithmetic(a)
            return UnaryOp(o.getText(), A)

    def visitBracket_arithmetic(self, ctx: ZCodeParser.Bracket_arithmeticContext):
        if ctx.atomic():
            return self.visitAtomic(ctx.atomic())
        else:
            return self.visitArithmetic(ctx.arithmetic())

    def visitList_arithmetic(self, ctx: ZCodeParser.List_arithmeticContext):
        if ctx.list_of_arithmetic_argument():
            return ArrayLiteral(self.visitList_of_arithmetic_argument(ctx.list_of_arithmetic_argument()))
        else:
            return ArrayLiteral([])

    def visitElement_expression(self, ctx: ZCodeParser.Element_expressionContext):
        if ctx.IDENTIFIER():
            A = ctx.IDENTIFIER().getText()
            A = Id(A)
        else:
            a = ctx.function_expression()
            A = self.visit(a)
        b = ctx.index_expression()
        B = self.visitIndex_expression(b)
        return ArrayCell(A, B)

    def visitFunction_call(self, ctx: ZCodeParser.Function_callContext):
        A = Id(ctx.IDENTIFIER().getText())
        if ctx.list_of_arithmetic_argument():
            B = self.visitList_of_arithmetic_argument(ctx.list_of_arithmetic_argument())
            return CallStmt(A, B)
        else:
            return CallStmt(A, [])

    def visitFunction_expression(self, ctx: ZCodeParser.Function_expressionContext):
        A = Id(ctx.IDENTIFIER().getText())
        if ctx.list_of_arithmetic_argument():
            B = self.visitList_of_arithmetic_argument(ctx.list_of_arithmetic_argument())
            return CallExpr(A, B)
        else:
            return CallExpr(A, [])

    def visitList_of_arithmetic_argument(self, ctx: ZCodeParser.List_of_arithmetic_argumentContext):
        a = ctx.arithmetic()
        A = self.visitArithmetic(a)
        if ctx.list_of_arithmetic_argument():
            b = ctx.list_of_arithmetic_argument()
            B = self.visitList_of_arithmetic_argument(b)
            return [A] + B
        else:
            return [A]

    def visitFunction_declaration(self, ctx: ZCodeParser.Function_declarationContext):
        a = ctx.IDENTIFIER()
        if ctx.list_of_function_parameter():
            b = ctx.list_of_function_parameter()
            B = self.visitList_of_function_parameter(b)
            if ctx.line():
                c = ctx.line()
                C = self.visitLine(c)
                return FuncDecl(Id(a.getText()), B, C)
            else:
                return FuncDecl(Id(a.getText()), B)
        else:
            if ctx.line():
                c = ctx.line()
                C = self.visitLine(c)
                return FuncDecl(Id(a.getText()), [], C)
            else:
                return FuncDecl(Id(a.getText()), [])

    def visitArray_form_parameter(self, ctx: ZCodeParser.Array_form_parameterContext):
        a = ctx.IDENTIFIER()
        b = ctx.index_array_form_parameter()
        B = self.visitIndex_array_form_parameter(b)
        return a.getText(), B

    def visitIndex_array_form_parameter(self, ctx: ZCodeParser.Index_array_form_parameterContext):
        A = ctx.NUMBER_TOKEN().getText()
        ai = [float(A)]
        if ctx.index_array_form_parameter():
            bi = self.visitIndex_array_form_parameter(ctx.index_array_form_parameter())
            ai = ai + bi
        return ai

    def visitList_of_function_parameter(self, ctx: ZCodeParser.List_of_function_parameterContext):
        t = ctx.TYPE().getText()
        token = None
        if t == 'bool':
            token = BoolType()
        elif t == 'string':
            token = StringType()
        elif t == 'number':
            token = NumberType()
        assert token is not None
        if ctx.IDENTIFIER():
            arg = [VarDecl(Id(ctx.IDENTIFIER().getText()), token)]
        else:
            name, size = self.visitArray_form_parameter(ctx.array_form_parameter())
            arg = [VarDecl(Id(name), ArrayType(size, token))]
        if ctx.list_of_function_parameter():
            left = self.visitList_of_function_parameter(ctx.list_of_function_parameter())
            return arg + left
        else:
            return arg

    def visitReturn_expression(self, ctx: ZCodeParser.Return_expressionContext):
        if ctx.math():
            r = self.visitMath(ctx.math())
            return Return(r)
        else:
            return Return()

    def visitBlock_statement(self, ctx: ZCodeParser.Block_statementContext):
        if ctx.list_of_lines():
            return Block(self.visitList_of_lines(ctx.list_of_lines()))
        else:
            return Block([])

    def visitList_of_lines(self, ctx: ZCodeParser.List_of_linesContext):
        a = ctx.line()
        A = self.visitLine(a)
        if ctx.list_of_lines():
            b = ctx.list_of_lines()
            B = self.visitList_of_lines(b)
            return [A] + B
        else:
            return [A]

    def visitLine(self, ctx: ZCodeParser.LineContext):
        if ctx.return_expression():
            return self.visitReturn_expression(ctx.return_expression())
        elif ctx.assign_statement():
            return self.visitAssign_statement(ctx.assign_statement())
        elif ctx.break_statement():
            return self.visitBreak_statement(ctx.break_statement())
        elif ctx.continue_statement():
            return self.visitContinue_statement(ctx.continue_statement())
        elif ctx.type_statement():
            return self.visitType_statement(ctx.type_statement())
        elif ctx.var_statement():
            return self.visitVar_statement(ctx.var_statement())
        elif ctx.function_call():
            return self.visitFunction_call(ctx.function_call())
        elif ctx.block_statement():
            return self.visitBlock_statement(ctx.block_statement())
        elif ctx.for_statement():
            return self.visitFor_statement(ctx.for_statement())
        elif ctx.if_statement():
            return self.visitIf_statement(ctx.if_statement())

    def visitAssign_statement(self, ctx: ZCodeParser.Assign_statementContext):
        if ctx.IDENTIFIER():
            destination = Id(ctx.IDENTIFIER().getText())
        else:
            destination = self.visitElement_expression(ctx.element_expression())
        b = ctx.math()
        B = self.visitMath(b)
        return Assign(destination, B)

    def visitType_statement(self, ctx: ZCodeParser.Type_statementContext):
        token = None
        if ctx.TYPE():
            if ctx.TYPE().getText() == 'number':
                token = NumberType()
            elif ctx.TYPE().getText() == 'bool':
                token = BoolType()
            elif ctx.TYPE().getText() == 'string':
                token = StringType()

        if ctx.array_form_parameter():
            a = ctx.array_form_parameter()
            name, size = self.visitArray_form_parameter(a)
            token = ArrayType(size, token)
            A = Id(name)
        else:
            a = ctx.IDENTIFIER()
            A = Id(a.getText())
        if ctx.ASSIGN_OP():
            b = ctx.math()
            B = self.visitMath(b)
        else:
            B = None
        mod = None if ctx.TYPE() else 'dynamic'
        return VarDecl(A, token, varInit=B, modifier=mod)

    def visitVar_statement(self, ctx: ZCodeParser.Var_statementContext):
        if ctx.array_form_parameter():
            a = ctx.array_form_parameter()
            name, size = self.visitArray_form_parameter(a)
            A = Id(name)
        else:
            a = ctx.IDENTIFIER()
            A = Id(a.getText())
        b = ctx.math()
        B = self.visitMath(b)
        return VarDecl(A, modifier='var', varInit=B)

    def visitIf_statement(self, ctx: ZCodeParser.If_statementContext):
        e = ctx.arithmetic()
        E = self.visitArithmetic(e)
        a = ctx.line(0)
        A = self.visitLine(a)
        B = []
        if ctx.elif_list():
            b = ctx.elif_list()
            B = self.visitElif_list(b)
        if ctx.ELSE():
            c = ctx.line(1)
            C = self.visitLine(c)
            return If(E, A, B, C)
        else:
            return If(E, A, B)

    def visitElif_list(self, ctx: ZCodeParser.Elif_listContext):
        a = ctx.arithmetic()
        A = self.visitArithmetic(a)
        b = ctx.line()
        B = self.visitLine(b)
        R = [(A, B)]
        if ctx.elif_list():
            c = ctx.elif_list()
            C = self.visitElif_list(c)
            return R + C
        else:
            return R

    def visitFor_statement(self, ctx: ZCodeParser.For_statementContext):
        if ctx.IDENTIFIER():
            a = ctx.IDENTIFIER()
            A = Id(a.getText())
        else:
            a = ctx.element_expression()
            A = self.visit(a)
        b = ctx.arithmetic(0)
        B = self.visitArithmetic(b)
        c = ctx.arithmetic(1)
        C = self.visitArithmetic(c)
        d = ctx.line()
        D = self.visitLine(d)
        return For(A, B, C, D)

    def visitArithmetic(self, ctx: ZCodeParser.ArithmeticContext):
        return self.visitString_arithmetic(ctx.string_arithmetic())

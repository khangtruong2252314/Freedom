# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#not_nullable_declaration.
    def visitNot_nullable_declaration(self, ctx:ZCodeParser.Not_nullable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#math.
    def visitMath(self, ctx:ZCodeParser.MathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arithmetic.
    def visitArithmetic(self, ctx:ZCodeParser.ArithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#atomic.
    def visitAtomic(self, ctx:ZCodeParser.AtomicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#string_arithmetic.
    def visitString_arithmetic(self, ctx:ZCodeParser.String_arithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#compare_arithmetic.
    def visitCompare_arithmetic(self, ctx:ZCodeParser.Compare_arithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logical_arithmetic.
    def visitLogical_arithmetic(self, ctx:ZCodeParser.Logical_arithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#adding_arithmetic.
    def visitAdding_arithmetic(self, ctx:ZCodeParser.Adding_arithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#multiplying_arithmetic.
    def visitMultiplying_arithmetic(self, ctx:ZCodeParser.Multiplying_arithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#not_arithmetic.
    def visitNot_arithmetic(self, ctx:ZCodeParser.Not_arithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sign_arithmetic.
    def visitSign_arithmetic(self, ctx:ZCodeParser.Sign_arithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#bracket_arithmetic.
    def visitBracket_arithmetic(self, ctx:ZCodeParser.Bracket_arithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_arithmetic.
    def visitList_arithmetic(self, ctx:ZCodeParser.List_arithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#element_expression.
    def visitElement_expression(self, ctx:ZCodeParser.Element_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_call.
    def visitFunction_call(self, ctx:ZCodeParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_expression.
    def visitFunction_expression(self, ctx:ZCodeParser.Function_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_of_arithmetic_argument.
    def visitList_of_arithmetic_argument(self, ctx:ZCodeParser.List_of_arithmetic_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_expression.
    def visitIndex_expression(self, ctx:ZCodeParser.Index_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_declaration.
    def visitFunction_declaration(self, ctx:ZCodeParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_form_parameter.
    def visitArray_form_parameter(self, ctx:ZCodeParser.Array_form_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_array_form_parameter.
    def visitIndex_array_form_parameter(self, ctx:ZCodeParser.Index_array_form_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_of_function_parameter.
    def visitList_of_function_parameter(self, ctx:ZCodeParser.List_of_function_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_expression.
    def visitReturn_expression(self, ctx:ZCodeParser.Return_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_statement.
    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_of_lines.
    def visitList_of_lines(self, ctx:ZCodeParser.List_of_linesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#line.
    def visitLine(self, ctx:ZCodeParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#atom.
    def visitAtom(self, ctx:ZCodeParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assign_statement.
    def visitAssign_statement(self, ctx:ZCodeParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#type_statement.
    def visitType_statement(self, ctx:ZCodeParser.Type_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_statement.
    def visitVar_statement(self, ctx:ZCodeParser.Var_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_statement.
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_list.
    def visitElif_list(self, ctx:ZCodeParser.Elif_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_statement.
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_statement.
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_statement.
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return self.visitChildren(ctx)



del ZCodeParser
// 2252314

grammar ZCode;

@lexer::header {
# 2252314
from lexererr import *
}

options {
	language=Python3;
}

WS : [ \t\r\b\f]+ -> skip ; // skip spaces, tabs, newlines

program: not_nullable_declaration NEWLINE * EOF;

not_nullable_declaration
            :   NEWLINE * function_declaration not_nullable_declaration?
            |   NEWLINE * type_statement NEWLINE not_nullable_declaration?
            |   NEWLINE * var_statement NEWLINE not_nullable_declaration?
            ;

math        :   arithmetic;

arithmetic  :
            string_arithmetic
            ;

atomic:
                TRUE | FALSE
            |   IDENTIFIER
            |   STRING_TOKEN
            |   list_arithmetic
            |   atom
            ;



string_arithmetic
            :   compare_arithmetic ETC_OP compare_arithmetic
            |   compare_arithmetic
            ;

compare_arithmetic
            :   logical_arithmetic (GE_OP | LE_OP) logical_arithmetic
            |   logical_arithmetic (L_OP | G_OP | NE_OP | SINGLE_EQUAL_OP) logical_arithmetic
            |   logical_arithmetic DOUBLE_EQUAL_OP logical_arithmetic
            |   logical_arithmetic
            ;

logical_arithmetic
            :   logical_arithmetic (AND | OR) logical_arithmetic
            |   adding_arithmetic
            ;

adding_arithmetic
            :   adding_arithmetic (ADD_OP | SUB_OP) adding_arithmetic
            |   multiplying_arithmetic
            ;

multiplying_arithmetic
            :   multiplying_arithmetic (MULT_OP | DIV_OP | MOD_OP) multiplying_arithmetic
            |   not_arithmetic
            ;

not_arithmetic:
                NOT not_arithmetic
            |   sign_arithmetic
            ;

sign_arithmetic:
                SUB_OP sign_arithmetic
            |   bracket_arithmetic
            ;

bracket_arithmetic  :
                LEFT_BRACKET arithmetic RIGHT_BRACKET
            |   atomic
            ;

list_arithmetic     :
                    LEFT_SQUARE_BRACKET list_of_arithmetic_argument? RIGHT_SQUARE_BRACKET
                    ;

element_expression  :   (IDENTIFIER | function_expression) LEFT_SQUARE_BRACKET index_expression RIGHT_SQUARE_BRACKET
                    ;

function_call       :   IDENTIFIER LEFT_BRACKET list_of_arithmetic_argument? RIGHT_BRACKET
                    ;

function_expression :   IDENTIFIER LEFT_BRACKET list_of_arithmetic_argument? RIGHT_BRACKET
                    ;

list_of_arithmetic_argument
                    :   arithmetic (COMMA list_of_arithmetic_argument)?
                    ;

index_expression    :   arithmetic
                    |   index_expression COMMA arithmetic
                    ;

function_declaration    :   FUNC IDENTIFIER LEFT_BRACKET (list_of_function_parameter)?
                            RIGHT_BRACKET (NEWLINE* line | NEWLINE)
                        ;

array_form_parameter    :   IDENTIFIER LEFT_SQUARE_BRACKET index_array_form_parameter RIGHT_SQUARE_BRACKET
                        ;

index_array_form_parameter  :   NUMBER_TOKEN (COMMA index_array_form_parameter)?
                            ;

list_of_function_parameter
                        :       TYPE (IDENTIFIER | array_form_parameter) (COMMA list_of_function_parameter)?
                        ;

TYPE :  NUMBER | BOOL | STRING;

return_expression       :   RETURN math?;


COMMENT :   WS* COMMENT_SIGN (~('\n'))* -> skip;

block_statement :   BEGIN NEWLINE+ list_of_lines? END
                ;

list_of_lines   :   line NEWLINE* list_of_lines
                |   line NEWLINE*
                ;

line:
(       return_expression
    |   assign_statement
    |   break_statement
    |   continue_statement
    |   type_statement
    |   var_statement
    |   function_call
    |   block_statement
)   NEWLINE
|
(
        if_statement
    |   for_statement
)   NEWLINE *
    ;

atom:   NUMBER_TOKEN
    |   STRING_TOKEN
    |   element_expression
    |   function_expression
    ;

assign_statement:   (element_expression | IDENTIFIER) ASSIGN_OP math
                ;
type_statement  :   (TYPE | DYNAMIC) (array_form_parameter | IDENTIFIER) (ASSIGN_OP math)?
                ;
var_statement   :   VAR (array_form_parameter | IDENTIFIER) ASSIGN_OP math
                ;
if_statement    :   IF arithmetic NEWLINE * line
                    elif_list?
                    (ELSE NEWLINE * line)?;
elif_list       :   ELIF arithmetic NEWLINE * line elif_list?
                ;

for_statement   :   FOR (IDENTIFIER | element_expression) UNTIL arithmetic BY arithmetic NEWLINE * line;

break_statement :   BREAK;

continue_statement:     CONTINUE;

NUMBER_TOKEN:   [0-9]+('.'[0-9]*)?([Ee][+-]?[0-9]+)?;
STRING_TOKEN:   DOUBLE_HOOK (STRING_ELEMENT)* DOUBLE_HOOK {self.text = self.text[1:-1]}
            ;

fragment ESCAPE:         [\\][bfrnt'\\];
TRUE:   'true';
FALSE:  'false';
NUMBER: 'number';
BOOL:   'bool';
STRING: 'string';
RETURN: 'return';
VAR:    'var';
DYNAMIC:'dynamic';
FUNC:   'func';
FOR:    'for';
UNTIL:  'until';
BY:     'by';
BREAK:  'break';
CONTINUE:
        'continue';
IF:     'if';
ELSE:   'else';
ELIF:   'elif';
BEGIN:  'begin';
END:    'end';
NOT:    'not';
AND:    'and';
OR:     'or';
fragment COMMENT_SIGN:   '##';



ADD_OP  :   '+';
SUB_OP  :   '-';
MULT_OP :   '*';
DIV_OP  :   '/';
MOD_OP  :   '%';
NE_OP   :   '!=';
GE_OP   :   '>=';
LE_OP   :   '<=';
SINGLE_EQUAL_OP
        :   '=';
L_OP    :   '<';
G_OP    :   '>';
DOUBLE_EQUAL_OP
        :   '==';
ETC_OP  :   '...';
ASSIGN_OP
        :   '<-';

OPERATOR:
            ADD_OP
        |   SUB_OP
        |   MULT_OP
        |   DIV_OP
        |   MOD_OP
        |   NE_OP
        |   GE_OP
        |   LE_OP
        |   SINGLE_EQUAL_OP
        |   L_OP
        |   G_OP
        |   NOT
        |   AND
        |   OR
        |   DOUBLE_EQUAL_OP
        |   ETC_OP
        ;

IDENTIFIER: [A-Za-z_][A-Za-z0-9_]*;


NEWLINE : [\n];
LEFT_SQUARE_BRACKET:    '[';
RIGHT_SQUARE_BRACKET:   ']';
LEFT_BRACKET:           '(';
RIGHT_BRACKET:          ')';
COMMA:                  ',';
fragment SINGLE_HOOK :   ['];
fragment DOUBLE_HOOK :   ["];
END_COMMAND :   EOF;
SEPARATOR   :   LEFT_BRACKET
            |   RIGHT_BRACKET
            |   LEFT_SQUARE_BRACKET
            |   RIGHT_SQUARE_BRACKET
            ;
fragment STRING_ELEMENT
                :   [']["]
                |   [']
                |   ESCAPE
                |   ~('\\' | '"' | '\n' | '\r' | '\b' | '\f' | '\'')
                ;

ILLEGAL_ESCAPE: DOUBLE_HOOK STRING_ELEMENT* [\\]~[bfrnt'\\] {self.text = self.text[1:]; raise IllegalEscape(self.text)};
UNCLOSE_STRING: DOUBLE_HOOK STRING_ELEMENT* {self.text = self.text[1:]; raise UncloseString(self.text.replace('\n', ''))};
ERROR_CHAR: . {raise ErrorToken(self.text)};
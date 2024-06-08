# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38")
        buf.write("\u01a8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\3\2\3")
        buf.write("\2\7\2M\n\2\f\2\16\2P\13\2\3\2\3\2\3\3\7\3U\n\3\f\3\16")
        buf.write("\3X\13\3\3\3\3\3\5\3\\\n\3\3\3\7\3_\n\3\f\3\16\3b\13\3")
        buf.write("\3\3\3\3\3\3\5\3g\n\3\3\3\7\3j\n\3\f\3\16\3m\13\3\3\3")
        buf.write("\3\3\3\3\5\3r\n\3\5\3t\n\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6\u0080\n\6\3\7\3\7\3\7\3\7\3\7\5\7\u0087")
        buf.write("\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\5\b\u0096\n\b\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u009e\n\t")
        buf.write("\f\t\16\t\u00a1\13\t\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u00a9")
        buf.write("\n\n\f\n\16\n\u00ac\13\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\7\13\u00b4\n\13\f\13\16\13\u00b7\13\13\3\f\3\f\3\f\5")
        buf.write("\f\u00bc\n\f\3\r\3\r\3\r\5\r\u00c1\n\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00c8\n\16\3\17\3\17\5\17\u00cc\n\17\3")
        buf.write("\17\3\17\3\20\3\20\5\20\u00d2\n\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\5\21\u00db\n\21\3\21\3\21\3\22\3\22\3")
        buf.write("\22\5\22\u00e2\n\22\3\22\3\22\3\23\3\23\3\23\5\23\u00e9")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00f1\n\24\f")
        buf.write("\24\16\24\u00f4\13\24\3\25\3\25\3\25\3\25\5\25\u00fa\n")
        buf.write("\25\3\25\3\25\7\25\u00fe\n\25\f\25\16\25\u0101\13\25\3")
        buf.write("\25\3\25\5\25\u0105\n\25\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\5\27\u010f\n\27\3\30\3\30\3\30\5\30\u0114\n")
        buf.write("\30\3\30\3\30\5\30\u0118\n\30\3\31\3\31\5\31\u011c\n\31")
        buf.write("\3\32\3\32\6\32\u0120\n\32\r\32\16\32\u0121\3\32\5\32")
        buf.write("\u0125\n\32\3\32\3\32\3\33\3\33\7\33\u012b\n\33\f\33\16")
        buf.write("\33\u012e\13\33\3\33\3\33\3\33\3\33\7\33\u0134\n\33\f")
        buf.write("\33\16\33\u0137\13\33\5\33\u0139\n\33\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\5\34\u0143\n\34\3\34\3\34\3\34")
        buf.write("\3\34\5\34\u0149\n\34\3\34\7\34\u014c\n\34\f\34\16\34")
        buf.write("\u014f\13\34\5\34\u0151\n\34\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u0157\n\35\3\36\3\36\5\36\u015b\n\36\3\36\3\36\3\36\3")
        buf.write("\37\3\37\3\37\5\37\u0163\n\37\3\37\3\37\5\37\u0167\n\37")
        buf.write("\3 \3 \3 \5 \u016c\n \3 \3 \3 \3!\3!\3!\7!\u0174\n!\f")
        buf.write("!\16!\u0177\13!\3!\3!\5!\u017b\n!\3!\3!\7!\u017f\n!\f")
        buf.write("!\16!\u0182\13!\3!\5!\u0185\n!\3\"\3\"\3\"\7\"\u018a\n")
        buf.write("\"\f\"\16\"\u018d\13\"\3\"\3\"\5\"\u0191\n\"\3#\3#\3#")
        buf.write("\5#\u0196\n#\3#\3#\3#\3#\3#\7#\u019d\n#\f#\16#\u01a0\13")
        buf.write("#\3#\3#\3$\3$\3%\3%\3%\2\6\20\22\24&&\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFH\2")
        buf.write("\b\3\2$%\4\2##&(\3\2\34\35\3\2\36\37\3\2 \"\4\2\4\4\17")
        buf.write("\17\2\u01c6\2J\3\2\2\2\4s\3\2\2\2\6u\3\2\2\2\bw\3\2\2")
        buf.write("\2\n\177\3\2\2\2\f\u0086\3\2\2\2\16\u0095\3\2\2\2\20\u0097")
        buf.write("\3\2\2\2\22\u00a2\3\2\2\2\24\u00ad\3\2\2\2\26\u00bb\3")
        buf.write("\2\2\2\30\u00c0\3\2\2\2\32\u00c7\3\2\2\2\34\u00c9\3\2")
        buf.write("\2\2\36\u00d1\3\2\2\2 \u00d7\3\2\2\2\"\u00de\3\2\2\2$")
        buf.write("\u00e5\3\2\2\2&\u00ea\3\2\2\2(\u00f5\3\2\2\2*\u0106\3")
        buf.write("\2\2\2,\u010b\3\2\2\2.\u0110\3\2\2\2\60\u0119\3\2\2\2")
        buf.write("\62\u011d\3\2\2\2\64\u0138\3\2\2\2\66\u0150\3\2\2\28\u0156")
        buf.write("\3\2\2\2:\u015a\3\2\2\2<\u015f\3\2\2\2>\u0168\3\2\2\2")
        buf.write("@\u0170\3\2\2\2B\u0186\3\2\2\2D\u0192\3\2\2\2F\u01a3\3")
        buf.write("\2\2\2H\u01a5\3\2\2\2JN\5\4\3\2KM\7.\2\2LK\3\2\2\2MP\3")
        buf.write("\2\2\2NL\3\2\2\2NO\3\2\2\2OQ\3\2\2\2PN\3\2\2\2QR\7\2\2")
        buf.write("\3R\3\3\2\2\2SU\7.\2\2TS\3\2\2\2UX\3\2\2\2VT\3\2\2\2V")
        buf.write("W\3\2\2\2WY\3\2\2\2XV\3\2\2\2Y[\5(\25\2Z\\\5\4\3\2[Z\3")
        buf.write("\2\2\2[\\\3\2\2\2\\t\3\2\2\2]_\7.\2\2^]\3\2\2\2_b\3\2")
        buf.write("\2\2`^\3\2\2\2`a\3\2\2\2ac\3\2\2\2b`\3\2\2\2cd\5<\37\2")
        buf.write("df\7.\2\2eg\5\4\3\2fe\3\2\2\2fg\3\2\2\2gt\3\2\2\2hj\7")
        buf.write(".\2\2ih\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2\2ln\3\2\2")
        buf.write("\2mk\3\2\2\2no\5> \2oq\7.\2\2pr\5\4\3\2qp\3\2\2\2qr\3")
        buf.write("\2\2\2rt\3\2\2\2sV\3\2\2\2s`\3\2\2\2sk\3\2\2\2t\5\3\2")
        buf.write("\2\2uv\5\b\5\2v\7\3\2\2\2wx\5\f\7\2x\t\3\2\2\2y\u0080")
        buf.write("\7\b\2\2z\u0080\7\t\2\2{\u0080\7-\2\2|\u0080\7\7\2\2}")
        buf.write("\u0080\5\34\17\2~\u0080\58\35\2\177y\3\2\2\2\177z\3\2")
        buf.write("\2\2\177{\3\2\2\2\177|\3\2\2\2\177}\3\2\2\2\177~\3\2\2")
        buf.write("\2\u0080\13\3\2\2\2\u0081\u0082\5\16\b\2\u0082\u0083\7")
        buf.write("*\2\2\u0083\u0084\5\16\b\2\u0084\u0087\3\2\2\2\u0085\u0087")
        buf.write("\5\16\b\2\u0086\u0081\3\2\2\2\u0086\u0085\3\2\2\2\u0087")
        buf.write("\r\3\2\2\2\u0088\u0089\5\20\t\2\u0089\u008a\t\2\2\2\u008a")
        buf.write("\u008b\5\20\t\2\u008b\u0096\3\2\2\2\u008c\u008d\5\20\t")
        buf.write("\2\u008d\u008e\t\3\2\2\u008e\u008f\5\20\t\2\u008f\u0096")
        buf.write("\3\2\2\2\u0090\u0091\5\20\t\2\u0091\u0092\7)\2\2\u0092")
        buf.write("\u0093\5\20\t\2\u0093\u0096\3\2\2\2\u0094\u0096\5\20\t")
        buf.write("\2\u0095\u0088\3\2\2\2\u0095\u008c\3\2\2\2\u0095\u0090")
        buf.write("\3\2\2\2\u0095\u0094\3\2\2\2\u0096\17\3\2\2\2\u0097\u0098")
        buf.write("\b\t\1\2\u0098\u0099\5\22\n\2\u0099\u009f\3\2\2\2\u009a")
        buf.write("\u009b\f\4\2\2\u009b\u009c\t\4\2\2\u009c\u009e\5\20\t")
        buf.write("\5\u009d\u009a\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\21\3\2\2\2\u00a1\u009f")
        buf.write("\3\2\2\2\u00a2\u00a3\b\n\1\2\u00a3\u00a4\5\24\13\2\u00a4")
        buf.write("\u00aa\3\2\2\2\u00a5\u00a6\f\4\2\2\u00a6\u00a7\t\5\2\2")
        buf.write("\u00a7\u00a9\5\22\n\5\u00a8\u00a5\3\2\2\2\u00a9\u00ac")
        buf.write("\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab")
        buf.write("\23\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00ae\b\13\1\2\u00ae")
        buf.write("\u00af\5\26\f\2\u00af\u00b5\3\2\2\2\u00b0\u00b1\f\4\2")
        buf.write("\2\u00b1\u00b2\t\6\2\2\u00b2\u00b4\5\24\13\5\u00b3\u00b0")
        buf.write("\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5")
        buf.write("\u00b6\3\2\2\2\u00b6\25\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8")
        buf.write("\u00b9\7\33\2\2\u00b9\u00bc\5\26\f\2\u00ba\u00bc\5\30")
        buf.write("\r\2\u00bb\u00b8\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\27")
        buf.write("\3\2\2\2\u00bd\u00be\7\37\2\2\u00be\u00c1\5\30\r\2\u00bf")
        buf.write("\u00c1\5\32\16\2\u00c0\u00bd\3\2\2\2\u00c0\u00bf\3\2\2")
        buf.write("\2\u00c1\31\3\2\2\2\u00c2\u00c3\7\61\2\2\u00c3\u00c4\5")
        buf.write("\b\5\2\u00c4\u00c5\7\62\2\2\u00c5\u00c8\3\2\2\2\u00c6")
        buf.write("\u00c8\5\n\6\2\u00c7\u00c2\3\2\2\2\u00c7\u00c6\3\2\2\2")
        buf.write("\u00c8\33\3\2\2\2\u00c9\u00cb\7/\2\2\u00ca\u00cc\5$\23")
        buf.write("\2\u00cb\u00ca\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd")
        buf.write("\3\2\2\2\u00cd\u00ce\7\60\2\2\u00ce\35\3\2\2\2\u00cf\u00d2")
        buf.write("\7-\2\2\u00d0\u00d2\5\"\22\2\u00d1\u00cf\3\2\2\2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\7/\2\2")
        buf.write("\u00d4\u00d5\5&\24\2\u00d5\u00d6\7\60\2\2\u00d6\37\3\2")
        buf.write("\2\2\u00d7\u00d8\7-\2\2\u00d8\u00da\7\61\2\2\u00d9\u00db")
        buf.write("\5$\23\2\u00da\u00d9\3\2\2\2\u00da\u00db\3\2\2\2\u00db")
        buf.write("\u00dc\3\2\2\2\u00dc\u00dd\7\62\2\2\u00dd!\3\2\2\2\u00de")
        buf.write("\u00df\7-\2\2\u00df\u00e1\7\61\2\2\u00e0\u00e2\5$\23\2")
        buf.write("\u00e1\u00e0\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3\3")
        buf.write("\2\2\2\u00e3\u00e4\7\62\2\2\u00e4#\3\2\2\2\u00e5\u00e8")
        buf.write("\5\b\5\2\u00e6\u00e7\7\63\2\2\u00e7\u00e9\5$\23\2\u00e8")
        buf.write("\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9%\3\2\2\2\u00ea")
        buf.write("\u00eb\b\24\1\2\u00eb\u00ec\5\b\5\2\u00ec\u00f2\3\2\2")
        buf.write("\2\u00ed\u00ee\f\3\2\2\u00ee\u00ef\7\63\2\2\u00ef\u00f1")
        buf.write("\5\b\5\2\u00f0\u00ed\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2")
        buf.write("\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\'\3\2\2\2\u00f4")
        buf.write("\u00f2\3\2\2\2\u00f5\u00f6\7\20\2\2\u00f6\u00f7\7-\2\2")
        buf.write("\u00f7\u00f9\7\61\2\2\u00f8\u00fa\5.\30\2\u00f9\u00f8")
        buf.write("\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb")
        buf.write("\u0104\7\62\2\2\u00fc\u00fe\7.\2\2\u00fd\u00fc\3\2\2\2")
        buf.write("\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3")
        buf.write("\2\2\2\u0100\u0102\3\2\2\2\u0101\u00ff\3\2\2\2\u0102\u0105")
        buf.write("\5\66\34\2\u0103\u0105\7.\2\2\u0104\u00ff\3\2\2\2\u0104")
        buf.write("\u0103\3\2\2\2\u0105)\3\2\2\2\u0106\u0107\7-\2\2\u0107")
        buf.write("\u0108\7/\2\2\u0108\u0109\5,\27\2\u0109\u010a\7\60\2\2")
        buf.write("\u010a+\3\2\2\2\u010b\u010e\7\6\2\2\u010c\u010d\7\63\2")
        buf.write("\2\u010d\u010f\5,\27\2\u010e\u010c\3\2\2\2\u010e\u010f")
        buf.write("\3\2\2\2\u010f-\3\2\2\2\u0110\u0113\7\4\2\2\u0111\u0114")
        buf.write("\7-\2\2\u0112\u0114\5*\26\2\u0113\u0111\3\2\2\2\u0113")
        buf.write("\u0112\3\2\2\2\u0114\u0117\3\2\2\2\u0115\u0116\7\63\2")
        buf.write("\2\u0116\u0118\5.\30\2\u0117\u0115\3\2\2\2\u0117\u0118")
        buf.write("\3\2\2\2\u0118/\3\2\2\2\u0119\u011b\7\r\2\2\u011a\u011c")
        buf.write("\5\6\4\2\u011b\u011a\3\2\2\2\u011b\u011c\3\2\2\2\u011c")
        buf.write("\61\3\2\2\2\u011d\u011f\7\31\2\2\u011e\u0120\7.\2\2\u011f")
        buf.write("\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u011f\3\2\2\2")
        buf.write("\u0121\u0122\3\2\2\2\u0122\u0124\3\2\2\2\u0123\u0125\5")
        buf.write("\64\33\2\u0124\u0123\3\2\2\2\u0124\u0125\3\2\2\2\u0125")
        buf.write("\u0126\3\2\2\2\u0126\u0127\7\32\2\2\u0127\63\3\2\2\2\u0128")
        buf.write("\u012c\5\66\34\2\u0129\u012b\7.\2\2\u012a\u0129\3\2\2")
        buf.write("\2\u012b\u012e\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012d")
        buf.write("\3\2\2\2\u012d\u012f\3\2\2\2\u012e\u012c\3\2\2\2\u012f")
        buf.write("\u0130\5\64\33\2\u0130\u0139\3\2\2\2\u0131\u0135\5\66")
        buf.write("\34\2\u0132\u0134\7.\2\2\u0133\u0132\3\2\2\2\u0134\u0137")
        buf.write("\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136")
        buf.write("\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0138\u0128\3\2\2\2")
        buf.write("\u0138\u0131\3\2\2\2\u0139\65\3\2\2\2\u013a\u0143\5\60")
        buf.write("\31\2\u013b\u0143\5:\36\2\u013c\u0143\5F$\2\u013d\u0143")
        buf.write("\5H%\2\u013e\u0143\5<\37\2\u013f\u0143\5> \2\u0140\u0143")
        buf.write("\5 \21\2\u0141\u0143\5\62\32\2\u0142\u013a\3\2\2\2\u0142")
        buf.write("\u013b\3\2\2\2\u0142\u013c\3\2\2\2\u0142\u013d\3\2\2\2")
        buf.write("\u0142\u013e\3\2\2\2\u0142\u013f\3\2\2\2\u0142\u0140\3")
        buf.write("\2\2\2\u0142\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0145")
        buf.write("\7.\2\2\u0145\u0151\3\2\2\2\u0146\u0149\5@!\2\u0147\u0149")
        buf.write("\5D#\2\u0148\u0146\3\2\2\2\u0148\u0147\3\2\2\2\u0149\u014d")
        buf.write("\3\2\2\2\u014a\u014c\7.\2\2\u014b\u014a\3\2\2\2\u014c")
        buf.write("\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2")
        buf.write("\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0142\3")
        buf.write("\2\2\2\u0150\u0148\3\2\2\2\u0151\67\3\2\2\2\u0152\u0157")
        buf.write("\7\6\2\2\u0153\u0157\7\7\2\2\u0154\u0157\5\36\20\2\u0155")
        buf.write("\u0157\5\"\22\2\u0156\u0152\3\2\2\2\u0156\u0153\3\2\2")
        buf.write("\2\u0156\u0154\3\2\2\2\u0156\u0155\3\2\2\2\u01579\3\2")
        buf.write("\2\2\u0158\u015b\5\36\20\2\u0159\u015b\7-\2\2\u015a\u0158")
        buf.write("\3\2\2\2\u015a\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c")
        buf.write("\u015d\7+\2\2\u015d\u015e\5\6\4\2\u015e;\3\2\2\2\u015f")
        buf.write("\u0162\t\7\2\2\u0160\u0163\5*\26\2\u0161\u0163\7-\2\2")
        buf.write("\u0162\u0160\3\2\2\2\u0162\u0161\3\2\2\2\u0163\u0166\3")
        buf.write("\2\2\2\u0164\u0165\7+\2\2\u0165\u0167\5\6\4\2\u0166\u0164")
        buf.write("\3\2\2\2\u0166\u0167\3\2\2\2\u0167=\3\2\2\2\u0168\u016b")
        buf.write("\7\16\2\2\u0169\u016c\5*\26\2\u016a\u016c\7-\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016b\u016a\3\2\2\2\u016c\u016d\3\2\2\2")
        buf.write("\u016d\u016e\7+\2\2\u016e\u016f\5\6\4\2\u016f?\3\2\2\2")
        buf.write("\u0170\u0171\7\26\2\2\u0171\u0175\5\b\5\2\u0172\u0174")
        buf.write("\7.\2\2\u0173\u0172\3\2\2\2\u0174\u0177\3\2\2\2\u0175")
        buf.write("\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0178\3\2\2\2")
        buf.write("\u0177\u0175\3\2\2\2\u0178\u017a\5\66\34\2\u0179\u017b")
        buf.write("\5B\"\2\u017a\u0179\3\2\2\2\u017a\u017b\3\2\2\2\u017b")
        buf.write("\u0184\3\2\2\2\u017c\u0180\7\27\2\2\u017d\u017f\7.\2\2")
        buf.write("\u017e\u017d\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3")
        buf.write("\2\2\2\u0180\u0181\3\2\2\2\u0181\u0183\3\2\2\2\u0182\u0180")
        buf.write("\3\2\2\2\u0183\u0185\5\66\34\2\u0184\u017c\3\2\2\2\u0184")
        buf.write("\u0185\3\2\2\2\u0185A\3\2\2\2\u0186\u0187\7\30\2\2\u0187")
        buf.write("\u018b\5\b\5\2\u0188\u018a\7.\2\2\u0189\u0188\3\2\2\2")
        buf.write("\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c\3")
        buf.write("\2\2\2\u018c\u018e\3\2\2\2\u018d\u018b\3\2\2\2\u018e\u0190")
        buf.write("\5\66\34\2\u018f\u0191\5B\"\2\u0190\u018f\3\2\2\2\u0190")
        buf.write("\u0191\3\2\2\2\u0191C\3\2\2\2\u0192\u0195\7\21\2\2\u0193")
        buf.write("\u0196\7-\2\2\u0194\u0196\5\36\20\2\u0195\u0193\3\2\2")
        buf.write("\2\u0195\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0198")
        buf.write("\7\22\2\2\u0198\u0199\5\b\5\2\u0199\u019a\7\23\2\2\u019a")
        buf.write("\u019e\5\b\5\2\u019b\u019d\7.\2\2\u019c\u019b\3\2\2\2")
        buf.write("\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3")
        buf.write("\2\2\2\u019f\u01a1\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01a2")
        buf.write("\5\66\34\2\u01a2E\3\2\2\2\u01a3\u01a4\7\24\2\2\u01a4G")
        buf.write("\3\2\2\2\u01a5\u01a6\7\25\2\2\u01a6I\3\2\2\2\66NV[`fk")
        buf.write("qs\177\u0086\u0095\u009f\u00aa\u00b5\u00bb\u00c0\u00c7")
        buf.write("\u00cb\u00d1\u00da\u00e1\u00e8\u00f2\u00f9\u00ff\u0104")
        buf.write("\u010e\u0113\u0117\u011b\u0121\u0124\u012c\u0135\u0138")
        buf.write("\u0142\u0148\u014d\u0150\u0156\u015a\u0162\u0166\u016b")
        buf.write("\u0175\u017a\u0180\u0184\u018b\u0190\u0195\u019e")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'true'", "'false'", "'number'", 
                     "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
                     "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'!='", "'>='", "'<='", "'='", "'<'", "'>'", "'=='", 
                     "'...'", "'<-'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'['", "']'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "WS", "TYPE", "COMMENT", "NUMBER_TOKEN", 
                      "STRING_TOKEN", "TRUE", "FALSE", "NUMBER", "BOOL", 
                      "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", 
                      "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                      "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD_OP", 
                      "SUB_OP", "MULT_OP", "DIV_OP", "MOD_OP", "NE_OP", 
                      "GE_OP", "LE_OP", "SINGLE_EQUAL_OP", "L_OP", "G_OP", 
                      "DOUBLE_EQUAL_OP", "ETC_OP", "ASSIGN_OP", "OPERATOR", 
                      "IDENTIFIER", "NEWLINE", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                      "LEFT_BRACKET", "RIGHT_BRACKET", "COMMA", "END_COMMAND", 
                      "SEPARATOR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_not_nullable_declaration = 1
    RULE_math = 2
    RULE_arithmetic = 3
    RULE_atomic = 4
    RULE_string_arithmetic = 5
    RULE_compare_arithmetic = 6
    RULE_logical_arithmetic = 7
    RULE_adding_arithmetic = 8
    RULE_multiplying_arithmetic = 9
    RULE_not_arithmetic = 10
    RULE_sign_arithmetic = 11
    RULE_bracket_arithmetic = 12
    RULE_list_arithmetic = 13
    RULE_element_expression = 14
    RULE_function_call = 15
    RULE_function_expression = 16
    RULE_list_of_arithmetic_argument = 17
    RULE_index_expression = 18
    RULE_function_declaration = 19
    RULE_array_form_parameter = 20
    RULE_index_array_form_parameter = 21
    RULE_list_of_function_parameter = 22
    RULE_return_expression = 23
    RULE_block_statement = 24
    RULE_list_of_lines = 25
    RULE_line = 26
    RULE_atom = 27
    RULE_assign_statement = 28
    RULE_type_statement = 29
    RULE_var_statement = 30
    RULE_if_statement = 31
    RULE_elif_list = 32
    RULE_for_statement = 33
    RULE_break_statement = 34
    RULE_continue_statement = 35

    ruleNames =  [ "program", "not_nullable_declaration", "math", "arithmetic", 
                   "atomic", "string_arithmetic", "compare_arithmetic", 
                   "logical_arithmetic", "adding_arithmetic", "multiplying_arithmetic", 
                   "not_arithmetic", "sign_arithmetic", "bracket_arithmetic", 
                   "list_arithmetic", "element_expression", "function_call", 
                   "function_expression", "list_of_arithmetic_argument", 
                   "index_expression", "function_declaration", "array_form_parameter", 
                   "index_array_form_parameter", "list_of_function_parameter", 
                   "return_expression", "block_statement", "list_of_lines", 
                   "line", "atom", "assign_statement", "type_statement", 
                   "var_statement", "if_statement", "elif_list", "for_statement", 
                   "break_statement", "continue_statement" ]

    EOF = Token.EOF
    WS=1
    TYPE=2
    COMMENT=3
    NUMBER_TOKEN=4
    STRING_TOKEN=5
    TRUE=6
    FALSE=7
    NUMBER=8
    BOOL=9
    STRING=10
    RETURN=11
    VAR=12
    DYNAMIC=13
    FUNC=14
    FOR=15
    UNTIL=16
    BY=17
    BREAK=18
    CONTINUE=19
    IF=20
    ELSE=21
    ELIF=22
    BEGIN=23
    END=24
    NOT=25
    AND=26
    OR=27
    ADD_OP=28
    SUB_OP=29
    MULT_OP=30
    DIV_OP=31
    MOD_OP=32
    NE_OP=33
    GE_OP=34
    LE_OP=35
    SINGLE_EQUAL_OP=36
    L_OP=37
    G_OP=38
    DOUBLE_EQUAL_OP=39
    ETC_OP=40
    ASSIGN_OP=41
    OPERATOR=42
    IDENTIFIER=43
    NEWLINE=44
    LEFT_SQUARE_BRACKET=45
    RIGHT_SQUARE_BRACKET=46
    LEFT_BRACKET=47
    RIGHT_BRACKET=48
    COMMA=49
    END_COMMAND=50
    SEPARATOR=51
    ILLEGAL_ESCAPE=52
    UNCLOSE_STRING=53
    ERROR_CHAR=54

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_nullable_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Not_nullable_declarationContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.not_nullable_declaration()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 73
                self.match(ZCodeParser.NEWLINE)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_nullable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Function_declarationContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def not_nullable_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Not_nullable_declarationContext,0)


        def type_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Type_statementContext,0)


        def var_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Var_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_not_nullable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_nullable_declaration" ):
                return visitor.visitNot_nullable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def not_nullable_declaration(self):

        localctx = ZCodeParser.Not_nullable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_not_nullable_declaration)
        self._la = 0 # Token type
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 81
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 86
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 87
                self.function_declaration()
                self.state = 89
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 88
                    self.not_nullable_declaration()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 91
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 96
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 97
                self.type_statement()
                self.state = 98
                self.match(ZCodeParser.NEWLINE)
                self.state = 100
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 99
                    self.not_nullable_declaration()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 102
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 107
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 108
                self.var_statement()
                self.state = 109
                self.match(ZCodeParser.NEWLINE)
                self.state = 111
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 110
                    self.not_nullable_declaration()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.ArithmeticContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_math

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMath" ):
                return visitor.visitMath(self)
            else:
                return visitor.visitChildren(self)




    def math(self):

        localctx = ZCodeParser.MathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_math)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.arithmetic()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.String_arithmeticContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arithmetic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic" ):
                return visitor.visitArithmetic(self)
            else:
                return visitor.visitChildren(self)




    def arithmetic(self):

        localctx = ZCodeParser.ArithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arithmetic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.string_arithmetic()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def STRING_TOKEN(self):
            return self.getToken(ZCodeParser.STRING_TOKEN, 0)

        def list_arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.List_arithmeticContext,0)


        def atom(self):
            return self.getTypedRuleContext(ZCodeParser.AtomContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_atomic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic" ):
                return visitor.visitAtomic(self)
            else:
                return visitor.visitChildren(self)




    def atomic(self):

        localctx = ZCodeParser.AtomicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atomic)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.match(ZCodeParser.TRUE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.match(ZCodeParser.FALSE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 122
                self.match(ZCodeParser.STRING_TOKEN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 123
                self.list_arithmetic()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 124
                self.atom()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_arithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compare_arithmetic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Compare_arithmeticContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Compare_arithmeticContext,i)


        def ETC_OP(self):
            return self.getToken(ZCodeParser.ETC_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_string_arithmetic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_arithmetic" ):
                return visitor.visitString_arithmetic(self)
            else:
                return visitor.visitChildren(self)




    def string_arithmetic(self):

        localctx = ZCodeParser.String_arithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_string_arithmetic)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.compare_arithmetic()
                self.state = 128
                self.match(ZCodeParser.ETC_OP)
                self.state = 129
                self.compare_arithmetic()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.compare_arithmetic()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compare_arithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_arithmetic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Logical_arithmeticContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Logical_arithmeticContext,i)


        def GE_OP(self):
            return self.getToken(ZCodeParser.GE_OP, 0)

        def LE_OP(self):
            return self.getToken(ZCodeParser.LE_OP, 0)

        def L_OP(self):
            return self.getToken(ZCodeParser.L_OP, 0)

        def G_OP(self):
            return self.getToken(ZCodeParser.G_OP, 0)

        def NE_OP(self):
            return self.getToken(ZCodeParser.NE_OP, 0)

        def SINGLE_EQUAL_OP(self):
            return self.getToken(ZCodeParser.SINGLE_EQUAL_OP, 0)

        def DOUBLE_EQUAL_OP(self):
            return self.getToken(ZCodeParser.DOUBLE_EQUAL_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_compare_arithmetic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare_arithmetic" ):
                return visitor.visitCompare_arithmetic(self)
            else:
                return visitor.visitChildren(self)




    def compare_arithmetic(self):

        localctx = ZCodeParser.Compare_arithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_compare_arithmetic)
        self._la = 0 # Token type
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.logical_arithmetic(0)
                self.state = 135
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.GE_OP or _la==ZCodeParser.LE_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 136
                self.logical_arithmetic(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.logical_arithmetic(0)
                self.state = 139
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NE_OP) | (1 << ZCodeParser.SINGLE_EQUAL_OP) | (1 << ZCodeParser.L_OP) | (1 << ZCodeParser.G_OP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 140
                self.logical_arithmetic(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.logical_arithmetic(0)
                self.state = 143
                self.match(ZCodeParser.DOUBLE_EQUAL_OP)
                self.state = 144
                self.logical_arithmetic(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 146
                self.logical_arithmetic(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_arithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def adding_arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.Adding_arithmeticContext,0)


        def logical_arithmetic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Logical_arithmeticContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Logical_arithmeticContext,i)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_logical_arithmetic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_arithmetic" ):
                return visitor.visitLogical_arithmetic(self)
            else:
                return visitor.visitChildren(self)



    def logical_arithmetic(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Logical_arithmeticContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_logical_arithmetic, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.adding_arithmetic(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Logical_arithmeticContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_arithmetic)
                    self.state = 152
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 153
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 154
                    self.logical_arithmetic(3) 
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Adding_arithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplying_arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.Multiplying_arithmeticContext,0)


        def adding_arithmetic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Adding_arithmeticContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Adding_arithmeticContext,i)


        def ADD_OP(self):
            return self.getToken(ZCodeParser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(ZCodeParser.SUB_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_adding_arithmetic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_arithmetic" ):
                return visitor.visitAdding_arithmetic(self)
            else:
                return visitor.visitChildren(self)



    def adding_arithmetic(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Adding_arithmeticContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_adding_arithmetic, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.multiplying_arithmetic(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Adding_arithmeticContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_arithmetic)
                    self.state = 163
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 164
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD_OP or _la==ZCodeParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 165
                    self.adding_arithmetic(3) 
                self.state = 170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplying_arithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.Not_arithmeticContext,0)


        def multiplying_arithmetic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Multiplying_arithmeticContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Multiplying_arithmeticContext,i)


        def MULT_OP(self):
            return self.getToken(ZCodeParser.MULT_OP, 0)

        def DIV_OP(self):
            return self.getToken(ZCodeParser.DIV_OP, 0)

        def MOD_OP(self):
            return self.getToken(ZCodeParser.MOD_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_multiplying_arithmetic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_arithmetic" ):
                return visitor.visitMultiplying_arithmetic(self)
            else:
                return visitor.visitChildren(self)



    def multiplying_arithmetic(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Multiplying_arithmeticContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_multiplying_arithmetic, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.not_arithmetic()
            self._ctx.stop = self._input.LT(-1)
            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Multiplying_arithmeticContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_arithmetic)
                    self.state = 174
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 175
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULT_OP) | (1 << ZCodeParser.DIV_OP) | (1 << ZCodeParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 176
                    self.multiplying_arithmetic(3) 
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Not_arithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def not_arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.Not_arithmeticContext,0)


        def sign_arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_arithmeticContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_not_arithmetic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_arithmetic" ):
                return visitor.visitNot_arithmetic(self)
            else:
                return visitor.visitChildren(self)




    def not_arithmetic(self):

        localctx = ZCodeParser.Not_arithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_not_arithmetic)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(ZCodeParser.NOT)
                self.state = 183
                self.not_arithmetic()
                pass
            elif token in [ZCodeParser.NUMBER_TOKEN, ZCodeParser.STRING_TOKEN, ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB_OP, ZCodeParser.IDENTIFIER, ZCodeParser.LEFT_SQUARE_BRACKET, ZCodeParser.LEFT_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.sign_arithmetic()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_arithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_OP(self):
            return self.getToken(ZCodeParser.SUB_OP, 0)

        def sign_arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_arithmeticContext,0)


        def bracket_arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.Bracket_arithmeticContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sign_arithmetic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_arithmetic" ):
                return visitor.visitSign_arithmetic(self)
            else:
                return visitor.visitChildren(self)




    def sign_arithmetic(self):

        localctx = ZCodeParser.Sign_arithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_sign_arithmetic)
        try:
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.match(ZCodeParser.SUB_OP)
                self.state = 188
                self.sign_arithmetic()
                pass
            elif token in [ZCodeParser.NUMBER_TOKEN, ZCodeParser.STRING_TOKEN, ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.IDENTIFIER, ZCodeParser.LEFT_SQUARE_BRACKET, ZCodeParser.LEFT_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.bracket_arithmetic()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bracket_arithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_BRACKET, 0)

        def arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.ArithmeticContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_BRACKET, 0)

        def atomic(self):
            return self.getTypedRuleContext(ZCodeParser.AtomicContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_bracket_arithmetic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBracket_arithmetic" ):
                return visitor.visitBracket_arithmetic(self)
            else:
                return visitor.visitChildren(self)




    def bracket_arithmetic(self):

        localctx = ZCodeParser.Bracket_arithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_bracket_arithmetic)
        try:
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LEFT_BRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.match(ZCodeParser.LEFT_BRACKET)
                self.state = 193
                self.arithmetic()
                self.state = 194
                self.match(ZCodeParser.RIGHT_BRACKET)
                pass
            elif token in [ZCodeParser.NUMBER_TOKEN, ZCodeParser.STRING_TOKEN, ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.IDENTIFIER, ZCodeParser.LEFT_SQUARE_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.atomic()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_arithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_SQUARE_BRACKET, 0)

        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_SQUARE_BRACKET, 0)

        def list_of_arithmetic_argument(self):
            return self.getTypedRuleContext(ZCodeParser.List_of_arithmetic_argumentContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_arithmetic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_arithmetic" ):
                return visitor.visitList_arithmetic(self)
            else:
                return visitor.visitChildren(self)




    def list_arithmetic(self):

        localctx = ZCodeParser.List_arithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list_arithmetic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER_TOKEN) | (1 << ZCodeParser.STRING_TOKEN) | (1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.SUB_OP) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.LEFT_SQUARE_BRACKET) | (1 << ZCodeParser.LEFT_BRACKET))) != 0):
                self.state = 200
                self.list_of_arithmetic_argument()


            self.state = 203
            self.match(ZCodeParser.RIGHT_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_SQUARE_BRACKET, 0)

        def index_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Index_expressionContext,0)


        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_SQUARE_BRACKET, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def function_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Function_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_element_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_expression" ):
                return visitor.visitElement_expression(self)
            else:
                return visitor.visitChildren(self)




    def element_expression(self):

        localctx = ZCodeParser.Element_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_element_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 205
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 206
                self.function_expression()
                pass


            self.state = 209
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 210
            self.index_expression(0)
            self.state = 211
            self.match(ZCodeParser.RIGHT_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFT_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_BRACKET, 0)

        def RIGHT_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_BRACKET, 0)

        def list_of_arithmetic_argument(self):
            return self.getTypedRuleContext(ZCodeParser.List_of_arithmetic_argumentContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = ZCodeParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 214
            self.match(ZCodeParser.LEFT_BRACKET)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER_TOKEN) | (1 << ZCodeParser.STRING_TOKEN) | (1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.SUB_OP) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.LEFT_SQUARE_BRACKET) | (1 << ZCodeParser.LEFT_BRACKET))) != 0):
                self.state = 215
                self.list_of_arithmetic_argument()


            self.state = 218
            self.match(ZCodeParser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFT_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_BRACKET, 0)

        def RIGHT_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_BRACKET, 0)

        def list_of_arithmetic_argument(self):
            return self.getTypedRuleContext(ZCodeParser.List_of_arithmetic_argumentContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_expression" ):
                return visitor.visitFunction_expression(self)
            else:
                return visitor.visitChildren(self)




    def function_expression(self):

        localctx = ZCodeParser.Function_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_function_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 221
            self.match(ZCodeParser.LEFT_BRACKET)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER_TOKEN) | (1 << ZCodeParser.STRING_TOKEN) | (1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.SUB_OP) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.LEFT_SQUARE_BRACKET) | (1 << ZCodeParser.LEFT_BRACKET))) != 0):
                self.state = 222
                self.list_of_arithmetic_argument()


            self.state = 225
            self.match(ZCodeParser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_arithmetic_argumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.ArithmeticContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_of_arithmetic_argument(self):
            return self.getTypedRuleContext(ZCodeParser.List_of_arithmetic_argumentContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_of_arithmetic_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_arithmetic_argument" ):
                return visitor.visitList_of_arithmetic_argument(self)
            else:
                return visitor.visitChildren(self)




    def list_of_arithmetic_argument(self):

        localctx = ZCodeParser.List_of_arithmetic_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_list_of_arithmetic_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.arithmetic()
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.COMMA:
                self.state = 228
                self.match(ZCodeParser.COMMA)
                self.state = 229
                self.list_of_arithmetic_argument()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.ArithmeticContext,0)


        def index_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Index_expressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_index_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expression" ):
                return visitor.visitIndex_expression(self)
            else:
                return visitor.visitChildren(self)



    def index_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Index_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_index_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.arithmetic()
            self._ctx.stop = self._input.LT(-1)
            self.state = 240
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Index_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_expression)
                    self.state = 235
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 236
                    self.match(ZCodeParser.COMMA)
                    self.state = 237
                    self.arithmetic() 
                self.state = 242
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFT_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_BRACKET, 0)

        def RIGHT_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_BRACKET, 0)

        def line(self):
            return self.getTypedRuleContext(ZCodeParser.LineContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def list_of_function_parameter(self):
            return self.getTypedRuleContext(ZCodeParser.List_of_function_parameterContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = ZCodeParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(ZCodeParser.FUNC)
            self.state = 244
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 245
            self.match(ZCodeParser.LEFT_BRACKET)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.TYPE:
                self.state = 246
                self.list_of_function_parameter()


            self.state = 249
            self.match(ZCodeParser.RIGHT_BRACKET)
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 250
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 255
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 256
                self.line()
                pass

            elif la_ == 2:
                self.state = 257
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_form_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_SQUARE_BRACKET, 0)

        def index_array_form_parameter(self):
            return self.getTypedRuleContext(ZCodeParser.Index_array_form_parameterContext,0)


        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_form_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_form_parameter" ):
                return visitor.visitArray_form_parameter(self)
            else:
                return visitor.visitChildren(self)




    def array_form_parameter(self):

        localctx = ZCodeParser.Array_form_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_array_form_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 261
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 262
            self.index_array_form_parameter()
            self.state = 263
            self.match(ZCodeParser.RIGHT_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_array_form_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_TOKEN(self):
            return self.getToken(ZCodeParser.NUMBER_TOKEN, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index_array_form_parameter(self):
            return self.getTypedRuleContext(ZCodeParser.Index_array_form_parameterContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_array_form_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_array_form_parameter" ):
                return visitor.visitIndex_array_form_parameter(self)
            else:
                return visitor.visitChildren(self)




    def index_array_form_parameter(self):

        localctx = ZCodeParser.Index_array_form_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_index_array_form_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(ZCodeParser.NUMBER_TOKEN)
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.COMMA:
                self.state = 266
                self.match(ZCodeParser.COMMA)
                self.state = 267
                self.index_array_form_parameter()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_function_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(ZCodeParser.TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_form_parameter(self):
            return self.getTypedRuleContext(ZCodeParser.Array_form_parameterContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_of_function_parameter(self):
            return self.getTypedRuleContext(ZCodeParser.List_of_function_parameterContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_of_function_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_function_parameter" ):
                return visitor.visitList_of_function_parameter(self)
            else:
                return visitor.visitChildren(self)




    def list_of_function_parameter(self):

        localctx = ZCodeParser.List_of_function_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_list_of_function_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(ZCodeParser.TYPE)
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 271
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 272
                self.array_form_parameter()
                pass


            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.COMMA:
                self.state = 275
                self.match(ZCodeParser.COMMA)
                self.state = 276
                self.list_of_function_parameter()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def math(self):
            return self.getTypedRuleContext(ZCodeParser.MathContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_expression" ):
                return visitor.visitReturn_expression(self)
            else:
                return visitor.visitChildren(self)




    def return_expression(self):

        localctx = ZCodeParser.Return_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_return_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(ZCodeParser.RETURN)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER_TOKEN) | (1 << ZCodeParser.STRING_TOKEN) | (1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.SUB_OP) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.LEFT_SQUARE_BRACKET) | (1 << ZCodeParser.LEFT_BRACKET))) != 0):
                self.state = 280
                self.math()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def list_of_lines(self):
            return self.getTypedRuleContext(ZCodeParser.List_of_linesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = ZCodeParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(ZCodeParser.BEGIN)
            self.state = 285 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 284
                self.match(ZCodeParser.NEWLINE)
                self.state = 287 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TYPE) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FOR) | (1 << ZCodeParser.BREAK) | (1 << ZCodeParser.CONTINUE) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.BEGIN) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 289
                self.list_of_lines()


            self.state = 292
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_linesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self):
            return self.getTypedRuleContext(ZCodeParser.LineContext,0)


        def list_of_lines(self):
            return self.getTypedRuleContext(ZCodeParser.List_of_linesContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_list_of_lines

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_lines" ):
                return visitor.visitList_of_lines(self)
            else:
                return visitor.visitChildren(self)




    def list_of_lines(self):

        localctx = ZCodeParser.List_of_linesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_list_of_lines)
        self._la = 0 # Token type
        try:
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.line()
                self.state = 298
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 295
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 300
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 301
                self.list_of_lines()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.line()
                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 304
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 309
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def return_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Return_expressionContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_statementContext,0)


        def type_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Type_statementContext,0)


        def var_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Var_statementContext,0)


        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(ZCodeParser.For_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = ZCodeParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_line)
        try:
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 312
                    self.return_expression()
                    pass

                elif la_ == 2:
                    self.state = 313
                    self.assign_statement()
                    pass

                elif la_ == 3:
                    self.state = 314
                    self.break_statement()
                    pass

                elif la_ == 4:
                    self.state = 315
                    self.continue_statement()
                    pass

                elif la_ == 5:
                    self.state = 316
                    self.type_statement()
                    pass

                elif la_ == 6:
                    self.state = 317
                    self.var_statement()
                    pass

                elif la_ == 7:
                    self.state = 318
                    self.function_call()
                    pass

                elif la_ == 8:
                    self.state = 319
                    self.block_statement()
                    pass


                self.state = 322
                self.match(ZCodeParser.NEWLINE)
                pass
            elif token in [ZCodeParser.FOR, ZCodeParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.IF]:
                    self.state = 324
                    self.if_statement()
                    pass
                elif token in [ZCodeParser.FOR]:
                    self.state = 325
                    self.for_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 331
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 328
                        self.match(ZCodeParser.NEWLINE) 
                    self.state = 333
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_TOKEN(self):
            return self.getToken(ZCodeParser.NUMBER_TOKEN, 0)

        def STRING_TOKEN(self):
            return self.getToken(ZCodeParser.STRING_TOKEN, 0)

        def element_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Element_expressionContext,0)


        def function_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Function_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = ZCodeParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_atom)
        try:
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.match(ZCodeParser.NUMBER_TOKEN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
                self.match(ZCodeParser.STRING_TOKEN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 338
                self.element_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 339
                self.function_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN_OP(self):
            return self.getToken(ZCodeParser.ASSIGN_OP, 0)

        def math(self):
            return self.getTypedRuleContext(ZCodeParser.MathContext,0)


        def element_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Element_expressionContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = ZCodeParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 342
                self.element_expression()
                pass

            elif la_ == 2:
                self.state = 343
                self.match(ZCodeParser.IDENTIFIER)
                pass


            self.state = 346
            self.match(ZCodeParser.ASSIGN_OP)
            self.state = 347
            self.math()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(ZCodeParser.TYPE, 0)

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def array_form_parameter(self):
            return self.getTypedRuleContext(ZCodeParser.Array_form_parameterContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN_OP(self):
            return self.getToken(ZCodeParser.ASSIGN_OP, 0)

        def math(self):
            return self.getTypedRuleContext(ZCodeParser.MathContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_type_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_statement" ):
                return visitor.visitType_statement(self)
            else:
                return visitor.visitChildren(self)




    def type_statement(self):

        localctx = ZCodeParser.Type_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_type_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.TYPE or _la==ZCodeParser.DYNAMIC):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 350
                self.array_form_parameter()
                pass

            elif la_ == 2:
                self.state = 351
                self.match(ZCodeParser.IDENTIFIER)
                pass


            self.state = 356
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN_OP:
                self.state = 354
                self.match(ZCodeParser.ASSIGN_OP)
                self.state = 355
                self.math()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def ASSIGN_OP(self):
            return self.getToken(ZCodeParser.ASSIGN_OP, 0)

        def math(self):
            return self.getTypedRuleContext(ZCodeParser.MathContext,0)


        def array_form_parameter(self):
            return self.getTypedRuleContext(ZCodeParser.Array_form_parameterContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_var_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_statement" ):
                return visitor.visitVar_statement(self)
            else:
                return visitor.visitChildren(self)




    def var_statement(self):

        localctx = ZCodeParser.Var_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_var_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(ZCodeParser.VAR)
            self.state = 361
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 359
                self.array_form_parameter()
                pass

            elif la_ == 2:
                self.state = 360
                self.match(ZCodeParser.IDENTIFIER)
                pass


            self.state = 363
            self.match(ZCodeParser.ASSIGN_OP)
            self.state = 364
            self.math()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.ArithmeticContext,0)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.LineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.LineContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(ZCodeParser.IF)
            self.state = 367
            self.arithmetic()
            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 368
                self.match(ZCodeParser.NEWLINE)
                self.state = 373
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 374
            self.line()
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 375
                self.elif_list()


            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 378
                self.match(ZCodeParser.ELSE)
                self.state = 382
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 379
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 384
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 385
                self.line()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.ArithmeticContext,0)


        def line(self):
            return self.getTypedRuleContext(ZCodeParser.LineContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_list" ):
                return visitor.visitElif_list(self)
            else:
                return visitor.visitChildren(self)




    def elif_list(self):

        localctx = ZCodeParser.Elif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_elif_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(ZCodeParser.ELIF)
            self.state = 389
            self.arithmetic()
            self.state = 393
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 390
                self.match(ZCodeParser.NEWLINE)
                self.state = 395
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 396
            self.line()
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 397
                self.elif_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def arithmetic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ArithmeticContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ArithmeticContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def line(self):
            return self.getTypedRuleContext(ZCodeParser.LineContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def element_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Element_expressionContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(ZCodeParser.FOR)
            self.state = 403
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 401
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 402
                self.element_expression()
                pass


            self.state = 405
            self.match(ZCodeParser.UNTIL)
            self.state = 406
            self.arithmetic()
            self.state = 407
            self.match(ZCodeParser.BY)
            self.state = 408
            self.arithmetic()
            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 409
                self.match(ZCodeParser.NEWLINE)
                self.state = 414
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 415
            self.line()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.match(ZCodeParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.logical_arithmetic_sempred
        self._predicates[8] = self.adding_arithmetic_sempred
        self._predicates[9] = self.multiplying_arithmetic_sempred
        self._predicates[18] = self.index_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logical_arithmetic_sempred(self, localctx:Logical_arithmeticContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def adding_arithmetic_sempred(self, localctx:Adding_arithmeticContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiplying_arithmetic_sempred(self, localctx:Multiplying_arithmeticContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def index_expression_sempred(self, localctx:Index_expressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         





# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


# 2252314
from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\28")
        buf.write("\u01a3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\6\2{\n\2\r\2\16\2|\3\2\3\2\3\3\3\3\3")
        buf.write("\3\5\3\u0084\n\3\3\4\7\4\u0087\n\4\f\4\16\4\u008a\13\4")
        buf.write("\3\4\3\4\7\4\u008e\n\4\f\4\16\4\u0091\13\4\3\4\3\4\3\5")
        buf.write("\6\5\u0096\n\5\r\5\16\5\u0097\3\5\3\5\7\5\u009c\n\5\f")
        buf.write("\5\16\5\u009f\13\5\5\5\u00a1\n\5\3\5\3\5\5\5\u00a5\n\5")
        buf.write("\3\5\6\5\u00a8\n\5\r\5\16\5\u00a9\5\5\u00ac\n\5\3\6\3")
        buf.write("\6\7\6\u00b0\n\6\f\6\16\6\u00b3\13\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3")
        buf.write(")\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u0165\n-\3.\3.\7.\u0169\n")
        buf.write(".\f.\16.\u016c\13.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38")
        buf.write("\38\38\38\58\u0184\n8\39\39\39\39\39\59\u018b\n9\3:\3")
        buf.write(":\7:\u018f\n:\f:\16:\u0192\13:\3:\3:\3:\3:\3;\3;\7;\u019a")
        buf.write("\n;\f;\16;\u019d\13;\3;\3;\3<\3<\3<\2\2=\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\2\17\b\21\t\23\n\25\13\27\f\31\r\33\16\35\17")
        buf.write("\37\20!\21#\22%\23\'\24)\25+\26-\27/\30\61\31\63\32\65")
        buf.write("\33\67\349\35;\2=\36?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[")
        buf.write("-]._/a\60c\61e\62g\63i\2k\2m\64o\65q\2s\66u\67w8\3\2\16")
        buf.write("\5\2\n\13\16\17\"\"\3\2\f\f\3\2\62;\4\2GGgg\4\2--//\3")
        buf.write("\2^^\t\2))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\3\2)")
        buf.write(")\3\2$$\b\2\n\n\f\f\16\17$$))^^\2\u01c1\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2=\3\2\2")
        buf.write("\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2")
        buf.write("\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3")
        buf.write("\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[")
        buf.write("\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2")
        buf.write("e\3\2\2\2\2g\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\3z\3\2\2\2\5\u0083\3\2\2\2\7\u0088")
        buf.write("\3\2\2\2\t\u0095\3\2\2\2\13\u00ad\3\2\2\2\r\u00b7\3\2")
        buf.write("\2\2\17\u00ba\3\2\2\2\21\u00bf\3\2\2\2\23\u00c5\3\2\2")
        buf.write("\2\25\u00cc\3\2\2\2\27\u00d1\3\2\2\2\31\u00d8\3\2\2\2")
        buf.write("\33\u00df\3\2\2\2\35\u00e3\3\2\2\2\37\u00eb\3\2\2\2!\u00f0")
        buf.write("\3\2\2\2#\u00f4\3\2\2\2%\u00fa\3\2\2\2\'\u00fd\3\2\2\2")
        buf.write(")\u0103\3\2\2\2+\u010c\3\2\2\2-\u010f\3\2\2\2/\u0114\3")
        buf.write("\2\2\2\61\u0119\3\2\2\2\63\u011f\3\2\2\2\65\u0123\3\2")
        buf.write("\2\2\67\u0127\3\2\2\29\u012b\3\2\2\2;\u012e\3\2\2\2=\u0131")
        buf.write("\3\2\2\2?\u0133\3\2\2\2A\u0135\3\2\2\2C\u0137\3\2\2\2")
        buf.write("E\u0139\3\2\2\2G\u013b\3\2\2\2I\u013e\3\2\2\2K\u0141\3")
        buf.write("\2\2\2M\u0144\3\2\2\2O\u0146\3\2\2\2Q\u0148\3\2\2\2S\u014a")
        buf.write("\3\2\2\2U\u014d\3\2\2\2W\u0151\3\2\2\2Y\u0164\3\2\2\2")
        buf.write("[\u0166\3\2\2\2]\u016d\3\2\2\2_\u016f\3\2\2\2a\u0171\3")
        buf.write("\2\2\2c\u0173\3\2\2\2e\u0175\3\2\2\2g\u0177\3\2\2\2i\u0179")
        buf.write("\3\2\2\2k\u017b\3\2\2\2m\u017d\3\2\2\2o\u0183\3\2\2\2")
        buf.write("q\u018a\3\2\2\2s\u018c\3\2\2\2u\u0197\3\2\2\2w\u01a0\3")
        buf.write("\2\2\2y{\t\2\2\2zy\3\2\2\2{|\3\2\2\2|z\3\2\2\2|}\3\2\2")
        buf.write("\2}~\3\2\2\2~\177\b\2\2\2\177\4\3\2\2\2\u0080\u0084\5")
        buf.write("\23\n\2\u0081\u0084\5\25\13\2\u0082\u0084\5\27\f\2\u0083")
        buf.write("\u0080\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0082\3\2\2\2")
        buf.write("\u0084\6\3\2\2\2\u0085\u0087\5\3\2\2\u0086\u0085\3\2\2")
        buf.write("\2\u0087\u008a\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089")
        buf.write("\3\2\2\2\u0089\u008b\3\2\2\2\u008a\u0088\3\2\2\2\u008b")
        buf.write("\u008f\5;\36\2\u008c\u008e\n\3\2\2\u008d\u008c\3\2\2\2")
        buf.write("\u008e\u0091\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3")
        buf.write("\2\2\2\u0090\u0092\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0093")
        buf.write("\b\4\2\2\u0093\b\3\2\2\2\u0094\u0096\t\4\2\2\u0095\u0094")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0095\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0098\u00a0\3\2\2\2\u0099\u009d\7\60\2")
        buf.write("\2\u009a\u009c\t\4\2\2\u009b\u009a\3\2\2\2\u009c\u009f")
        buf.write("\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e")
        buf.write("\u00a1\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u0099\3\2\2\2")
        buf.write("\u00a0\u00a1\3\2\2\2\u00a1\u00ab\3\2\2\2\u00a2\u00a4\t")
        buf.write("\5\2\2\u00a3\u00a5\t\6\2\2\u00a4\u00a3\3\2\2\2\u00a4\u00a5")
        buf.write("\3\2\2\2\u00a5\u00a7\3\2\2\2\u00a6\u00a8\t\4\2\2\u00a7")
        buf.write("\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00a7\3\2\2\2")
        buf.write("\u00a9\u00aa\3\2\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00a2\3")
        buf.write("\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\n\3\2\2\2\u00ad\u00b1")
        buf.write("\5k\66\2\u00ae\u00b0\5q9\2\u00af\u00ae\3\2\2\2\u00b0\u00b3")
        buf.write("\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2")
        buf.write("\u00b4\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5\5k\66\2")
        buf.write("\u00b5\u00b6\b\6\3\2\u00b6\f\3\2\2\2\u00b7\u00b8\t\7\2")
        buf.write("\2\u00b8\u00b9\t\b\2\2\u00b9\16\3\2\2\2\u00ba\u00bb\7")
        buf.write("v\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd\7w\2\2\u00bd\u00be")
        buf.write("\7g\2\2\u00be\20\3\2\2\2\u00bf\u00c0\7h\2\2\u00c0\u00c1")
        buf.write("\7c\2\2\u00c1\u00c2\7n\2\2\u00c2\u00c3\7u\2\2\u00c3\u00c4")
        buf.write("\7g\2\2\u00c4\22\3\2\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7")
        buf.write("\7w\2\2\u00c7\u00c8\7o\2\2\u00c8\u00c9\7d\2\2\u00c9\u00ca")
        buf.write("\7g\2\2\u00ca\u00cb\7t\2\2\u00cb\24\3\2\2\2\u00cc\u00cd")
        buf.write("\7d\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf\7q\2\2\u00cf\u00d0")
        buf.write("\7n\2\2\u00d0\26\3\2\2\2\u00d1\u00d2\7u\2\2\u00d2\u00d3")
        buf.write("\7v\2\2\u00d3\u00d4\7t\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6")
        buf.write("\7p\2\2\u00d6\u00d7\7i\2\2\u00d7\30\3\2\2\2\u00d8\u00d9")
        buf.write("\7t\2\2\u00d9\u00da\7g\2\2\u00da\u00db\7v\2\2\u00db\u00dc")
        buf.write("\7w\2\2\u00dc\u00dd\7t\2\2\u00dd\u00de\7p\2\2\u00de\32")
        buf.write("\3\2\2\2\u00df\u00e0\7x\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2")
        buf.write("\7t\2\2\u00e2\34\3\2\2\2\u00e3\u00e4\7f\2\2\u00e4\u00e5")
        buf.write("\7{\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7\7c\2\2\u00e7\u00e8")
        buf.write("\7o\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea\7e\2\2\u00ea\36")
        buf.write("\3\2\2\2\u00eb\u00ec\7h\2\2\u00ec\u00ed\7w\2\2\u00ed\u00ee")
        buf.write("\7p\2\2\u00ee\u00ef\7e\2\2\u00ef \3\2\2\2\u00f0\u00f1")
        buf.write("\7h\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3\7t\2\2\u00f3\"")
        buf.write("\3\2\2\2\u00f4\u00f5\7w\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7")
        buf.write("\7v\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7n\2\2\u00f9$\3")
        buf.write("\2\2\2\u00fa\u00fb\7d\2\2\u00fb\u00fc\7{\2\2\u00fc&\3")
        buf.write("\2\2\2\u00fd\u00fe\7d\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100")
        buf.write("\7g\2\2\u0100\u0101\7c\2\2\u0101\u0102\7m\2\2\u0102(\3")
        buf.write("\2\2\2\u0103\u0104\7e\2\2\u0104\u0105\7q\2\2\u0105\u0106")
        buf.write("\7p\2\2\u0106\u0107\7v\2\2\u0107\u0108\7k\2\2\u0108\u0109")
        buf.write("\7p\2\2\u0109\u010a\7w\2\2\u010a\u010b\7g\2\2\u010b*\3")
        buf.write("\2\2\2\u010c\u010d\7k\2\2\u010d\u010e\7h\2\2\u010e,\3")
        buf.write("\2\2\2\u010f\u0110\7g\2\2\u0110\u0111\7n\2\2\u0111\u0112")
        buf.write("\7u\2\2\u0112\u0113\7g\2\2\u0113.\3\2\2\2\u0114\u0115")
        buf.write("\7g\2\2\u0115\u0116\7n\2\2\u0116\u0117\7k\2\2\u0117\u0118")
        buf.write("\7h\2\2\u0118\60\3\2\2\2\u0119\u011a\7d\2\2\u011a\u011b")
        buf.write("\7g\2\2\u011b\u011c\7i\2\2\u011c\u011d\7k\2\2\u011d\u011e")
        buf.write("\7p\2\2\u011e\62\3\2\2\2\u011f\u0120\7g\2\2\u0120\u0121")
        buf.write("\7p\2\2\u0121\u0122\7f\2\2\u0122\64\3\2\2\2\u0123\u0124")
        buf.write("\7p\2\2\u0124\u0125\7q\2\2\u0125\u0126\7v\2\2\u0126\66")
        buf.write("\3\2\2\2\u0127\u0128\7c\2\2\u0128\u0129\7p\2\2\u0129\u012a")
        buf.write("\7f\2\2\u012a8\3\2\2\2\u012b\u012c\7q\2\2\u012c\u012d")
        buf.write("\7t\2\2\u012d:\3\2\2\2\u012e\u012f\7%\2\2\u012f\u0130")
        buf.write("\7%\2\2\u0130<\3\2\2\2\u0131\u0132\7-\2\2\u0132>\3\2\2")
        buf.write("\2\u0133\u0134\7/\2\2\u0134@\3\2\2\2\u0135\u0136\7,\2")
        buf.write("\2\u0136B\3\2\2\2\u0137\u0138\7\61\2\2\u0138D\3\2\2\2")
        buf.write("\u0139\u013a\7\'\2\2\u013aF\3\2\2\2\u013b\u013c\7#\2\2")
        buf.write("\u013c\u013d\7?\2\2\u013dH\3\2\2\2\u013e\u013f\7@\2\2")
        buf.write("\u013f\u0140\7?\2\2\u0140J\3\2\2\2\u0141\u0142\7>\2\2")
        buf.write("\u0142\u0143\7?\2\2\u0143L\3\2\2\2\u0144\u0145\7?\2\2")
        buf.write("\u0145N\3\2\2\2\u0146\u0147\7>\2\2\u0147P\3\2\2\2\u0148")
        buf.write("\u0149\7@\2\2\u0149R\3\2\2\2\u014a\u014b\7?\2\2\u014b")
        buf.write("\u014c\7?\2\2\u014cT\3\2\2\2\u014d\u014e\7\60\2\2\u014e")
        buf.write("\u014f\7\60\2\2\u014f\u0150\7\60\2\2\u0150V\3\2\2\2\u0151")
        buf.write("\u0152\7>\2\2\u0152\u0153\7/\2\2\u0153X\3\2\2\2\u0154")
        buf.write("\u0165\5=\37\2\u0155\u0165\5? \2\u0156\u0165\5A!\2\u0157")
        buf.write("\u0165\5C\"\2\u0158\u0165\5E#\2\u0159\u0165\5G$\2\u015a")
        buf.write("\u0165\5I%\2\u015b\u0165\5K&\2\u015c\u0165\5M\'\2\u015d")
        buf.write("\u0165\5O(\2\u015e\u0165\5Q)\2\u015f\u0165\5\65\33\2\u0160")
        buf.write("\u0165\5\67\34\2\u0161\u0165\59\35\2\u0162\u0165\5S*\2")
        buf.write("\u0163\u0165\5U+\2\u0164\u0154\3\2\2\2\u0164\u0155\3\2")
        buf.write("\2\2\u0164\u0156\3\2\2\2\u0164\u0157\3\2\2\2\u0164\u0158")
        buf.write("\3\2\2\2\u0164\u0159\3\2\2\2\u0164\u015a\3\2\2\2\u0164")
        buf.write("\u015b\3\2\2\2\u0164\u015c\3\2\2\2\u0164\u015d\3\2\2\2")
        buf.write("\u0164\u015e\3\2\2\2\u0164\u015f\3\2\2\2\u0164\u0160\3")
        buf.write("\2\2\2\u0164\u0161\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0163")
        buf.write("\3\2\2\2\u0165Z\3\2\2\2\u0166\u016a\t\t\2\2\u0167\u0169")
        buf.write("\t\n\2\2\u0168\u0167\3\2\2\2\u0169\u016c\3\2\2\2\u016a")
        buf.write("\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b\\\3\2\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016d\u016e\t\3\2\2\u016e^\3\2\2\2\u016f")
        buf.write("\u0170\7]\2\2\u0170`\3\2\2\2\u0171\u0172\7_\2\2\u0172")
        buf.write("b\3\2\2\2\u0173\u0174\7*\2\2\u0174d\3\2\2\2\u0175\u0176")
        buf.write("\7+\2\2\u0176f\3\2\2\2\u0177\u0178\7.\2\2\u0178h\3\2\2")
        buf.write("\2\u0179\u017a\t\13\2\2\u017aj\3\2\2\2\u017b\u017c\t\f")
        buf.write("\2\2\u017cl\3\2\2\2\u017d\u017e\7\2\2\3\u017en\3\2\2\2")
        buf.write("\u017f\u0184\5c\62\2\u0180\u0184\5e\63\2\u0181\u0184\5")
        buf.write("_\60\2\u0182\u0184\5a\61\2\u0183\u017f\3\2\2\2\u0183\u0180")
        buf.write("\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0182\3\2\2\2\u0184")
        buf.write("p\3\2\2\2\u0185\u0186\t\13\2\2\u0186\u018b\t\f\2\2\u0187")
        buf.write("\u018b\t\13\2\2\u0188\u018b\5\r\7\2\u0189\u018b\n\r\2")
        buf.write("\2\u018a\u0185\3\2\2\2\u018a\u0187\3\2\2\2\u018a\u0188")
        buf.write("\3\2\2\2\u018a\u0189\3\2\2\2\u018br\3\2\2\2\u018c\u0190")
        buf.write("\5k\66\2\u018d\u018f\5q9\2\u018e\u018d\3\2\2\2\u018f\u0192")
        buf.write("\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191")
        buf.write("\u0193\3\2\2\2\u0192\u0190\3\2\2\2\u0193\u0194\t\7\2\2")
        buf.write("\u0194\u0195\n\b\2\2\u0195\u0196\b:\4\2\u0196t\3\2\2\2")
        buf.write("\u0197\u019b\5k\66\2\u0198\u019a\5q9\2\u0199\u0198\3\2")
        buf.write("\2\2\u019a\u019d\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c")
        buf.write("\3\2\2\2\u019c\u019e\3\2\2\2\u019d\u019b\3\2\2\2\u019e")
        buf.write("\u019f\b;\5\2\u019fv\3\2\2\2\u01a0\u01a1\13\2\2\2\u01a1")
        buf.write("\u01a2\b<\6\2\u01a2x\3\2\2\2\24\2|\u0083\u0088\u008f\u0097")
        buf.write("\u009d\u00a0\u00a4\u00a9\u00ab\u00b1\u0164\u016a\u0183")
        buf.write("\u018a\u0190\u019b\7\b\2\2\3\6\2\3:\3\3;\4\3<\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    TYPE = 2
    COMMENT = 3
    NUMBER_TOKEN = 4
    STRING_TOKEN = 5
    TRUE = 6
    FALSE = 7
    NUMBER = 8
    BOOL = 9
    STRING = 10
    RETURN = 11
    VAR = 12
    DYNAMIC = 13
    FUNC = 14
    FOR = 15
    UNTIL = 16
    BY = 17
    BREAK = 18
    CONTINUE = 19
    IF = 20
    ELSE = 21
    ELIF = 22
    BEGIN = 23
    END = 24
    NOT = 25
    AND = 26
    OR = 27
    ADD_OP = 28
    SUB_OP = 29
    MULT_OP = 30
    DIV_OP = 31
    MOD_OP = 32
    NE_OP = 33
    GE_OP = 34
    LE_OP = 35
    SINGLE_EQUAL_OP = 36
    L_OP = 37
    G_OP = 38
    DOUBLE_EQUAL_OP = 39
    ETC_OP = 40
    ASSIGN_OP = 41
    OPERATOR = 42
    IDENTIFIER = 43
    NEWLINE = 44
    LEFT_SQUARE_BRACKET = 45
    RIGHT_SQUARE_BRACKET = 46
    LEFT_BRACKET = 47
    RIGHT_BRACKET = 48
    COMMA = 49
    END_COMMAND = 50
    SEPARATOR = 51
    ILLEGAL_ESCAPE = 52
    UNCLOSE_STRING = 53
    ERROR_CHAR = 54

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!='", "'>='", "'<='", "'='", "'<'", "'>'", "'=='", 
            "'...'", "'<-'", "'['", "']'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "WS", "TYPE", "COMMENT", "NUMBER_TOKEN", "STRING_TOKEN", "TRUE", 
            "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", 
            "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
            "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD_OP", "SUB_OP", 
            "MULT_OP", "DIV_OP", "MOD_OP", "NE_OP", "GE_OP", "LE_OP", "SINGLE_EQUAL_OP", 
            "L_OP", "G_OP", "DOUBLE_EQUAL_OP", "ETC_OP", "ASSIGN_OP", "OPERATOR", 
            "IDENTIFIER", "NEWLINE", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
            "LEFT_BRACKET", "RIGHT_BRACKET", "COMMA", "END_COMMAND", "SEPARATOR", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "WS", "TYPE", "COMMENT", "NUMBER_TOKEN", "STRING_TOKEN", 
                  "ESCAPE", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                  "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", 
                  "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                  "NOT", "AND", "OR", "COMMENT_SIGN", "ADD_OP", "SUB_OP", 
                  "MULT_OP", "DIV_OP", "MOD_OP", "NE_OP", "GE_OP", "LE_OP", 
                  "SINGLE_EQUAL_OP", "L_OP", "G_OP", "DOUBLE_EQUAL_OP", 
                  "ETC_OP", "ASSIGN_OP", "OPERATOR", "IDENTIFIER", "NEWLINE", 
                  "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "LEFT_BRACKET", 
                  "RIGHT_BRACKET", "COMMA", "SINGLE_HOOK", "DOUBLE_HOOK", 
                  "END_COMMAND", "SEPARATOR", "STRING_ELEMENT", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[4] = self.STRING_TOKEN_action 
            actions[56] = self.ILLEGAL_ESCAPE_action 
            actions[57] = self.UNCLOSE_STRING_action 
            actions[58] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:]; raise IllegalEscape(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:]; raise UncloseString(self.text.replace('\n', ''))
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     



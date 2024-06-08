.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.field static a F

.method public static foo(FF)F
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
	fload_0
	fload_1
	fadd
	freturn
Label1:
	freturn
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
Label2:
Label4:
Label5:
Label3:
	return
.limit stack 5
.limit locals 2
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label6 to Label7
Label6:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label7:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label8 to Label9
Label8:
	ldc 0.0
	putstatic ZCodeClass.a F

Label9:
    return 
.end method

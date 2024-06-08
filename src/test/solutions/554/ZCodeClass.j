.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static main([Ljava/lang/String;)V
Label0:
Label2:

	ldc 1.0
	fneg
	fneg

	invokestatic io/writeNumber(F)V

	ldc 1.0
	fneg

	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 8
.limit locals 1
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label10 to Label11
Label10:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label11:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label12 to Label13
Label12:

Label13:
    return 
.end method

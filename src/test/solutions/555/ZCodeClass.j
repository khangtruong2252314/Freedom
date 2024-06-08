.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static foo()V
Label0:
Label2:

	ldc 1.0

	invokestatic io/writeNumber(F)V

	return

	ldc 1.0

	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 5
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label4:
Label6:

	invokestatic ZCodeClass/foo()V
Label7:
Label5:
	return
.limit stack 8
.limit locals 1
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label8 to Label9
Label8:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label9:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label10 to Label11
Label10:

Label11:
    return 
.end method

.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static foo(FB)F
.var 0 is a F from Label0 to Label1
.var 1 is b B from Label0 to Label1
Label0:
Label2:

	iload_1
	ifle Label4
Label5:

	fload_0
	ldc 1.0
	fadd
	freturn
Label6:
	goto Label7
Label4:
Label7:

	fload_0
	freturn
Label3:
Label1:
	freturn
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
Label8:
Label10:

	ldc 2.0
	iconst_1
	invokestatic ZCodeClass/foo(FB)F

	invokestatic io/writeNumber(F)V
Label11:
Label9:
	return
.limit stack 5
.limit locals 2
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label12 to Label13
Label12:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label13:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label14 to Label15
Label14:

Label15:
    return 
.end method

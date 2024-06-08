.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static main([Ljava/lang/String;)V
Label0:
Label2:

	ldc 0.0
	fstore_1

	fload_1
Label6:
	fload_1
	ldc 3.0
	fcmpl
	ifle Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
	fload_1

	invokestatic io/writeNumber(F)V
Label4:
	fload_1
	ldc 1.0
	fadd
	fstore_1
	goto Label6
Label5:
	fstore_1

	fload_1

	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 7
.limit locals 2
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label9 to Label10
Label9:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label10:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label11 to Label12
Label11:

Label12:
    return 
.end method

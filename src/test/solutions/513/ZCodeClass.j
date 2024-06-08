.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static foo()V
Label0:
Label2:

	ldc 0.0
	fstore_0

	ldc 0.0
	fstore_1

	fload_0
Label6:
	fload_0
	ldc 3.0
	fcmpl
	iflt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
Label9:

	fload_0
	ldc 1.0
	fcmpl
	ifne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	goto Label4
	goto Label14
Label11:
Label14:

	fload_0

	invokestatic io/writeNumber(F)V
Label10:
Label4:
	fload_0
	ldc 1.0
	fadd
	fstore_0
	goto Label6
Label5:
	fstore_0
Label3:
Label1:
	return
.limit stack 8
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
Label15:
Label17:

	invokestatic ZCodeClass/foo()V
Label18:
Label16:
	return
.limit stack 8
.limit locals 2
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label19 to Label20
Label19:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label20:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label21 to Label22
Label21:

Label22:
    return 
.end method

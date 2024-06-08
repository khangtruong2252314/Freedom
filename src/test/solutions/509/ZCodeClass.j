.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static print([F)V
.var 0 is a [F from Label0 to Label1
Label0:
Label2:

	ldc 0.0
	fstore_1

	fload_1
Label6:
	fload_1
	ldc 2.0
	fcmpl
	ifle Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
	aload_0
	iconst_1
	fload_1
	f2i
	imul
	faload

	invokestatic io/writeNumber(F)V
Label4:
	fload_1
	ldc 1.0
	fadd
	fstore_1
	goto Label6
Label5:
	fstore_1
Label3:
Label1:
	return
.limit stack 10
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
Label9:
Label11:

	iconst_3
	newarray float
	dup
	iconst_0
	ldc 1.0
	fastore
	dup
	iconst_1
	ldc 2.0
	fastore
	dup
	iconst_2
	ldc 3.0
	fastore
	astore_1

	aload_1
	invokestatic ZCodeClass/foo([F)V

	aload_1
	invokestatic ZCodeClass/print([F)V
Label12:
Label10:
	return
.limit stack 26
.limit locals 2
.end method

.method public static foo([F)V
.var 0 is a [F from Label13 to Label14
Label13:
Label15:

	aload_0
	iconst_1
	ldc 0.0
	f2i
	imul
	aload_0
	iconst_1
	ldc 0.0
	f2i
	imul
	faload
	ldc 1.0
	fadd
	fastore
Label16:
Label14:
	return
.limit stack 36
.limit locals 2
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label17 to Label18
Label17:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label18:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label19 to Label20
Label19:

Label20:
    return 
.end method

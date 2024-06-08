.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static main([Ljava/lang/String;)V
Label0:
Label2:

	bipush 10
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
	dup
	iconst_3
	ldc 4.0
	fastore
	dup
	iconst_4
	ldc 5.0
	fastore
	dup
	iconst_5
	ldc 6.0
	fastore
	dup
	bipush 6
	ldc 7.0
	fastore
	dup
	bipush 7
	ldc 8.0
	fastore
	dup
	bipush 8
	ldc 9.0
	fastore
	dup
	bipush 9
	ldc 10.0
	fastore
	astore_1

	aload_1
	invokestatic ZCodeClass/printArray([F)V
Label3:
Label1:
	return
.limit stack 39
.limit locals 2
.end method

.method public static printArray([F)V
.var 0 is x [F from Label4 to Label5
Label4:
Label6:

	ldc 0.0
	fstore_1

	ldc 0.0
	fstore_2

	fload_1
Label10:
	fload_1
	ldc 10.0
	fcmpl
	iflt Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifgt Label9
Label13:

	fload_2
	aload_0
	iconst_1
	fload_1
	f2i
	imul
	faload
	fadd
	fstore_2
Label14:
Label8:
	fload_1
	ldc 1.0
	fadd
	fstore_1
	goto Label10
Label9:
	fstore_1

	fload_2

	invokestatic io/writeNumber(F)V
Label7:
Label5:
	return
.limit stack 49
.limit locals 3
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label15 to Label16
Label15:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label16:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label17 to Label18
Label17:

Label18:
    return 
.end method

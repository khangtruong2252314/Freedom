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

	ldc 0.0
	fstore_2

	fload_2
Label6:
	fload_2
	ldc 10.0
	fcmpl
	iflt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
Label9:

	aload_1
	iconst_1
	fload_2
	f2i
	imul
	faload

	invokestatic io/writeNumber(F)V
Label10:
Label4:
	fload_2
	ldc 1.0
	fadd
	fstore_2
	goto Label6
Label5:
	fstore_2
Label3:
Label1:
	return
.limit stack 47
.limit locals 3
.end method

.method public static printArray([F)V
.var 0 is x [F from Label11 to Label12
Label11:
Label13:

	ldc 0.0
	fstore_1

	fload_1
Label17:
	fload_1
	ldc 10.0
	fcmpl
	iflt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifgt Label16
Label20:

	aload_0
	iconst_1
	fload_1
	f2i
	imul
	aload_0
	iconst_1
	fload_1
	f2i
	imul
	faload
	ldc 1.0
	fadd
	fastore
Label21:
Label15:
	fload_1
	ldc 1.0
	fadd
	fstore_1
	goto Label17
Label16:
	fstore_1
Label14:
Label12:
	return
.limit stack 58
.limit locals 3
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label22 to Label23
Label22:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label23:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label24 to Label25
Label24:

Label25:
    return 
.end method

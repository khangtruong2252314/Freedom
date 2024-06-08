.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static printMinArray([F)F
.var 0 is x [F from Label0 to Label1
Label0:
Label2:

	ldc 1.0
	fstore_1

	aload_0
	iconst_1
	ldc 0.0
	f2i
	imul
	faload
	fstore_2

	fload_1
Label6:
	fload_1
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

	fload_2
	aload_0
	iconst_1
	fload_1
	f2i
	imul
	faload
	fcmpl
	ifle Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	aload_0
	iconst_1
	fload_1
	f2i
	imul
	faload
	fstore_2
	goto Label14
Label11:
Label14:
Label10:
Label4:
	fload_1
	ldc 1.0
	fadd
	fstore_1
	goto Label6
Label5:
	fstore_1

	fload_2
	freturn
Label3:
Label1:
	freturn
.limit stack 13
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
Label15:
Label17:

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
	ldc 0.0
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
	ldc 1.0
	fneg
	fastore
	dup
	bipush 9
	ldc 10.0
	fastore
	astore_1

	aload_1
	invokestatic ZCodeClass/printMinArray([F)F
	fstore_2

	fload_2

	invokestatic io/writeNumber(F)V
Label18:
Label16:
	return
.limit stack 50
.limit locals 3
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label21 to Label22
Label21:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label22:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label23 to Label24
Label23:

Label24:
    return 
.end method

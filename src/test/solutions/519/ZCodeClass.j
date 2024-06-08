.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.field static x [F

.method public static main([Ljava/lang/String;)V
Label0:
Label2:

	iconst_5
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
	putstatic ZCodeClass.x [F

	getstatic ZCodeClass.x [F
	invokestatic ZCodeClass/foo([F)V
Label3:
Label1:
	return
.limit stack 47
.limit locals 1
.end method

.method public static foo([F)V
.var 0 is a [F from Label4 to Label5
Label4:
Label6:

	ldc 0.0
	fstore_1

	fload_1
Label10:
	fload_1
	ldc 5.0
	fcmpl
	ifle Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifgt Label9
Label13:

	fload_1
	ldc 5.0
	fcmpl
	ifne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label15
	goto Label9
	goto Label18
Label15:
Label18:

	aload_0
	iconst_1
	fload_1
	f2i
	imul
	getstatic ZCodeClass.x [F
	iconst_1
	fload_1
	f2i
	imul
	faload
	aload_0
	iconst_1
	fload_1
	f2i
	imul
	faload
	fadd
	fastore
Label14:
Label8:
	fload_1
	ldc 1.0
	fadd
	fstore_1
	goto Label10
Label9:
	fstore_1

	fload_1
Label21:
	fload_1
	ldc 5.0
	fcmpl
	iflt Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifgt Label20
Label24:

	getstatic ZCodeClass.x [F
	iconst_1
	fload_1
	f2i
	imul
	faload

	invokestatic io/writeNumber(F)V
Label25:
Label19:
	fload_1
	ldc 1.0
	fadd
	fstore_1
	goto Label21
Label20:
	fstore_1
Label7:
Label5:
	return
.limit stack 69
.limit locals 2
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label26 to Label27
Label26:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label27:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label28 to Label29
Label28:
	iconst_5
	newarray float
	dup
	iconst_0
	ldc 0.0
	fastore
	dup
	iconst_1
	ldc 0.0
	fastore
	dup
	iconst_2
	ldc 0.0
	fastore
	dup
	iconst_3
	ldc 0.0
	fastore
	dup
	iconst_4
	ldc 0.0
	fastore
	putstatic ZCodeClass.x [F

Label29:
    return 
.end method

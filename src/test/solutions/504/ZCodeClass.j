.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static foo([FF)F
.var 0 is a [F from Label0 to Label1
.var 1 is n F from Label0 to Label1
Label0:
Label2:

	fload_1
	ldc 1.0
	fcmpl
	ifne Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label4
	aload_0
	iconst_1
	ldc 0.0
	f2i
	imul
	faload
	freturn
	goto Label7
Label4:
Label7:

	aload_0
	fload_1
	ldc 1.0
	fsub
	invokestatic ZCodeClass/foo([FF)F
	fstore_2

	aload_0
	iconst_1
	fload_1
	ldc 1.0
	fsub
	f2i
	imul
	faload
	fload_2
	fcmpl
	ifle Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label8
	aload_0
	iconst_1
	fload_1
	ldc 1.0
	fsub
	f2i
	imul
	faload
	freturn
	goto Label11
Label8:
	fload_2
	freturn
Label11:
Label3:
Label1:
	freturn
.limit stack 8
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
Label12:
Label14:

	iconst_5
	newarray float
	dup
	iconst_0
	ldc 3.0
	fastore
	dup
	iconst_1
	ldc 9.0
	fastore
	dup
	iconst_2
	ldc 1.0
	fneg
	fastore
	dup
	iconst_3
	ldc 2.0
	fastore
	dup
	iconst_4
	ldc 6.0
	fastore
	astore_1

	aload_1
	ldc 5.0
	invokestatic ZCodeClass/foo([FF)F

	invokestatic io/writeNumber(F)V
Label15:
Label13:
	return
.limit stack 32
.limit locals 3
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label18 to Label19
Label18:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label19:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label20 to Label21
Label20:

Label21:
    return 
.end method

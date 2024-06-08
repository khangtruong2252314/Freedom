.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static main([Ljava/lang/String;)V
Label0:
Label2:



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
.var 1 is x [F from Label2 to Label3
	astore_1

	iconst_3
	newarray float
	dup
	iconst_0
	ldc 4.0
	fastore
	dup
	iconst_1
	ldc 5.0
	fastore
	dup
	iconst_2
	ldc 6.0
	fastore
.var 2 is y [F from Label2 to Label3
	astore_2

	aload_1
	aload_2
	invokestatic ZCodeClass/foo([F[F)V
Label3:
Label1:
	return
.limit stack 37
.limit locals 3
.end method

.method public static foo([F[F)V
.var 0 is a [F from Label4 to Label5
.var 1 is b [F from Label4 to Label5
Label4:
	aload_0
	iconst_1
	ldc 1.0
	f2i
	imul
	faload
	aload_1
	iconst_1
	ldc 2.0
	f2i
	imul
	faload
	fadd

	invokestatic io/writeNumber(F)V
Label5:
	return
.limit stack 44
.limit locals 3
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label6 to Label7
Label6:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label7:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label8 to Label9
Label8:

Label9:
    return 
.end method

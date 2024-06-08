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
	dup
	iconst_5
	ldc 0.0
	fastore
	dup
	bipush 6
	ldc 0.0
	fastore
	dup
	bipush 7
	ldc 0.0
	fastore
	dup
	bipush 8
	ldc 0.0
	fastore
	dup
	bipush 9
	ldc 0.0
	fastore
	astore_1

	aload_1
	iconst_1
	ldc 0.0
	f2i
	imul
	faload

	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 42
.limit locals 2
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label4 to Label5
Label4:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label5:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label6 to Label7
Label6:

Label7:
    return 
.end method

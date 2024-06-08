.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.field static x [F

.method public static foo()V
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
	putstatic ZCodeClass.x [F
Label3:
Label1:
	return
.limit stack 33
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label4:
Label6:

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
	putstatic ZCodeClass.x [F

	invokestatic ZCodeClass/foo()V

	getstatic ZCodeClass.x [F
	iconst_1
	ldc 0.0
	f2i
	imul
	faload

	invokestatic io/writeNumber(F)V
Label7:
Label5:
	return
.limit stack 54
.limit locals 1
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label8 to Label9
Label8:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label9:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label10 to Label11
Label10:
	iconst_3
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
	putstatic ZCodeClass.x [F

Label11:
    return 
.end method

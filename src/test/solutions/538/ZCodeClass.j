.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.field static a [F

.method public static main([Ljava/lang/String;)V
Label0:
Label2:

	getstatic ZCodeClass.a [F
	iconst_1
	ldc 0.0
	f2i
	imul
	faload
	fstore_1

	fload_1

	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 19
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
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 0.0
	fastore
	dup
	iconst_1
	ldc 0.0
	fastore
	putstatic ZCodeClass.a [F

Label7:
    return 
.end method

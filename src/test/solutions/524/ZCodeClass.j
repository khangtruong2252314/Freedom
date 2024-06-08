.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static foo([Ljava/lang/String;)V
.var 0 is a [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:

	ldc "x"
	astore_1

	aload_0
	iconst_1
	ldc 1.0
	f2i
	imul
	iconst_2
	ldc 1.0
	f2i
	imul
	iadd
	aload_1
	aastore
Label3:
Label1:
	return
.limit stack 11
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
Label4:
Label6:

	iconst_4
	anewarray java/lang/String
	dup
	iconst_0
	ldc ""
	aastore
	dup
	iconst_1
	ldc ""
	aastore
	dup
	iconst_2
	ldc ""
	aastore
	dup
	iconst_3
	ldc ""
	aastore
	astore_1

	aload_1
	invokestatic ZCodeClass/foo([Ljava/lang/String;)V

	aload_1
	iconst_2
	ldc 1.0
	f2i
	imul
	iconst_1
	ldc 1.0
	f2i
	imul
	iadd
	aaload

	invokestatic io/writeString(Ljava/lang/String;)V
Label7:
Label5:
	return
.limit stack 39
.limit locals 2
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

Label11:
    return 
.end method

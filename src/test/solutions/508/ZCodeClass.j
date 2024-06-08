.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static main([Ljava/lang/String;)V
Label0:
Label2:

	ldc 0.0
	fstore_1

	fload_1
	ldc 0.0
	fcmpl
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ldc 1.0
	fload_1
	fdiv
	ldc 0.0
	fcmpl
	ifle Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ior

	invokestatic io/writeBool(Z)V
Label3:
Label1:
	return
.limit stack 6
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

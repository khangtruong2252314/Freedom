.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static main([Ljava/lang/String;)V
Label0:
Label2:

	ldc 1.0
	ldc 1.0
	fcmpl
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:

	invokestatic io/writeBool(Z)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 1
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

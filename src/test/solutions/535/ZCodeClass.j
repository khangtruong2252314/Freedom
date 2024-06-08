.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static main([Ljava/lang/String;)V
Label0:
Label2:

	ldc 0.0
	fstore_1

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

	fload_1
	ldc 3.0
	fcmpl
	ifne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	goto Label5
	goto Label14
Label11:
Label14:

	fload_1

	invokestatic io/writeNumber(F)V
Label10:
Label4:
	fload_1
	ldc 2.0
	fadd
	fstore_1
	goto Label6
Label5:
	fstore_1
Label3:
Label1:
	return
.limit stack 7
.limit locals 2
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label15 to Label16
Label15:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label16:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label17 to Label18
Label17:

Label18:
    return 
.end method

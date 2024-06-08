.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static main([Ljava/lang/String;)V
Label0:
Label2:

	ldc 1.0
	fneg
	fstore_1

	fload_1
	ldc 0.0
	fcmpl
	ifne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label6
	ldc 1.0

	invokestatic io/writeNumber(F)V
	goto Label15
Label6:
	fload_1
	ldc 1.0
	fcmpl
	ifne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label7
	ldc 2.0

	invokestatic io/writeNumber(F)V
	goto Label15
Label7:
	fload_1
	ldc 2.0
	fcmpl
	ifne Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label8
	ldc 3.0

	invokestatic io/writeNumber(F)V
	goto Label15
Label8:
	ldc 4.0

	invokestatic io/writeNumber(F)V
Label15:
Label3:
Label1:
	return
.limit stack 11
.limit locals 2
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label16 to Label17
Label16:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label17:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label18 to Label19
Label18:

Label19:
    return 
.end method

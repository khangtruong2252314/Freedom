.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static foo(F)V
.var 0 is n F from Label0 to Label1
Label0:
Label2:

	fload_0

	invokestatic io/writeNumber(F)V

	fload_0
	ldc 1.0
	fcmpl
	ifne Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label4
Label7:

	return
Label8:
	goto Label9
Label4:
Label9:

	fload_0
	ldc 2.0
	frem
	ldc 0.0
	fcmpl
	ifne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label10
Label13:

	fload_0
	ldc 2.0
	fdiv
	invokestatic ZCodeClass/foo(F)V
Label14:
	goto Label15
Label10:
Label16:

	fload_0
	ldc 3.0
	fmul
	ldc 1.0
	fadd
	invokestatic ZCodeClass/foo(F)V
Label17:
Label15:
Label3:
Label1:
	return
.limit stack 9
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
Label18:
Label20:

	ldc 29.0
	invokestatic ZCodeClass/foo(F)V
Label21:
Label19:
	return
.limit stack 11
.limit locals 1
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label22 to Label23
Label22:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label23:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label24 to Label25
Label24:

Label25:
    return 
.end method

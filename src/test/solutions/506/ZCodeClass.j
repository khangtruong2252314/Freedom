.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static foo(F)B
.var 0 is n F from Label0 to Label1
Label0:
Label2:

	ldc 1.0
	fstore_1

	fload_1
Label6:
	fload_1
	fload_0
	fcmpl
	iflt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
Label9:

	iconst_0
	istore_2

	fload_0
	ldc 1.0
	fsub
	fstore_3

	fload_3
Label13:
	fload_3
	fload_1
	fcmpl
	ifge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label12
Label16:

	fload_0
	fload_1
	fload_3
	fmul
	frem
	ldc 0.0
	fcmpl
	ifne Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifle Label18
Label21:

	iconst_1
	istore_2

	goto Label12
Label22:
	goto Label23
Label18:
Label23:
Label17:
Label11:
	fload_3
	ldc 1.0
	fneg
	fadd
	fstore_3
	goto Label13
Label12:
	fstore_3

	iload_2
	ifle Label26
	iload_2
	ireturn
	goto Label27
Label26:
Label27:

	fload_1

	invokestatic io/writeNumber(F)V
Label10:
Label4:
	fload_1
	ldc 1.0
	fadd
	fstore_1
	goto Label6
Label5:
	fstore_1

	iconst_0
	ireturn
Label3:
Label1:
	ireturn
.limit stack 16
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
Label28:
Label30:

	ldc 7.0
	invokestatic ZCodeClass/foo(F)B

	invokestatic io/writeBool(Z)V
Label31:
Label29:
	return
.limit stack 18
.limit locals 4
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label32 to Label33
Label32:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label33:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label34 to Label35
Label34:

Label35:
    return 
.end method

.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static main([Ljava/lang/String;)V
Label0:
Label2:

	ldc 9.0
	fneg
	fstore_1

	fload_1
	invokestatic ZCodeClass/isPrime(F)B
	ifle Label6
	ldc "Yes"

	invokestatic io/writeString(Ljava/lang/String;)V
	goto Label7
Label6:
	ldc "No"

	invokestatic io/writeString(Ljava/lang/String;)V
Label7:
Label3:
Label1:
	return
.limit stack 8
.limit locals 2
.end method

.method public static isPrime(F)B
.var 0 is x F from Label8 to Label9
Label8:
Label10:

	fload_0
	ldc 1.0
	fcmpl
	ifgt Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label12
	iconst_0
	ireturn
	goto Label15
Label12:
Label15:

	ldc 2.0
	fstore_1

	fload_1
Label18:
	fload_1
	fload_0
	ldc 2.0
	fdiv
	fcmpl
	ifle Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifgt Label17
Label21:

	fload_0
	fload_1
	frem
	ldc 0.0
	fcmpl
	ifne Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifle Label23
	iconst_0
	ireturn
	goto Label26
Label23:
Label26:
Label22:
Label16:
	fload_1
	ldc 1.0
	fadd
	fstore_1
	goto Label18
Label17:
	fstore_1

	iconst_1
	ireturn
Label11:
Label9:
	ireturn
.limit stack 18
.limit locals 2
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label27 to Label28
Label27:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label28:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label29 to Label30
Label29:

Label30:
    return 
.end method

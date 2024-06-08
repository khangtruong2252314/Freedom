.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static main([Ljava/lang/String;)V
Label0:
Label2:

	ldc 59.0
	fstore_1

	fload_1
	invokestatic ZCodeClass/isPrime(F)B
	ifle Label4
	ldc "Yes"

	invokestatic io/writeString(Ljava/lang/String;)V
	goto Label5
Label4:
	ldc "No"

	invokestatic io/writeString(Ljava/lang/String;)V
Label5:
Label3:
Label1:
	return
.limit stack 7
.limit locals 2
.end method

.method public static isPrime(F)B
.var 0 is x F from Label6 to Label7
Label6:
Label8:

	fload_0
	ldc 1.0
	fcmpl
	ifgt Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label10
	iconst_0
	ireturn
	goto Label13
Label10:
Label13:

	ldc 2.0
	fstore_1

	fload_1
Label16:
	fload_1
	fload_0
	ldc 2.0
	fdiv
	fcmpl
	ifle Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifgt Label15
Label19:

	fload_0
	fload_1
	frem
	ldc 0.0
	fcmpl
	ifne Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifle Label21
	iconst_0
	ireturn
	goto Label24
Label21:
Label24:
Label20:
Label14:
	fload_1
	ldc 1.0
	fadd
	fstore_1
	goto Label16
Label15:
	fstore_1

	iconst_1
	ireturn
Label9:
Label7:
	ireturn
.limit stack 17
.limit locals 2
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label25 to Label26
Label25:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label26:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label27 to Label28
Label27:

Label28:
    return 
.end method

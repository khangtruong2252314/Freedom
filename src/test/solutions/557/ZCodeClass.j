.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static areDivisors(FF)B
.var 0 is num1 F from Label0 to Label1
.var 1 is num2 F from Label0 to Label1
Label0:
	fload_0
	fload_1
	frem
	ldc 0.0
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	fload_1
	fload_0
	frem
	ldc 0.0
	fcmpl
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ior
	ireturn
Label1:
	ireturn
.limit stack 6
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
Label6:
Label8:

	ldc 2.0
	fstore_1

	ldc 4.0
	fstore_2

	fload_1
	fload_2
	invokestatic ZCodeClass/areDivisors(FF)B
	ifle Label10
	ldc "Yes"

	invokestatic io/writeString(Ljava/lang/String;)V
	goto Label11
Label10:
	ldc "No"

	invokestatic io/writeString(Ljava/lang/String;)V
Label11:
Label9:
Label7:
	return
.limit stack 11
.limit locals 3
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label12 to Label13
Label12:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label13:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label14 to Label15
Label14:

Label15:
    return 
.end method

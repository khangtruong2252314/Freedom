.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static main([Ljava/lang/String;)V
Label0:
Label2:

	ldc 2.0
	fstore_1


	fload_1
	ldc 0.0
	fcmpl
	ifne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label4
	ldc 2.0
.var 2 is b F from Label2 to Label3
	fstore_2
	goto Label13
Label4:
	fload_1
	ldc 1.0
	fcmpl
	ifne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label5
	ldc 3.0
	fstore_2
	goto Label13
Label5:
	fload_1
	ldc 2.0
	fcmpl
	ifne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label6
	ldc 4.0
	fstore_2
	goto Label13
Label6:
	ldc 5.0
	fstore_2
Label13:

	fload_2

	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 13
.limit locals 3
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label14 to Label15
Label14:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label15:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label16 to Label17
Label16:

Label17:
    return 
.end method

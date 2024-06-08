.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static foo(F)F
.var 0 is n F from Label0 to Label1
Label0:
Label2:

	fload_0
	ldc 20.0
	fcmpl
	ifne Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label4
	fload_0
	freturn
	goto Label7
Label4:
	ldc 20.0
	freturn
Label7:
Label3:
Label1:
	freturn
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
Label8:
Label10:

	ldc 7.0
	invokestatic ZCodeClass/foo(F)F

	invokestatic io/writeNumber(F)V
Label11:
Label9:
	return
.limit stack 3
.limit locals 1
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

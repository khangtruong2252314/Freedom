.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static gcd(FF)F
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
Label2:

	fload_1
	ldc 0.0
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
Label7:

	fload_1
	fload_0
	fload_1
	frem
	invokestatic ZCodeClass/gcd(FF)F
	freturn
Label3:
Label1:
	freturn
.limit stack 3
.limit locals 2
.end method

.method public static lcm(FF)F
.var 0 is a F from Label8 to Label9
.var 1 is b F from Label8 to Label9
Label8:
Label10:

	fload_0
	fload_1
	fmul
	fload_0
	fload_1
	invokestatic ZCodeClass/gcd(FF)F
	fdiv
	freturn
Label11:
Label9:
	freturn
.limit stack 4
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
Label12:
Label14:

	ldc 196.0
	fstore_1

	ldc 14.0
	fstore_2

	fload_1
	fload_2
	invokestatic ZCodeClass/gcd(FF)F
	fload_1
	fload_2
	invokestatic ZCodeClass/lcm(FF)F
	fadd

	invokestatic io/writeNumber(F)V
Label15:
Label13:
	return
.limit stack 8
.limit locals 3
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

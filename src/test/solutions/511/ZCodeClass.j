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

.method public static lcm(FFF)F
.var 0 is a F from Label8 to Label9
.var 1 is b F from Label8 to Label9
.var 2 is m F from Label8 to Label9
Label8:
Label10:

	fload_2
	fload_0
	frem
	ldc 0.0
	fcmpl
	ifne Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	fload_2
	fload_1
	frem
	ldc 0.0
	fcmpl
	ifne Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	iand
	fload_2
	ldc 0.0
	fcmpl
	ifeq Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	iand
	ifle Label12
	fload_2
	freturn
	goto Label19
Label12:
Label19:

	fload_0
	fload_1
	fload_2
	fload_0
	fadd
	invokestatic ZCodeClass/lcm(FFF)F
	freturn
Label11:
Label9:
	freturn
.limit stack 7
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
Label20:
Label22:

	ldc 196.0
	fstore_1

	ldc 14.0
	fstore_2

	fload_1
	fload_2
	invokestatic ZCodeClass/gcd(FF)F
	fload_1
	fload_2
	ldc 0.0
	invokestatic ZCodeClass/lcm(FFF)F
	fadd

	invokestatic io/writeNumber(F)V
Label23:
Label21:
	return
.limit stack 11
.limit locals 3
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label24 to Label25
Label24:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label25:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label26 to Label27
Label26:

Label27:
    return 
.end method

.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object


.method public static main([Ljava/lang/String;)V
Label0:
Label2:

	iconst_1
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:

	invokestatic io/writeBool(Z)V

	iconst_1
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:

	invokestatic io/writeBool(Z)V

	iconst_0
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:

	invokestatic io/writeBool(Z)V
Label3:
Label1:
	return
.limit stack 14
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

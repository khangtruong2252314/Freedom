.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.field static a F

.method public static main([Ljava/lang/String;)V
Label0:
Label2:

	getstatic ZCodeClass.a F

	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 7
.limit locals 1
.end method

.method public <init>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label4 to Label5
Label4:
    aload_0
    invokespecial java/lang/Object/<init>()V
Label5:
    return
.end method

.method public <clinit>()V
.limit stack 100
.limit locals 100
.var 0 is this LZCodeClass; from Label6 to Label7
Label6:
	ldc 1.0
	putstatic ZCodeClass.a F

Label7:
    return 
.end method

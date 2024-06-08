import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_01(self):
        input = """
        func foo(number a[3], number b[3])
        func main ()
        begin
            dynamic x
            dynamic y
            x <- [1, 2, 3]
            y <- [4, 5, 6]
            foo(x, y)
        end
        func foo(number a[3], number b[3])
            writeNumber(a[1] + b[2])
        """
        expect = "8.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_02(self):
        input = """
        func foo(number a, number b)
            return a + b
        number a <- 0
        func main ()
        begin
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_03(self):
        inputs = """
        func foo(number a)
            begin
                if (a > 1)
                    return a * foo(a - 1)
                else
                    return 1
            end
        func main()
            begin
            writeNumber(foo(4))
            end
        """
        expect = '24.0\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 503))

    def test_04(self):
        inputs = """
        func foo(number a[5], number n)
            begin
                if (n = 1)
                    return a[0]
                number k <- foo(a, n - 1)
                if (a[n - 1] > k)
                    return a[n - 1]
                else 
                    return k
            end
        func main()
            begin
                number a[5] <- [3, 9, -1, 2, 6]
                writeNumber(foo(a, 5))
            end
        """
        expect = '9.0\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 504))

    def test_05(self):
        inputs = """
        func foo(number n)
            begin
                if (n = 20)
                    return n
                else 
                    return 20
            end
        func main()
            begin
                writeNumber(foo(7))
            end
        """
        expect = '20.0\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 505))

    def test_06(self):
        inputs = """
        func foo(number n)
            begin
                number i <- 1
                for i until i >= n by 1
                    begin
                    bool flag <- false
                    number j <- n - 1
                    for j until j < i by -1
                        begin
                            if (n % (i * j) = 0)
                                begin
                                    flag <- true
                                    break
                                end 
                        end
                    if (flag) 
                        return flag
                    writeNumber(i)
                    end
                return false
            end
        func main()
            begin
                writeBool(foo(7))
            end
        """
        expect = 'true\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 506))

    def test_07(self):
        inputs = """
                func foo(number n)
                    begin
                        writeNumber(n)
                        if (n = 1)
                        begin
                            return
                        end
                        if (n % 2 = 0)
                        begin
                            foo(n / 2)
                        end
                        else
                        begin
                            foo(n * 3 + 1)
                        end
                    end
                func main()
                    begin
                        foo(29)
                    end
                """
        expect = """29.0
88.0
44.0
22.0
11.0
34.0
17.0
52.0
26.0
13.0
40.0
20.0
10.0
5.0
16.0
8.0
4.0
2.0
1.0
"""
        self.assertTrue(TestCodeGen.test(inputs, expect, 507))

    def test_08(self):
        inputs = """
                func main()
                    begin
                        number a <- 0
                        writeBool((a = 0) or (1 / a > 0))
                    end
                """
        expect = 'true\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 508))

    def test_09(self):
        inputs = """
                func foo(number a[3])
                func print(number a[3])
                    begin
                    number i <- 0
                    for i until i > 2 by 1
                        writeNumber(a[i])
                    end
                func main()
                    begin
                        number a[3] <- [1, 2, 3]
                        foo(a)
                        print(a)
                    end
                func foo(number a[3])
                    begin
                        a[0] <- a[0] + 1
                    end
                """
        expect = '2.0\n2.0\n3.0\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 509))

    def test_10(self):
        inputs = """
                func gcd(number a, number b)
                    begin
                        if (b = 0)
                            return a 
                        return gcd(b, a % b)
                    end
                func lcm(number a, number b)
                    begin
                        return a * b / gcd(a, b)
                    end
                func main()
                    begin
                        number a <- 196
                        number b <- 14
                        writeNumber(gcd(a, b) + lcm(a, b))
                    end
                """
        expect = '210.0\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 510))

    def test_11(self):
        inputs = """
                func gcd(number a, number b)
                    begin
                        if (b = 0)
                            return a 
                        return gcd(b, a % b)
                    end
                func lcm(number a, number b, number m)
                    begin
                        if (((m % a) = 0) and ((m % b) = 0) and (m != 0))
                            return m
                        return lcm(a, b, m + a)
                    end
                func main()
                    begin
                        number a <- 196
                        number b <- 14
                        writeNumber(gcd(a, b) + lcm(a, b, 0))
                    end
                """
        expect = '210.0\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 511))

    def test_12(self):
        inputs = """
                func foo(number a, bool b)
                begin
                    if (b)
                        begin
                        return a + 1
                        end
                    return a
                end
                func main()
                    begin
                        writeNumber(foo(2, true))
                    end
                """
        expect = '3.0\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 512))

    def test_13(self):
        inputs = """
                func foo()
                    begin
                        number i <- 0
                        number j <- 0
                        for i until i >= 3 by 1
                            begin
                                if (i = 1)
                                    continue
                                writeNumber(i)
                            end
                    end
                func main()
                    begin
                        foo()
                    end
                """
        expect = '0.0\n2.0\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 513))

    def test_14(self):
        inputs = """
                func main()
                    begin
                        number i <- 0
                        for i until i > 3 by 1
                            writeNumber(i)
                        writeNumber(i)
                    end
                """
        expect = '0.0\n1.0\n2.0\n3.0\n0.0\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 514))

    def test_15(self):
        inputs = """
                func main()
                    begin
                    end
                """
        expect = ''
        self.assertTrue(TestCodeGen.test(inputs, expect, 515))

    def test_16(self):
        inputs = """
                func main()
                    begin
                    number a
                    writeNumber(a)
                    end
                """
        expect = '0.0\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 516))

    def test_17(self):
        inputs = """
                func main()
                    begin
                    number a[10]
                    writeNumber(a[0])
                    end
                """
        expect = '0.0\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 517))

    def test_18(self):
        inputs = """
                func main()
                    begin
                    writeBool("ab" == "ab")
                    end
                """
        expect = 'true\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 518))

    def test_19(self):
        inputs = """
                dynamic x
                func foo(number a[5])

                func main()
                    begin
                    x <- [1, 2, 3, 4, 5]
                    foo(x)
                    end

                func foo(number a[5])
                    begin 
                    number i
                    for i until i > 5 by 1
                        begin
                            if (i = 5)
                                break
                            a[i] <- x[i] + a[i]
                        end
                    for i until i >= 5 by 1
                        begin
                            writeNumber(x[i]) 
                        end
                    end

                """
        expect = '2.0\n4.0\n6.0\n8.0\n10.0\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 519))

    def test_20(self):
        inputs = """
        func main()
            begin
                writeBool(1 = 1)
            end
        """
        expect = 'true\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 520))

    def test_21(self):
        inputs = """
        func main()
            begin
                bool a[100]
                writeBool(a[1])
            end
        """
        expect = 'true\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 521))

    def test_22(self):
        inputs = """
        func main()
            begin
                writeString("It is writing something\\n")
                number a <- 1
                if (a = 0)
                    writeNumber(0)
                elif (a = 1)
                    writeNumber(1)
                elif (a = 2)
                    writeNumber(2)
                else 
                    writeNumber(3)
            end
        """
        expect = 'It is writing something\n\n1.0\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 522))

    def test_23(self):
        inputs = """
        func foo()
            return 1 = 1
        func main()
            begin
                writeBool(foo())
            end
        """
        expect = 'true\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 523))

    def test_24(self):
        inputs = """
        func foo(string a[2, 2])
            begin
                string s <- "x"
                a[1, 1] <- s
            end
        func main()
            begin 
                string b[2, 2]
                foo(b)
                writeString(b[1, 1])
            end
        """
        expect = 'x\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 524))

    def test_25(self):
        inputs = """
        dynamic x
        func foo ()
            begin
                x <- [1, 2, 3]
            end
        
        func main()
            begin
                x <- [4, 5, 6]
                foo()
                writeNumber(x[0])
                
            end
        """
        expect = '1.0\n'
        self.assertTrue(TestCodeGen.test(inputs, expect, 525))

    def test_26(self):

        input = """
        func main ()
        begin
            writeNumber(1.0)
            writeBool(false)
            writeString("")
        end
        """
        expect = "1.0\nfalse\n\n"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test_27(self):
        input = """
        number a <- 1
        func main ()
        begin
            writeNumber(a)
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test_28(self):
        input = """
        number a <- 1
        func main ()
        begin
            number a <- 2
            writeNumber(a)
        end
        """
        expect = "2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_29(self):
        input = """
        number a <- 1
        func main ()
        begin
            begin
                number a <- 2
            end
            writeNumber(a)
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_30(self):
        input = """
        number a <- 1
        func main ()
        begin
            begin
                number a <- 2
                writeNumber(a)
            end
            writeNumber(a)
        end
        """
        expect = "2.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_31(self):
        input = """
            func main()
            begin
                var a <- 0
                if (a = 0) writeNumber(1)
                elif (a = 1) writeNumber(2)
                elif (a = 2) writeNumber(3)
            end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_32(self):
        input = """
            func main()
            begin
                var a <- -1
                if (a = 0) writeNumber(1)
                elif (a = 1) writeNumber(2)
                elif (a = 2) writeNumber(3)
                else writeNumber(4)
            end
        """
        expect = "4.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_33(self):
        input = """
            func main()
            begin
                var a <- 2
                dynamic b
                if (a = 0) 
                    b <- 2
                elif (a = 1) 
                    b <- 3
                elif (a = 2) 
                    b <- 4
                else  
                    b <- 5
                writeNumber(b)
            end
        """
        expect = "4.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_34(self):
        input = """
            func main()
            begin
                var i <- 0
                for i until i >= 10 by 1
                begin
                    if (i = 3) break
                    writeNumber(i)
                end 
            end
        """
        expect = "0.0\n1.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_35(self):
        input = """
            func main()
            begin
                var i <- 0
                for i until i >= 10 by 2
                begin
                    if (i = 3) break
                    writeNumber(i)
                end 
            end
        """
        expect = "0.0\n2.0\n4.0\n6.0\n8.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_36(self):
        input = """
        number a[2]
        func main ()
        begin
            writeNumber(a[1])
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_37(self):
        input = """
        number a[2]
        func main ()
        begin
            writeNumber(a[1] + 1)
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_38(self):
        input = """
        number a[2]
        func main ()
        begin
            var x <- a[0]
            writeNumber(x)
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test_39(self):
        input = """
        func main ()
        begin
            number a[2]
            var x <- a[0] + 2.5
            writeNumber(x)
        end
        """
        expect = "2.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test_40(self):
        input = """
        func main ()
        begin
            writeNumber(1 + 1)
            writeNumber(1 - 1)
            writeNumber(1 * 2)
            writeNumber(1 / 2)
            writeNumber(7.5%3.5)
            writeNumber(7.8%3.38)
        end
        """
        expect = "2.0\n0.0\n2.0\n0.5\n0.5\n1.04\n"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_41(self):
        input = """
        func main ()
        begin
            writeNumber(1 + 1 + 1)
            writeNumber(1 + 1 * 3 - 1 * 2 / 2)
            writeNumber(2 * 3 % 2)
        end
        """
        expect = "3.0\n3.0\n0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_42(self):
        input = """
        func main ()
        begin
            writeBool(1 > 2) ## push -1
            writeBool(2 > 1) ## push 1
            writeBool(1 > 1) ## push 0
        end
        """
        expect = "false\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_43(self):
        input = """
        func main ()
        begin
            writeBool(1 >= 2)
            writeBool(2 >= 1) 
            writeBool(1 >= 1) 
        end
        """
        expect = "false\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_44(self):
        input = """
        func main ()
        begin
            writeBool(1 < 2) 
            writeBool(2 < 1) 
            writeBool(1 < 1) 
        end
        """
        expect = "true\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_45(self):
        input = """
        func main ()
        begin
            writeBool(1 <= 2) 
            writeBool(2 <= 1) 
            writeBool(1 <= 1) 
        end
        """
        expect = "true\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_46(self):
        input = """
        func main ()
        begin
            writeBool(1 != 2) 
            writeBool(2 != 1) 
            writeBool(1 != 1) 
        end
        """
        expect = "true\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_47(self):
        input = """
        func main ()
        begin
            writeBool(1 = 2) 
            writeBool(2 = 1) 
            writeBool(1 = 1) 
        end
        """
        expect = "false\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_48(self):
        input = """
        func main ()
        begin
            writeBool(true and true) 
            writeBool(true and false)
            writeBool(false and true) 
            writeBool(false and false)  
        end
        """
        expect = "true\nfalse\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_49(self):
        input = """
        func main ()
        begin
            writeBool(true or true) 
            writeBool(true or false)
            writeBool(false or true) 
            writeBool(false or false)  
        end
        """
        expect = "true\ntrue\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_50(self):
        input = """
        func main ()
        begin
            writeBool(true or true and false or true) 
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_51(self):
        input = """
        func main ()
        begin
            writeString("vo" ... "tien") 
        end
        """
        expect = "votien\n"
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_52(self):
        input = """
        func main ()
        begin
            writeBool("vo" == "tien") 
            writeBool("tien" == "tien")
        end
        """
        expect = "false\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_53(self):
        input = """
        func main ()
        begin
            writeBool(not not true) 
            writeBool(not true)
            writeBool(not false)
        end
        """
        expect = "true\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test_54(self):
        input = """
        func main ()
        begin
            writeNumber(--1) 
            writeNumber(-1)
        end
        """
        expect = "1.0\n-1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_55(self):
        input = """
                func foo()
                begin
                    writeNumber(1.0)
                    return
                    writeNumber(1.0)
                end        
                func main ()
                begin
                    foo()
                end
                """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_56(self):
        input = """
        func areDivisors(number num1, number num2)
        return ((num1 % num2 = 0) or (num2 % num1 = 0))
        func main()
        begin
        var num1 <- 3
        var num2 <- 4
        if (areDivisors(num1, num2)) writeString("Yes")
        else writeString("No")
        end
                """
        expect = "No\n"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_57(self):
        input = """
        func areDivisors(number num1, number num2)
        return ((num1 % num2 = 0) or (num2 % num1 = 0))
        func main()
        begin
        var num1 <- 2
        var num2 <- 4
        if (areDivisors(num1, num2)) writeString("Yes")
        else writeString("No")
        end
                """
        expect = "Yes\n"
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_58(self):
        input = """
        func isPrime(number x)
        func main()
        begin
        number x <- 7
        if (isPrime(x)) writeString("Yes")
        else writeString("No")
        end
        func isPrime(number x)
        begin
        if (x <= 1) return false
        var i <- 2
        for i until i > x / 2 by 1
        begin
        if (x % i = 0) return false

        end
        return true
        end
                """
        expect = "Yes\n"
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_59(self):
        input = """
            func isPrime(number x)
            func main()
            begin
            number x <- 59
            if (isPrime(x)) writeString("Yes")
            else writeString("No")
            end
            func isPrime(number x)
            begin
            if (x <= 1) return false
            var i <- 2
            for i until i > x / 2 by 1
            begin
            if (x % i = 0) return false

            end
            return true
            end
                    """
        expect = "Yes\n"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_60(self):
        input = """
        func isPrime(number x)
        func main()
        begin
        number x <- -9
        if (isPrime(x)) writeString("Yes")
        else writeString("No")
        end
        func isPrime(number x)
        begin
        if (x <= 1) return false
        var i <- 2
        for i until i > x / 2 by 1
        begin
        if (x % i = 0) return false

        end
        return true
        end
                """
        expect = "No\n"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_61(self):
        input = """
        func printArray(number x[10])
        func main()
        begin
            var a <- [1,2,3,4,5,6,7,8,9,10]
            printArray(a)
        end

        func printArray(number x[10])
        begin
            var i <- 0
            for i until i >= 10 by 1
                writeNumber(x[i])
        end

                """
        expect = "1.0\n2.0\n3.0\n4.0\n5.0\n6.0\n7.0\n8.0\n9.0\n10.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_62(self):
        input = """
        func printArray(number x[10])
        func main()
        begin
            var a <- [1,2,3,4,5,6,7,8,9,10]
            printArray(a)
        end

        func printArray(number x[10])
        begin
            var i <- 0
            var c <- 0
            for i until i >= 10 by 1
            begin
                c <- c + x[i]
            end
            writeNumber(c)
        end

                """
        expect = "55.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_63(self):
        input = """
        func printArray(number x[10])
        func main()
        begin
            var a <- [1,2,3,4,5,6,7,8,9,10]
            printArray(a)
            var i <- 0
            for i until i >= 10 by 1
            begin
                writeNumber(a[i])
            end
        end

        func printArray(number x[10])
        begin
            var i <- 0
            for i until i >= 10 by 1
            begin
                x[i] <-  x[i] + 1
            end
        end
                """
        expect = "2.0\n3.0\n4.0\n5.0\n6.0\n7.0\n8.0\n9.0\n10.0\n11.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test_64(self):
        input = """
        func printMinArray(number x[10])
        begin
            var i <- 1
            var min <- x[0]
            for i until i >= 10 by 1
            begin
                if (min > x[i]) min <- x[i]
            end
            return min
        end
        
        func main()
        begin
            var a <- [1,2,3,4,5,0,7,8,9,10]
            var c <- printMinArray(a)
            writeNumber(c)
        end
                """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_65(self):
        input = """
        func printMinArray(number x[10])
        begin
            var i <- 1
            var min <- x[0]
            for i until i >= 10 by 1
            begin
                if (min > x[i]) min <- x[i]
            end
            return min
        end
        
        func main()
        begin
            var a <- [1,2,3,4,5,0,7,8,-1,10]
            var c <- printMinArray(a)
            writeNumber(c)
        end

                """
        expect = "-1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 565))


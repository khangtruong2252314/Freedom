import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):
	def test_301(self):
		input = '''
func Scur (bool Jj[98.45,3.25], string uNrB)	begin
		string xgb[69.98,25.97] <- false
		begin
			return
		end
	end

var gD <- not 97.91
func QY (number fYYW[38.17])
	begin
	end

number Tyhg[19.76,4.57] <- Mtz(DvZC(0.56, FfAV))
'''
		expect = '''Program([FuncDecl(Id(Scur), [VarDecl(Id(Jj), ArrayType([98.45, 3.25], BoolType), None, None), VarDecl(Id(uNrB), StringType, None, None)], Block([VarDecl(Id(xgb), ArrayType([69.98, 25.97], StringType), None, BooleanLit(False)), Block([Return()])])), VarDecl(Id(gD), None, var, UnaryOp(not, NumLit(97.91))), FuncDecl(Id(QY), [VarDecl(Id(fYYW), ArrayType([38.17], NumberType), None, None)], Block([])), VarDecl(Id(Tyhg), ArrayType([19.76, 4.57], NumberType), None, CallExpr(Id(Mtz), [CallExpr(Id(DvZC), [NumLit(0.56), Id(FfAV)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 301))

	def test_302(self):
		input = '''
func TE (string W5)	return 66.54

'''
		expect = '''Program([FuncDecl(Id(TE), [VarDecl(Id(W5), StringType, None, None)], Return(NumLit(66.54)))])'''
		self.assertTrue(TestAST.test(input, expect, 302))

	def test_303(self):
		input = '''
func ZRy ()
	return "f"
func Rc (number gs[37.17,58.26], number i7q, string s5wI)	begin
		number sZS <- yKI
		var QRb <- "Z"
		for Ij until BHEE by "yCyYA"
			IBiy(82.43, fJit)
	end

dynamic CHVm <- false
string nNXq[68.31,83.16,83.65] <- true
bool uML <- true
'''
		expect = '''Program([FuncDecl(Id(ZRy), [], Return(StringLit(f))), FuncDecl(Id(Rc), [VarDecl(Id(gs), ArrayType([37.17, 58.26], NumberType), None, None), VarDecl(Id(i7q), NumberType, None, None), VarDecl(Id(s5wI), StringType, None, None)], Block([VarDecl(Id(sZS), NumberType, None, Id(yKI)), VarDecl(Id(QRb), None, var, StringLit(Z)), For(Id(Ij), Id(BHEE), StringLit(yCyYA), CallStmt(Id(IBiy), [NumLit(82.43), Id(fJit)]))])), VarDecl(Id(CHVm), None, dynamic, BooleanLit(False)), VarDecl(Id(nNXq), ArrayType([68.31, 83.16, 83.65], StringType), None, BooleanLit(True)), VarDecl(Id(uML), BoolType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 303))

	def test_304(self):
		input = '''
bool tdo[70.06,50.24,2.66]
bool AGv[11.72] <- 77.93
func VN6y ()
	return false
number Cru[43.77,38.18,71.25] <- HCA
string pjq[2.76,40.75]
'''
		expect = '''Program([VarDecl(Id(tdo), ArrayType([70.06, 50.24, 2.66], BoolType), None, None), VarDecl(Id(AGv), ArrayType([11.72], BoolType), None, NumLit(77.93)), FuncDecl(Id(VN6y), [], Return(BooleanLit(False))), VarDecl(Id(Cru), ArrayType([43.77, 38.18, 71.25], NumberType), None, Id(HCA)), VarDecl(Id(pjq), ArrayType([2.76, 40.75], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 304))

	def test_305(self):
		input = '''
func P7 ()	begin
		return 1.12
		kv(false, true)
	end
func ojw (string m7v_)
	return

number VgGH[22.6,84.97,94.83]
func ZaBA (string Bl[38.71,22.26], number Tub[38.19], bool WSp)
	return

func pwv ()	begin
		for NHm until true by "fT"
			for SwO until 89.2 by false
				return true
		for DmG until nkau by "SjTks"
			EAU8(nS65)
	end
'''
		expect = '''Program([FuncDecl(Id(P7), [], Block([Return(NumLit(1.12)), CallStmt(Id(kv), [BooleanLit(False), BooleanLit(True)])])), FuncDecl(Id(ojw), [VarDecl(Id(m7v_), StringType, None, None)], Return()), VarDecl(Id(VgGH), ArrayType([22.6, 84.97, 94.83], NumberType), None, None), FuncDecl(Id(ZaBA), [VarDecl(Id(Bl), ArrayType([38.71, 22.26], StringType), None, None), VarDecl(Id(Tub), ArrayType([38.19], NumberType), None, None), VarDecl(Id(WSp), BoolType, None, None)], Return()), FuncDecl(Id(pwv), [], Block([For(Id(NHm), BooleanLit(True), StringLit(fT), For(Id(SwO), NumLit(89.2), BooleanLit(False), Return(BooleanLit(True)))), For(Id(DmG), Id(nkau), StringLit(SjTks), CallStmt(Id(EAU8), [Id(nS65)]))]))])'''
		self.assertTrue(TestAST.test(input, expect, 305))

	def test_306(self):
		input = '''
string ff[68.64] <- 34.72
number ZV <- "oO"
bool bUh[57.77]
number Fyo[23.11,41.98] <- "L"
'''
		expect = '''Program([VarDecl(Id(ff), ArrayType([68.64], StringType), None, NumLit(34.72)), VarDecl(Id(ZV), NumberType, None, StringLit(oO)), VarDecl(Id(bUh), ArrayType([57.77], BoolType), None, None), VarDecl(Id(Fyo), ArrayType([23.11, 41.98], NumberType), None, StringLit(L))])'''
		self.assertTrue(TestAST.test(input, expect, 306))

	def test_307(self):
		input = '''
dynamic WaP
func Vpra (string fz23[97.81,85.93], bool U_)	begin
	end

string aJC8[45.7,58.68] <- true
'''
		expect = '''Program([VarDecl(Id(WaP), None, dynamic, None), FuncDecl(Id(Vpra), [VarDecl(Id(fz23), ArrayType([97.81, 85.93], StringType), None, None), VarDecl(Id(U_), BoolType, None, None)], Block([])), VarDecl(Id(aJC8), ArrayType([45.7, 58.68], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 307))

	def test_308(self):
		input = '''
var TRw <- e0t
func SrS ()	return "vg"
func tG6 ()	return
dynamic INA <- siD
'''
		expect = '''Program([VarDecl(Id(TRw), None, var, Id(e0t)), FuncDecl(Id(SrS), [], Return(StringLit(vg))), FuncDecl(Id(tG6), [], Return()), VarDecl(Id(INA), None, dynamic, Id(siD))])'''
		self.assertTrue(TestAST.test(input, expect, 308))

	def test_309(self):
		input = '''
func ZhNe (number ze[22.02,91.51])
	return false
number SJ
func TP ()	return 20.37
func o1 ()
	return

'''
		expect = '''Program([FuncDecl(Id(ZhNe), [VarDecl(Id(ze), ArrayType([22.02, 91.51], NumberType), None, None)], Return(BooleanLit(False))), VarDecl(Id(SJ), NumberType, None, None), FuncDecl(Id(TP), [], Return(NumLit(20.37))), FuncDecl(Id(o1), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 309))

	def test_310(self):
		input = '''
func FCe (bool uLVL[32.76,55.22], number Ob[96.55,78.15,49.91])	return Cf
'''
		expect = '''Program([FuncDecl(Id(FCe), [VarDecl(Id(uLVL), ArrayType([32.76, 55.22], BoolType), None, None), VarDecl(Id(Ob), ArrayType([96.55, 78.15, 49.91], NumberType), None, None)], Return(Id(Cf)))])'''
		self.assertTrue(TestAST.test(input, expect, 310))

	def test_311(self):
		input = '''
func rX (number ISs, string kl)	return
'''
		expect = '''Program([FuncDecl(Id(rX), [VarDecl(Id(ISs), NumberType, None, None), VarDecl(Id(kl), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 311))

	def test_312(self):
		input = '''
bool wp <- Lf
number jWx[82.64,73.18]
string TaTI <- tNxo
func I9 (bool CMWW[26.81,77.9])
	return
func t4 (string zO2[25.25,3.89,11.73], number mi[3.28])	return 91.77
'''
		expect = '''Program([VarDecl(Id(wp), BoolType, None, Id(Lf)), VarDecl(Id(jWx), ArrayType([82.64, 73.18], NumberType), None, None), VarDecl(Id(TaTI), StringType, None, Id(tNxo)), FuncDecl(Id(I9), [VarDecl(Id(CMWW), ArrayType([26.81, 77.9], BoolType), None, None)], Return()), FuncDecl(Id(t4), [VarDecl(Id(zO2), ArrayType([25.25, 3.89, 11.73], StringType), None, None), VarDecl(Id(mi), ArrayType([3.28], NumberType), None, None)], Return(NumLit(91.77)))])'''
		self.assertTrue(TestAST.test(input, expect, 312))

	def test_313(self):
		input = '''
func dg (bool n2o5[82.79], number zwF[41.43,8.67,75.05], bool QN6U[18.31,16.3])
	return false

string vow5
'''
		expect = '''Program([FuncDecl(Id(dg), [VarDecl(Id(n2o5), ArrayType([82.79], BoolType), None, None), VarDecl(Id(zwF), ArrayType([41.43, 8.67, 75.05], NumberType), None, None), VarDecl(Id(QN6U), ArrayType([18.31, 16.3], BoolType), None, None)], Return(BooleanLit(False))), VarDecl(Id(vow5), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 313))

	def test_314(self):
		input = '''
func Mjx ()	return
func XZ (number CF7F[88.29,11.28], string qt[61.56,54.76], string K9uv)	return

func h_Z (number pAT_)	return

bool M9[85.83,72.89]
'''
		expect = '''Program([FuncDecl(Id(Mjx), [], Return()), FuncDecl(Id(XZ), [VarDecl(Id(CF7F), ArrayType([88.29, 11.28], NumberType), None, None), VarDecl(Id(qt), ArrayType([61.56, 54.76], StringType), None, None), VarDecl(Id(K9uv), StringType, None, None)], Return()), FuncDecl(Id(h_Z), [VarDecl(Id(pAT_), NumberType, None, None)], Return()), VarDecl(Id(M9), ArrayType([85.83, 72.89], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 314))

	def test_315(self):
		input = '''
var LS <- cVI
func lJ ()	return Af
var wZE <- "WPE"
string msU
'''
		expect = '''Program([VarDecl(Id(LS), None, var, Id(cVI)), FuncDecl(Id(lJ), [], Return(Id(Af))), VarDecl(Id(wZE), None, var, StringLit(WPE)), VarDecl(Id(msU), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 315))

	def test_317(self):
		input = '''
func VUl2 (bool hI_A, string V4G[81.18,27.91])
	return
func ttO (string Eh, bool IB)	return "bFIAO"
func UPww ()	return 21.64

string uN2[92.5,28.47] <- false
bool kFMn[8.28,93.41,27.65] <- "W"
'''
		expect = '''Program([FuncDecl(Id(VUl2), [VarDecl(Id(hI_A), BoolType, None, None), VarDecl(Id(V4G), ArrayType([81.18, 27.91], StringType), None, None)], Return()), FuncDecl(Id(ttO), [VarDecl(Id(Eh), StringType, None, None), VarDecl(Id(IB), BoolType, None, None)], Return(StringLit(bFIAO))), FuncDecl(Id(UPww), [], Return(NumLit(21.64))), VarDecl(Id(uN2), ArrayType([92.5, 28.47], StringType), None, BooleanLit(False)), VarDecl(Id(kFMn), ArrayType([8.28, 93.41, 27.65], BoolType), None, StringLit(W))])'''
		self.assertTrue(TestAST.test(input, expect, 317))

	def test_318(self):
		input = '''
func U5Q (bool zA9p, number K8A3)
	return ND

func Zf54 (bool WN[39.31,48.93], number C4m9)	begin
	end

string nYCl <- true
string rDF <- false
'''
		expect = '''Program([FuncDecl(Id(U5Q), [VarDecl(Id(zA9p), BoolType, None, None), VarDecl(Id(K8A3), NumberType, None, None)], Return(Id(ND))), FuncDecl(Id(Zf54), [VarDecl(Id(WN), ArrayType([39.31, 48.93], BoolType), None, None), VarDecl(Id(C4m9), NumberType, None, None)], Block([])), VarDecl(Id(nYCl), StringType, None, BooleanLit(True)), VarDecl(Id(rDF), StringType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 318))

	def test_319(self):
		input = '''
string rM[37.82] <- true
func Tl (number X9[57.37], string A7H, bool inrx[85.97,78.76,82.74])	return NNkM

number hPl
bool rGx[70.35] <- 71.2
func p9y (bool M6AL, number JI, string gQ3)
	return true
'''
		expect = '''Program([VarDecl(Id(rM), ArrayType([37.82], StringType), None, BooleanLit(True)), FuncDecl(Id(Tl), [VarDecl(Id(X9), ArrayType([57.37], NumberType), None, None), VarDecl(Id(A7H), StringType, None, None), VarDecl(Id(inrx), ArrayType([85.97, 78.76, 82.74], BoolType), None, None)], Return(Id(NNkM))), VarDecl(Id(hPl), NumberType, None, None), VarDecl(Id(rGx), ArrayType([70.35], BoolType), None, NumLit(71.2)), FuncDecl(Id(p9y), [VarDecl(Id(M6AL), BoolType, None, None), VarDecl(Id(JI), NumberType, None, None), VarDecl(Id(gQ3), StringType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 319))

	def test_320(self):
		input = '''
string MbPL
bool yLm[63.85] <- "hPtU"
dynamic VYt <- Pe2
func xZ (string rDmG[83.16])
	return false
number g55
'''
		expect = '''Program([VarDecl(Id(MbPL), StringType, None, None), VarDecl(Id(yLm), ArrayType([63.85], BoolType), None, StringLit(hPtU)), VarDecl(Id(VYt), None, dynamic, Id(Pe2)), FuncDecl(Id(xZ), [VarDecl(Id(rDmG), ArrayType([83.16], StringType), None, None)], Return(BooleanLit(False))), VarDecl(Id(g55), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 320))

	def test_321(self):
		input = '''
func BLzf (bool qY)	return
string rFGw[85.71,6.64] <- eDR
func hddM (string cs[78.86,46.94,3.37])	return 66.06
string vT <- 23.91
func rh6v ()
	return true

'''
		expect = '''Program([FuncDecl(Id(BLzf), [VarDecl(Id(qY), BoolType, None, None)], Return()), VarDecl(Id(rFGw), ArrayType([85.71, 6.64], StringType), None, Id(eDR)), FuncDecl(Id(hddM), [VarDecl(Id(cs), ArrayType([78.86, 46.94, 3.37], StringType), None, None)], Return(NumLit(66.06))), VarDecl(Id(vT), StringType, None, NumLit(23.91)), FuncDecl(Id(rh6v), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 321))

	def test_323(self):
		input = '''
string ArN2
func h6o (string AY[70.73,86.64], bool xan[91.8,51.63,95.56])
	return
func qcO (string Cmi[44.16,91.26])	return false
'''
		expect = '''Program([VarDecl(Id(ArN2), StringType, None, None), FuncDecl(Id(h6o), [VarDecl(Id(AY), ArrayType([70.73, 86.64], StringType), None, None), VarDecl(Id(xan), ArrayType([91.8, 51.63, 95.56], BoolType), None, None)], Return()), FuncDecl(Id(qcO), [VarDecl(Id(Cmi), ArrayType([44.16, 91.26], StringType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 323))

	def test_324(self):
		input = '''
func yWH (number C3[12.56])
	return 88.14

bool JHx[61.39,83.41] <- 3.73
'''
		expect = '''Program([FuncDecl(Id(yWH), [VarDecl(Id(C3), ArrayType([12.56], NumberType), None, None)], Return(NumLit(88.14))), VarDecl(Id(JHx), ArrayType([61.39, 83.41], BoolType), None, NumLit(3.73))])'''
		self.assertTrue(TestAST.test(input, expect, 324))

	def test_325(self):
		input = '''
string QL[87.77,61.78]
func CZ (string W8f[26.47], number p_z)
	begin
	end
'''
		expect = '''Program([VarDecl(Id(QL), ArrayType([87.77, 61.78], StringType), None, None), FuncDecl(Id(CZ), [VarDecl(Id(W8f), ArrayType([26.47], StringType), None, None), VarDecl(Id(p_z), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 325))

	def test_326(self):
		input = '''
number D0[25.93,60.58] <- upm3
number j2c
func FPzk (string Aq8q[93.1], number lj2[0.85,61.88], string vN7)	return
func Hiu (bool qrVc, bool YX, string lK[5.53,37.62])
	return 1.59
'''
		expect = '''Program([VarDecl(Id(D0), ArrayType([25.93, 60.58], NumberType), None, Id(upm3)), VarDecl(Id(j2c), NumberType, None, None), FuncDecl(Id(FPzk), [VarDecl(Id(Aq8q), ArrayType([93.1], StringType), None, None), VarDecl(Id(lj2), ArrayType([0.85, 61.88], NumberType), None, None), VarDecl(Id(vN7), StringType, None, None)], Return()), FuncDecl(Id(Hiu), [VarDecl(Id(qrVc), BoolType, None, None), VarDecl(Id(YX), BoolType, None, None), VarDecl(Id(lK), ArrayType([5.53, 37.62], StringType), None, None)], Return(NumLit(1.59)))])'''
		self.assertTrue(TestAST.test(input, expect, 326))

	def test_327(self):
		input = '''
string D9[66.8]
func XoDb (string dgrp)	return
func Ef (bool pxDM[28.82,21.1], bool vuY, bool XW[49.6,46.28])	return

func aZ ()	return
'''
		expect = '''Program([VarDecl(Id(D9), ArrayType([66.8], StringType), None, None), FuncDecl(Id(XoDb), [VarDecl(Id(dgrp), StringType, None, None)], Return()), FuncDecl(Id(Ef), [VarDecl(Id(pxDM), ArrayType([28.82, 21.1], BoolType), None, None), VarDecl(Id(vuY), BoolType, None, None), VarDecl(Id(XW), ArrayType([49.6, 46.28], BoolType), None, None)], Return()), FuncDecl(Id(aZ), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 327))

	def test_328(self):
		input = '''
string wPjs
'''
		expect = '''Program([VarDecl(Id(wPjs), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 328))

	def test_329(self):
		input = '''
func JXV (number ouK[16.57], bool kzhw)	return false
number p6d[83.71]
func VjT (bool deFd[6.26])	return

'''
		expect = '''Program([FuncDecl(Id(JXV), [VarDecl(Id(ouK), ArrayType([16.57], NumberType), None, None), VarDecl(Id(kzhw), BoolType, None, None)], Return(BooleanLit(False))), VarDecl(Id(p6d), ArrayType([83.71], NumberType), None, None), FuncDecl(Id(VjT), [VarDecl(Id(deFd), ArrayType([6.26], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 329))

	def test_330(self):
		input = '''
func UkE (bool LV[27.72])
	return 98.04

number YokD <- "RKA"
string cig
dynamic V0 <- 27.19
func l0p (string pD[47.38,7.51,79.63])
	return 11.83
'''
		expect = '''Program([FuncDecl(Id(UkE), [VarDecl(Id(LV), ArrayType([27.72], BoolType), None, None)], Return(NumLit(98.04))), VarDecl(Id(YokD), NumberType, None, StringLit(RKA)), VarDecl(Id(cig), StringType, None, None), VarDecl(Id(V0), None, dynamic, NumLit(27.19)), FuncDecl(Id(l0p), [VarDecl(Id(pD), ArrayType([47.38, 7.51, 79.63], StringType), None, None)], Return(NumLit(11.83)))])'''
		self.assertTrue(TestAST.test(input, expect, 330))

	def test_331(self):
		input = '''
func Wf ()
	begin
		if (fP) for b3 until "U" by "Ft"
			number Ig
		elif (Tt0y)
		break
		elif (hB)
		break
		elif ("yVK")
		begin
			continue
			wv(false)
			for fa until Dwu by true
				yi7p()
		end
		else return
		if (51.43) bool Te[17.59,24.6,34.25] <- Qoo0
		else break
		if (false) dynamic rK_
		elif ("YFVu")
		string jQw[39.99]
		elif (69.84)
		continue
		elif (false) bool II[20.17,21.4,94.73] <- true
	end
func mP (string wY)
	begin
	end

func au3m (number XV)	return

'''
		expect = '''Program([FuncDecl(Id(Wf), [], Block([If((Id(fP), For(Id(b3), StringLit(U), StringLit(Ft), VarDecl(Id(Ig), NumberType, None, None))), [(Id(Tt0y), Break), (Id(hB), Break), (StringLit(yVK), Block([Continue, CallStmt(Id(wv), [BooleanLit(False)]), For(Id(fa), Id(Dwu), BooleanLit(True), CallStmt(Id(yi7p), []))]))], Return()), If((NumLit(51.43), VarDecl(Id(Te), ArrayType([17.59, 24.6, 34.25], BoolType), None, Id(Qoo0))), [], Break), If((BooleanLit(False), VarDecl(Id(rK_), None, dynamic, None)), [(StringLit(YFVu), VarDecl(Id(jQw), ArrayType([39.99], StringType), None, None)), (NumLit(69.84), Continue), (BooleanLit(False), VarDecl(Id(II), ArrayType([20.17, 21.4, 94.73], BoolType), None, BooleanLit(True)))], None)])), FuncDecl(Id(mP), [VarDecl(Id(wY), StringType, None, None)], Block([])), FuncDecl(Id(au3m), [VarDecl(Id(XV), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 331))

	def test_332(self):
		input = '''
var NWI <- zmk
number bR5h[47.7,25.05,40.35]
'''
		expect = '''Program([VarDecl(Id(NWI), None, var, Id(zmk)), VarDecl(Id(bR5h), ArrayType([47.7, 25.05, 40.35], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 332))

	def test_333(self):
		input = '''
bool WB4[26.34]
bool txuY[89.72,32.58,56.65] <- "yfNz"
number Tyk <- zh
'''
		expect = '''Program([VarDecl(Id(WB4), ArrayType([26.34], BoolType), None, None), VarDecl(Id(txuY), ArrayType([89.72, 32.58, 56.65], BoolType), None, StringLit(yfNz)), VarDecl(Id(Tyk), NumberType, None, Id(zh))])'''
		self.assertTrue(TestAST.test(input, expect, 333))

	def test_334(self):
		input = '''
bool u2[19.3,65.36,72.05]
func hSs ()	return
func wZ ()	begin
		for A42V until "ZR" by false
			bool RDE[40.17,28.78,56.86]
	end

bool Y0u[12.51,33.0]
string GLxr[56.68] <- 36.83
'''
		expect = '''Program([VarDecl(Id(u2), ArrayType([19.3, 65.36, 72.05], BoolType), None, None), FuncDecl(Id(hSs), [], Return()), FuncDecl(Id(wZ), [], Block([For(Id(A42V), StringLit(ZR), BooleanLit(False), VarDecl(Id(RDE), ArrayType([40.17, 28.78, 56.86], BoolType), None, None))])), VarDecl(Id(Y0u), ArrayType([12.51, 33.0], BoolType), None, None), VarDecl(Id(GLxr), ArrayType([56.68], StringType), None, NumLit(36.83))])'''
		self.assertTrue(TestAST.test(input, expect, 334))

	def test_335(self):
		input = '''
func igzc (number wcT)	return

bool rEM[66.39,38.59,83.73] <- DoR
func tDB (string vf[75.38,15.83,68.29], number duC, bool Fa)	return
func YkZ (number Na, bool xJ[99.68,42.66])
	begin
		KkG()
	end
'''
		expect = '''Program([FuncDecl(Id(igzc), [VarDecl(Id(wcT), NumberType, None, None)], Return()), VarDecl(Id(rEM), ArrayType([66.39, 38.59, 83.73], BoolType), None, Id(DoR)), FuncDecl(Id(tDB), [VarDecl(Id(vf), ArrayType([75.38, 15.83, 68.29], StringType), None, None), VarDecl(Id(duC), NumberType, None, None), VarDecl(Id(Fa), BoolType, None, None)], Return()), FuncDecl(Id(YkZ), [VarDecl(Id(Na), NumberType, None, None), VarDecl(Id(xJ), ArrayType([99.68, 42.66], BoolType), None, None)], Block([CallStmt(Id(KkG), [])]))])'''
		self.assertTrue(TestAST.test(input, expect, 335))

	def test_336(self):
		input = '''
dynamic e0l <- ta
'''
		expect = '''Program([VarDecl(Id(e0l), None, dynamic, Id(ta))])'''
		self.assertTrue(TestAST.test(input, expect, 336))

	def test_337(self):
		input = '''
number dTkl[38.73,79.92] <- 9.15
'''
		expect = '''Program([VarDecl(Id(dTkl), ArrayType([38.73, 79.92], NumberType), None, NumLit(9.15))])'''
		self.assertTrue(TestAST.test(input, expect, 337))

	def test_338(self):
		input = '''
func yR ()
	begin
	end
number jrt[97.26,14.99]
number prp7[96.46] <- true
number TP[24.91,76.83] <- x8vd
'''
		expect = '''Program([FuncDecl(Id(yR), [], Block([])), VarDecl(Id(jrt), ArrayType([97.26, 14.99], NumberType), None, None), VarDecl(Id(prp7), ArrayType([96.46], NumberType), None, BooleanLit(True)), VarDecl(Id(TP), ArrayType([24.91, 76.83], NumberType), None, Id(x8vd))])'''
		self.assertTrue(TestAST.test(input, expect, 338))

	def test_339(self):
		input = '''
func zoa3 (string Xy, number SU[69.52,63.11,21.39], bool W10U)
	return
func Nj (bool Upu[90.4,39.17,11.96], number ZHP3)	return il

'''
		expect = '''Program([FuncDecl(Id(zoa3), [VarDecl(Id(Xy), StringType, None, None), VarDecl(Id(SU), ArrayType([69.52, 63.11, 21.39], NumberType), None, None), VarDecl(Id(W10U), BoolType, None, None)], Return()), FuncDecl(Id(Nj), [VarDecl(Id(Upu), ArrayType([90.4, 39.17, 11.96], BoolType), None, None), VarDecl(Id(ZHP3), NumberType, None, None)], Return(Id(il)))])'''
		self.assertTrue(TestAST.test(input, expect, 339))

	def test_340(self):
		input = '''
func bvi ()	return "rv"
number dbpB[90.4,63.83,45.15]
string AK_
var tikv <- true
'''
		expect = '''Program([FuncDecl(Id(bvi), [], Return(StringLit(rv))), VarDecl(Id(dbpB), ArrayType([90.4, 63.83, 45.15], NumberType), None, None), VarDecl(Id(AK_), StringType, None, None), VarDecl(Id(tikv), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 340))

	def test_342(self):
		input = '''
func Hi1 ()
	begin
		ZBYz(77.87, PQvd)
		if (false)
		number AKTi[41.62,92.46,15.26]
		elif (false)
		break
		elif ("Rjk")
		for NDDx until "W" by true
			for m3h until 23.98 by "VRq"
				if ("p")
				break
				elif (8.48) jk[87.3, 97.29] <- 31.89
				elif (Tk)
				break
				elif (Sj) string yGpt[33.57,61.16]
				elif ("FvqTD")
				continue
				elif ("ZtO") return
		elif (94.69) break
		elif (47.57)
		bool Li <- "d"
		else continue
	end
string bR[14.38,3.96,17.44] <- "B"
func QNWl (string ex, string qWb[81.11,12.45,9.85], string doHA[42.64,93.22])
	begin
		v9jl[vTqH, 20.13] <- true
		break
	end

func lA (bool SLBY[44.41,99.65], number xk8, bool pf[56.07,48.49])	return 56.21
string J0m <- puy
'''
		expect = '''Program([FuncDecl(Id(Hi1), [], Block([CallStmt(Id(ZBYz), [NumLit(77.87), Id(PQvd)]), If((BooleanLit(False), VarDecl(Id(AKTi), ArrayType([41.62, 92.46, 15.26], NumberType), None, None)), [(BooleanLit(False), Break), (StringLit(Rjk), For(Id(NDDx), StringLit(W), BooleanLit(True), For(Id(m3h), NumLit(23.98), StringLit(VRq), If((StringLit(p), Break), [(NumLit(8.48), AssignStmt(ArrayCell(Id(jk), [NumLit(87.3), NumLit(97.29)]), NumLit(31.89))), (Id(Tk), Break), (Id(Sj), VarDecl(Id(yGpt), ArrayType([33.57, 61.16], StringType), None, None)), (StringLit(FvqTD), Continue), (StringLit(ZtO), Return()), (NumLit(94.69), Break), (NumLit(47.57), VarDecl(Id(Li), BoolType, None, StringLit(d)))], Continue))))], None)])), VarDecl(Id(bR), ArrayType([14.38, 3.96, 17.44], StringType), None, StringLit(B)), FuncDecl(Id(QNWl), [VarDecl(Id(ex), StringType, None, None), VarDecl(Id(qWb), ArrayType([81.11, 12.45, 9.85], StringType), None, None), VarDecl(Id(doHA), ArrayType([42.64, 93.22], StringType), None, None)], Block([AssignStmt(ArrayCell(Id(v9jl), [Id(vTqH), NumLit(20.13)]), BooleanLit(True)), Break])), FuncDecl(Id(lA), [VarDecl(Id(SLBY), ArrayType([44.41, 99.65], BoolType), None, None), VarDecl(Id(xk8), NumberType, None, None), VarDecl(Id(pf), ArrayType([56.07, 48.49], BoolType), None, None)], Return(NumLit(56.21))), VarDecl(Id(J0m), StringType, None, Id(puy))])'''
		self.assertTrue(TestAST.test(input, expect, 342))

	def test_343(self):
		input = '''
string hA[73.5]
'''
		expect = '''Program([VarDecl(Id(hA), ArrayType([73.5], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 343))

	def test_344(self):
		input = '''
var KS9 <- 59.9
string oSv
func HBh (string Nj85[27.55], string V7Lm, number SGdP[80.49,54.91])
	return
func dE7f (string FcDY[54.43], bool Say)
	return "X"
'''
		expect = '''Program([VarDecl(Id(KS9), None, var, NumLit(59.9)), VarDecl(Id(oSv), StringType, None, None), FuncDecl(Id(HBh), [VarDecl(Id(Nj85), ArrayType([27.55], StringType), None, None), VarDecl(Id(V7Lm), StringType, None, None), VarDecl(Id(SGdP), ArrayType([80.49, 54.91], NumberType), None, None)], Return()), FuncDecl(Id(dE7f), [VarDecl(Id(FcDY), ArrayType([54.43], StringType), None, None), VarDecl(Id(Say), BoolType, None, None)], Return(StringLit(X)))])'''
		self.assertTrue(TestAST.test(input, expect, 344))

	def test_345(self):
		input = '''
number l9[25.0,74.01]
var mXsD <- true
number PB[35.34,9.55,24.39] <- "U"
func YUB4 (string m32, bool UrJR[46.67,90.68])	return
dynamic FvJm <- 29.41
'''
		expect = '''Program([VarDecl(Id(l9), ArrayType([25.0, 74.01], NumberType), None, None), VarDecl(Id(mXsD), None, var, BooleanLit(True)), VarDecl(Id(PB), ArrayType([35.34, 9.55, 24.39], NumberType), None, StringLit(U)), FuncDecl(Id(YUB4), [VarDecl(Id(m32), StringType, None, None), VarDecl(Id(UrJR), ArrayType([46.67, 90.68], BoolType), None, None)], Return()), VarDecl(Id(FvJm), None, dynamic, NumLit(29.41))])'''
		self.assertTrue(TestAST.test(input, expect, 345))

	def test_346(self):
		input = '''
var dq <- "aJuZ"
func cser (string hJG[39.66], bool xO0[71.75,87.0], string XcK)	begin
	end
func Mm (number XyZ, string nTa[18.02], number wr[84.8])
	return 82.27

'''
		expect = '''Program([VarDecl(Id(dq), None, var, StringLit(aJuZ)), FuncDecl(Id(cser), [VarDecl(Id(hJG), ArrayType([39.66], StringType), None, None), VarDecl(Id(xO0), ArrayType([71.75, 87.0], BoolType), None, None), VarDecl(Id(XcK), StringType, None, None)], Block([])), FuncDecl(Id(Mm), [VarDecl(Id(XyZ), NumberType, None, None), VarDecl(Id(nTa), ArrayType([18.02], StringType), None, None), VarDecl(Id(wr), ArrayType([84.8], NumberType), None, None)], Return(NumLit(82.27)))])'''
		self.assertTrue(TestAST.test(input, expect, 346))

	def test_347(self):
		input = '''
func M4P ()	begin
	end

func xKqJ (number Lb0g, bool Uc[54.15], bool Pgm[5.12,12.37])	return false
func UcIy (number Ovs[50.1], string WA)
	return
'''
		expect = '''Program([FuncDecl(Id(M4P), [], Block([])), FuncDecl(Id(xKqJ), [VarDecl(Id(Lb0g), NumberType, None, None), VarDecl(Id(Uc), ArrayType([54.15], BoolType), None, None), VarDecl(Id(Pgm), ArrayType([5.12, 12.37], BoolType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(UcIy), [VarDecl(Id(Ovs), ArrayType([50.1], NumberType), None, None), VarDecl(Id(WA), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 347))

	def test_348(self):
		input = '''
dynamic oPD
number Pu[21.84,31.78,46.06]
func IHOP ()	return rFM
func H5N ()	begin
		if (wOr0)
		for olLX until gmz6 by false
			for DOu until 31.73 by "RRFl"
				pCd(false)
	end

func bw1K ()	return

'''
		expect = '''Program([VarDecl(Id(oPD), None, dynamic, None), VarDecl(Id(Pu), ArrayType([21.84, 31.78, 46.06], NumberType), None, None), FuncDecl(Id(IHOP), [], Return(Id(rFM))), FuncDecl(Id(H5N), [], Block([If((Id(wOr0), For(Id(olLX), Id(gmz6), BooleanLit(False), For(Id(DOu), NumLit(31.73), StringLit(RRFl), CallStmt(Id(pCd), [BooleanLit(False)])))), [], None)])), FuncDecl(Id(bw1K), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 348))

	def test_349(self):
		input = '''
func i9 (string a_V, string Z2kw)	return 42.13
'''
		expect = '''Program([FuncDecl(Id(i9), [VarDecl(Id(a_V), StringType, None, None), VarDecl(Id(Z2kw), StringType, None, None)], Return(NumLit(42.13)))])'''
		self.assertTrue(TestAST.test(input, expect, 349))

	def test_350(self):
		input = '''
func Yz (string P1)
	return

'''
		expect = '''Program([FuncDecl(Id(Yz), [VarDecl(Id(P1), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 350))

	def test_351(self):
		input = '''
func F9T (string EG[20.35,91.29,80.97], string Uy[94.11], string gQOY[31.96])
	return

number bHW_[87.04,7.13,2.2]
'''
		expect = '''Program([FuncDecl(Id(F9T), [VarDecl(Id(EG), ArrayType([20.35, 91.29, 80.97], StringType), None, None), VarDecl(Id(Uy), ArrayType([94.11], StringType), None, None), VarDecl(Id(gQOY), ArrayType([31.96], StringType), None, None)], Return()), VarDecl(Id(bHW_), ArrayType([87.04, 7.13, 2.2], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 351))

	def test_352(self):
		input = '''
func RCF ()
	begin
		for vr until "Lgmk" by 17.84
			begin
				for JyHs until "pzu" by AzkR
					for Vqae until 67.8 by 0.97
						break
			end
	end

func zi (bool Gc[73.48,14.11,53.22], bool RIP, bool Tcay)	return

'''
		expect = '''Program([FuncDecl(Id(RCF), [], Block([For(Id(vr), StringLit(Lgmk), NumLit(17.84), Block([For(Id(JyHs), StringLit(pzu), Id(AzkR), For(Id(Vqae), NumLit(67.8), NumLit(0.97), Break))]))])), FuncDecl(Id(zi), [VarDecl(Id(Gc), ArrayType([73.48, 14.11, 53.22], BoolType), None, None), VarDecl(Id(RIP), BoolType, None, None), VarDecl(Id(Tcay), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 352))

	def test_353(self):
		input = '''
string bW[69.23]
bool K5c9[6.36]
dynamic gu
'''
		expect = '''Program([VarDecl(Id(bW), ArrayType([69.23], StringType), None, None), VarDecl(Id(K5c9), ArrayType([6.36], BoolType), None, None), VarDecl(Id(gu), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 353))

	def test_354(self):
		input = '''
func cY (string qs)
	begin
		for KQ until 27.28 by "OftS"
			Q4M[true, false, yL] <- "RS"
	end
'''
		expect = '''Program([FuncDecl(Id(cY), [VarDecl(Id(qs), StringType, None, None)], Block([For(Id(KQ), NumLit(27.28), StringLit(OftS), AssignStmt(ArrayCell(Id(Q4M), [BooleanLit(True), BooleanLit(False), Id(yL)]), StringLit(RS)))]))])'''
		self.assertTrue(TestAST.test(input, expect, 354))

	def test_355(self):
		input = '''
number PS <- "d"
'''
		expect = '''Program([VarDecl(Id(PS), NumberType, None, StringLit(d))])'''
		self.assertTrue(TestAST.test(input, expect, 355))

	def test_356(self):
		input = '''
func kw17 ()	return
'''
		expect = '''Program([FuncDecl(Id(kw17), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 356))

	def test_358(self):
		input = '''
string GLn[47.82,68.78,58.6]
func gp (string v4D[32.85,43.78], string fPn[88.23,0.1,10.4], bool ivLt[57.23,24.54])
	return false
var ICQZ <- true
func N4 (bool CVOK[22.56,57.31,3.41], string O2[26.78,22.55,38.34], string C48l)
	return

func YbAe ()
	return uz
'''
		expect = '''Program([VarDecl(Id(GLn), ArrayType([47.82, 68.78, 58.6], StringType), None, None), FuncDecl(Id(gp), [VarDecl(Id(v4D), ArrayType([32.85, 43.78], StringType), None, None), VarDecl(Id(fPn), ArrayType([88.23, 0.1, 10.4], StringType), None, None), VarDecl(Id(ivLt), ArrayType([57.23, 24.54], BoolType), None, None)], Return(BooleanLit(False))), VarDecl(Id(ICQZ), None, var, BooleanLit(True)), FuncDecl(Id(N4), [VarDecl(Id(CVOK), ArrayType([22.56, 57.31, 3.41], BoolType), None, None), VarDecl(Id(O2), ArrayType([26.78, 22.55, 38.34], StringType), None, None), VarDecl(Id(C48l), StringType, None, None)], Return()), FuncDecl(Id(YbAe), [], Return(Id(uz)))])'''
		self.assertTrue(TestAST.test(input, expect, 358))

	def test_359(self):
		input = '''
bool Ka4Q
'''
		expect = '''Program([VarDecl(Id(Ka4Q), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 359))

	def test_360(self):
		input = '''
bool OAO
func X28 ()
	return
var qNfC <- false
func JHZ ()	begin
	end
func dDHq (bool YA, bool Vr[24.42,89.0,17.58], string JAad)
	begin
		return
		YGtB <- "fE"
		if (NEkJ) return false
		elif (true) continue
		elif (false) uKE <- 98.21
		elif ("P") continue
		elif (18.85)
		for Xa until 73.22 by 31.5
			var QUf <- "RO"
	end

'''
		expect = '''Program([VarDecl(Id(OAO), BoolType, None, None), FuncDecl(Id(X28), [], Return()), VarDecl(Id(qNfC), None, var, BooleanLit(False)), FuncDecl(Id(JHZ), [], Block([])), FuncDecl(Id(dDHq), [VarDecl(Id(YA), BoolType, None, None), VarDecl(Id(Vr), ArrayType([24.42, 89.0, 17.58], BoolType), None, None), VarDecl(Id(JAad), StringType, None, None)], Block([Return(), AssignStmt(Id(YGtB), StringLit(fE)), If((Id(NEkJ), Return(BooleanLit(False))), [(BooleanLit(True), Continue), (BooleanLit(False), AssignStmt(Id(uKE), NumLit(98.21))), (StringLit(P), Continue), (NumLit(18.85), For(Id(Xa), NumLit(73.22), NumLit(31.5), VarDecl(Id(QUf), None, var, StringLit(RO))))], None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 360))

	def test_361(self):
		input = '''
func EV (string z3A[16.09], string eE, number O2)
	return 19.04

number FF[53.94,66.84]
string Xm2[51.52,85.24,99.41]
func byRQ (bool zx)	begin
		Zjk9[PIe, false, false] <- true
		for Zaop until false by 40.37
			begin
				q6iA(true)
			end
	end

'''
		expect = '''Program([FuncDecl(Id(EV), [VarDecl(Id(z3A), ArrayType([16.09], StringType), None, None), VarDecl(Id(eE), StringType, None, None), VarDecl(Id(O2), NumberType, None, None)], Return(NumLit(19.04))), VarDecl(Id(FF), ArrayType([53.94, 66.84], NumberType), None, None), VarDecl(Id(Xm2), ArrayType([51.52, 85.24, 99.41], StringType), None, None), FuncDecl(Id(byRQ), [VarDecl(Id(zx), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(Zjk9), [Id(PIe), BooleanLit(False), BooleanLit(False)]), BooleanLit(True)), For(Id(Zaop), BooleanLit(False), NumLit(40.37), Block([CallStmt(Id(q6iA), [BooleanLit(True)])]))]))])'''
		self.assertTrue(TestAST.test(input, expect, 361))

	def test_362(self):
		input = '''
bool cM_h[3.39] <- LXiZ
'''
		expect = '''Program([VarDecl(Id(cM_h), ArrayType([3.39], BoolType), None, Id(LXiZ))])'''
		self.assertTrue(TestAST.test(input, expect, 362))

	def test_363(self):
		input = '''
string u3LN
func Ndiu (number Xe30[34.05], string Ttm, string C_4[71.98])
	return true

dynamic s_
func c0 (number myzg[90.03], bool Y8bC, string zo[93.25,74.11,36.21])	return

'''
		expect = '''Program([VarDecl(Id(u3LN), StringType, None, None), FuncDecl(Id(Ndiu), [VarDecl(Id(Xe30), ArrayType([34.05], NumberType), None, None), VarDecl(Id(Ttm), StringType, None, None), VarDecl(Id(C_4), ArrayType([71.98], StringType), None, None)], Return(BooleanLit(True))), VarDecl(Id(s_), None, dynamic, None), FuncDecl(Id(c0), [VarDecl(Id(myzg), ArrayType([90.03], NumberType), None, None), VarDecl(Id(Y8bC), BoolType, None, None), VarDecl(Id(zo), ArrayType([93.25, 74.11, 36.21], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 363))

	def test_364(self):
		input = '''
var Ydyf <- ubM6
'''
		expect = '''Program([VarDecl(Id(Ydyf), None, var, Id(ubM6))])'''
		self.assertTrue(TestAST.test(input, expect, 364))

	def test_365(self):
		input = '''
func r6f (bool OXw[47.26,95.07], string Sp[88.15], string spAb)	begin
		begin
			if (true) break
			elif (ebu) return diL1
			elif (GA)
			break
			elif (true) begin
				number VX2 <- "MVif"
				lQ(true, "mOTjl")
			end
			else if (36.04) begin
				return
			end
			elif (15.99)
			eg("Ed", true, "Ik")
			elif ("TXS")
			N3P()
			elif ("ySN")
			aOw <- 77.21
			elif (70.36) begin
				string jHb[15.35,73.58,22.28]
				begin
				end
				for NvT until 84.82 by false
					return q8Ov
			end
			elif (67.26) bJ <- UZNC
			return
			continue
		end
		for DQ until RnY6 by false
			for E_ until 82.33 by 64.04
				if (true) for OtaA until "wdm" by false
					number mu
				elif ("VPWMK") if (false) bool uKbn[25.97,35.66,74.84] <- "uXw"
				elif (53.37)
				break
				elif (false) begin
					YdC <- false
					zkoK("cO", 75.92, 92.37)
				end
				elif (4.04)
				begin
					for Wa until dp by 31.26
						for cH until 67.99 by 59.27
							ZGk <- "jfUeo"
				end
				elif (false)
				K3 <- false
				elif (XQ)
				LIvb <- "UDff"
				elif (true)
				if ("pc") return
				elif ("CqK")
				if (false)
				begin
				end
				elif ("cKV") string Cn[28.72]
				elif ("xxV")
				continue
				elif (33.31) continue
				elif (64.35)
				break
				elif (true)
				m7_(N7nc, xu0)
	end
number Xv[49.64,98.72]
number iZ7Q[47.93,37.36]
func OhW ()	return 43.57

'''
		expect = '''Program([FuncDecl(Id(r6f), [VarDecl(Id(OXw), ArrayType([47.26, 95.07], BoolType), None, None), VarDecl(Id(Sp), ArrayType([88.15], StringType), None, None), VarDecl(Id(spAb), StringType, None, None)], Block([Block([If((BooleanLit(True), Break), [(Id(ebu), Return(Id(diL1))), (Id(GA), Break), (BooleanLit(True), Block([VarDecl(Id(VX2), NumberType, None, StringLit(MVif)), CallStmt(Id(lQ), [BooleanLit(True), StringLit(mOTjl)])]))], If((NumLit(36.04), Block([Return()])), [(NumLit(15.99), CallStmt(Id(eg), [StringLit(Ed), BooleanLit(True), StringLit(Ik)])), (StringLit(TXS), CallStmt(Id(N3P), [])), (StringLit(ySN), AssignStmt(Id(aOw), NumLit(77.21))), (NumLit(70.36), Block([VarDecl(Id(jHb), ArrayType([15.35, 73.58, 22.28], StringType), None, None), Block([]), For(Id(NvT), NumLit(84.82), BooleanLit(False), Return(Id(q8Ov)))])), (NumLit(67.26), AssignStmt(Id(bJ), Id(UZNC)))], None)), Return(), Continue]), For(Id(DQ), Id(RnY6), BooleanLit(False), For(Id(E_), NumLit(82.33), NumLit(64.04), If((BooleanLit(True), For(Id(OtaA), StringLit(wdm), BooleanLit(False), VarDecl(Id(mu), NumberType, None, None))), [(StringLit(VPWMK), If((BooleanLit(False), VarDecl(Id(uKbn), ArrayType([25.97, 35.66, 74.84], BoolType), None, StringLit(uXw))), [(NumLit(53.37), Break), (BooleanLit(False), Block([AssignStmt(Id(YdC), BooleanLit(False)), CallStmt(Id(zkoK), [StringLit(cO), NumLit(75.92), NumLit(92.37)])])), (NumLit(4.04), Block([For(Id(Wa), Id(dp), NumLit(31.26), For(Id(cH), NumLit(67.99), NumLit(59.27), AssignStmt(Id(ZGk), StringLit(jfUeo))))])), (BooleanLit(False), AssignStmt(Id(K3), BooleanLit(False))), (Id(XQ), AssignStmt(Id(LIvb), StringLit(UDff))), (BooleanLit(True), If((StringLit(pc), Return()), [(StringLit(CqK), If((BooleanLit(False), Block([])), [(StringLit(cKV), VarDecl(Id(Cn), ArrayType([28.72], StringType), None, None)), (StringLit(xxV), Continue), (NumLit(33.31), Continue), (NumLit(64.35), Break), (BooleanLit(True), CallStmt(Id(m7_), [Id(N7nc), Id(xu0)]))], None))], None))], None))], None)))])), VarDecl(Id(Xv), ArrayType([49.64, 98.72], NumberType), None, None), VarDecl(Id(iZ7Q), ArrayType([47.93, 37.36], NumberType), None, None), FuncDecl(Id(OhW), [], Return(NumLit(43.57)))])'''
		self.assertTrue(TestAST.test(input, expect, 365))

	def test_366(self):
		input = '''
bool QE <- ZBM
var VSWM <- "VIxx"
string spM[24.09,7.2,87.64] <- V2
'''
		expect = '''Program([VarDecl(Id(QE), BoolType, None, Id(ZBM)), VarDecl(Id(VSWM), None, var, StringLit(VIxx)), VarDecl(Id(spM), ArrayType([24.09, 7.2, 87.64], StringType), None, Id(V2))])'''
		self.assertTrue(TestAST.test(input, expect, 366))

	def test_367(self):
		input = '''
var yC <- 5.45
bool hFx1[62.92,11.32,85.82]
bool ZVAh[66.58] <- 18.07
func B2N (string ctV)	return "ccMC"

'''
		expect = '''Program([VarDecl(Id(yC), None, var, NumLit(5.45)), VarDecl(Id(hFx1), ArrayType([62.92, 11.32, 85.82], BoolType), None, None), VarDecl(Id(ZVAh), ArrayType([66.58], BoolType), None, NumLit(18.07)), FuncDecl(Id(B2N), [VarDecl(Id(ctV), StringType, None, None)], Return(StringLit(ccMC)))])'''
		self.assertTrue(TestAST.test(input, expect, 367))

	def test_368(self):
		input = '''
func L5 (number Ep[78.45,55.56], string Mxh[60.35,64.92,70.65])	return
func CPeM (string cLng, string xAb, bool vitP[25.55,48.02])	return

bool Y7rM[93.32,72.18]
func hnU7 (number h9E7, number raG[26.85,53.12,90.75], bool pnhJ)
	return false

'''
		expect = '''Program([FuncDecl(Id(L5), [VarDecl(Id(Ep), ArrayType([78.45, 55.56], NumberType), None, None), VarDecl(Id(Mxh), ArrayType([60.35, 64.92, 70.65], StringType), None, None)], Return()), FuncDecl(Id(CPeM), [VarDecl(Id(cLng), StringType, None, None), VarDecl(Id(xAb), StringType, None, None), VarDecl(Id(vitP), ArrayType([25.55, 48.02], BoolType), None, None)], Return()), VarDecl(Id(Y7rM), ArrayType([93.32, 72.18], BoolType), None, None), FuncDecl(Id(hnU7), [VarDecl(Id(h9E7), NumberType, None, None), VarDecl(Id(raG), ArrayType([26.85, 53.12, 90.75], NumberType), None, None), VarDecl(Id(pnhJ), BoolType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 368))

	def test_369(self):
		input = '''
number bu[70.68] <- "jRvJ"
func w4Ji ()	return
string FUy <- "gq"
'''
		expect = '''Program([VarDecl(Id(bu), ArrayType([70.68], NumberType), None, StringLit(jRvJ)), FuncDecl(Id(w4Ji), [], Return()), VarDecl(Id(FUy), StringType, None, StringLit(gq))])'''
		self.assertTrue(TestAST.test(input, expect, 369))

	def test_370(self):
		input = '''
func C9 (string qQ, bool wZP[1.92,34.59])
	begin
	end

var tn <- false
func UL (bool CFqo, number PL)	return
string C_Y[53.06]
'''
		expect = '''Program([FuncDecl(Id(C9), [VarDecl(Id(qQ), StringType, None, None), VarDecl(Id(wZP), ArrayType([1.92, 34.59], BoolType), None, None)], Block([])), VarDecl(Id(tn), None, var, BooleanLit(False)), FuncDecl(Id(UL), [VarDecl(Id(CFqo), BoolType, None, None), VarDecl(Id(PL), NumberType, None, None)], Return()), VarDecl(Id(C_Y), ArrayType([53.06], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 370))

	def test_371(self):
		input = '''
var vAKN <- false
func Vd (string qfk, number sZn[98.34,53.3,54.7], number nrsn)	begin
		continue
	end
string nXmD
number zW[25.48] <- "m"
'''
		expect = '''Program([VarDecl(Id(vAKN), None, var, BooleanLit(False)), FuncDecl(Id(Vd), [VarDecl(Id(qfk), StringType, None, None), VarDecl(Id(sZn), ArrayType([98.34, 53.3, 54.7], NumberType), None, None), VarDecl(Id(nrsn), NumberType, None, None)], Block([Continue])), VarDecl(Id(nXmD), StringType, None, None), VarDecl(Id(zW), ArrayType([25.48], NumberType), None, StringLit(m))])'''
		self.assertTrue(TestAST.test(input, expect, 371))

	def test_372(self):
		input = '''
func yHCc (bool QGgC[50.18,61.75], number EMwK)	begin
		number zmc[26.97,30.34,66.13] <- "AOnC"
		begin
			continue
			dx[false, "zfJg"] <- 80.71
		end
	end
var u24x <- Pl
func Rof (bool u25Y[70.46,76.84,15.42])
	begin
	end
string d8Ag[79.03] <- true
number um85[98.73]
'''
		expect = '''Program([FuncDecl(Id(yHCc), [VarDecl(Id(QGgC), ArrayType([50.18, 61.75], BoolType), None, None), VarDecl(Id(EMwK), NumberType, None, None)], Block([VarDecl(Id(zmc), ArrayType([26.97, 30.34, 66.13], NumberType), None, StringLit(AOnC)), Block([Continue, AssignStmt(ArrayCell(Id(dx), [BooleanLit(False), StringLit(zfJg)]), NumLit(80.71))])])), VarDecl(Id(u24x), None, var, Id(Pl)), FuncDecl(Id(Rof), [VarDecl(Id(u25Y), ArrayType([70.46, 76.84, 15.42], BoolType), None, None)], Block([])), VarDecl(Id(d8Ag), ArrayType([79.03], StringType), None, BooleanLit(True)), VarDecl(Id(um85), ArrayType([98.73], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 372))

	def test_373(self):
		input = '''
string bySU[61.46,14.78,45.95]
func Xk1L (bool As, bool gmI)
	return 55.79
func YaR8 ()
	return

func Jxd0 (string w4[95.96,94.76])	return 14.18
'''
		expect = '''Program([VarDecl(Id(bySU), ArrayType([61.46, 14.78, 45.95], StringType), None, None), FuncDecl(Id(Xk1L), [VarDecl(Id(As), BoolType, None, None), VarDecl(Id(gmI), BoolType, None, None)], Return(NumLit(55.79))), FuncDecl(Id(YaR8), [], Return()), FuncDecl(Id(Jxd0), [VarDecl(Id(w4), ArrayType([95.96, 94.76], StringType), None, None)], Return(NumLit(14.18)))])'''
		self.assertTrue(TestAST.test(input, expect, 373))

	def test_374(self):
		input = '''
bool TQP[39.96,67.19] <- false
string Xg[47.79,52.34] <- false
func QTH0 (bool Iz[6.98,62.68,62.84], number r56)
	return

func v30z (bool l1[31.88], bool bxP, string epWT)	return
bool jG[96.48,91.12,28.45] <- true
'''
		expect = '''Program([VarDecl(Id(TQP), ArrayType([39.96, 67.19], BoolType), None, BooleanLit(False)), VarDecl(Id(Xg), ArrayType([47.79, 52.34], StringType), None, BooleanLit(False)), FuncDecl(Id(QTH0), [VarDecl(Id(Iz), ArrayType([6.98, 62.68, 62.84], BoolType), None, None), VarDecl(Id(r56), NumberType, None, None)], Return()), FuncDecl(Id(v30z), [VarDecl(Id(l1), ArrayType([31.88], BoolType), None, None), VarDecl(Id(bxP), BoolType, None, None), VarDecl(Id(epWT), StringType, None, None)], Return()), VarDecl(Id(jG), ArrayType([96.48, 91.12, 28.45], BoolType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 374))

	def test_375(self):
		input = '''
func wZ (number HV[34.8])	return

func Xp7 (bool fg[27.29,86.58,28.9])	begin
	end
func qr (bool TSXg, number PzIx[10.85,93.5], string l0S)
	begin
		jl("xQKx", Ta)
	end

func UeB ()
	begin
		hTfp[28.42, omuB] <- false
	end
'''
		expect = '''Program([FuncDecl(Id(wZ), [VarDecl(Id(HV), ArrayType([34.8], NumberType), None, None)], Return()), FuncDecl(Id(Xp7), [VarDecl(Id(fg), ArrayType([27.29, 86.58, 28.9], BoolType), None, None)], Block([])), FuncDecl(Id(qr), [VarDecl(Id(TSXg), BoolType, None, None), VarDecl(Id(PzIx), ArrayType([10.85, 93.5], NumberType), None, None), VarDecl(Id(l0S), StringType, None, None)], Block([CallStmt(Id(jl), [StringLit(xQKx), Id(Ta)])])), FuncDecl(Id(UeB), [], Block([AssignStmt(ArrayCell(Id(hTfp), [NumLit(28.42), Id(omuB)]), BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 375))

	def test_376(self):
		input = '''
var woM <- "QKPMm"
func xlU (string D5[13.38,86.77], string hd4r)
	return
func ib7 (string eoQQ, bool t1[75.76,99.94,41.6], string xriT[1.8])
	return
number u9s[74.88,43.37,18.13] <- "P"
func fZV ()
	return "lctOX"
'''
		expect = '''Program([VarDecl(Id(woM), None, var, StringLit(QKPMm)), FuncDecl(Id(xlU), [VarDecl(Id(D5), ArrayType([13.38, 86.77], StringType), None, None), VarDecl(Id(hd4r), StringType, None, None)], Return()), FuncDecl(Id(ib7), [VarDecl(Id(eoQQ), StringType, None, None), VarDecl(Id(t1), ArrayType([75.76, 99.94, 41.6], BoolType), None, None), VarDecl(Id(xriT), ArrayType([1.8], StringType), None, None)], Return()), VarDecl(Id(u9s), ArrayType([74.88, 43.37, 18.13], NumberType), None, StringLit(P)), FuncDecl(Id(fZV), [], Return(StringLit(lctOX)))])'''
		self.assertTrue(TestAST.test(input, expect, 376))

	def test_377(self):
		input = '''
number cZm[19.41,41.02] <- "TtADD"
'''
		expect = '''Program([VarDecl(Id(cZm), ArrayType([19.41, 41.02], NumberType), None, StringLit(TtADD))])'''
		self.assertTrue(TestAST.test(input, expect, 377))

	def test_378(self):
		input = '''
func lK (bool uFG_[64.63,71.06])	return
func JTq (bool Heun)
	return

bool g0m[2.71] <- 81.15
func FrH (number EOP8, bool x0Lf[2.96,68.37])
	begin
		return
		return wZU
	end
'''
		expect = '''Program([FuncDecl(Id(lK), [VarDecl(Id(uFG_), ArrayType([64.63, 71.06], BoolType), None, None)], Return()), FuncDecl(Id(JTq), [VarDecl(Id(Heun), BoolType, None, None)], Return()), VarDecl(Id(g0m), ArrayType([2.71], BoolType), None, NumLit(81.15)), FuncDecl(Id(FrH), [VarDecl(Id(EOP8), NumberType, None, None), VarDecl(Id(x0Lf), ArrayType([2.96, 68.37], BoolType), None, None)], Block([Return(), Return(Id(wZU))]))])'''
		self.assertTrue(TestAST.test(input, expect, 378))

	def test_379(self):
		input = '''
string Al[40.87,23.7]
func BquZ ()
	return true

bool r5[70.65,2.49] <- "giSG"
'''
		expect = '''Program([VarDecl(Id(Al), ArrayType([40.87, 23.7], StringType), None, None), FuncDecl(Id(BquZ), [], Return(BooleanLit(True))), VarDecl(Id(r5), ArrayType([70.65, 2.49], BoolType), None, StringLit(giSG))])'''
		self.assertTrue(TestAST.test(input, expect, 379))

	def test_380(self):
		input = '''
bool Qh[60.56,44.96]
func LHtb (number mc[85.05,43.38,53.94], bool fO[73.43])	begin
		uMN(17.51)
		if (false)
		continue
		elif (73.88)
		return false
	end

'''
		expect = '''Program([VarDecl(Id(Qh), ArrayType([60.56, 44.96], BoolType), None, None), FuncDecl(Id(LHtb), [VarDecl(Id(mc), ArrayType([85.05, 43.38, 53.94], NumberType), None, None), VarDecl(Id(fO), ArrayType([73.43], BoolType), None, None)], Block([CallStmt(Id(uMN), [NumLit(17.51)]), If((BooleanLit(False), Continue), [(NumLit(73.88), Return(BooleanLit(False)))], None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 380))

	def test_381(self):
		input = '''
number BR0t[63.24,97.73] <- true
func wXuS (number YY, bool wr3o[26.64], number ut0B[52.94,45.04,65.32])
	begin
		continue
		return 40.92
	end

number xosh[30.48,81.13]
number cobj[35.86,6.45]
'''
		expect = '''Program([VarDecl(Id(BR0t), ArrayType([63.24, 97.73], NumberType), None, BooleanLit(True)), FuncDecl(Id(wXuS), [VarDecl(Id(YY), NumberType, None, None), VarDecl(Id(wr3o), ArrayType([26.64], BoolType), None, None), VarDecl(Id(ut0B), ArrayType([52.94, 45.04, 65.32], NumberType), None, None)], Block([Continue, Return(NumLit(40.92))])), VarDecl(Id(xosh), ArrayType([30.48, 81.13], NumberType), None, None), VarDecl(Id(cobj), ArrayType([35.86, 6.45], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 381))

	def test_382(self):
		input = '''
func aL91 (bool Zt, bool GzMF, bool ZrQd)
	return
func ct (bool MO8[67.4,21.34], number zipZ[86.47], string dN[60.54,66.03])	return

func UO (number w4[69.28,44.9,14.56], string UcF[38.73], number I0[59.25,11.37])	return "l"
'''
		expect = '''Program([FuncDecl(Id(aL91), [VarDecl(Id(Zt), BoolType, None, None), VarDecl(Id(GzMF), BoolType, None, None), VarDecl(Id(ZrQd), BoolType, None, None)], Return()), FuncDecl(Id(ct), [VarDecl(Id(MO8), ArrayType([67.4, 21.34], BoolType), None, None), VarDecl(Id(zipZ), ArrayType([86.47], NumberType), None, None), VarDecl(Id(dN), ArrayType([60.54, 66.03], StringType), None, None)], Return()), FuncDecl(Id(UO), [VarDecl(Id(w4), ArrayType([69.28, 44.9, 14.56], NumberType), None, None), VarDecl(Id(UcF), ArrayType([38.73], StringType), None, None), VarDecl(Id(I0), ArrayType([59.25, 11.37], NumberType), None, None)], Return(StringLit(l)))])'''
		self.assertTrue(TestAST.test(input, expect, 382))

	def test_383(self):
		input = '''
bool Vx
bool FL5C[72.24,83.53,11.9] <- 71.69
'''
		expect = '''Program([VarDecl(Id(Vx), BoolType, None, None), VarDecl(Id(FL5C), ArrayType([72.24, 83.53, 11.9], BoolType), None, NumLit(71.69))])'''
		self.assertTrue(TestAST.test(input, expect, 383))

	def test_385(self):
		input = '''
func RBA4 (number Xa5g)	return

'''
		expect = '''Program([FuncDecl(Id(RBA4), [VarDecl(Id(Xa5g), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 385))

	def test_386(self):
		input = '''
number Rgl7 <- "ZY"
func fsS (string pR)
	return

'''
		expect = '''Program([VarDecl(Id(Rgl7), NumberType, None, StringLit(ZY)), FuncDecl(Id(fsS), [VarDecl(Id(pR), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 386))

	def test_387(self):
		input = '''
func ztIJ (bool BcUb, string YrU[10.35])	return oM

'''
		expect = '''Program([FuncDecl(Id(ztIJ), [VarDecl(Id(BcUb), BoolType, None, None), VarDecl(Id(YrU), ArrayType([10.35], StringType), None, None)], Return(Id(oM)))])'''
		self.assertTrue(TestAST.test(input, expect, 387))

	def test_388(self):
		input = '''
func GLf0 (number Xd, number f0Tt[83.85])
	return "X"

func pFVm ()	return true

'''
		expect = '''Program([FuncDecl(Id(GLf0), [VarDecl(Id(Xd), NumberType, None, None), VarDecl(Id(f0Tt), ArrayType([83.85], NumberType), None, None)], Return(StringLit(X))), FuncDecl(Id(pFVm), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 388))

	def test_389(self):
		input = '''
string HNqP <- UN
func lO (bool bs)
	return "C"

'''
		expect = '''Program([VarDecl(Id(HNqP), StringType, None, Id(UN)), FuncDecl(Id(lO), [VarDecl(Id(bs), BoolType, None, None)], Return(StringLit(C)))])'''
		self.assertTrue(TestAST.test(input, expect, 389))

	def test_390(self):
		input = '''
func TeR ()	return Qfw

func Q7i (string Dsm, bool GznL)	begin
		break
		break
	end
func lqXB ()
	begin
		return
		continue
		s1q[61.14, "Mhc"] <- "PZmj"
	end
'''
		expect = '''Program([FuncDecl(Id(TeR), [], Return(Id(Qfw))), FuncDecl(Id(Q7i), [VarDecl(Id(Dsm), StringType, None, None), VarDecl(Id(GznL), BoolType, None, None)], Block([Break, Break])), FuncDecl(Id(lqXB), [], Block([Return(), Continue, AssignStmt(ArrayCell(Id(s1q), [NumLit(61.14), StringLit(Mhc)]), StringLit(PZmj))]))])'''
		self.assertTrue(TestAST.test(input, expect, 390))

	def test_391(self):
		input = '''
func Y1E1 ()
	return

func MH8 (number uW, string i0)	return "fGxy"

string iZ[27.31,45.5,81.9] <- true
func Xa7 (bool Pv, string Qyp[76.11,22.46,46.26], string e7MN[24.59,97.35])	return false

func CwTk ()
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(Y1E1), [], Return()), FuncDecl(Id(MH8), [VarDecl(Id(uW), NumberType, None, None), VarDecl(Id(i0), StringType, None, None)], Return(StringLit(fGxy))), VarDecl(Id(iZ), ArrayType([27.31, 45.5, 81.9], StringType), None, BooleanLit(True)), FuncDecl(Id(Xa7), [VarDecl(Id(Pv), BoolType, None, None), VarDecl(Id(Qyp), ArrayType([76.11, 22.46, 46.26], StringType), None, None), VarDecl(Id(e7MN), ArrayType([24.59, 97.35], StringType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(CwTk), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 391))

	def test_392(self):
		input = '''
number DZm[6.24]
dynamic ui
var ZNBL <- jt
number etY <- 23.41
var S5 <- OJwm
'''
		expect = '''Program([VarDecl(Id(DZm), ArrayType([6.24], NumberType), None, None), VarDecl(Id(ui), None, dynamic, None), VarDecl(Id(ZNBL), None, var, Id(jt)), VarDecl(Id(etY), NumberType, None, NumLit(23.41)), VarDecl(Id(S5), None, var, Id(OJwm))])'''
		self.assertTrue(TestAST.test(input, expect, 392))

	def test_393(self):
		input = '''
func W3t ()	return "MfRAo"
'''
		expect = '''Program([FuncDecl(Id(W3t), [], Return(StringLit(MfRAo)))])'''
		self.assertTrue(TestAST.test(input, expect, 393))

	def test_394(self):
		input = '''
string pEya
bool A9ye
'''
		expect = '''Program([VarDecl(Id(pEya), StringType, None, None), VarDecl(Id(A9ye), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 394))

	def test_395(self):
		input = '''
number PN
'''
		expect = '''Program([VarDecl(Id(PN), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 395))

	def test_396(self):
		input = '''
string hwJ[49.79] <- Ib_
'''
		expect = '''Program([VarDecl(Id(hwJ), ArrayType([49.79], StringType), None, Id(Ib_))])'''
		self.assertTrue(TestAST.test(input, expect, 396))

	def test_397(self):
		input = '''
func JjDD (bool qs[8.99,40.75,39.82], string uG)
	return false

func xq ()
	return 91.3
'''
		expect = '''Program([FuncDecl(Id(JjDD), [VarDecl(Id(qs), ArrayType([8.99, 40.75, 39.82], BoolType), None, None), VarDecl(Id(uG), StringType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(xq), [], Return(NumLit(91.3)))])'''
		self.assertTrue(TestAST.test(input, expect, 397))

	def test_398(self):
		input = '''
func s8 (number G8u[67.82], string KQi[36.72,15.99])
	begin
		lDO("bENV", "PKI")
		if (haD) begin
			return "MR"
		end
		elif (43.43)
		continue
		elif (40.53)
		u3Eb("xxtu", true)
		return
	end
number aT6[96.9]
bool rx <- "yErnE"
func hRK (bool cXnd)
	return false
'''
		expect = '''Program([FuncDecl(Id(s8), [VarDecl(Id(G8u), ArrayType([67.82], NumberType), None, None), VarDecl(Id(KQi), ArrayType([36.72, 15.99], StringType), None, None)], Block([CallStmt(Id(lDO), [StringLit(bENV), StringLit(PKI)]), If((Id(haD), Block([Return(StringLit(MR))])), [(NumLit(43.43), Continue), (NumLit(40.53), CallStmt(Id(u3Eb), [StringLit(xxtu), BooleanLit(True)]))], None), Return()])), VarDecl(Id(aT6), ArrayType([96.9], NumberType), None, None), VarDecl(Id(rx), BoolType, None, StringLit(yErnE)), FuncDecl(Id(hRK), [VarDecl(Id(cXnd), BoolType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 398))

	def test_399(self):
		input = '''
number nI0c
'''
		expect = '''Program([VarDecl(Id(nI0c), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 399))

	def test_400(self):
		input = '''
func Son (string qL[51.73,81.1,23.74], string rblK[61.71,14.0,79.34])
	return

func eu6 ()
	return

number WI[79.03,24.91]
'''
		expect = '''Program([FuncDecl(Id(Son), [VarDecl(Id(qL), ArrayType([51.73, 81.1, 23.74], StringType), None, None), VarDecl(Id(rblK), ArrayType([61.71, 14.0, 79.34], StringType), None, None)], Return()), FuncDecl(Id(eu6), [], Return()), VarDecl(Id(WI), ArrayType([79.03, 24.91], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 400))

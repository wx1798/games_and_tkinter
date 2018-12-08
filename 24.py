import random
import itertools
class Solve24:
    ''' 用于计算24点游戏，并且实现自动计算'''

    # 初始化函数
    def __init__(self, numList = [8, 8, 4, 8]):
        if type(numList) == list and len(numList) == 4:
            self.numList = numList
            print('指定计算数字', self.numList, '\n')
        else:
            self.numList = numList
            print('指定数字计算', self.numList, '\n')
        # numList=[]
        # for _ in range(4):
        #    numList.append(random.randint(1,13))
        # print(numList)
        self.numList = [random.randint(1, 13) for _ in range(4)]
        # print(numList)
        self.nlist = []
        [self.nlist.append(n) for n in list(itertools.permutations(self.numList)) if n not in self.nlist]
        self.operate = ['+', '-', '*', '/']
        self.operateList = list(itertools.product(self.operate, repeat=3))


        # print(nlist)
    def Sovle(self):
        '''计算24点游戏，拼凑4个数字歌三个运算符'''
        # 第一种情况（a+b)+(c+d)
        solveList0 = ['('+str(n[0])+m[0]+str(n[1])+')'+m[1]+'('+str(n[2])+m[2]+str(n[3])+')'\
                              for n in self.nlist for m in self.operateList]
        solveList1 = ['('*2+str(n[0])+m[0]+str(n[1])+')'+m[1]+str(n[2])+')'+m[2]+str(n[3]) \
                      for n in self.nlist for m in self.operateList]
        solveList2 = ['('+str(n[0]) + m[0] + '(' + str(n[1]) + m[1] + str(n[2]) + ')'+')'+m[2]  + str(n[3]) \
                      for n in self.nlist for m in self.operateList]
        solveList3 = [str(n[0]) + m[0]+'('+'(' + str(n[1]) + m[1] + str(n[2]) + ')' + m[2] + str(n[3]) +')'\
                      for n in self.nlist for m in self.operateList]
        solveList4 = [str(n[0]) + m[0] + '(' + str(n[1]) + m[1]+'(' + str(n[2]) + m[2] + str(n[3])+')'+')' \
                      for n in self.nlist for m in self.operateList]
        allSolves = [solveList0, solveList1, solveList2, solveList3, solveList4]
        count = False
        for n in allSolves:
            for m in n:
                if eval(m) == 24:
                    count = True
                    print(m+'=24')
        if count == False:
            print('失败')
if __name__ == '__main__':

   solve24 = Solve24()
   solve24.Sovle()

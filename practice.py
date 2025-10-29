# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # lt = [1, 2, 3, 4, 5, True]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("-".join(map(str, lt)))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(lt[-2]) # Accessing the second last element

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(lt[5])


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # lol = [('易大師','我的劍，就是你的劍。'),('犽宿','死亡如風，常伴吾身。'),('阿祈爾','蘇瑞瑪！你的王已經歸來了！')]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # diclol = dict(lol)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(diclol['犽宿'])  # Output: 死亡如風，常伴吾身。

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # diclol.update({'阿祈爾':'吾乃沙漠之王，風暴將至！'})

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(diclol)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # st1 = {'A', 'C', 'E'}
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # st2 = {'B', 'C', 'A', 'D'}
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(st1 & st2)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(st1 | st2)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(st2 | st1)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(st2 - st1) # st2.difference(st1)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # shrimp = dict()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # shrimp['炸鳳尾蝦'] = '核果 油'
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # shrimp['雲龍炸蝦'] = '核果 醬汁 豆皮'

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # lee = set(shrimp.get('炸鳳尾蝦').split())
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # liu = set(shrimp.get('雲龍炸蝦').split())
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(liu & lee)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # lt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # lt1 = lt[0::2]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # lt2 = lt[1::2]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(lt[1::2])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # lt1.extend(lt2)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # new_list = lt1 + lt2
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # new_list.sort()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(new_list)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # shrimp = {'炸鳳尾蝦':['蝦子','核果','油'],'雲龍炸蝦':['蝦子','核果','油','豆皮','醬汁']}
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for name, ingre in shrimp.items():
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #   print(name, ingre)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(shrimp.items())


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # range(7)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(list(range(7)))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print([2 * i for i in range(9) if i % 2 == 0])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print([0 for i in range(3)])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print([[0, 0, 0] for j in range(4)])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print([[0 for i in range(3)] for j in range(4)])


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # def area(radius, pi=3.14159):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #     if pi != 3.14159:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #         pi = 3.14
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #     return pi * radius**2


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(area(5, 3.14))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # fak = 'global'
# # # # # # # # # # # # # # # # # # # # # # # # # # # # def home3():
# # # # # # # # # # # # # # # # # # # # # # # # # # # #     global fak  # 告訴Python現在要用的就是全域的那個fak
# # # # # # # # # # # # # # # # # # # # # # # # # # # #     fak = "h3"
# # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(fak)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # print("Before home3:")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print(fak)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # home3()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print("After home3:")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print(fak)


# # # # # # # # # # # # # # # # # # # # # # # # # # # evens = list(range(2, 11, 2))
# # # # # # # # # # # # # # # # # # # # # # # # # # # products = list()
# # # # # # # # # # # # # # # # # # # # # # # # # # # print(range(2, 11, 2))

# # # # # # # # # # # # # # # # # # # # # # # # # # # for a in evens:
# # # # # # # # # # # # # # # # # # # # # # # # # # #     for b in evens:
# # # # # # # # # # # # # # # # # # # # # # # # # # #         products.append(a * b)
# # # # # # # # # # # # # # # # # # # # # # # # # # # print(products)

# # # # # # # # # # # # # # # # # # # # # # # # # # # products2 = [a * b for a in evens for b in evens]
# # # # # # # # # # # # # # # # # # # # # # # # # # # products3 = [a for a in evens]
# # # # # # # # # # # # # # # # # # # # # # # # # # # print(products3)


# # # # # # # # # # # # # # # # # # # # # # # # # # def cal(end=100):
# # # # # # # # # # # # # # # # # # # # # # # # # #     res = 0
# # # # # # # # # # # # # # # # # # # # # # # # # #     for i in range(1, end + 1):
# # # # # # # # # # # # # # # # # # # # # # # # # #         res += i
# # # # # # # # # # # # # # # # # # # # # # # # # #     return res
# # # # # # # # # # # # # # # # # # # # # # # # # # print(cal())

# # # # # # # # # # # # # # # # # # # # # # # # # # import sys
# # # # # # # # # # # # # # # # # # # # # # # # # # print(sys.getrecursionlimit())


# # # # # # # # # # # # # # # # # # # # # # # # # def cs(n, dic):
# # # # # # # # # # # # # # # # # # # # # # # # #     if n in dic:
# # # # # # # # # # # # # # # # # # # # # # # # #         return dic[n]
# # # # # # # # # # # # # # # # # # # # # # # # #     dic[n] = cs(n-1, dic) + cs(n-2, dic)
# # # # # # # # # # # # # # # # # # # # # # # # #     return dic[n]


# # # # # # # # # # # # # # # # # # # # # # # # # dic = {1: 1, 2: 2}
# # # # # # # # # # # # # # # # # # # # # # # # # # print(cs(5, dic))
# # # # # # # # # # # # # # # # # # # # # # # # # for i in range(1, 101):
# # # # # # # # # # # # # # # # # # # # # # # # # 	print(cs(i, dic))


# # # # # # # # # # # # # # # # # # # # # # # # from utils import check, schedule  # 透過套件的模式來匯入

# # # # # # # # # # # # # # # # # # # # # # # # print("Check a lucky number: ", check.getLucky())
# # # # # # # # # # # # # # # # # # # # # # # # print("Check daily routine: ", schedule.get())


# # # # # # # # # # # # # # # # # # # # # # # from random import randint

# # # # # # # # # # # # # # # # # # # # # # # ans, guess = randint(1, 100), 0
# # # # # # # # # # # # # # # # # # # # # # # l, r = 1, 100
# # # # # # # # # # # # # # # # # # # # # # # print(ans)
# # # # # # # # # # # # # # # # # # # # # # # while ans != guess:
# # # # # # # # # # # # # # # # # # # # # # #     try:
# # # # # # # # # # # # # # # # # # # # # # #         guess = int(input("\n請在" + str(l) + "到" + str(r) + "之間猜一個數:"))
# # # # # # # # # # # # # # # # # # # # # # #     except:  # 加入continue，直接跳過後面的範圍處理，回到迴圈的開頭
# # # # # # # # # # # # # # # # # # # # # # #         print("請輸入正常的數字，不要加其他字母或符號呦！")
# # # # # # # # # # # # # # # # # # # # # # #         continue
# # # # # # # # # # # # # # # # # # # # # # #     if (
# # # # # # # # # # # # # # # # # # # # # # #         guess < l or guess > r
# # # # # # # # # # # # # # # # # # # # # # #     ):  # 超出範圍的部分同樣也要跳過(當然，也可以用elif和下面的判斷連起來)
# # # # # # # # # # # # # # # # # # # # # # #         print("請輸入正確範圍內的數字！")
# # # # # # # # # # # # # # # # # # # # # # #         continue
# # # # # # # # # # # # # # # # # # # # # # #     if guess < ans:
# # # # # # # # # # # # # # # # # # # # # # #         print("您猜的數字比答案還要小，請再猜大一點~")
# # # # # # # # # # # # # # # # # # # # # # #         l = guess + 1
# # # # # # # # # # # # # # # # # # # # # # #     elif guess > ans:
# # # # # # # # # # # # # # # # # # # # # # #         print("您猜的數字比答案還要大，請再猜小一點~")
# # # # # # # # # # # # # # # # # # # # # # #         r = guess - 1
# # # # # # # # # # # # # # # # # # # # # # # print("恭喜你猜出答案啦！")


# # # # # # # # # # # # # # # # # # # # # # # python
# # # # # # # # # # # # # # # # # # # # # # from random import SystemRandom
# # # # # # # # # # # # # # # # # # # # # # x = SystemRandom().uniform(1, 100)

# # # # # # # # # # # # # # # # # # # # # # print(x)


# # # # # # # # # # # # # # # # # # # # # from collections import defaultdict

# # # # # # # # # # # # # # # # # # # # # cnt = defaultdict(lambda: 12)
# # # # # # # # # # # # # # # # # # # # # cnt["a"] = 1
# # # # # # # # # # # # # # # # # # # # # print(cnt["b"])


# # # # # # # # # # # # # # # # # # # # from collections import OrderedDict
# # # # # # # # # # # # # # # # # # # # scores = OrderedDict(
# # # # # # # # # # # # # # # # # # # #   [('James', 80), ('Alice', 95), ('Bob', 78)]
# # # # # # # # # # # # # # # # # # # # )

# # # # # # # # # # # # # # # # # # # # print(scores)

# # # # # # # # # # # # # # # # # # # # for s in scores:
# # # # # # # # # # # # # # # # # # # #     print(s, scores[s])


# # # # # # # # # # # # # # # # # # # from collections import deque
# # # # # # # # # # # # # # # # # # # s = 'abcde'
# # # # # # # # # # # # # # # # # # # print(deque(s))


# # # # # # # # # # # # # # # # # # class Student():
# # # # # # # # # # # # # # # # # #     def __init__(self, name):
# # # # # # # # # # # # # # # # # #         self.name = name
# # # # # # # # # # # # # # # # # #     def readName(self):
# # # # # # # # # # # # # # # # # #         print('Student name is:', self.name)

# # # # # # # # # # # # # # # # # # ming = Student('Simon')
# # # # # # # # # # # # # # # # # # ming.readName()
# # # # # # # # # # # # # # # # # # # mei = Student()

# # # # # # # # # # # # # # # # # # print(ming)


# # # # # # # # # # # # # # # # # class Score:
# # # # # # # # # # # # # # # # #     def __init__(self, name, scores=None):
# # # # # # # # # # # # # # # # #         self.name = name
# # # # # # # # # # # # # # # # #         # default subjects (未輸入則視為缺考 0 分)
# # # # # # # # # # # # # # # # #         subjects = ["數學", "英文", "物理"]
# # # # # # # # # # # # # # # # #         self.score = {sub: 0 for sub in subjects}
# # # # # # # # # # # # # # # # #         if scores:
# # # # # # # # # # # # # # # # #             for subj, val in scores.items():
# # # # # # # # # # # # # # # # #                 # 若提供非預設科目，也一併儲存
# # # # # # # # # # # # # # # # #                 self.score[subj] = val

# # # # # # # # # # # # # # # # #     def __repr__(self):
# # # # # # # # # # # # # # # # #         return f"Score(name={self.name!r}, score={self.score})"


# # # # # # # # # # # # # # # # # # 產生阿明及小美並帶入成績
# # # # # # # # # # # # # # # # # aming = Score("阿明", {"數學": 55, "英文": 70, "物理": 55})
# # # # # # # # # # # # # # # # # meimei = Score("小美", {"數學": 90, "英文": 88, "物理": 100})

# # # # # # # # # # # # # # # # # print(aming)
# # # # # # # # # # # # # # # # # print(meimei)


# # # # # # # # # # # # # # # # class Car:
# # # # # # # # # # # # # # # #     def __init__(self, name):
# # # # # # # # # # # # # # # #         self.name = name

# # # # # # # # # # # # # # # #     def whoAmI(self):
# # # # # # # # # # # # # # # #         print("I am a car, my name is", self.name)


# # # # # # # # # # # # # # # # class Tesla(Car):
# # # # # # # # # # # # # # # #     def __init__(self, name, mode):
# # # # # # # # # # # # # # # #         super().__init__(name)
# # # # # # # # # # # # # # # #         self.pilotMode = mode

# # # # # # # # # # # # # # # #     def whoAmI(self):
# # # # # # # # # # # # # # # #         super().whoAmI()
# # # # # # # # # # # # # # # #         print("Also, I am a Tesla")
# # # # # # # # # # # # # # # #         print("Auto-pilot mode: " + str(self.pilotMode))

# # # # # # # # # # # # # # # #     def autopilot_switch(self):
# # # # # # # # # # # # # # # #         self.pilotMode ^= 1
# # # # # # # # # # # # # # # #         if self.pilotMode == 0:
# # # # # # # # # # # # # # # #             print("Auto-pilot mode switch off!\n")
# # # # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # # # #             print("Auto-pilot mode switch on!\n")

# # # # # # # # # # # # # # # # car = Car('CC')
# # # # # # # # # # # # # # # # tla = Tesla('TT', 0)
# # # # # # # # # # # # # # # # car.whoAmI()
# # # # # # # # # # # # # # # # print()
# # # # # # # # # # # # # # # # tla.whoAmI()
# # # # # # # # # # # # # # # # tla.autopilot_switch()
# # # # # # # # # # # # # # # # tla.whoAmI()
# # # # # # # # # # # # # # # # tla.autopilot_switch()


# # # # # # # # # # # # # # # class Student:
# # # # # # # # # # # # # # #     cnt = 0

# # # # # # # # # # # # # # #     def __init__(self, name, score):
# # # # # # # # # # # # # # #         Student.cnt += 1
# # # # # # # # # # # # # # #         self.name = name
# # # # # # # # # # # # # # #         self.score = score

# # # # # # # # # # # # # # #     def readMyName(self):
# # # # # # # # # # # # # # #         print("My name is" + self.name)

# # # # # # # # # # # # # # #     def compare(self, b):
# # # # # # # # # # # # # # #         diff = sum(self.score.value()) - sum(b.score.value())

# # # # # # # # # # # # # # #         if diff > 0:
# # # # # # # # # # # # # # #             print(self.name + "贏了！")
# # # # # # # # # # # # # # #         elif diff == 0:
# # # # # # # # # # # # # # #             print("什麼？竟然平手？！")
# # # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # # #             print("可...可惡，難道，這就是" + b.name + "真正的實力嗎？")

# # # # # # # # # # # # # # #     def getCount(cls):
# # # # # # # # # # # # # # #         print("目前的學生總數：%d" % cls.cnt)  # 別忘了print也可以用format類型的形式

# # # # # # # # # # # # # # #     def getCount(cls):
# # # # # # # # # # # # # # #         print("目前的學生x總x數：%d" % cls.cnt)  # 別忘了print也可以用format類型的形式


# # # # # # # # # # # # # # # Student.getCount(23)
# # # # # # # # # # # # # # # ming = Student("阿明", {"數學": 55, "英文": 70, "物理": 55})
# # # # # # # # # # # # # # # ming.readMyName()
# # # # # # # # # # # # # # # Student.getCount()


# # # # # # # # # # # # # # class Student:
# # # # # # # # # # # # # #     cp_cnt = 0  # 這個變數是屬於整個Student類別的

# # # # # # # # # # # # # #     def __init__(self, name, score):
# # # # # # # # # # # # # #         self.name = name
# # # # # # # # # # # # # #         self.score = score

# # # # # # # # # # # # # #     def __eq__(self, b):
# # # # # # # # # # # # # #         # 為了方便讀者檢查是否有問題
# # # # # # # # # # # # # #         print(
# # # # # # # # # # # # # #             "self = %d, b = %d"
# # # # # # # # # # # # # #             % (
# # # # # # # # # # # # # #                 self.score["數學"] * 2 + self.score["英文"] * 5,
# # # # # # # # # # # # # #                 b.score["數學"] * 2 + b.score["英文"] * 5,
# # # # # # # # # # # # # #             )
# # # # # # # # # # # # # #         )
# # # # # # # # # # # # # #         return (
# # # # # # # # # # # # # #             self.score["數學"] * 2 + self.score["英文"] * 5
# # # # # # # # # # # # # #             == b.score["數學"] * 2 + b.score["英文"] * 5
# # # # # # # # # # # # # #         )

# # # # # # # # # # # # # #     def __gt__(self, b):
# # # # # # # # # # # # # #         return (
# # # # # # # # # # # # # #             self.score["數學"] * 2 + self.score["英文"] * 5
# # # # # # # # # # # # # #             > b.score["數學"] * 2 + b.score["英文"] * 5
# # # # # # # # # # # # # #         )

# # # # # # # # # # # # # #     def readMyName(self):
# # # # # # # # # # # # # #         print("聽清楚了，我的名字是" + self.name + "!!!")

# # # # # # # # # # # # # #     def compare(self, b):
# # # # # # # # # # # # # #         Student.cp_cnt += 1
# # # # # # # # # # # # # #         # 同樣，印出diff方便檢查正確性，讀者可自行註解掉。
# # # # # # # # # # # # # #         diff = sum(self.score.values()) - sum(b.score.values())
# # # # # # # # # # # # # #         print("diff = %d" % diff)
# # # # # # # # # # # # # #         # 有冒號的式子如果底下程式碼只有一行，也可以選擇直接和判斷式寫成同一行
# # # # # # # # # # # # # #         if diff > 0:
# # # # # # # # # # # # # #             print(self.name + "贏了！")
# # # # # # # # # # # # # #         elif diff == 0:
# # # # # # # # # # # # # #             print("什麼？竟然平手？！")
# # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # #             print("可...可惡，難道，這就是" + b.name + "真正的實力嗎？")
# # # # # # # # # # # # # #         print("已比較 %d 次!\n" % Student.cp_cnt)

# # # # # # # # # # # # # #     def compareE(self, b):
# # # # # # # # # # # # # #         Student.cp_cnt += 1
# # # # # # # # # # # # # #         if self > b:
# # # # # # # # # # # # # #             print(self.name + " >  " + b.name)
# # # # # # # # # # # # # #         elif self == b:
# # # # # # # # # # # # # #             print(self.name + " == " + b.name)
# # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # #             print(self.name + " <  " + b.name)
# # # # # # # # # # # # # #         print("已比較 %d 次!\n" % Student.cp_cnt)

# # # # # # # # # # # # # #     @classmethod
# # # # # # # # # # # # # #     def getCpCount(cls):
# # # # # # # # # # # # # #         print("目前的比較次數：%d" % cls.cp_cnt)  # 別忘了print也可以用format類型的形式


# # # # # # # # # # # # # # print("開始之前")
# # # # # # # # # # # # # # Student.getCpCount()  # 開始前先看看是不是0

# # # # # # # # # # # # # # ming = Student("阿明", {"數學": 55, "英文": 70, "物理": 55})
# # # # # # # # # # # # # # ming.readMyName()
# # # # # # # # # # # # # # mei = Student("小美", {"數學": 90, "英文": 88, "物理": 100})
# # # # # # # # # # # # # # mei.readMyName()
# # # # # # # # # # # # # # howhow = Student("HowHow", {"數學": 80, "英文": 60, "物理": 40})
# # # # # # # # # # # # # # howhow.readMyName()

# # # # # # # # # # # # # # print("\n來PK吧! 先比總分，再比加權分!\n")
# # # # # # # # # # # # # # ming.compare(howhow)
# # # # # # # # # # # # # # ming.compareE(howhow)
# # # # # # # # # # # # # # ming.compare(mei)
# # # # # # # # # # # # # # ming.compareE(mei)
# # # # # # # # # # # # # # mei.compare(howhow)
# # # # # # # # # # # # # # mei.compareE(howhow)


# # # # # # # # # # # # # f = open('poem.txt', 'w')
# # # # # # # # # # # # # f.write('院子落葉\n跟我的思念厚厚一疊')
# # # # # # # # # # # # # f.close()

# # # # # # # # # # # # # 'r' -> 讀取(read)
# # # # # # # # # # # # # 'w' -> 寫入(write)(但不給r預設還是會可讀)
# # # # # # # # # # # # # 'x' -> 新增檔案(exclusive creation)，如果檔案已存在則回傳錯誤
# # # # # # # # # # # # # 'a' -> 在結尾處寫入(append)

# # # # # # # # # # # # try:
# # # # # # # # # # # #     f = open("poem.txt", "x")
# # # # # # # # # # # #     f.write("窗外的麻雀")
# # # # # # # # # # # # except FileExistsError:  # 想直接全包也行啦XD!
# # # # # # # # # # # #     print("檔案已存在!")

# # # # # # # # # # # # f = open("poem.txt", "r")
# # # # # # # # # # # # content = ""

# # # # # # # # # # # # while True:
# # # # # # # # # # # #     next = f.read(3)  # 每次讀三個字元
# # # # # # # # # # # #     if not next:
# # # # # # # # # # # #         break
# # # # # # # # # # # #     content += next

# # # # # # # # # # # # f.close()

# # # # # # # # # # # # print(content)


# # # # # # # # # # # import csv

# # # # # # # # # # # # 寫進去
# # # # # # # # # # # with open("students.csv", "w", newline="", encoding="utf-8-sig") as f:
# # # # # # # # # # #     csvw = csv.writer(f, delimiter=" ")
# # # # # # # # # # #     csvw.writerow(["姓名", "數學", "英文", "物理"])

# # # # # # # # # # #     students = [["阿明", 60, 70, 55], ["小美", 90, 88, 100], ["HowHow", 80, 60, 40]]
# # # # # # # # # # #     csvw.writerows(students)


# # # # # # # # # # # with open("students.csv", "r", encoding="utf-8-sig") as f_read:
# # # # # # # # # # #     csvr = csv.reader(f_read, delimiter=" ")
# # # # # # # # # # #     students_from_file = [row for row in csvr]

# # # # # # # # # # # print(students_from_file)


# # # # # # # # # # import csv

# # # # # # # # # # with open("students_dic.csv", "w", newline="", encoding="utf-8-sig") as f:
# # # # # # # # # #     field = ["姓名", "數學", "英文", "物理"]
# # # # # # # # # #     csvw = csv.DictWriter(f, delimiter=",", fieldnames=field)
# # # # # # # # # #     csvw.writeheader()
# # # # # # # # # #     csvw.writerow({"姓名": "阿明", "數學": 55, "英文": 70, "物理": 55})
# # # # # # # # # #     csvw.writerow({"姓名": "小美", "數學": 90, "英文": 88, "物理": 100})
# # # # # # # # # #     csvw.writerow({"姓名": "HowHow", "數學": 80, "英文": 60, "物理": 40})


# # # # # # # # # # with open("students_dic.csv", "r", encoding="utf-8-sig") as f:
# # # # # # # # # #     csvr = csv.DictReader(f, delimiter=",")
# # # # # # # # # #     student = [row for row in csvr]
# # # # # # # # # #     print(student)


# # # # # # # # # how_school = {
# # # # # # # # #     "校長": "How哥",
# # # # # # # # #     "工友": "林阿嘉",
# # # # # # # # #     "class": {
# # # # # # # # #         "A": {
# # # # # # # # #             "teacher": "蔡阿嘎",
# # # # # # # # #             "students": {
# # # # # # # # #                 "阿明": {"數學": 55, "英文": 70, "物理": 55},
# # # # # # # # #                 "HowHow": {"數學": 80, "英文": 60, "物理": 40},
# # # # # # # # #             },
# # # # # # # # #         },
# # # # # # # # #         "B": {
# # # # # # # # #             "teacher": "二伯",
# # # # # # # # #             "students": {
# # # # # # # # #                 "小美": {"數學": 90, "英文": 88, "物理": 100},
# # # # # # # # #                 "蔡哥": {"數學": 50, "英文": 50, "物理": 40},
# # # # # # # # #             },
# # # # # # # # #         },
# # # # # # # # #     },
# # # # # # # # # }

# # # # # # # # # import json

# # # # # # # # # # how_school_json = json.dumps(how_school, ensure_ascii=False)
# # # # # # # # # # how_school_json_loads = json.loads(how_school_json)
# # # # # # # # # # classA = how_school_json_loads["class"]["A"]
# # # # # # # # # # 直接取出 A 班資料（不需要先 dumps 再 loads）
# # # # # # # # # classA = how_school["class"]["A"]

# # # # # # # # # # 寫入 classA.json（包含中文，並排版）
# # # # # # # # # with open("classA.json", "w", encoding="utf-8") as f:
# # # # # # # # #     json.dump(classA, f, ensure_ascii=False)

# # # # # # # # # # 若要把整個 class（包含 A 與 B）寫入 class.json，請這樣：
# # # # # # # # # with open("class.json", "w", encoding="utf-8") as f:
# # # # # # # # #     json.dump(how_school["class"], f, ensure_ascii=False ,indent=2)

# # # # # # # # # # 讀回示範（指定 encoding）
# # # # # # # # # with open("classA.json", "r", encoding="utf-8") as f:
# # # # # # # # #     reclassA = json.load(f)

# # # # # # # # # print(reclassA)


# # # # # # # # import os, shutil
# # # # # # # # # print("目前工作目錄：", os.getcwd())
# # # # # # # # # print(os.path.isdir("practice.py"))

# # # # # # # # # shutil.copy("practice.py", "practice_copy.py")

# # # # # # # # for root, dirs, files in os.walk('.'):
# # # # # # # #   print("目前目錄路徑：", root)
# # # # # # # #   print("目前目錄下的子目錄：", dirs)


# # # # # # # from datetime import date

# # # # # # # doubleten = date(2024, 10, 10)
# # # # # # # today = date.today()
# # # # # # # days_left = (doubleten - today).days
# # # # # # # # print(f"距離雙十節還有 {days_left} 天")
# # # # # # # print(today)

# # # # # # from datetime import time

# # # # # # now = time()
# # # # # # now.isoformat()
# # # # # # now = time(0, 0, 0, 38)
# # # # # # now = time(12, 30, 45)
# # # # # # print(now.strftime("%H-%M-%S"))


# # # # # from datetime import date

# # # # # today = date.today()
# # # # # anniversary = date(2024, 8, 23)
# # # # # days_left = (today - anniversary).days
# # # # # print(days_left)


# # # # import time
# # # # # print(time.localtime())
# # # # # print(time.ctime())
# # # # print(time.time())
# # # # print(time.sleep(10))
# # # # print(time.time())


# # # from datetime import date, datetime, time, timedelta

# # # now = date(2025, 10, 27)
# # # mem = [
# # #     date(2021, 8, 14),
# # #     date(2021, 2, 14),
# # #     date(2021, 3, 14),
# # #     date(2020, 10, 3),
# # #     date(2021, 11, 3),
# # # ]
# # # diff = sorted([d - now for d in mem])
# # # print(diff)


# # import timeit


# # def f():
# #     import os

# #     for path, dirs, files in os.walk("."):
# #         print(path)
# #         for f in files:
# #             print(os.path.join(path, f))
# #         for d in dirs:
# #             print(os.path.join(path, d))


# # print(timeit.timeit(f, number=5))


# import timeit, functools


# def cs1(n):
#     if n == 1 or n == 2:
#         return n
#     return cs1(n - 1) + cs1(n - 2)


# def cs2(n, dic):
#     if n in dic:
#         return dic[n]

#     dic[n] = cs2(n - 1, dic) + cs2(n - 2, dic)
#     return dic[n]


# @functools.lru_cache(maxsize=None)
# def cs3(n):
#     if n == 1 or n == 2:
#         return n
#     return cs3(n - 1) + cs3(n - 2)


# print(timeit.timeit("print(cs1(35))", globals=globals(), number=10))
# print()
# print(
#     timeit.timeit(
#         "print(cs2(35, dic))",
#         setup="dic = {1 : 1, 2 : 2}",
#         globals=globals(),
#         number=10,
#     )
# )
# print()
# print(
#     timeit.timeit(
#         "print(cs3(35))", setup="import functools", globals=globals(), number=10
#     )
# )


# from PIL import Image, ImageDraw, ImageFont

# img = Image.open("flower.jpg")
# backup_img = img.copy()

# draw = ImageDraw.Draw(img)
# # font = ImageFont.truetype("arial.ttf", 36)
# text = "Hello, World!"
# draw.text((960, 320), text, fill=(255, 0, 0))
# img.show()

from PIL import Image, ImageDraw, ImageFont

# 如果要用空白畫布來繪製，可以用Image.new("RGB", (400,300))的形式建立。
img = Image.open("flower.jpg")
# copy可以用來複製一個Image物件，先備份一下，不行就拿它來蓋掉img
backup_img = img.copy()
backup_img.show()
# 建立一個Draw物件，接下來draw所有的操作都會影響到img上面。
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("./msjhbd.ttc", 100)  # 給定字型及大小
text = "霹靂卡霹靂拉拉 波波力那貝貝魯多"
draw.text((960, 320), text, font=font)  # 好像太大了?
img.show()
font = ImageFont.truetype("./msjhbd.ttc", 50)  # 改一下大小
draw.text((960, 320), text, font=font)  # 再畫一次(應該會重複)
img.show()
img = backup_img.copy()  # 洗掉吧！
draw = ImageDraw.Draw(img)  # 蓋回來會影響到draw跟img的連結，所以要重置
draw.ink = 0xFF0000  # 我們可以更改要使用的顏色(0x代表16進位)
draw.text((960, 320), text, font=font)
img.show()  # 看起來應該是藍色
# 也可以使用fill參數代入，順序是RGBA，也就是紅、綠、藍、透明度(alpha)
draw.text((1060, 960), "認同請分享", font=font, fill=(255, 0, 0, 128))
img.show()
# 正式來囉！關於顏色的選擇可以使用如htmlcolorcodes等網站來取得色碼
img = backup_img.copy()
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("./msjhbd.ttc", 60)
draw.ink = 0xF39C12
# draw.text()可以多行
text = "請常唸\n\n　　霹靂卡霹靂拉拉\n　　波波力那貝貝魯多\n\n唸時\n須心無雜念 專注 便可心想事成"
draw.text((1000, 300), text, font=font)
font = ImageFont.truetype("./msjhbd.ttc", 70)
draw.text((1520, 960), "認同請分享", font=font, fill=(165, 105, 189, 0))
img.show()
img.save("elder.jpg")  # 送給長輩吧XD！

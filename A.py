










exit()


print("L", end='')


# 入力！ 型！
a = int(input())
b = input()
b2 = int(b)
a, b = map(int, input().split())
a,b=(int(x) for x in input().split())
a, b = input().split()

#n個の入力
n = int(input())

# ?個の入力 
numbers = list(map(int, input().split()))

# 文字列を連結して出力
print("L"+"o"*n+"ng")

# 改行しないで出力
print("L", end='')
print("o"*n, end='')

# 配列をスペース区切りで出力
print(*arr)



# 間違い
ANS = [[0]*m]*n
# 正しい
ANS = [[0]*m for _ in range(n)]



# 配列をプリント
print(numbers[1])

# 空の配列
arr = []

#DPテーブル(0 で初期化)
dp = [ [0 for i in range(W+1)] for j in range(n+1)]

# 配列を同じ文字で埋める        これは「参照してしまう」！！
array = ["."*w] * h
# 正解は　↓
array = [["."]*w for _ in range(h)]
# こっちの ↓ 方が良い
y_arr=[0]*n

# 1, 2, 3, 4, 5・・・
x_arr=list(range(1, n+1))
# 7, 6, 5, 4, 3, 2, 1
x_arr=list(range(n, 0, -1))

# insertは遅い！！！　　appendにしよう！

# 配列を改行区切りで出力
print('\n'.join(array))

# ソートして、新しい配列を作る
a_arr2 = sorted(a_arr)

# 辞書(連想配列)で高速化
index_dict = {num: i+1 for i, num in enumerate(numbers)}


# 空の dict を使う
from collections import defaultdict
# dict の中身を set にするとき
AB = defaultdict(set)
# dict の中身を int にするとき
AB = defaultdict(int)



# if文
if abs(a2 - b2) == 1:
    print("Yes")
    exit()

if abs(a2 - b2) == 9:
    print("Yes")
    exit()

print("No")



for i in range(3):
    print(i)


for i in range(n - 1):
    next_index = index_dict[search_number]
    arr.append(next_index)
    search_number = next_index


for i in range(30):
    if(n%2==1):
        break
    else:
        n=n/2
        answer += 1




# ソートする！！
X, A = map(list, zip(*sorted(zip(X, A))))



再帰が 1000 を超えるとき
import sys
sys.setrecursionlimit(10**7)
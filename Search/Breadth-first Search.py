'''
# 廣度優先搜尋法(Breadth-First Search, BFS): 
    1. 為解決最短路徑問題(Shortest-Path Problem)的演算法
    2. 為一種圖形演算法
    3. 搜尋範圍由起點向外呈放射性發展
    4. 先搜尋所有一等連接, 再搜尋二等連接 ...
    5. 必須按照加入清單的順序搜尋, 此種資料結構稱為: 佇列(Queue)
## 圖形:
    1. 由節點和邊組成
    2. 一個節點可連接其他許多節點,稱相鄰節點(Neighbor)
    3. 有向圖(Directed Graph): 兩節點只有單向關係
       無向圖(Undirected Graph): 兩節點互為相鄰節點
## 佇列(Queue):
    1. FIFO(First-In-Fist-Out)資料結構
    2. 新增(Enqueue)和刪除(Dequeue)兩個操作
## Python用雙向佇列(deque)撰寫, 支援四種操作:
    1. push():把元素加入deque最前端
    2. inject():把元素加入deque最後端
    3. pop():把deque最前端元素移除
    4. eject():把deque最後端元素移除
## 拓撲排序(Topological sort):
    任務A取決於任務B, 任務A列在任務B後面 (任務B完成了才有任務A)

'''
from collections import deque
# 搜尋芒果經銷商
# 建立搜尋圖形
graph = {}
graph["me"] = ["alice","bob","claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name):
    return name[-1] == 'm'    # 名子為m結尾的為True(芒果經銷商)

def search(name):
    search_queue = deque()    # 建立新的雙向佇列
    search_queue += graph[name]    # 把"name"的所有相鄰節點加入佇列
    searched = []
    while search_queue:    # 只要佇列不為空
        #print(search_queue)
        person = search_queue.popleft()    # 移除佇列的第一個人
        #print(person)
        if not person in searched:
            if person_is_seller(person):
                print(person+" is a mango seller!")    # 為芒果經銷商
                return True
            else:
                search_queue += graph[person]    # 若非芒果經銷商, 將此人的所有朋友加入搜尋佇列
                searched.append(person)
    return False

search("me")
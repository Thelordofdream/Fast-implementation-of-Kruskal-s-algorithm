# coding=utf-8
from math import sqrt
import matplotlib.pyplot as plt


def kruskal(edge, vertex, draw):
    length = get_length(edge, vertex)
    n = len(edge)  # 边数量
    num_Of_edge = [i for i in range(n)]  # 生成边的编号,以便在大规模数据情况下,从外部可以获取最小生成树的边集

    quick_sort(0, len(length) - 1, length, edge, num_Of_edge)  # 用快速排序根据边长对edge排序,直接更改edge了顺序

    m = len(vertex)  # 节点个数
    tree_Of_vertex = [i for i in range(m)]  # 对所有节点依次编号,即已经产生了映射关系,同时不同编号表示属于不同的树
    mst = []  # 声明空的最小生成树边集
    num_mst = []  # 声明空的最小生成树内边的编号集
    i = 0
    while len(mst) < m - 1:
        if tree_Of_vertex[edge[i][0]] != tree_Of_vertex[edge[i][1]]:  # 是否在两个端点同一棵树
            mst.append(edge[i])  # 加入生成树集合
            num_mst.append(num_Of_edge[i])
            temp1 = tree_Of_vertex[edge[i][0]]
            temp2 = tree_Of_vertex[edge[i][1]]
            for j in range(m):
                if tree_Of_vertex[j] == temp1:
                    tree_Of_vertex[j] = temp2  # 将之前两棵树的所有节点标记成同一棵树,拥有共同的编号

        i += 1
    print mst
    print num_mst
    if draw == 1:
        draw_map(vertex, edge, mst, map)


def quick_sort(left, right, temp, edge, num_Of_edge):
    if left >= right:
        return
    k = temp[right]
    ke = edge[right]
    kn = num_Of_edge[right]
    i = left
    j = right
    while i < j:
        while i < j and k >= temp[i]:
            i += 1
        temp[j] = temp[i]
        edge[j] = edge[i]
        num_Of_edge[j] = num_Of_edge[i]
        while i < j and k <= temp[j]:
            j -= 1
        temp[i] = temp[j]
        edge[i] = edge[j]
        num_Of_edge[i] = num_Of_edge[j]
    temp[j] = k
    edge[j] = ke
    num_Of_edge[j] = kn
    quick_sort(left, i - 1, temp, edge, num_Of_edge)
    quick_sort(i + 1, right, temp, edge, num_Of_edge)


def get_length(edge, vertex):
    length = []
    for each in edge:
        length.append(
            sqrt(pow(vertex[each[0]][0] - vertex[each[1]][0], 2) + pow(vertex[each[0]][1] - vertex[each[1]][1], 2)))
    return length


def draw_map(vertex, edge, mst, map):
    x = [i[0] for i in vertex]
    y = [i[1] for i in vertex]
    x_min = min(x)
    x_max = max(x)
    y_min = min(y)
    y_max = max(y)

    plt.figure(1)
    for each in edge:
        plt.plot([vertex[each[0]][0], vertex[each[1]][0]], [vertex[each[0]][1], vertex[each[1]][1]], marker='o')
    plt.xlim([x_min - 1, x_max + 1])
    plt.ylim([y_min - 1, y_max + 1])

    plt.figure(2)
    for each in mst:
        plt.plot([vertex[each[0]][0], vertex[each[1]][0]], [vertex[each[0]][1], vertex[each[1]][1]], marker='o')
    plt.xlim([x_min - 1, x_max + 1])
    plt.ylim([y_min - 1, y_max + 1])
    plt.show()

#Example1:
edge = [[0, 1], [1, 3], [3, 4], [1, 2], [2, 5], [2, 3], [4, 5], [0, 7], [7, 5], [0, 6], [6, 5], [6, 7]]  # 以端点编号确定的边
vertex = [[0, 0], [2, 0], [2, 3], [3, 0], [3, 4], [2, 5], [0, 5], [1, 2]]  # 按编号排序的点的坐标
map = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
kruskal(edge, vertex, 1)  # 0/1表示是否需要画图

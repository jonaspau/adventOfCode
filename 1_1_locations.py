def sortList(list):
    list_sorted = sorted(list)
    return list_sorted


def getLists():
    list1 = []
    list2 = []
    
    with open("1_1_input.txt", "r") as f:
        for line in f:
            num1, num2 = map(int, line.split())
            list1.append(num1)
            list2.append(num2)
    return list1, list2


def getDiff(l1, l2):
    diff = 0

    for i in range(len(l1)):
        diff_i = abs(l1[i] - l2[i])
        diff = diff + diff_i

    print(f"1: Total diff between lists: {diff}")

def getSimilars(l1, l2):
    similars = {}

    for num in l1:
        count = l2.count(num)
        similars[num] = count

    similarity = 0

    for num, count in similars.items():
        if count != 0:
            sim = num * count
            similarity = similarity + sim
    
    print(f"Similarity score: {similarity}")


def main():
    list1, list2 = getLists()

    l1_sorted = sortList(list1)
    l2_sorted = sortList(list2)

    getDiff(l1_sorted, l2_sorted)

    getSimilars(l1_sorted, l2_sorted)

    


main()
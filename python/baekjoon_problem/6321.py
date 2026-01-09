# 백준 6321 IBM 빼기 1
alphabet = {
    "A": "B", "B": "C", "C": "D", "D": "E", "E": "F",
    "F": "G", "G": "H", "H": "I", "I": "J", "J": "K",
    "K": "L", "L": "M", "M": "N", "N": "O", "O": "P",
    "P": "Q", "Q": "R", "R": "S", "S": "T", "T": "U",
    "U": "V", "V": "W", "W": "X", "X": "Y", "Y": "Z",
    "Z": "A"
}

T = int(input())

for tc in range(1, T+1):
    string = input()
    result = ""
    for word in string:
        result += alphabet[word]

    print(f"String #{tc}")
    print(result)
    
    # tc 사이에 빈 줄 추가
    if tc == T:
        continue
    else:
        print("")
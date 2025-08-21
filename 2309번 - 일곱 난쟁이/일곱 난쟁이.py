#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2309                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ktd562 <boj.kr/u/ktd562>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2309                           #+#        #+#      #+#     #
#    Solved: 2025/08/21 16:49:47 by ktd562        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from itertools import combinations
import sys
input = sys.stdin.readline
heights = []

for _ in range(9):
    num = int(input())
    heights.append(num)

candidates = list(combinations(heights, 7))

for i in range(len(candidates)):
    if sum(candidates[i]) == 100:
        result = candidates[i]

for i in range(7):
    print(sorted(result)[i])
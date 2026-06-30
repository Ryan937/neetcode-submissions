from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)

        for i in range(len(edges)):
            u, v = edges[i]
            p = succProb[i]

            graph[u].append((v, p))
            graph[v].append((u, p))

        best = [0] * n
        best[start] = 1

        heap = [(-1, start)]

        while heap:
            prob, node = heapq.heappop(heap)
            prob = -prob

            if prob < best[node]:
                continue

            if node == end:
                return prob

            for neighbor, edgeProb in graph[node]:
                newProb = prob * edgeProb

                if newProb > best[neighbor]:
                    best[neighbor] = newProb
                    heapq.heappush(heap, (-newProb, neighbor))

        return 0
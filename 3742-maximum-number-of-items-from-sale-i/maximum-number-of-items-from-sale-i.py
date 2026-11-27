class Solution:

  def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
    n = len(items)
    bonus = [0] * n

    for i in range(n):
      fi = items[i][0]
      cnt = 0
      for j in range(n):
        if i != j and items[j][0] % fi == 0:
          cnt += 1
      bonus[i] = cnt

    # dp1[b] = max copies from buying the FIRST copy of a subset of items with cost b
    NEG_INF = -(10**9)
    dp1 = [NEG_INF] * (budget + 1)
    dp1[0] = 0

    for i in range(n):
      _, price = items[i]
      gain = 1 + bonus[i]
      if price <= budget:
        for b in range(budget, price - 1, -1):
          if dp1[b - price] != NEG_INF:
            dp1[b] = max(dp1[b], dp1[b - price] + gain)

    min_price = min(price for _, price in items)

    ans = 0
    for b in range(budget + 1):
      if dp1[b] != NEG_INF:
        extra_copies = (budget - b) // min_price
        ans = max(ans, dp1[b] + extra_copies)

    return ans
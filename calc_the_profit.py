def profit(info):
    profit = round((info["sell_price"] - info["cost_price"]) * info["inventory"])
  
    return profit

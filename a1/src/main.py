# A1

import const
import json

def main():
  file = open(const.DATA_PATH + "sunshine.json")
  json_data = json.load(file)["data"]

  print(json_data.keys())

  # for data in 

# get the x contiguous months with most sun 
def _kadane(data, count=const.SUMMER_LEN):
  max_total = 0

  cur_start = 0
  cur_total = 0

  while cur_start + count <= len(data):
    cur_total = sum(data[cur_start : cur_start + count])
    if cur_total > max_total:
      max_start = cur_start
      max_total = cur_total

  return max_total, max_start

if __name__ == "__main__":
  main()

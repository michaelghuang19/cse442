# A1

import const
import json
import matplotlib.pyplot as plt
import numpy as np

def main():
  file = open(const.DATA_PATH + 'sunshine.json')
  json_data = json.load(file)['data']

  n = len(json_data['city'])
  data = {}

  for i in range(n):
    city = json_data['city'][i]
    sunshine = json_data['sunshine'][i]

    if city not in data.keys():
      data[city] = []

    data[city].append(sunshine)

  max_data = {}

  for key in data.keys():
    max_data[key], _ = _kadane(data[key])

  avg_data = [(sum(data[city]) / len(data[city])) for city in data.keys()]
  summer_ratio = [(1.0 * max_data[city] / sum(data[city])) for city in data.keys()]

  plt.scatter(avg_data, summer_ratio)
  z = np.polyfit(avg_data, summer_ratio, 1)
  p = np.poly1d(z)
  plt.plot(avg_data, p(avg_data), 'r-')

  plt.xlabel('Average Sunny Hours Per Month')
  plt.ylabel('Proportion of Sunny Hours in Summer Months')
  plt.title('Sunny Hours Per Month vs Proportion of Sun in Summer Months')
  plt.tight_layout()

  plt.savefig(const.RESULTS_PATH + 'mhuang19_a1.png')


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
    
    cur_start += 1

  return max_total, max_start

if __name__ == "__main__":
  main()

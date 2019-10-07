n = int(input())
prev_score = -1
curr_score = 0
candies = 0
tot_candies = 0
red_series = 0 
for _ in range(n):
    curr_score =int(input())
    if prev_score < curr_score:
        if candies > 1:
            tot_candies -= red_series
        candies += 1
        red_series = 0 
    elif candies > 1:
        candies -= 1
        red_series += 1 
    prev_score = curr_score
    tot_candies += candies
if candies > 1:
    tot_candies -= red_series
print(tot_candies)
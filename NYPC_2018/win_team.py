import sys


def win_team():
    won_team = []
    times = int(sys.stdin.readline())
    for i in range(times):
        kind = sys.stdin.readline()
        kind = kind.split()
        kind = kind[0]
        if kind == 'item':
            first = 30000
            team = 'red'
            for j in range(8):
                record = sys.stdin.readline()
                record = record.split()
                time_num = record[1].replace(':', '')
                time_num = time_num.replace('.', '')
                time_num = int(time_num)
                if time_num < first:
                    first = time_num
                    team = record[0]
                    first_num = time_num
            won_team.append(team)
        elif kind == 'speed':
            red_nums = []
            blue_nums = []
            red = 0
            blue = 0
            nums = []
            for j in range(1,8):
                record = sys.stdin.readline()
                record = record.split()
                record_time = record[1].replace(':', '')
                record_time = record_time.replace('.', '')
                record_time = int(record_time)
                if record[0] == 'red':
                    red_nums.append(record_time)
                elif record[0] == 'blue':
                    blue_nums.append(record_time)
                nums.sort()
                nums.append(record_time)
            for j in range(1,8):
                if nums[0] + 1000 < nums[j]:
                    nums.remove(nums[j])
                print(nums)

            score = [10, 8, 6, 5, 4, 3, 2, 1]
            best = nums[0]
            for j in range(len(nums)):
                plus = score[0]
                if nums[j] in red_nums:
                    red += plus
                if nums[j] in blue_nums:
                    blue += plus
                print(red, '   ', blue)
                score.remove(score[0])
            if red > blue:
                won_team.append('red')
            elif blue > red:
                won_team.append('blue')
            elif blue == red:
                if best in blue_nums:
                    won_team.append('blue')
                elif best in red_nums:
                    won_team.append('red')
            print(red, '   ', blue)
    for i in range(len(won_team)):
        print(won_team[i])



win_team()


import os

VALID_DIRECTORY = 'valid'
COOKIE_DIRECTORY = 'cookie'
ONE_FRIEND = 0.5
TEN_FRIENDS = 5
FIFTY_FRIENDS = 100
ONE_HUNDRED_FRIENDS = 15
TWO_HUNDRED_FRIENDS = 20

def count_files(directory):
    return len(os.listdir(directory))

def count_nospam_before_ten(directory):
    numbers = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)) and 'nospam' in file and ('noCT' in file):
            for x in file.split(']')[1].strip(' []').strip(',').split(','):
                if x.strip(' []').strip(',').isdigit():
                    numbers.append(int(x.strip(' []').strip(',')))
    tiers = [0, 0, 0, 0, 0]
    for num in numbers:
        if num < 10:
            tiers[0] += 1
        elif num >= 10 and num < 50:
            tiers[1] += 1
        elif num >= 50 and num < 100:
            tiers[2] += 1
        elif num >= 100 and num < 200:
            tiers[3] += 1
        elif num >= 200:
            tiers[4] += 1
    return tiers

valid_file_count = count_files(VALID_DIRECTORY)
cookie_file_count = count_files(COOKIE_DIRECTORY)

total_friends = 0
nospam_numbers = []

for file in os.listdir(VALID_DIRECTORY):
    if os.path.isfile(os.path.join(VALID_DIRECTORY, file)):
        total_friends += sum(int(x.strip(' []').strip(',')) for x in file.split(']')[1].strip(' []').strip(',').split(',') if x.strip(' []').strip(',').isdigit())

nospam_10 = count_nospam_before_ten(VALID_DIRECTORY)

files_with_meybe_ct = sum(os.path.isfile(os.path.join(VALID_DIRECTORY, file)) for file in os.listdir(VALID_DIRECTORY) if 'meybe_ct' in file and 'noCT' not in file)
files_with_ct = sum(os.path.isfile(os.path.join(VALID_DIRECTORY, file)) for file in os.listdir(VALID_DIRECTORY) if 'CT' in file and 'noCT' not in file)
files_with_nochats = sum(os.path.isfile(os.path.join(VALID_DIRECTORY, file)) for file in os.listdir(VALID_DIRECTORY) if 'nochats' in file)

nospam_files = sum(os.path.isfile(os.path.join(VALID_DIRECTORY, file)) for file in os.listdir(VALID_DIRECTORY) if 'nospam' in file and 'noCT' in file)
spam_files = sum(os.path.isfile(os.path.join(VALID_DIRECTORY, file)) for file in os.listdir(VALID_DIRECTORY) if 'spam' in file and 'nospam' not in file)

nospam_tiers = count_nospam_before_ten(VALID_DIRECTORY)

sum_1 = nospam_tiers[0] * ONE_FRIEND
sum_2 = nospam_tiers[1] * TEN_FRIENDS
sum_3 = nospam_tiers[2] * FIFTY_FRIENDS
sum_4 = nospam_tiers[3] * ONE_HUNDRED_FRIENDS
sum_5 = nospam_tiers[4] * TWO_HUNDRED_FRIENDS
sum_ = (sum_1 + sum_2 + sum_3+ sum_4 + sum_5)

print(f"""
Валид: {valid_file_count}
Невалид: {cookie_file_count - valid_file_count}
Всего друзей: {total_friends}
=============
Непроспам:
{'1+'.ljust(15)} | {nospam_tiers[0]}
{'10+'.ljust(15)} | {nospam_tiers[1]}
{'50+'.ljust(15)} | {nospam_tiers[2]}
{'100+'.ljust(15)} | {nospam_tiers[3]}
{'200+'.ljust(15)} | {nospam_tiers[4]}
=============
Всего:
Не проспамленных: {nospam_files}
Проспамленных: {spam_files}
-------------
Возможное кт: {files_with_meybe_ct}
Заблокированных: {files_with_ct}
0 Друзей: {files_with_nochats}
=============
Итоговая сумма:  {sum_}₽""")

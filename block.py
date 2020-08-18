import json
import os
import hashlib


blockchain_dir = os.curdir + '/blockchain/'


def get_hash(filename):
    file = open(blockchain_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()


def get_files():
    files = os.listdir(blockchain_dir)
    return sorted([int(i) for i in files])


def check_integrity():
    files = get_files()

    results = []

    for file in files[1:]:
        h = json.load(open(blockchain_dir + str(file)))['hash']

        prev_file = str(file - 1)
        actual_hash = get_hash(prev_file)

        if h == actual_hash:
            res = 'Ok'
        else:
            res = 'Corrupted'

        #print('block {} is: {}'.format(prev_file, res))

        results.append({'block': prev_file, 'result': res})

    return results

def write_block(id, vote, voting, prev_hash=''):
    files = get_files()
    prev_file = files[-1]

    filename = str(prev_file + 1)

    prev_hash = get_hash(str(prev_file))

    data = {'id': id,
            'vote': vote,
            'voting': voting,
            'hash': prev_hash}
    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    #write_block(id=4, vote='blue', voting='more selection')
    print(check_integrity())


if __name__ == '__main__':
    main()


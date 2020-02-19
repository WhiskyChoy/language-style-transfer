from random import shuffle


def distribute(original_file_path, distribute_dict):
    original_file = open(original_file_path, 'r', encoding='utf-8')
    original_lines = original_file.readlines()
    shuffle(original_lines)
    original_lines_len = len(original_lines)
    sum_of_val = sum(distribute_dict.values())
    list_norm = map(lambda item: (item[0], int(item[1] / sum_of_val * original_lines_len)), distribute_dict.items())
    counter = 0
    for key, value in list_norm:
        output_file = open(key, 'w', encoding='utf-8')
        output_file.writelines(original_lines[counter: counter + value])
        counter = counter + value + 1
        output_file.close()
    original_file.close()


if __name__ == '__main__':
    # original_f0 = '../data/chinese/sentiment.origin2_cut_char.0'
    # train_path0 = '../data/chinese/sentiment.train2_cut_char.0'
    # dev_path0 = '../data/chinese/sentiment.dev2_cut_char.0'
    # test_path0 = '../data/chinese/sentiment.test2_cut_char.0'
    # dist_dict0 = {train_path0: 7, dev_path0: 2, test_path0: 1}
    # distribute(original_f0, dist_dict0)
    #
    # original_f1 = '../data/chinese/sentiment.origin2_cut_char.1'
    # train_path1 = '../data/chinese/sentiment.train2_cut_char.1'
    # dev_path1 = '../data/chinese/sentiment.dev2_cut_char.1'
    # test_path1 = '../data/chinese/sentiment.test2_cut_char.1'
    # dist_dict1 = {train_path1: 7, dev_path1: 2, test_path1: 1}
    # distribute(original_f1, dist_dict1)

    original_f0 = '../data/chinese/sentiment.origin2_cut_word.0'
    train_path0 = '../data/chinese/sentiment.train2_cut_word.0'
    dev_path0 = '../data/chinese/sentiment.dev2_cut_word.0'
    test_path0 = '../data/chinese/sentiment.test2_cut_word.0'
    dist_dict0 = {train_path0: 7, dev_path0: 2, test_path0: 1}
    distribute(original_f0, dist_dict0)

    original_f1 = '../data/chinese/sentiment.origin2_cut_word.1'
    train_path1 = '../data/chinese/sentiment.train2_cut_word.1'
    dev_path1 = '../data/chinese/sentiment.dev2_cut_word.1'
    test_path1 = '../data/chinese/sentiment.test2_cut_word.1'
    dist_dict1 = {train_path1: 7, dev_path1: 2, test_path1: 1}
    distribute(original_f1, dist_dict1)

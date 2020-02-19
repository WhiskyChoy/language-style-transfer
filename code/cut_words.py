import jieba
import nltk
import re

WORD_SEP = " "
LINE_SEP = "\n"

LANGUAGE_ZH = "zh"
LANGUAGE_EN = "en"


def word_tokenize(sentence, language=None):
    sentence = sentence.strip()
    if language == LANGUAGE_ZH:
        # 中文去掉所有空格
        sentence = ''.join(sentence.split())
        return list(jieba.cut(sentence))
    elif language == LANGUAGE_EN:
        return nltk.word_tokenize(sentence)
    elif language is None:
        pattern = re.compile('\\S')
        return pattern.findall(sentence)
    else:
        raise Exception("Invalid Language!")


def cut_words(input_file_path, output_file_path, language=None):
    input_file = open(input_file_path, 'r', encoding='utf-8')
    output_file = open(output_file_path, 'w', encoding='utf-8')
    print("Successfully open %s with language %s, and the output file is %s, now writing..." %
          (input_file_path, language, output_file_path))
    for line in input_file.readlines():
        # strip去掉首尾空格
        line = line.strip()
        # 不能去除空行，可能会导致两个文件不一样长，然后就空值对有值 到batch的时候用filter_length解决，那里用and是两边一起满足
        # 之前这么写直接给变成从中间某个位置开始一一错位了
        # 我研究了一下文件，进入下一个视频之前会重新对齐，这时经常英文这边没空行，中文那边有空行
        # 应该像示例代码一样采取有一处有空行 两边一起删除的做法
        # 视频的重新对齐首先可以保证以视频为采样单位时，两边的内容是对应的
        # 其次即便是以句子为单位，也不会导致两个从某一行开始完全错位，到下个视频又会被纠正过来
        # 下面这行注释掉，并左缩进再下面三行
        # 改完注意从本文件开始的后续步骤往下要重新跑
        # 其实一开是就应该写个程序检查源语言文件和目标语言文件的行数
        # if line != '':
        word_list = word_tokenize(line, language)
        joint_sentence = WORD_SEP.join(word_list)
        output_file.write(joint_sentence + LINE_SEP)
    input_file.close()
    output_file.close()
    print("Finished writing %s" % output_file_path)


if __name__ == "__main__":
    # 初始化 jieba
    # jieba 采用延迟加载，import jieba 和 jieba.Tokenizer() 不会立即触发词典的加载，一旦有必要才开始加载词典构建前缀字典。
    jieba.initialize()
    # cut_words("../data/chinese/sentiment.origin2.0", "../data/chinese/sentiment.origin2_cut_word.0", LANGUAGE_ZH)
    # cut_words("../data/chinese/sentiment.origin2.1", "../data/chinese/sentiment.origin2_cut_word.1", LANGUAGE_ZH)
    # cut_words("../data/chinese/sentiment.origin2.0", "../data/chinese/sentiment.origin2_cut_char.0")
    # cut_words("../data/chinese/sentiment.origin2.1", "../data/chinese/sentiment.origin2_cut_char.1")

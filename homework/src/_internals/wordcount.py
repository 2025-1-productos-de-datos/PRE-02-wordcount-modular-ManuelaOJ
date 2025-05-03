# obtain a list of files in the input directory

from .count_words import count_words
from .preprocess_lines import preprocess_lines
from .read_all_lines import read_all_lines
from .split_into_words import split_in_words

from .write_word_counts import write_word_counts


def main():


    all_lines = read_all_lines()
    all_lines = preprocess_lines(all_lines)
    words = split_in_words(all_lines)
    counter = count_words(words)

    # count the frequency of the words in the files in the input directory
    # counter = {}
    # for filename in input_file_list:
    #     with open("data/input/" + filename) as f:
    #         for l in f:
    #             for w in l.split():
    #                 w = w.lower().strip(",.!?")
    #                 counter[w] = counter.get(w, 0) + 1

    ##
    write_word_counts(counter)


if __name__ == "__main__":
    main()

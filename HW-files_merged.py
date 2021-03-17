import os
files_list = ['1.txt', '2.txt', '3.txt']
files_dict = {}

for i in files_list:
    file_path = os.path.join(os.getcwd(), i)
    with open(file_path, "r", encoding="utf-8") as f:
        files_dict[i] = len(f.readlines())

sorted_keys = sorted(files_dict, key=files_dict.get)


def count_lines(txt):
    file_path = os.path.join(os.getcwd(), txt)
    with open(file_path, "r", encoding="utf-8") as f:
        return str(len(f.readlines()))


def merge_files(sorted_keys):
    for i in sorted_keys:
        file_path = os.path.join(os.getcwd(), i)
        with open(file_path, "r", encoding="utf-8") as f:
            with open(os.path.join(os.getcwd(), 'merged.txt'), "a", encoding="utf-8") as f_1:
                f_1.write(i + '\n')
                f_1.write(count_lines(i) + '\n')
                while True:
                    line = f.readline()
                    f_1.write(line)
                    if not line:
                        f_1.write('\n')
                        break


merge_files(sorted_keys)

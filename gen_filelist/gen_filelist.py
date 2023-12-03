import os
import time


def open_file_dict(in_file_path):
    file = open(in_file_path, 'r')
    text = file.readlines()
    text_dict = dict()
    line = 0
    for rtl_line in text:
        line = line + 1
        text_dict[line] = rtl_line
    file.close()
    print("[Info]: {} read file success !".format(in_file_path))
    return text_dict  # <class 'dict'>
 
 
def open_file(in_file_path):
    file = open(in_file_path, 'r')
    text = file.readlines()
    file.close()
    print("[Info]: {} read file success !".format(in_file_path))
    return text  # <class 'list'>
 
 
def gen_file(in_module_name, in_text):
    text = ""
    if type(in_text) == list:
        text = text + "\n".join(in_text)
    elif type(in_text) == str:
        text = text + in_text
    elif type(in_text) == dict:
        tmp_text = list()
        for key, value in in_text.items():
            tmp_text.append(str(key) + str(value) + "\n")
        text = text + "".join(tmp_text)
    file = open(in_module_name, 'w')
    file.write(text)
    file.close()
    print("[Info]: {} save file success !".format(in_module_name))
 
 
def gen_log_file(in_module_name, in_text):
    text = ""
    if type(in_text) == list:
        text = text + "".join(in_text)
    elif type(in_text) == str:
        text = text + in_text
    elif type(in_text) == dict:
        tmp_text = list()
        for key, value in in_text.items():
            tmp_text.append(str(key) + '\n' + str(value) + "\n")
        text = text + "".join(tmp_text)
    file = open(in_module_name, 'w')
    file.write(text)
    file.close()
    print("[Info]: {} save file success !".format(in_module_name))
 
 
def gen_rtl_file(in_module_name, in_text):
    text = ""
    if type(in_text) == list:
        text = text + "".join(in_text)
    elif type(in_text) == str:
        text = text + in_text
    elif type(in_text) == dict:
        tmp_text = list()
        for key, value in in_text.items():
            tmp_text.append(str(key) + str(value) + "\n")
        text = text + "".join(tmp_text)
    file = open(in_module_name, 'w')
    file.write(text)
    file.close()
    print("[Info]: {} save file success !".format(in_module_name))
# -----------------------------------------------------------------------------


class FileList:
    def __init__(self):
        self.filelist = []

    def generate(self, input_path, output_path):
        dict_1 = {}
        total_cnt = 0
        for root, dirs, files in os.walk(input_path):
            # 添加文件路径到文件列表中
            dict_1[root] = {'cnt':'', 'files' : []}
            for file in files:
                # 捕获指定类型 'vh', 'vhdl', 'v', 'sv'
                if file.split('.')[-1] in ['vh', 'vhdl', 'v', 'sv']:
                    dict_1[root]['files'].append(file)
            dict_1[root]['cnt'] = len(dict_1[root]['files'])
            total_cnt = total_cnt + dict_1[root]['cnt']
        
        # 生成时间信息
        cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.filelist.append(f"// ---------- {cur_time} ----------\n")
        # 生成文件总数
        self.filelist.append(f"// ---------- total files cnt {total_cnt} ----------\n")

        for key, values in dict_1.items():
            cnt, files_lst = values['cnt'], values['files']
            if cnt != 0:
                # 生成注释
                self.filelist.append(f"\n// ----------{key}, files cnt {cnt} ----------\n")
                # 生成文件路径
                for file in files_lst:
                    self.filelist.append(f"{key}/{file}\n")
        # 调用函数生成文件
        gen_log_file(output_path, self.filelist)
# -----------------------------------------------------------------------------


if __name__ == '__main__':
    # 示例用法
    input_path = r"./sub_sys/"
    output_path = r"./sub_sys/file_list.f"
    test_filelist = FileList()
    test_filelist.generate(input_path, output_path)

    print("-----------------------------")
    print("文件列表生成完成！")
    print("-----------------------------")

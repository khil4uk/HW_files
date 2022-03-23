import os

path = os.getcwd()
files = os.listdir(path)
txt_files = filter(lambda x: x.endswith('.txt'), files) #фильтруем по файлам в папке, имеющим расширение '.txt'
summary_list = []

def create_new_file(files, new_file):
    for file in txt_files:
        with open(file, encoding = 'utf-8') as f:
            text = f.read()
            count = len(text.split('\n')) #подсчитываем количество строк (разделение \n)
            if text == '':
                count = 0
            summary_list.append([file, count, text]) #добавляем информацию в сводный список
            summary_list_sorted = sorted(summary_list, key=lambda x: x[1]) #производим сортировку списка
        with open(new_file, 'w', encoding = 'utf-8') as w:
            for file in summary_list_sorted: #проходимся циклом по полученному списку и записываем результат
                w.write(f'{file[0]}\n')
                w.write(f'{file[1]}\n')
                w.write(f'{file[2]}\n\n')

#выполним функцию вызова написанного кода, создадим объединенный и отсортированный файл
if __name__ == '__main__':
    create_new_file(txt_files, 'final_file.txt')
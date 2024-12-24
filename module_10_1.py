import time
import threading


def write_words(word_count, file_name):
    file = open(file_name, 'a', encoding="utf-8")
    for word in range(1, word_count + 1):
        file.write(f'\n Какое-то слово № {word}')
        time.sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')


start_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time()

print(f'Время залписи в файлы без потоков: {time.strftime('%H:%M:%S', time.gmtime((end_time - start_time)))}')

start_time = time.time()

stream_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
stream_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
stream_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
stream_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

stream_1.start()
stream_2.start()
stream_3.start()
stream_4.start()

stream_1.join()
stream_2.join()
stream_3.join()
stream_4.join()

end_time = time.time()

print(f'Время залписи в файлы с потоками: {time.strftime('%H:%M:%S', time.gmtime((end_time - start_time)))}')

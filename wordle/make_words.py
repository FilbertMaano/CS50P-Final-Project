with open('w.txt') as file:
    lines = file.readlines()
    words = [line for line in lines if len(line.strip()) == 5]
    with open('words.txt', 'w') as word_file:
        word_file.writelines(words)
        
            
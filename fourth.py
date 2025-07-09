def count_words(fourth):
    try:
        with open(fourth, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"Total number of words: {word_count}")
    except FileNotFoundError:
        print("File not found")
count_words('fourth.txt')
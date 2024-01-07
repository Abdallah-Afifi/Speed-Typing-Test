import time
import random

def generate_random_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a high-level, interpreted programming language.",
        "Programming is the process of creating a set of instructions that tell a computer how to perform a task.",
        "Coding is fun!",
        "Hello World!"
    ]
    return random.choice(sentences)

def speed_typing_test():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter when you are ready to start...")

    sentence = generate_random_sentence()
    print("\nType the following sentence as fast as you can:\n")
    print(sentence)

    start_time = time.time()
    user_input = input("\nYour typing: ")
    end_time = time.time()

    if user_input == sentence:
        elapsed_time = end_time - start_time
        words_per_minute = int((len(sentence.split()) / elapsed_time) * 60)
        print(f"\nCongratulations! You typed it correctly in {elapsed_time:.2f} seconds.")
        print(f"Your typing speed: {words_per_minute} words per minute.")
    else:
        print("\nIncorrect typing. Please try again.")

if __name__ == "__main__":
    speed_typing_test()

import time

def typing_speed_test():
    prompt_text = "The quick brown fox jumps over the lazy dog."
    print("Type the following:")
    print(prompt_text)
    
    input("Press Enter when you are ready to start...")
    
    start_time = time.time()
    
    user_input = input("Start typing: ")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    word_count = len(prompt_text.split())
    user_word_count = len(user_input.split())
    
    accuracy = calculate_accuracy(prompt_text, user_input)
    words_per_minute = calculate_words_per_minute(user_word_count, elapsed_time)
    
    print("\nTyping test results:")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Words per minute: {words_per_minute:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

def calculate_accuracy(prompt, user_input):
    prompt_words = prompt.split()
    user_words = user_input.split()
    
    correct_words = 0
    for i in range(min(len(prompt_words), len(user_words))):
        if prompt_words[i] == user_words[i]:
            correct_words += 1
    
    accuracy = (correct_words / len(prompt_words)) * 100
    return accuracy

def calculate_words_per_minute(word_count, elapsed_time):
    minutes = elapsed_time / 60
    words_per_minute = word_count / minutes
    return words_per_minute

if __name__ == "__main__":
    typing_speed_test()


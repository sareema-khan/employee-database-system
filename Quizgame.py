
#quiz game 
#concepts used variables , input/output, loops , conditions 

print("\t======================")
print("\tAdvanced AI Quiz")
print("\t======================")                                  
print("Answer with a, b, c, or d")

score = 0
total = 5


while True:
    print("\nQ1. Which architecture powers most modern LLMs?")
    print("a. CNN")
    print("b. Transformer")
    print("c. RNN")
    print("d. GAN")

    answer = input("Your answer: ") 
    if answer == "b":
        score += 1

    print("\nQ2. What does RLHF stand for?")
    print("a. Reinforcement Learning from Human Feedback")
    print("b. Recursive Learning Human Function")
    print("c. Reinforced Language Hybrid Framework")
    print("d. Random Learning Human Feedback")

    answer = input("Your answer: ")

    if answer == "a":
        score += 1

    print("\nQ3. Which technique helps an AI model find relevant external information?")
    print("a. Tokenization")
    print("b. Quantization")
    print("c. RAG")
    print("d. Embedding Removal")

    answer = input("Your answer: ")

    if answer == "c":
        score += 1

    print("\nQ4. What is a hallucination in AI?")
    print("a. AI training process")
    print("b. AI generates incorrect information confidently")
    print("c. AI compression method")
    print("d. AI hardware failure")

    answer = input("Your answer: ")

    if answer == "b":
        score += 1

    print("\nQ5. What is the main purpose of fine tuning?")
    print("a. Reduce electricity usage")
    print("b. Increase RAM")
    print("c. Adapt a model for specific tasks")
    print("d. Delete training data")

    answer = input("Your answer: ")

    if answer == "c":
        score += 1
    break
    


print("\n Congratulations Quiz Finished")


print("\n\t==========================")
print("\t\tRESULT CARD")
print("\t===========================")
print("Your Score:", score, "/ 5")
percentage = score * 100 / total
print(f"Your percentage: {percentage}")

if score == 5:
    print("A+ Grade")
    print("Outstanding")
elif score >= 3:
    print("B Grade")
    print("Not Bad")
else:
    print("Poor performance Try next time! ")
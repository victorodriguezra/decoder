def extraction(file_path):
    numbers = []
#This is where I "extract" the information from the txt file to make the pyramid or the sequence of information.
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split()
            if parts[0].isdigit():
                numbers.append(int(parts[0]))

    return numbers
def organize(numbers):
    numbers.sort()
    numbers_lists = []
    index = 0                                                   #
#this is my number sorter.
    while index < len(numbers):
        count = len(numbers_lists) + 1
        current_list = []
        for _ in range(count):
            if index >= len(numbers):
                break
            current_list.append(numbers[index])
            index += 1
        numbers_lists.append(current_list)

    return numbers_lists
def extractionlast(numbers_lists):
    numbers_last = []
    for numbers_list in numbers_lists:
        numbers_last.append(numbers_list[-1])
    return numbers_last
#here I extract the last digit from the series of rows in the pyramid, or my number lists, which apply the same.
def decoder(sorted_sequence, file_path):
    message = ""

    with open(file_path, "r") as file:
        lines = file.readlines()

        for number in sorted_sequence:
            for line in lines:
                parts = line.strip().split()
                if len(parts) >= 2 and parts[0].isdigit() and int(parts[0]) == number:
                    message += parts[1] + " "
                    break

    return message.strip()
#lastly this is the decoder, where I grab the actual text to the right of each number in the txt and using my sorted sequence I find the message.

#EXTRACTED NUMBERS FROM TXT
numbers = extraction("test_input.txt")

#ORGANIZED NUMBERS INTO LIST FOR DECODING
numbers_lists = organize(numbers)

#EXTRACTED LAST NUMBER FROM LISTS
numbers_last = extractionlast(numbers_lists)

#ORGINIZED NUMBERS FOR DECODING
sorted_sequence = sorted(numbers_last)

#DECODING THE MESSAGE
message = decoder(sorted_sequence, "test_input.txt")

#PRINT OF FINAL MESSAGE
print(message)

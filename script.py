f = open("file.txt", "r")
fileContent = f.read().split("\n")

counter = 0
final_result = ""
for line in fileContent:
    leadind_string = "<string name=\"resource_name"+ str(counter) + "\">"
    ending_string = "</string>"
    filtered_line = line.lstrip()[3:].lstrip()
    
    line_result = leadind_string + filtered_line + ending_string
    final_result += line_result + "\n"
    counter+=1



f = open("result.txt", "a")
f.write(final_result)

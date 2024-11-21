
def file_filter():
    """
    Function searches for all .txt files in the current directory, reads each file line by line,
    filters the lines containing the keyword 'opened', and writes the results to 
    'filtered_results.txt'. The results are stored as tuples containing the filename, 
    line number, and line content.
    """
    desired_files=[] # Initialize a list to store the names of desired .txt files
    
    # part 1:
    # Filter out files that do not end with '.txt' using lambda function
    filter_function=lambda char : char.lower().endswith('.txt')
    filtered_files=list(map(filter_function,all_files))
    for index,char in enumerate(filtered_files):#loop looks for document that evaluated to True
        if char== True:
            desired_files.append(all_files[index])

    # part 2: # Iterate over the filtered files and append the .txt file names to desired_files list
    for doc in desired_files:
        with open (doc , 'r') as file:
            newer=file.readlines() #search line by line and keep tabs with the row number
            answer=tuple([[doc,index,newer[index]]  for index,char in enumerate(newer) if 'opened' in newer[index] ])
        
            os.mkdir('filtered_results.txt')
            with open ('filtered_results.txt','w') as file:
                results=file.writelines(str(answer))     
    
file_filter()   

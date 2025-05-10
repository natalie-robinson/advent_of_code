f = open('/users/natalierobinson/Desktop/github/advent_of_code/2022/input7.txt', 'r')
code = f.read()

# code = '$ cd /\n\$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k'
code = code.replace('/','root')

def updateParents(dirString, addTo, masterDictionary):
    while dirString:
        lastUnderscore = dirString.rfind('_')
        if lastUnderscore > -1:
            parentDir = dirString[0:lastUnderscore]
            masterDictionary[parentDir] += addTo
            dirString = parentDir
        else:
            dirString = ''
        print (dirString)
        
        
def calcFiles(parentDir, currentDir, masterDictionary):
    # Get directory contents
    currentContents = list(filter(None, code.split('$ cd ' + currentDir.replace('dir ', ''))[1].split('$ cd')[0].replace('\n$ ls','').split('\n')))
    # Sum files in directory
    files = [f for f in currentContents if f.split(' ')[0] != 'dir']
    filesSum = sum([int(f.split(' ')[0]) for f in files])
    # Update currentDir to reflect whole path and add to master dictionary
    currentDir = parentDir + '_' + currentDir.replace('dir ','')
    masterDictionary[currentDir] = filesSum
    # Add filesSum to all parents of current directory
    updateParents(currentDir, filesSum, masterDictionary)
    # Recursively handle subdirectories
    dirs = [d for d in currentContents if d not in files]
    # if not dirs:
    #     # Add filesSum to all parents of current directory
    #     updateParents(currentDir, filesSum, masterDictionary)
    for d in dirs:
        masterDictionary = calcFiles(currentDir, d, masterDictionary)
    return masterDictionary
    
# Process directories #######################################################
masterDictionary = {}
rootContents = list(filter(None, code.split('$ cd root\n$ ls')[1].split('$ cd')[0].split('\n')))
rootFiles = [f for f in rootContents if f.split(' ')[0] != 'dir']
masterDictionary['root'] = sum([int(f.split(' ')[0]) for f in rootFiles])
rootDirs = [i for i in rootContents if i not in rootFiles]

for d in rootDirs:
    masterDictionary = calcFiles('root', d, masterDictionary)


output = sum([v for v in masterDictionary.values() if v < 100000])






d = rootDirs[0]
for d in rootDirs:
    fileSum = 0
    stack = list(filter(None, code.split('$ cd ' + d.replace('dir ', ''))[1].split('$ cd')[0].replace('\n$ ls','').split('\n')))
    fullyProcessed = [s for s in stack if s in ret.keys()]
    if fullyProcessed:
        for fp in fullyProcessed:
            ind = [s for s in stack if s == fp]
            stack[s] = ret['fp']
    
    files = [f for f in stack if f.split(' ')[0] != 'dir']
    dirs = [s for s in stack if s not in files]
    # Add to main dictionary        
    if not dirs:
        ret[d] = str(sum([int(f.split(' ')[0]) for f in files])) + ' files'
    else:
        # If any subdirectories are fully processed, replace
        
        
    
    
    
    dirFiles = list(filter(None, [f for f in dirContents if f.split(' ')[0] != 'dir']))
    fileSum += sum([int(f.split(' ')[0]) for f in dirFiles])
    dirDirs = [i for i in dirContents if i not in dirFiles and i != '']
    for d in dirContents:
        
        
        if d.split(' ')[0] != 'dir':
           fileSum += int(d.split(' ')[0])
           dirContents = [dc for dc in dirContents if dc != d]
        
        

d = rootDirs[0]
dFileSum = 0
dirContents = code.split('$ cd ' + d.replace('dir ', ''))[1].split('$ cd')[0]

dirFiles = [f for f in dirDirs if any([i for i in f.split() if i.isdigit()])]
dFileSum += sum([int(f.split(' ')[0]) for f in dirFiles])
dirDirs = [i for i in dirDirs if i not in dirFiles and i != '']


def crawlDirectory(directory, fileSum = 0):
    dirContents = code.split('$ cd ' + directory.replace('dir ', '') + '\n$ ls')[1].split('$ cd')[0]
    dirDirs = dirContents.split('\n')
    dirFiles = [f for f in dirDirs if any([i for i in f.split() if i.isdigit()])]
    fileSum += sum([int(f.split(' ')[0]) for f in dirFiles])
    dirDirs = [i for i in dirDirs if i not in dirFiles and i != '']
    if len(dirDirs) > 0:
        for d in dirDirs:
            crawlDirectory(d, fileSum=fileSum)
    else:
        ret[directory] = fileSum
    
    return dirDirs


# Function to find contents of individual directory
def crawl_directory(directory):
    dir_contents = code.split('cd '+directory+'\n$ ls\n')[1]
    if '\n$ cd ' in dir_contents:
        dir_contents = dir_contents.split('\n$ cd ')[0].split('\n')
    else:
        dir_contents = dir_contents.split('\n')
    # Sum files, leave directories
    files = [f for f in dir_contents if any([i for i in f.split() if i.isdigit()])]
    dir_contents = [i for i in dir_contents if i not in files]
    if files:
        dir_contents.append(sum([int(i.split(' ')[0]) for i in files]))
    return(dir_contents)


def total_data(has_sub_dirs, revisit):
    ret = {}
    for k in has_sub_dirs:
        print(k)
        # print(working_on)
        for d in [i for i in dirs[k] if type(i) == str]:
            # Replace with directory data size if possible
            if all([type(i) == int for i in dirs[d]]):
                replace_index = [i for i in range(0,len(dirs[k])) if dirs[k][i] == d]
                dirs[k][replace_index[0]] = sum([i for i in dirs[d]])
        if all([type(i) == int for i in dirs[k]]):
            dirs[k] = [sum(dirs[k])]
            has_sub_dirs.remove(k)
        else:
            # Move to back to handle later
            has_sub_dirs.remove(k)
            revisit.append(k)
    has_sub_dirs = list(set(has_sub_dirs))
    ret['has_sub_dirs'] = has_sub_dirs
    ret['revisit'] = revisit
    return(ret)


# Process data ----------------------------------------------------------------
# Find subdirectories
dirNames = re.findall('dir (.*)', code)

dirs = {key: [] for key in ['dir ' + d for d in dirNames]}

# Fill contents per directory/subdirectory
for k in dirs.keys():
    dirs[k] = crawl_directory(k.replace('dir ',''))

# # Add root
# dirs['root'] = code.split('cd /\n\$ ls\n')[1].split('\n$ cd ')[0].split('\n')

# -----------------------------------------------------------------------------
# Part 1 - Calculate sum of total sizes of directories with <= 100000 of data

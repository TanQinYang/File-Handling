
def total_hours(filename):
    '''
    Purpose: Take in one parameter, filename, which should be a string 
    representing the name of a file that contains an employee’s hours worked,
    then return the total amount of hours the employee worked.
    Parameter(s): Take in one parameter, filename, which should be a string 
    representing the name of a file that contains an employee’s hours worked.
    Return Value: Return the total amount of hours the employee worked.
    '''
    p = open(filename)
    nums = p.readlines()
    sum=0
    for num in nums:
        sum+=int(num)
    p.close()
    return sum

if __name__ == '__main__':
    print(total_hours('employee1.txt')) #30
    print(total_hours('employee2.txt')) #22
    print(total_hours('employee3.txt')) #40


def label_days(filename):
    '''
    Purpose: Take in one parameter, filename, which should be a string 
    representing the name of a file that contains an employee’s hours worked.
    The function should create a new file which has the same name as the 
    original, but with 'labeled_' concatenated to the beginning.
    The new file should have the same numbers on each line, but each 
    number should be preceded by the day of the week (starting with Sunday), 
    then a colon, then a space.
    This function should not return anything.
    Parameter(s): See total_hours Parameter(s) description.
    Return Value: This function should not return anything.
    '''
    p = open(filename)
    nums = []
    for num in p:
        nums.append(num)
    p.close()

    p1 =open('labeled_'+filename,'w')
    week = ['Sunday','Monday','Tuesday','Wednesday'
            ,'Thursday','Friday','Saturday']
    for i in range(len(nums)):
        p1.write(f"{week[i]}: {nums[i]}")
    p1.close()

if __name__ == '__main__':
    label_days('employee1.txt') 
    label_days('employee2.txt') 
    label_days('employee3.txt') 


def stretch_model(fname_in, fname_out):
    '''
    Purpose: Read all the vertices and faces in the OBJ file specified 
    by the string fname_in.  The function should then transform the 
    vertices to stretch the model by a factor of 2 along the y-axis, 
    and then save the transformed vertices and faces to a file specified 
    by the string fname_out.  This function should return the total 
    number of vertices in the file.  
    If the specified file fname_in does not exist, stretch_model should 
    instead return -1.
    Parameter(s): Take in two strings representing the name of the file to 
    read and the name of the file to write.
    Return Value: Return the total number of vertices in the file.  
    If the specified file fname_in does not exist, stretch_model should 
    instead return -1.
    ''' 
    try:
        p = open(fname_in)
        text =[]
        vertices=0
        for line in p:
            line=line.split(' ')
            temp=[]
            if line[0]=='v':
                for i in range(len(line)):
                    if i!=2:
                        temp.append(line[i])
                    else:
                        temp.append(str(float(line[2])*2))
                temp=' '.join(temp)
                text.append(temp)
                vertices+=1
                line=' '.join(line)
            else:
                line=' '.join(line)
                text.append(line)
        p.close()
        p1 = open(fname_out,'w')
        for line in text:
            p1.write(line)
        p1.close()
        return vertices
    except FileNotFoundError:
        return -1


if __name__ == '__main__':
    print(stretch_model('missing.obj', 'doesntmatter.obj')) #-1
    print(stretch_model('triforce.obj', 'triforce_stretched.obj')) #9
    print(stretch_model('teapot.obj', 'tall_teapot.obj')) #3644

def count_votes(district, office):
    '''
    Purpose: Take in two strings as parameters. 
    district should be the name of a file containing all voting data for a 
    given district, in the format specified above.  You can assume that 
    said file actually exists (no need for a try-except block).
    office should be the name of one of the column titles present in the 
    CSV file.  You can assume that the office passed in will match one of 
    the columns in the CSV file.  
    The function should return a two-element list: the first element is 
    a string representing the name of the candidate who won the most votes 
    for the given office, and the second is an integer representing a count 
    of the number of votes they got.  You may assume that there will not be 
    a tie.
    Parameter(s): Take in two strings as parameters. 
    district should be the name of a file containing all voting data for a 
    given district, in the format specified above.  You can assume that 
    said file actually exists (no need for a try-except block).
    office should be the name of one of the column titles present in the 
    CSV file.  You can assume that the office passed in will match one of 
    the columns in the CSV file.  
    Return Value: The function should return a two-element list: the first 
    element is a string representing the name of the candidate who won the 
    most votes for the given office, and the second is an integer representing
    a count of the number of votes they got.  You may assume that there 
    will not be a tie.
    ''' 
    import statistics as stats
    p = open(district)
    positions = p.readline().strip('\n').split(',')
    i=0
    while positions[i]!= office:
        i+=1
    votes=[]
    for line in p:
        line=line.strip('\n').split(',')
        votes.append(line[i])
    winner=stats.mode(votes)
    count=votes.count(winner)
    result=[winner,count]
    p.close()
    return result

if __name__ == '__main__':
    print()
    print(count_votes('district_0z.csv', 'Mayor'))
    #['Leslie Knope', 2]

    print(count_votes('district_4b.csv', 'City Question 1'))
    #['YES', 10]

    print(count_votes('district_60b.csv', 'County Commissioner District 4'))
    #['Angela Conley', 49]

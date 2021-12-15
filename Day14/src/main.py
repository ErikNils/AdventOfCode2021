#!/usr/bin/python3
# Above is path for 'Code Runner' extension. OBS!! Needs to be first it seems.
import os



def _read_file(path):
    template = {}
    counter = {}
    temp_counter = {}
    file = open(path,'r')
    string = list(file.readline().strip())
    file.readline().strip()
    
    for line in file:
        a,b = line.split("->")
        template[a.strip()] = b.strip()
        counter[b.strip()] = 0
        temp_counter[a.strip()] = 0
        
    file.close()
    
    return string,template,counter,temp_counter


# The poorly scaling, shitty version
def _pair_insertion_old(string,template,counter,steps):
    for char in string:
        counter[char] += 1
    for _ in range(steps):
        str_list = []
        str_list.append(string[0])
        for i in range(len(string)-1):
            value = template[string[i]+string[i+1]]
            str_list.append(value)
            counter[value] += 1
            str_list.append(string[i+1])
        string = str_list
    
    return max(counter.values()) - min(counter.values())



# The chad version with incredible scaling
def _pair_insertion(string,template,counter,temp_counter,steps):
    # Just adding the right start values to the counters
    counter[string[0]] += 1
    for i in range(len(string)-1):
        a = string[i]
        b = string[i+1]
        temp_counter[a+b] += 1
        counter[b] += 1
    
    for _ in range(steps):
        new_temp = temp_counter.copy()
        # E.g SB -> B turns into SB and BB, which is updated in the counters
        for ele in temp_counter:
            value = temp_counter[ele]
            if value == 0: continue
            new_temp[ele] -= value
            char = template[ele]
            counter[char] += value
            a = ele[0] + char
            b = char + ele[1]
            new_temp[a] += value 
            new_temp[b] += value
        temp_counter = new_temp
    return max(counter.values()) - min(counter.values())

def main():
    
    # Path that works from any computer
    rel_path = "../polymer.csv"
    abs_path = os.path.join(os.path.dirname(__file__), rel_path)
    
    string,template,counter,temp_counter =_read_file(abs_path)
    result = _pair_insertion(string,template,counter,temp_counter,10)
    print("Part 1:")
    print(str(result) + "\n")

    #--------- Part 2 --------------------------------------------------
    string,template,counter,temp_counter =_read_file(abs_path)
    result = _pair_insertion(string,template,counter,temp_counter,40)
    print("Part 2:")
    print(result)

 
if __name__ == '__main__':
    main()
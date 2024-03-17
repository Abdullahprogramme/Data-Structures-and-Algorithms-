import list_adt as listadt
import random as r

def create_alien() -> dict:
    """
    Creates an 'alien' dictionary with a list to store messages.
    You can add other attributes if required

    Returns:
    A dictionary representing an 'alien' with a list to store messages:
    {
        'messages': listadt.create_list(100)    # List to store messages with a maximum capacity of 100
    }
    """
    alien = {"messages": listadt.create_list(100), 'last_added': None, 'min_num': 0, 'max_num': 0, 'pre_num': 0, 'cur_num': 0}

    # provide other required implementation here
    return alien

def add(seq: int, msg: str, alienList: dict):
    """
    Parameters:
    - seq: The sequence number of the message.
    - msg: The message to be added.
    - alienList: The 'alien' dictionary containing the messages list.
    """
 
    # provide implementation here
    tup = [seq, msg]
    listadt.add(alienList['messages']['i'] + 1, tup, alienList)
    # alienList['messages']['data'][alienList['messages']['i']] = (seq, msg)
    # alienList['messages']['i'] = (alienList['messages']['i'] + 1) % alienList['messages']['size']
    # alienList['messages']['n'] += 1
    alienList['last_added'] = seq

def delete(seq: int, msg: str, alienList: dict):
    """
    
    Parameters:
    - seq: The sequence number of the message to be deleted.
    - msg: The message to be deleted.
    - alienList: The 'alien' dictionary containing the messages list.
    """

    # provide implementation here
    listadt.remove_last(alienList)
    # alienList['messages']['data'][alienList['messages']['i'] - 1] = None
    # alienList['messages']['i'] = (alienList['messages']['i'] - 1) % alienList['messages']['size']
    # alienList['messages']['n'] -= 1



def get_messages(alienList: dict) -> list[str]:
    """

    Parameters:
    - alienList: The 'alien' dictionary containing the messages list.

    Returns:
    A list of all messages in the conversation.
    """

    # provide implementation here
    data = alienList['messages']['data']
    max_number = -1
    # print(alienList)
    for item in data:
        if item != None:
            order_number = item[0]
            if order_number > max_number:
                max_number = order_number

    messages = [None] * (max_number + 1)

    for item in data:
        if item != None:
            order_number = item[0]
            message = item[1]
            messages[order_number] = message

    count = 0
    for message in messages:
        if message != None:
            count += 1

    final_messages = [None] * count
    index = 0
    for message in messages:
        if message != None:
            final_messages[index] = message
            index += 1

    return final_messages
    # return ' '.join(final_messages)


def main(filename) -> list[str]:
    """
    Reads data from a file, processes it, and returns the conversation as a list.

    Data is provided in the following format:
    There can be multiple lines in the file, each line containing an integer and an optional string separated by a space. The integer represents the sequence number of the message, and the string represents the message itself. If the string is not provided, it is assumed to be an empty string. The sequence number 0 indicates the end of the conversation.

    Process the data as follows:
    - If the sequence number is 0, stop processing the file.
    - If the sequence number is positive, add the message to the conversation.
    - If the sequence number is negative, delete the message from the conversation.
    
    Parameters:
    - filename: The name of the file to read data from.

    Returns:
    A list representing the conversation obtained from the file.
    """
    
    alien = create_alien()

    # Provide your implementation here
    with open(filename, 'r') as f:
        seq, msg = f.readline().strip().split()
        alien['min_num'] = int(seq)
        alien['max_num'] = int(seq)

        alien['cur_num'] = r.randint(1, 10) # random number
        # while seq != 0
        while int(seq) != 0:

            # print(alien['pre_num'], alien['cur_num'], seq, alien['min_num'], alien['max_num'])

            if int(seq) < alien['max_num'] and int(seq) > alien['min_num']: # discarding the message
                # delete(int(seq), msg, alien)
                pass
            elif int(seq) > 0: # adding the message
                if int(seq) >= alien['max_num'] or int(seq) <= alien['min_num']: # excluding the range to be discarded
                    add(alien['cur_num'], msg, alien)
            elif int(seq) < 0: # discarding the last message
                # print(alien['pre_num'], pre_message)
                delete(alien['pre_num'], pre_message, alien)
            pre_message = msg # store the previous message
            alien['pre_num'] = alien['cur_num']
            line = f.readline().strip()
            if ' ' in line: # checking if the line contains a message
                seq, msg = line.split()
            else: seq, msg = line, ''

            # print('-------------------')
            # print(seq, msg)
            # print('-------------------')

            
            # assigning a new r_num based on old
            if int(seq) > alien['max_num']: # if the new number is greater than the max
                alien['cur_num'] += 1
            if int(seq) < alien['min_num']: # if the new number is less than the min
                alien['cur_num'] -= 1
            
            # update min and max
            if int(seq) != -1:
                if int(seq) > alien['max_num']:
                    alien['max_num'] = int(seq)
                if int(seq) < alien['min_num']:
                    alien['min_num'] = int(seq)

    f.close()
    output = get_messages(alien)
    # print(output)
    return(output)


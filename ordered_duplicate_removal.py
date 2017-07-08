import random
import string
import heapq
import timeit
import time

class OrderedHash:
    def __init__(self):
        self.size = 5
        self.slots = [None] * self.size
        self.ordered_list = []
        self.rehashed_slots = []
        self.slots_consumed = 0



    def hash(self, input_string, list_size):
        sum = 0
        for position in range(len(input_string)):
            sum = sum + ord(input_string[position]) * (position + 1)

        return sum % list_size

    def rehash(self, previous_hash, list_size):
        return (previous_hash + 1) % list_size

    def put(self, data):
        self._resize()
        hash_value = self.hash(data,self.size)
        print ""
        print "placing data %s" %(data)
        print "inital hash is %s" %(hash_value)
        if self.slots[hash_value] == None:
            self.slots[hash_value] = data
            print "data placed"
            self.slots_consumed = self.slots_consumed + 1
            self.ordered_list.append(data)
        else:
            if self.slots[hash_value] == data:
                print "duplicate. no insert"
                pass
            else:

                FLAG = False
                for i in range(self.size - self.slots_consumed):
                    next_slot = self.rehash(hash_value, len(self.slots))
                    print "current slot state"
                    print self.slots
                    print "next slot is %s" %(next_slot)
                    if self.slots[next_slot] == data:
                        print "data matches"
                        break
                    if self.slots[next_slot] is None:
                        print 'OK I am here'
                        self.slots[next_slot] = data
                        self.slots_consumed = self.slots_consumed + 1
                        self.ordered_list.append(data)
                        self.rehashed_slots.append(next_slot)
                        print "placing data here"
                        print self.slots
                        print "----"
                        break

                    else:
                        hash_value = next_slot
                        print "new hash value %s"  %(hash_value)
                """
                print "HERE"

                while self.slots[next_slot] is not None:
                        next_slot = self.rehash(next_slot, len(self.slots))
                        print "another slot post rehash %s" %(next_slot)
                        if self.slots[next_slot] is None:
                            print 'OK I am here'
                            self.slots[next_slot] = data
                            print "data placed post rehash"
                            self.slots_consumed = self.slots_consumed + 1
                            self.ordered_list.append(data)
                            self.rehashed_slots.append(next_slot)
                        break





                next_slot = self.rehash(hash_value, self.size)
                print "new nex slot is %s" %(next_slot)

                while self.slots[next_slot] != None and self.slots[next_slot] != data:
                    next_slot = self.rehash(next_slot, len(self.slots))
                    print "next slot post rehash is %s" %(next_slot)
                    if self.slots[next_slot] is None:
                        print "OK I AM HERE"
                        self.slots[next_slot] = data
                        print "data placed post rehash"
                        self.slots_consumed = self.slots_consumed + 1
                        self.ordered_list.append(data)
                        self.rehashed_slots.append(next_slot)
                    else:
                        pass
            """


    def get_ordered_list(self):
        #print self.rehashed_slots
        print "length of slots %s" %(len(self.slots))
        print "slots %s" %(self.slots)
        print "rehashed slot values %s" %(self.rehashed_slots)
        print "length of self ordered list %s" %(len(self.ordered_list))
        print "number of slots consumed %s" %(self.slots_consumed)
        return self.ordered_list


    def _resize(self):
        if self.slots_consumed > .75 * self.size:
            print "im getting reSized !!!"
            new_slots = self.size * [None]
            self.size = self.size * 2
            self.slots.extend(new_slots)
            tmp_rehashed_slots = self.rehashed_slots
            self.rehashed_slots = []
            while self.tmp_rehashed_slots != []:
                print "rehashed_slots"
                print self.tmp_rehashed_slots
                tmp_rehashed_slots_value = self.tmp_rehashed_slots.pop(0)
                data = self.slots[tmp_rehashed_slot_value]
                print data
                print "++++++"
                self.slots[tmp_rehashed_slot_value] = None
                self.put(data)
            print self.slots
            print "resizing done *****"






def random_string_generator(size=6, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def get_randomness_stat(some_list):
    # to see if data is random enough
    icount = {}
    for i in some_list:
        icount[i] = icount.get(i, 0) + 1
    print heapq.nlargest(100, icount.values())

def generate_emails():
    email_list = []
    while len(email_list) < 20:
        email_string = random_string_generator()
        if random.choice([True, False]):
            # if duplication set to true, duplicate by some duplication factor x 100
            # 0.25 factor is to increase the total unique values
            for _ in range(int(random.uniform(1, 10))):
                email_list.append(email_string)
        else:
            email_list.append(email_string)
    shuffled_email_list = random.sample(email_list, len(email_list))
    #get_randomness_stat(shuffled_email_list)
    return shuffled_email_list

# if using native dictionary
def remove_duplicates(emails):
    duplicate_free = {}
    for email in emails:
        duplicate_free[email] = 1
    return duplicate_free.keys()


# time to generate emails
#time_took = timeit.Timer("generate_emails()", "from __main__ import generate_emails")
#print time_took.timeit(1)

# removal of duplicates using python dictionary
#emails = generate_emails()
#print "length of emails using native dic"
#print len(remove_duplicates(emails))

#time_took = timeit.Timer("remove_duplicates(emails)", "from __main__ import remove_duplicates, emails")
#print time_took.timeit(1)

emails = ['vjecsz', 'vcrvtt', 'iklvur', 'vjecsz', 'vcrvtt', 'dbdmbm', 'dbdmbm', 'iklvur', 'vjecsz', 'vjecsz', 'dbdmbm', 'vjecsz', 'iklvur', 'vjecsz', 'vcrvtt', 'vcrvtt', 'dbdmbm', 'vjecsz', 'vcrvtt', 'dbdmbm', 'iklvur', 'vjecsz', 'vcrvtt', 'tfwclc', 'vcrvtt']


my_hash = OrderedHash()
start = time.time()
for item in emails:
    print "word generated %s" %(item)
    my_hash.put(item)
    print my_hash.get_ordered_list()
    print ""
stop = time.time()
duration = stop-start
print(duration)
"""
my_hash.put("tac")
my_hash.put("cat")
my_hash.put("cat")
my_hash.put("bat")
my_hash.put("cat")


print len(my_hash.get_ordered_list())
print len(remove_duplicates(emails))
print len(remove_duplicates(my_hash.get_ordered_list()))
"""
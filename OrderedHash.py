__author__ = 'smujoo'


#emails = ['vjecsz', 'vcrvtt', 'iklvur', 'vjecsz', 'vcrvtt', 'dbdmbm', 'dbdmbm', 'iklvur', 'vjecsz', 'vjecsz', 'dbdmbm', 'vjecsz', 'iklvur', 'vjecsz', 'vcrvtt', 'vcrvtt', 'dbdmbm', 'vjecsz', 'vcrvtt', 'dbdmbm', 'iklvur', 'vjecsz', 'vcrvtt', 'tfwclc', 'vcrvtt']




"""
Ordered hash is a modified hashmap implementation, which only implement
inserting of elements in hashmap. And in process storing the unique elements
in order

to store items using put method
to retrive ordered list use get_ordered_list method

"""
class OrderedHash():
    def __init__(self):
        self.size = 100000
        self.slots = [None] * self.size
        self.ordered_list = []
        self.rehashed_slots_list = []
        self.slots_consumed = 0
        self.resizeflag = False
        self.rehash_counter = 0

    def hash(self, input_string, list_size):

        sum = 0
        for position in range(len(input_string)):
            sum = sum + (ord(input_string[position]) * (position + 129))
        return int(((sum * 2731)% list_size))

    def rehash(self, previous_hash, list_size):
        self.rehash_counter = self.rehash_counter + 1
        return (previous_hash + 1299827) % list_size

    def _put_insert(self,hash_value, data):
        self.slots[hash_value] = data
        if not self.resizeflag:
            self.slots_consumed = self.slots_consumed + 1
            self.ordered_list.append(data)

        self.rehashed_slots_list.append(hash_value)


    def put(self, data):

        input_size = self.size
        hash_value = self.hash(data, input_size)
        if self.slots[hash_value] == None:
            self._put_insert(hash_value, data)
        else:
            if self.slots[hash_value] == data:
                pass
            else:
                hash_value = self.rehash(hash_value, self.size)
                for i in range(self.size - hash_value):
                    if self.slots[hash_value] == data:
                        break
                    if self.slots[hash_value] == None:
                        self._put_insert(hash_value, data)
                        break
                    else:
                        hash_value = self.rehash(hash_value, self.size)
            self._resize()

    def get_hash(self):
        return self.slots

    def get_ordered_list(self):
        return self.ordered_list

    def _resize(self):
        if self.slots_consumed > .7 * self.size:
            print "========= resizing started"
            self.resizeflag = True
            rehash_list = self.rehashed_slots_list
            self.rehashed_slots_list = []
            empty_slots_for_extention = self.size * [None]
            self.slots.extend(empty_slots_for_extention)
            self.size = self.size * 2
            for rehashed_index in rehash_list:
                tmp_data = self.slots[rehashed_index]
                self.slots[rehashed_index] = None
                self.put(tmp_data)
            print "========= resizing completed"
            self.resizeflag = False



__author__ = 'smujoo'

from flask import Flask
from flask import request
from flask import render_template
from OrderedHash import OrderedHash
import random
import string
import time

"""
functions for generating emails
"""
def random_string_generator(size=12, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def get_randomness_stat(some_list):
    icount = {}
    for i in some_list:
        icount[i] = icount.get(i, 0) + 1

def generate_emails():
    email_list = []
    while len(email_list) < 100000:
        email_string = random_string_generator()
        if random.choice([True, False]):
           for _ in range(int(random.uniform(1, 10))):
                email_list.append(email_string)
        else:
            email_list.append(email_string)
    shuffled_email_list = random.sample(email_list, len(email_list))
    return shuffled_email_list

"""
test function
"""
def test(emails):
    duplicate_free = {}
    for email in emails:
        duplicate_free[email] = 1
    return duplicate_free.keys()

def generate_sample(somelist):
    size_of_list = len(somelist)
    slice = random.choice(range(0,size_of_list-50))
    return somelist[slice:slice+50]

app = Flask(__name__)
@app.route('/')
def my_page():
    return render_template("ordered_hash_template.html")

@app.route('/', methods=['POST'])
def sort_email():
    # generating random email ids
    email_generation_start_time = time.strftime("%H:%M:%S", time.gmtime())
    print "generating emails at %s" %(email_generation_start_time)
    emails = generate_emails()

    # calling ordered hash to compute unique items
    start_time = time.strftime("%H:%M:%S", time.gmtime())
    print "started sorting emails to generate an ordered list at %s" %(start_time)
    myhash = OrderedHash()
    start = time.time()
    for email in emails:
        myhash.put(email)
    stop = time.time()
    stop_time = time.strftime("%H:%M:%S", time.gmtime())
    print "completed sorting emails to generate an ordered list at %s" %(stop_time)
    duration = stop-start
    unique_ids_using_ordered_hash = len(myhash.ordered_list)
    unique_ids_using_test = len(test(emails))

    sample_emails = generate_sample(emails)
    sample_ordered_list = generate_sample(myhash.ordered_list)
    return render_template('sort_stats.html', sample_emails=sample_emails, sample_ordered_list=sample_ordered_list, duration=duration, unique_ids_using_ordered_hash=unique_ids_using_ordered_hash, unique_ids_using_test=unique_ids_using_test)

if __name__ == '__main__':
    app.run()



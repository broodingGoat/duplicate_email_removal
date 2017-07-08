# duplicate_email_removal
```
This program sorts 100k random email user ids, with duplicates.
It generates 12 character random email IDs & repeats them randomly with duplicates.
To remove duplicates, I have implemented custom hashmap - OrderedHash

            1. Iterate over email list
            2. Implements insert, hash & rehashing to only store unique values
            3. When inserting a unique value it will update (in order) an internal array
            4. In order array does not get updated if a duplicate id insertion is attempted

On running the program, you will see:
            1. Sample of emails
            2. Sample of in order emails (with no duplicates)
            3. Stats & test
```

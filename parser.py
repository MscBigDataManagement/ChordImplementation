import hashlib
import random

def movies_hash(nodes, requests):
    
    hash_list = []

    with open('filenames.txt') as f:
        lines = random.sample(f.readlines(),requests)
        for line in lines:
            hash_object = hashlib.sha1(line)
            hash_key = int(hash_object.hexdigest(), 16) % ((2 ** nodes)-1)
            hash_list.append(hash_key)
            
    return hash_list


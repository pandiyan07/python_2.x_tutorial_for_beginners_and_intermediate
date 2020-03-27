# this sample python script program is a dictionary data structure library module and the contents will be imported to another file

def new(num_buckets=256):
	"""Initializes a map with the given number of buckets."""
	amap=[]
	for i in range(0, num_buckets):
		amap.append([])
	return amap

def hash_key(amap,key):
	"""given a key this will create a number and then convert a number and then convert it to an index for the amap's buckets."""
	return hash(key) %len(amap)
	
def get_bucket(amap,key):
	"""given a key, find the bucket where it would go"""
	bucket_id=hash_key(amap,key)
	return amap[bucket_id]
	
def get_slot(amap,key,default=None):
	"""Returns the index,key, and value of a slot found in a bucket.
	Returns -1,key , and default(none if not set) when not found.
	"""
	bucket=get_bucket(amap,key)
	for i,kv in enumerate(bucket):
		k,v=kv
		if key==k:
			return i,k,v
			
	return-1,key,default
	
def get(amap,key,default=None):
	"""Gets the value in a bucket for the given key, or the default."""
	i,k,v=get_slot(amap,key,default=default)
	return v
	
def set(amap,key,value):
	"""sets the key to the value. replacing any existing value."""
	bucket=get_bucket(amap,key)
	i,k,v=get_slot(amap,key)
	
	if i>=0:
		#the key exists,replace it
		bucket[i]=(key,value)
	else:
		#the key exists,replace it
		bucket.append((key,value))
		
def delete(amap,key):
	"""delets the given key from the map."""
	bucket=get_bucket(amap,key)
	
	for i in xrange(len(bucket)):
		k,v=bucket[i]
		if key==k:
			del bucket[i]
			break
			
def list(amap):
	"""prints out what's in the map"""
	for bucket in amap:
		if bucket:
			for k,v in bucket:
				print k,v
				
# end of the module.happy coding..!!
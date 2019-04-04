def main():
	
	arr = input().split()
	arr = [int(i) for i in arr]
	n = len(arr)

	freq = dict()
	bucket = [None for i in range(n+1)]

	for i in arr:
		if i in freq:
			freq[i] += 1
		else:
			freq[i] = 1

	for k,v in freq.items():
		if bucket[v] == None:
			bucket[v] = [k]
		else:
			bucket[v].append(k)

	for i in range(len(bucket)-1,0,-1):
		if bucket[i] != None:
			print(i,bucket[i])

main()



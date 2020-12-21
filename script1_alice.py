N=4
def alice_f_function(r, key, j):
        string = str(key) + str(j) + str(r)
        hash = get_md5_as_bytes(string)
        return hash
def bw_xor(b1, b2):
	arr = []
	size = len(b1)
	if len(b2) < size:
		size = len(b2)
	for i in range(size):
		arr.append(b1[i] ^ b2[i])
	return bytes(arr)
def abc(plaintext, K):
	L = plaintext[0:int(len(plaintext)/2)].encode()
	R = plaintext[int(len(plaintext)/2):len(plaintext)].encode()
	for i in range(2, N + 1):
		R_bak = R
		R = bw_xor(L, bytes(alice_f_function(R, key=K(i), j=i), encoding="UTF-8"))
		L = R_bak
import hashlib
def get_md5_as_bytes(data):
	m = hashlib.md5()
	m.update(data.encode())
	return m.hexdigest()[:4]

print("Input:")
plaintext = input()
list = []
print("Keys:")
for i in range(4):
	print("1.", end=" ")
	list.append(input())
def k(i):
	return list[i]
print(abc(plaintext, k))

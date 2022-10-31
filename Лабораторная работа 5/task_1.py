from pprint import pprint
dict_ = [{'dec': i, "bin": bin(i), "oct": oct(i), "hex": hex(i)} for i in range(0, 16)]
pprint(dict_)

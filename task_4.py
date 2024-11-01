import gostcrypto

hash_obj = gostcrypto.gosthash.new('streebog512')
oid_name = hash_obj.oid.name

print(oid_name)
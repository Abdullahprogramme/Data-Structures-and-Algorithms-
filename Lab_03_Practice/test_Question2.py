import pytest
import hashlib
from Question2 import Insert

insert_testcases = [
    ([None, None, None], 0, 'a', '134ee9beb24a226cc709c7365151d56a29d6c5e892d90a2122a7dd71861f58e5', '9bf4b5c1d663646e15eac5a644ee42b0b90740ebbf4afd76cfe061e66fe6c9a9'), 
    (['a', None, None], 1, 'b', '134ee9beb24a226cc709c7365151d56a29d6c5e892d90a2122a7dd71861f58e5', '26da2835afd041f34ebfc5a8e7a0582421933402fe77cd3fba8a23aedbbb6833'), 
    (['a', 'b', None], 2, 'c', '134ee9beb24a226cc709c7365151d56a29d6c5e892d90a2122a7dd71861f58e5', '8b7bff6e4f868e026388803fa14914c21d7e63da6197cdec8e88d75e7b3218bb'), 
    (['a', 'b', None], 4, 'e', 'a88ada13a2d454eaa7f2363f7c06c19d8328d10306baffb71139c2081bf35128', '26da2835afd041f34ebfc5a8e7a0582421933402fe77cd3fba8a23aedbbb6833'), 
    (['a', 'b', None], -1, 'e', 'a88ada13a2d454eaa7f2363f7c06c19d8328d10306baffb71139c2081bf35128', '26da2835afd041f34ebfc5a8e7a0582421933402fe77cd3fba8a23aedbbb6833'), 
    (['a', 'b', 'c'], 3, 'd', '71a7bcb2f28205b5712a8cc116ff4ebed793760be4d3209802de4eff77c83dc5', '8b7bff6e4f868e026388803fa14914c21d7e63da6197cdec8e88d75e7b3218bb'), 
    (['a'], 0, 'b', '71a7bcb2f28205b5712a8cc116ff4ebed793760be4d3209802de4eff77c83dc5', 'a326618a43c0b61aff497f4d8a82f4857fe952c5fae156ab94facf4adbf7dcb4')
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("list,index,element,output,result",insert_testcases)
def test_Insert(list,index,element,output,result):
    assert hashcode(Insert(list,index,element)) == output
    assert hashcode(list) == result
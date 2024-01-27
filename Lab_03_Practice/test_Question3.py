import pytest
import hashlib
from Question3 import Remove

remove_testcases = [
    ([10, 20, 30, 40, 50], 4, 'd8116103aeebda02e83f02448224e17cb44a78f61747ec2357fdd963ea986d10', '0837a13dc6529ae8a355c2f53ce26ed59c0a62cad8d05cdb36c8c19d48111657'), 
    ([10, 20, 30, 40, 50], 2, 'd8116103aeebda02e83f02448224e17cb44a78f61747ec2357fdd963ea986d10', '143eb0488e12ee5fdefe4bf3ddd18196ab065ede1138fca74fd2c1abfe86a863'), 
    ([10, 20, 40, 50, None], 0, 'd8116103aeebda02e83f02448224e17cb44a78f61747ec2357fdd963ea986d10', 'b79fab235453230e8ea3fc56ca8afa677cc88c35d916392312ae3998487d5208'), 
    ([20, 40, 50, None, None], 5, 'a88ada13a2d454eaa7f2363f7c06c19d8328d10306baffb71139c2081bf35128', 'b79fab235453230e8ea3fc56ca8afa677cc88c35d916392312ae3998487d5208'), 
    ([20, 40, 50, None, None], -1, 'a88ada13a2d454eaa7f2363f7c06c19d8328d10306baffb71139c2081bf35128', 'b79fab235453230e8ea3fc56ca8afa677cc88c35d916392312ae3998487d5208'), 
    ([None, None, None, None], 0, 'ba61eea246993d3ff552ff2645a632e9b743d05d0dd96a5cf93f3b472ab69c8a', '2023f50b8ba151cd10fdb2a83bd4cf75f645443e9303a516b1a78c90f269a310'), 
    ([None], 0, 'ba61eea246993d3ff552ff2645a632e9b743d05d0dd96a5cf93f3b472ab69c8a', '778d5d27b716881dd9d3b58baaed62878f93076984cf0cbb45d393bedf363cb2')
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("list,index,output,result",remove_testcases)
def test_Remove(list,index,output,result):
    assert hashcode(Remove(list,index)) == output
    assert hashcode(list) == result


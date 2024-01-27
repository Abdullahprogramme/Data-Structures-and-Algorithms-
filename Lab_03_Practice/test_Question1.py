import pytest
import hashlib

from Question1 import Initialize,Get,Set,Size,NumberOfElements,IsEmpty,IsFull

Initialize_testcases = [
    (5,"ed574e6bbc2fa787fa38baf99f0ca6903b20452f895756782f39391093ee957e"),
    (3,"b5848129e4ec6a5579ed8978bbbb50e9660cb676c4ddd56dc99e28b0db37bb21"),
    (0,"4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945"),
    (1,"778d5d27b716881dd9d3b58baaed62878f93076984cf0cbb45d393bedf363cb2")
]
Get_testcases = [
    ([10, 20, 30, 40, 50],0,"4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5"),
    ([10, 20, 30, 40, 50],1,"f5ca38f748a1d6eaf726b8a42fb575c3c71f1864a8143301782de13da2d9202b"),
    ([10, 20, 30, 40, 50],2,"624b60c58c9d8bfb6ff1886c2fd605d2adeb6ea4da576068201b6c6958ce93f4"),
    ([10, 20, 30, 40, 50],3,"d59eced1ded07f84c145592f65bdf854358e009c5cd705f5215bf18697fed103"),
]

Set_testcases = [
    ([10, 20, 30, 40, 50],0,60,"90447120d70cb0a99b1027cd6377b709b360ac81f806edfde4704350e3db8aa8"),
    ([10, 20, 30, 40, 50],1,60,"aa1a666feb499ce240fa851b5a029ba95d80c09ca86b45ba5c0e273f9cbff45b"),
    ([10, 20, 30, 40, 50],2,60,"abf8ed3903d4b113230ac53a0e0295eda5dafa4bfd81643130eba33eca47f752"),
    ([10, 20, 30, 40, 50],3,60,"84c1004425e0eae2afdcf73cec807514276ceff51d48a29b343e14087fec235f"),
]

Size_testcases = [
    ([10, 20, 30, 40, 50],"ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d"),
    ([42],"6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"),
    ([10,None,None],"4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce"),
    ([None,None,None],"4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce")
]


NumberOfElements_testcases = [
    ([10, 20, 30, 40, 50],"ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d"),
    ([42],"6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"),
    ([10,None,None],"6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"),
    ([None,None,None],"5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9")
]

IsFull_testcases = [
    ([10, 20, 30, 40, 50],"3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18"),
    ([42],"3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18"),
    ([10,None,None],"60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe"),
    ([None,None,None],"60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe")
]

IsEmpty_testcases = [
    ([10, 20, 30, 40, 50],"60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe"),
    ([42],"60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe"),
    ([10,None,None],"60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe"),
    ([None,None,None],"3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18")
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("n,result",Initialize_testcases)
def test_Initialize(n,result):
    assert hashcode(Initialize(n)) == result

@pytest.mark.parametrize("list,index,result",Get_testcases)
def test_Get(list,index,result):
    assert hashcode(Get(list,index)) == result

@pytest.mark.parametrize("list,index,value,result",Set_testcases)
def test_Set(list,index,value,result):
    Set(list,index,value)
    assert hashcode(list) == result

@pytest.mark.parametrize("list,result",Size_testcases)
def test_Size(list,result):
    assert hashcode(Size(list)) == result

@pytest.mark.parametrize("list,result",NumberOfElements_testcases)
def test_NumberOfElements(list,result):
    assert hashcode(NumberOfElements(list)) == result

@pytest.mark.parametrize("list,result",IsFull_testcases)
def test_IsFull(list,result):
    assert hashcode(IsFull(list)) == result

@pytest.mark.parametrize("list,result",IsEmpty_testcases)
def test_IsEmpty(list,result):
    assert hashcode(IsEmpty(list)) == result
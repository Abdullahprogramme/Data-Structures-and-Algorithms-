import pytest
import hashlib
from Question4 import InsertAtStart

insert_at_start_testcases = [
    ([None, None], 'a', '134ee9beb24a226cc709c7365151d56a29d6c5e892d90a2122a7dd71861f58e5', '3ab8d220bfe98366a8885ea3d26ff7bc8e1b4377e5fc080ab3a1f32354aa3175'), 
    (['a', None], 'b', '134ee9beb24a226cc709c7365151d56a29d6c5e892d90a2122a7dd71861f58e5', 'f9c31f7e1418d5930e9d8fc48189670976826b4cea4b7aa6a3c2db491e1533c7'), 
    (['a', 'b'], 'c', '71a7bcb2f28205b5712a8cc116ff4ebed793760be4d3209802de4eff77c83dc5', 'd26dae360fbeede3ae287f208ab879bce83f31c43218c75cd09e6a408f84a755'), 
    (['b'], 'c', '71a7bcb2f28205b5712a8cc116ff4ebed793760be4d3209802de4eff77c83dc5', 'd4a37d37ced8324ba67f3773dfbc749ff4db6deb8e95e2e9580e2e11e4e243be')
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("list,element,output,final",insert_at_start_testcases)
def test_InsertAtStart(list,element,output,final):
    assert hashcode(InsertAtStart(list,element)) == output
    assert hashcode(list) == final
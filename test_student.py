
from student import StudentDB
import pytest
#db=None
#Setup and Teardown method (to  open and close something before executing your code and before terminating it so it prevents the initialization of your database again and again)

"""
def setup_module(module):
    print('---------------setup---------------')
    global db
    db=StudentDB()
    db.connect('data.json')

def teardown_module(module):
    print('---------teardown------------')
    db.close()

"""

#alternatively fixtures can also be used here
#but here setup is called twice to solve this write scope=module in pytest decorator

@pytest.fixture(scope='module')
def db():
    print('---------------setup---------------')
    global db
    db=StudentDB()
    db.connect('data.json')
    yield db
    print('---------teardown------------')
    db.close()

def test_ram_data(db):
    ram_data=db.get_data('Ram')
    assert ram_data['id'] ==1
    assert ram_data['name'] =='Ram'
    assert ram_data['result'] =='pass'

def test_mohini_data(db):
    mohini_data=db.get_data('Mohini')
    assert mohini_data['id'] ==2
    assert mohini_data['name'] =='Mohini'
    assert mohini_data['result'] =='fail'
import pytest , session5 , re , inspect , os


#1 Inavlid Temperature Type Check
def test_invalidtemperature():
    with pytest.raises(NotImplementedError):
       session5.temp_converter(temp = 32 , temp_given_in = 'x')


#2 README Exists
def test_readmeexist():
    assert os.path.isfile("README.md") , 'README File is missing'


#5 identation check
def test_identation():
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.',lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space) , 'Your code identation does not follow PEP8 guidelines'
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0 , 'Your code doesnot follow PEP8 guidelines'


#4 Out of Range Polygon check.
def test_notvalidpolygon():
    with pytest.raises(NotImplementedError):
        session5.polygon_area(side_length = 5 , side = 10)


 

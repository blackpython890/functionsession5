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


#5 README formatting
def test_readme_for_formatting():
    readme = open('README.md','r')
    content = readme.read()
    readme.close()
    assert content.count('#') >= 5 , "Kindly format the README.md"


#6 speed_converter  negative check
def test_speed_negative_check():
    with pytest.raises(ValueError):
        session5.speed_converter(speed = -10 , dist = 'km' , time = 'ms' )



#7 Ploygon side length negative
def test_negative_side_length():
    with pytest.raises(ValueError):
        session5.polygon_area( side_length = -3 , side = 9)



#8 speed_converter  dist valid check
def test_valid_dist_check():
    with pytest.raises(ValueError):
        session5.speed_converter(speed = 10 , dist = 0 , time = 'ms')


#9 speed_converter Time valid check
def test_valid_time_check():
    with pytest.raises(ValueError):
        session5.speed_converter(speed = -100 , dist = 'KM' , time = 0)


#10 speed_converter wrong combination arguments.
def test_wrong_combination_input():
    with pytest.raises(ValueError):
        session5.speed_converter(speed = 200 , dist = 'KM' , time = 'lightyear')


#11 Function name had caps letter
def test_funcation_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction )
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"



#12 

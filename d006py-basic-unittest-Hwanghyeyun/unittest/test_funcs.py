# TODO: 사용자 모듈 import

from basic_func import check_num,check_avg,max_num,min_num




def test_check_num():
    assert check_num(2) == True
    assert check_num(3) == False
    assert check_num(0) == True
    assert check_num(-1) == False


def test_max_num():
    assert max_num([1, 2, 3]) == 3
    assert max_num([100, 99, 98]) == 100
    assert max_num([-5, -2, -10]) == -2


def test_min_num():
    assert min_num([1, 2, 3]) == 1
    assert min_num([100, 99, 98]) == 98
    assert min_num([-5, -2, -10]) == -10


def test_check_avg(capfd):  
    check_avg([1, 2, 3, 4])   
    out, err = capfd.readouterr()
    assert out.strip() == "2.5"

    check_avg([10, 20, 30])
    out, err = capfd.readouterr()
    assert out.strip() == "20.0"






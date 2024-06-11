from project import check_correct_args,select_house,select_grade
import pytest

def test_check_correct_args():
    with pytest.raises(SystemExit):
        check_correct_args()


def test_select_house():
    assert select_house("courage")=="Gryffindor"
    assert select_house("loyalty")=="Gryffindor"
    assert select_house("adventure")=="Gryffindor"
    assert select_house("dedication")=="Hufflepuff"
    assert select_house("patience")=="Hufflepuff"
    assert select_house("honesty")=="Hufflepuff"
    assert select_house("wisdom")=="Ravenclaw"
    assert select_house("creativity")=="Ravenclaw"
    assert select_house("perfectionism")=="Ravenclaw"
    assert select_house("ambition")=="Slytherin"
    assert select_house("competitive")=="Slytherin"
    assert select_house("leadership")=="Slytherin"
    assert select_house("house")=="No House"


def test_select_grade():
    assert select_grade(2004)=="Grade 15"
    assert select_grade(2008)=="Grade 11"
    assert select_grade(2006)=="Grade 13"
    assert select_grade(2005)=="Grade 14"
    assert select_grade(2010)=="Grade 9"
    assert select_grade(2012)=="Grade 7"

import Lab2.bmi as bmi

print("Test_bmi")

def test_bmi_normal_weight():
    result =bmi.calculate_bmi(1.73, 57) #BMI = 19.0)
    assert(result ==0)


def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.70, 90)   # BMI 31.1
    assert (result == 1)



def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.80, 50)   # BMI 15.4
    assert (result == -1)

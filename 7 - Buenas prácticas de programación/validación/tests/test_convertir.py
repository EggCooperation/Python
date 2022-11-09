from validación import convertir


def test_convertir_a_int():
    assert convertir.a_int(1) == 1
    assert convertir.a_int(-1) == -1
    assert convertir.a_int(0) == 0
    assert convertir.a_int("1") == 1
    assert convertir.a_int("-1") == -1
    assert convertir.a_int("0") == 0
    assert convertir.a_int(" 1 ") == 1
    assert convertir.a_int("+1") == 1
    assert convertir.a_int(+23) == 23
    assert convertir.a_int(-23) == -23
    assert convertir.a_int("") == False
    assert convertir.a_int(1.1) == False
    assert convertir.a_int("1.1") == False
    assert convertir.a_int("++1") == False
    assert convertir.a_int(23j) == False
    assert convertir.a_int([1]) == False


def test_convertir_a_float():
    assert convertir.a_float(1) == 1.0
    assert convertir.a_float(-1) == -1.0
    assert convertir.a_float(0) == 0
    assert convertir.a_float("1") == 1.0
    assert convertir.a_float("-1") == -1.0
    assert convertir.a_float("0") == 0
    assert convertir.a_float(" 1 ") == 1.0
    assert convertir.a_float("+1") == 1.0
    assert convertir.a_float("++1") == False
    assert convertir.a_float("-1") == -1.0
    assert convertir.a_float(" +1 ") == 1.0
    assert convertir.a_int("") == False
    assert convertir.a_float(1j) == False
    assert convertir.a_float([1]) == False
    assert convertir.a_float("") == False


def test_convertir_a_str():
    assert convertir.a_str("str") == "str"
    assert convertir.a_str("") == ""
    assert convertir.a_str(1) == "1"
    assert convertir.a_str(1.1) == "1.1"
    assert convertir.a_str(True) == False
    assert convertir.a_str([1]) == False

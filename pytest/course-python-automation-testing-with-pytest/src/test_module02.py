
class TestMyStuff():
    def test_type(self):
        assert type(1) == int

    def test_mistype(self):
        #assert type(1) == float, "This will fail"
        assert type(1.0) == float, "This will fail"


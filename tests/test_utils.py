from read_and_close import read_and_close


def test_read_and_close():
    contents = read_and_close('tests/somefile.txt')

    assert contents == 'hello\nworld\nthis\nis a file\n'

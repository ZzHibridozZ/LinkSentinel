import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from link_validator import check_link, find_links_in_file, scan_directory

# Sample content for test files
md_content = """
This is a test [valid link](http://example.com).
And a [broken link](http://broken-link.test).
"""

rst_content = """
This is a test `valid link <http://example.com>`_.
And a `broken link <http://broken-link.test>`_.
"""


@pytest.fixture
def tmp_md_file(tmp_path):
    file = tmp_path / "test.md"
    file.write_text(md_content)
    return file


@pytest.fixture
def tmp_rst_file(tmp_path):
    file = tmp_path / "test.rst"
    file.write_text(rst_content)
    return file


def test_find_links_in_md(tmp_md_file):
    links = find_links_in_file(tmp_md_file)
    assert "http://example.com" in links
    assert "http://broken-link.test" in links


def test_find_links_in_rst(tmp_rst_file):
    links = find_links_in_file(tmp_rst_file)
    assert "http://example.com" in links
    assert "http://broken-link.test" in links


def test_check_link_success(monkeypatch):
    monkeypatch.setattr(
        "link_validator.requests.head",
        lambda url, **kwargs: type("obj", (object,), {"status_code": 200})(),
    )
    ok, status = check_link("http://example.com")
    assert ok
    assert status == 200


def test_check_link_failure(monkeypatch):
    import requests

    def raise_exc(*args, **kwargs):
        raise requests.ConnectionError("Connection error")

    monkeypatch.setattr("link_validator.requests.head", raise_exc)
    ok, err = check_link("http://broken-link.test")
    assert not ok
    assert "Connection error" in err


def test_scan_directory(tmp_path, monkeypatch):
    # create md and rst files
    md_file = tmp_path / "test.md"
    md_file.write_text(md_content)

    rst_file = tmp_path / "test.rst"
    rst_file.write_text(rst_content)

    # Mock responses: example.com success, broken-link.test fail
    def mock_head(url, **kwargs):
        class Resp:
            def __init__(self, code):
                self.status_code = code

        if "example.com" in url:
            return Resp(200)
        else:
            return Resp(404)

    monkeypatch.setattr("link_validator.requests.head", mock_head)

    broken = scan_directory(tmp_path)
    assert any("http://broken-link.test" == b["link"] for b in broken)
    assert all(b["link"] != "http://example.com" for b in broken)

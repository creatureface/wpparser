import pytest

from wpparser import parse


def test_parse(sample_export):
    result = parse(sample_export)

    assert len(result["posts"]) == 3
    assert result["blog"]["title"] == "Blog"
    assert len(result["categories"]) == 1
    assert len(result["tags"]) == 1


def test_attachment_metadata(sample_export):
    result = parse(sample_export)

    post = result["posts"][2]

    assert "postmeta" in post
    assert "attached_file" in post["postmeta"]
    assert "attachment_metadata" in post["postmeta"]

    attached_file = post["postmeta"]["attached_file"]
    assert attached_file == "logo-promo.png"


def test_blog_metadata(sample_export):
    result = parse(sample_export)
    blog = result["blog"]

    assert blog["title"] == "Blog"
    assert blog["tagline"] == "Just another WordPress site"
    assert blog["language"] == "en-US"
    assert blog["site_url"] == "http://marteinn.se/blog"
    assert blog["blog_url"] == "http://marteinn.se/blog"


def test_authors(sample_export):
    result = parse(sample_export)
    authors = result["authors"]

    assert len(authors) == 1

    author = authors[0]
    assert author["login"] == "admin"
    assert author["email"] == "martin@marteinn.se"
    assert author["display_name"] == "admin"
    assert author["first_name"] is None
    assert author["last_name"] is None


def test_category_structure(sample_export):
    result = parse(sample_export)
    categories = result["categories"]

    assert len(categories) == 1
    cat = categories[0]
    assert cat["term_id"] == "1"
    assert cat["nicename"] == "uncategorized"
    assert cat["name"] == "Uncategorized"
    assert cat["parent"] is None
    assert cat["children"] == []


def test_tags(sample_export):
    result = parse(sample_export)
    tags = result["tags"]

    assert len(tags) == 1
    tag = tags[0]
    assert tag["term_id"] == "1"
    assert tag["slug"] == "bash"
    assert tag["name"] == "Bash"


def test_post_fields(sample_export):
    result = parse(sample_export)
    post = result["posts"][0]

    assert post["title"] == "Hello world!"
    assert post["content"] == "Welcome to WordPress. This is your first post. Edit or delete it, then start blogging!"
    assert post["post_date"] == "2014-09-26 18:47:05"
    assert post["post_date_gmt"] == "2014-09-26 18:47:06"
    assert post["status"] == "publish"
    assert post["post_type"] == "post"
    assert post["post_id"] == "1"
    assert post["post_name"] == "hello-world"
    assert post["creator"] == "admin"
    assert post["ping_status"] == "open"
    assert post["menu_order"] == "0"
    assert post["is_sticky"] == "0"


def test_post_modified_fields(sample_export):
    result = parse(sample_export)
    post = result["posts"][0]

    assert "post_modified" in post
    assert "post_modified_gmt" in post


def test_page_post_type(sample_export):
    result = parse(sample_export)
    page = result["posts"][1]

    assert page["title"] == "Sample Page"
    assert page["post_type"] == "page"


def test_comments(sample_export):
    result = parse(sample_export)
    post = result["posts"][0]
    comments = post["comments"]

    assert len(comments) == 1
    comment = comments[0]
    assert comment["id"] == "1"
    assert comment["author"] == "Mr WordPress"
    assert comment["author_url"] == "https://wordpress.org/"
    assert comment["date"] == "2014-09-26 18:47:05"
    assert comment["date_gmt"] == "2014-09-26 18:47:06"
    assert comment["approved"] == "1"
    assert comment["parent"] == "0"
    assert comment["user_id"] == "0"
    assert "Hi, this is a comment." in comment["content"]


def test_missing_channel_raises_valueerror(tmp_path):
    xml_content = '<?xml version="1.0" encoding="UTF-8" ?><rss version="2.0"></rss>'
    xml_file = tmp_path / "invalid.xml"
    xml_file.write_text(xml_content)

    with pytest.raises(ValueError, match="missing <channel> element"):
        parse(str(xml_file))


def test_post_categories_domain(sample_export):
    result = parse(sample_export)
    post = result["posts"][0]

    assert "category_category" in post
    cats = post["category_category"]
    assert len(cats) == 1
    assert cats[0]["nicename"] == "uncategorized"
    assert cats[0]["text"] == "Uncategorized"

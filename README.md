# wpparser

This library parses WordPress XML exports into a Python dictionary.

## Installation

```bash
pip install wpparser
```

## Usage

```python
import wpparser

data = wpparser.parse("./blog.wordpress.2014-09-26.xml")
```

## What it returns

A dictionary containing:

- **blog**: General blog information (title, tagline, site url, etc.)
- **authors**: List of authors
- **categories**: Categories organized as a nested tree
- **tags**: List of tags
- **posts**: List of posts, including comments and post metadata

### Example

```python
{
    "blog": {
        "tagline": "Tagline",
        "site_url": "http://marteinn.se/blog",
        "blog_url": "http://marteinn.se/blog",
        "language": "en-US",
        "title": "Marteinn / Blog",
    },
    "authors": [
        {
            "login": "admin",
            "last_name": None,
            "display_name": "admin",
            "email": "martin@marteinn.se",
            "first_name": None,
        }
    ],
    "categories": [
        {
            "parent": None,
            "term_id": "3",
            "name": "Action Script",
            "nicename": "action-script",
            "children": [
                {
                    "parent": "action-script",
                    "term_id": "20",
                    "name": "Flash related",
                    "nicename": "flash-related",
                    "children": [],
                }
            ],
        }
    ],
    "tags": [{"term_id": "1", "slug": "bash", "name": "Bash"}],
    "posts": [
        {
            "creator": "admin",
            "excerpt": None,
            "post_date_gmt": "2014-09-22 20:10:40",
            "post_date": "2014-09-22 21:10:40",
            "post_type": "post",
            "menu_order": "0",
            "guid": "http://marteinn.se/blog/?p=828",
            "title": "Post Title",
            "comments": [
                {
                    "date_gmt": "2014-09-24 23:08:31",
                    "parent": "0",
                    "date": "2014-09-25 00:08:31",
                    "id": "85929",
                    "user_id": "0",
                    "author": "Author",
                    "author_email": None,
                    "author_ip": "111.111.111.111",
                    "approved": "1",
                    "content": "Comment title",
                    "author_url": "http://example.com",
                    "type": "pingback",
                }
            ],
            "content": "Text",
            "post_parent": "0",
            "post_password": None,
            "status": "publish",
            "description": None,
            "tags": ["tag"],
            "ping_status": "open",
            "post_id": "1",
            "link": "http://www.marteinn.se/blog/slug/",
            "pub_date": "Mon, 22 Sep 2014 20:10:40 +0000",
            "categories": ["category"],
            "is_sticky": "0",
            "post_name": "slug",
        }
    ],
}
```

## Contributing

Want to contribute? Awesome. Just send a pull request.

## License

wpparser is released under the [MIT License](http://www.opensource.org/licenses/MIT).

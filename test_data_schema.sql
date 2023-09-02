
-- insert multiple rows of test data into post
INSERT INTO post (title, body) VALUES
  ("First post", '---
title: "Exploring the Wonders of Markdown"
date: 2023-09-02
author: "John Doe"
---

# Exploring the Wonders of Markdown

Markdown is a lightweight markup language that makes it easy to format text. In this post, we''ll explore its various features and show how it can make your writing experience more efficient and enjoyable.

![Markdown Logo](https://example.com/path/to/markdown-logo.png)

## Why Use Markdown?

Markdown offers several advantages:

- **Simplicity**: Its syntax is straightforward, making it easy to learn.
- **Portability**: Markdown files are just plain text, so they can be opened and edited with any text editor.
- **Flexibility**: It''s used in many platforms like GitHub, forums, and many blogging platforms.

## Basic Markdown Syntax

### Headers

You can create headers using the `#` symbol:

# H1
## H2
### H3
#### H4
##### H5
###### H6

### Emphasis

Use `*` or `_` for italics and `**` or `__` for bold:

*italic* or _italic_
**bold** or __bold__

### Lists

- Item 1
- Item 2
  - Subitem 2.1
  - Subitem 2.2

1. First item
2. Second item
3. Third item

### Links and Images

[Google](https://www.google.com)

![Alt Text for Image](https://example.com/path/to/image.jpg)

## Conclusion

Markdown is an incredibly powerful tool for writing and formatting text. Whether you''re a blogger, a developer, or just someone who likes to write, Markdown can help streamline your writing process.

---

*Thanks for reading! For more tips and tricks on using Markdown, stay tuned to this blog.*

  '),
  ("Second post", "This is my second post."),
  ("Third post", "This is my third post.");

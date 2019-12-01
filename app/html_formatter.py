class HtmlFormatter:
    head = """<!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <title>Anthony Asp's CS Club Project</title>
        <meta name="author" content="Anthony Asp">
        <meta name="description" content="This page was a project for the Seattle Central College CS Club">
        <link href="style.css" rel="stylesheet" type="text/css" />
    </head>"""
    body_top = """<body>
        <header>Anthony Asp's CS Club
            <br>Database Project</header>
        <div id="container">
            <div id="buttons">

                <div class="button">
                    <a href="index.html"> data 1</a>
                </div>
                <div class="button">
                    <a href="index1.html"> data 2</a>
                </div>
                <div class="button">
                    datal 3
                </div>
                """

    body_bottom = """        </div>
        </div>
    </body>

    </html>"""

    def __init__(self, img_html, html_file_name):
        self.img_html = img_html
        self.html_file_name = html_file_name

    def main(self):
        self.write_to_file(self.format())

    def format(self):
        return self.head + self.body_top + self.img_html + self.body_bottom


    def write_to_file(self, contents):
        with open(f"../{self.html_file_name}", 'w') as f:
            f.write(contents)

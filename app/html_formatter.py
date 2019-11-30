class HtmlFormatter:
    head = """<!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <title>Title</title>
        <link href="style.css" rel="stylesheet" type="text/css" />
    </head>"""
    body_top = """<body>
        <header>Anthony Asp's CS Club
            <br>Database Project</header>
        <div id="container">
            <div id="buttons">

                <div class="button">
                    data 1
                </div>
                <div class="button">
                    data 2
                </div>
                <div class="button">
                    datal 3
                </div>"""

    body_bottom = """        </div>
        </div>
    </body>

    </html>"""

    def __init__(self, img_html):
        self.img_html = img_html

    def main(self):
        self.write_to_file(self.format())

    def format(self):
        return self.head + self.body_top + self.img_html + self.body_bottom

    @staticmethod
    def write_to_file(contents):
        with open("../index.html", 'w') as f:
            f.write(contents)

#! /usr/bin/env python3

'''
Code required to generate html with Python.
'''


import webbrowser
import sys


output_url = 'example.html'
header_title = 'Example'
header_id = 'example'


def main():
    original_stdout = sys.stdout
    sys.stdout = open(output_url, 'w')
    html_header(
        headertitle=header_title,
        headerid=header_id
    )
    # Say we want to print two graphs per printer page
    print(
        '<p>'
        '<figure>'
        '<img src="path_to_your_graph_1.png" alt="alternate text graph 1"/>'
        '<figcaption>Caption for your graph 1</figcaption>'
        '</figure>'
        '</p>'
    )
    print(
        '<p>'
        '<figure>'
        '<img src="path_to_your_graph_2.png" alt="alternate text graph 2"/>'
        '<figcaption>Caption for your graph 2</figcaption>'
        '</figure>'
        '</p>'
    )
    page_break()
    print(
        '<p>'
        '<figure>'
        '<img src="path_to_your_graph_3.png" alt="alternate text graph 3"/>'
        '<figcaption>Caption for your graph 3</figcaption>'
        '</figure>'
        '</p>'
    )
    print(
        '<p>'
        '<figure>'
        '<img src="path_to_your_graph_4.png" alt="alternate text graph 4"/>'
        '<figcaption>Caption for your graph 4</figcaption>'
        '</figure>'
        '</p>'
    )
    html_footer()
    sys.stdout.close()
    sys.stdout = original_stdout
    webbrowser.open_new_tab(output_url)


def html_header(
    headertitle: str = 'Report',
    headerid: str = 'report'
) -> None:
    '''
    Creates an html header.
    '''

    print('<!DOCTYPE html>')
    print('<html lang="" xml:lang="" xmlns="http://www.w3.org/1999/xhtml">')
    print('<head>')
    print('<meta charset="utf-8"/>')
    print(
        '<meta content="width=device-width, initial-scale=1.0, '
        'user-scalable=yes" name="viewport"/>'
    )
    print('<style type="text/css">@import url("support.css");</style>')
    print(f'<title>{headertitle}</title>')
    print('</head>')
    print('<body>')
    print(
        f'<h1 class="title"'
        f' id="{headerid}">'
        f'{headertitle}</h1>'
    )
    print('<pre>')


def html_footer() -> None:
    '''
    Creates an html footer.
    '''

    print('</pre>')
    print('</body>')
    print('</html>')


def page_break():
    '''
    Create a page break for html output.
    '''

    print('<p style="page-break-after:always">')
    print('<p style="page-break-before:always"')


if __name__ == '__main__':
    main()

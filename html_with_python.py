#! /usr/bin/env python3
'''
Code required to generate html with Python.

Originally creted with built-in functions. Now uses datasense.
'''
import datasense as ds

output_url = 'example.html'
header_title = 'Example'
header_id = 'example'


def main():
    original_stdout = ds.html_begin(
        outputurl=output_url,
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
    ds.page_break()
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
    ds.html_end(
        originalstdout=original_stdout,
        outputurl=output_url
    )


if __name__ == '__main__':
    main()

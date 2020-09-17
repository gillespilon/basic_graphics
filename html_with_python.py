#! /usr/bin/env python3
'''
Code required to generate html with Python.
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
    listi = ['path1', 'path2', 'path3', 'path4']
    listj = ['altext1', 'alttext2', 'alttext3', 'alttext4']
    listk = ['caption1', 'caption2', 'caption3', 'caption4']
    listl = [False, True, False, False]
    for i, j, k, l in zip(listi, listj, listk, listl):
        print(
            '<p>'
            '<figure>'
            f'<img src="{i}.png" alt="{j}"/>'
            f'<figcaption>{k}</figcaption>'
            '</figure>'
            '</p>'
        )
        if l:
            ds.page_break()
    ds.html_end(
        originalstdout=original_stdout,
        outputurl=output_url
    )


if __name__ == '__main__':
    main()

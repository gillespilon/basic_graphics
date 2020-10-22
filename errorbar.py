#! /usr/bin/env python3
"""
Errorbar survery analysis

./errorbar.py
"""

import time
import math

import matplotlib.pyplot as plt
import datasense as ds


def main():
    start_time = time.time()
    figsize = (8, 4.5)
    output_url = 'risk_survey.html'
    header_title = 'risk_survey'
    header_id = 'risk-survey'
    graph_file_name = 'risk_survey_question'
    questions = [
        'Business continuity plan',
        'Updated annually',
        'Back-up generator',
        'Electronic storage',
        'Daily off-site backup',
        'Encrypted data',
        'Breach or near-breach',
        'Require suppliers business continuity plan',
        'Multiple suppliers & sources qualified',
        'Leadership change',
        'Covid-19 government loans',
        'Concern about repaying on time',
        'Percentage Molex business',
        'Lawsuits or liens',
        'Reductions and restructuring',
        'Facility control',
        'Security 24-7',
        'CCTV 24-7',
        'Sprinkler or fire suppression',
        'Limit visitors',
        'Open capacity',
        'Cross-trained',
        'Disaster recovery define process',
        'Additional capacity'
    ]
    question_numbers = [
        1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6,
        2.0, 2.1,
        3.0, 3.11, 3.12, 3.2, 3.3, 3.4,
        4.0, 4.1, 4.2,
        5.0, 5.1,
        6.0, 6.1, 6.2, 6.3
    ]
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    print('<pre style="white-space: pre-wrap;">')
    print('This report is a mock-up.')
    ds.page_break()
    for question, question_number in zip(questions, question_numbers):
        y = ds.random_data(
            distribution='randint',
            size=2000,
            low=1,
            high=3,
            scale=1
        )
        no = y.value_counts('1')[1]
        yes = y.value_counts(['2'])[2]
        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(111)
        ax.errorbar(
            ['1', '2'],
            [no, yes],
            yerr=[
                1.96 * math.sqrt(no * (1 - no) /
                                 (y.value_counts()[1] + y.value_counts()[2])),
                1.96 * math.sqrt(yes * (1 - yes) /
                                 (y.value_counts()[1] + y.value_counts()[2]))
            ],
            ls='None',
            marker='o',
            color='b',
            ecolor='r',
            markersize=4
        )
        ax.set_xlim(-1, 2)
        # ax.set_ylim(0, 1)
        ax.set_xlabel(xlabel='Answer', fontweight='bold', fontsize=12)
        ax.set_ylabel(ylabel='Proportion', fontweight='bold', fontsize=12)
        ax.set_xticks(['1', '2'])
        ax.set_xticklabels(['no', 'yes'])
        fig.suptitle(
            t=f'Question {question_number}\n{question}',
            fontweight='bold', fontsize=15
        )
        for proportion, count, x, y in zip(
            [y.value_counts('1')[1], y.value_counts('2')[2]],
            [y.value_counts()[1], y.value_counts()[2]],
            ['1', '2'],
            [no, yes]
        ):
            ax.annotate(
                text=f'p = {proportion}',
                xy=(x, y),
                xytext=(10, 5),
                textcoords="offset points"
            )
            ax.annotate(
                text=f'n = {count}',
                xy=(x, y),
                xytext=(10, -5),
                textcoords="offset points"
            )
        ds.despine(ax)
        fig.savefig(f'{graph_file_name}_{question_number}.svg', format='svg')
        print(
            f'<p><img src="{graph_file_name}_'
            f'{question_number}.svg"/></p>'
        )
        plt.close()
    stop_time = time.time()
    ds.page_break()
    ds.report_summary(
        start_time=start_time,
        stop_time=stop_time
    )
    print('</pre>')
    ds.html_end(
        original_stdout=original_stdout,
        output_url=output_url
    )


if __name__ == '__main__':
    main()

#! /usr/bin/env python3
"""
Errorbar survey analysis

./errorbar.py
"""

import time
import math

import matplotlib.pyplot as plt
from scipy import stats
import datasense as ds
import pandas as pd


def main():
    start_time = time.time()
    size = 2000
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
        'Percentage of business',
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
        'Additional capacity',
        'q25',
        'q26',
        'q27',
        'q28',
        'q29',
        'q30'
    ]
    question_numbers = [
        1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6,
        2.0, 2.1,
        3.0, 3.11, 3.12, 3.2, 3.3, 3.4,
        4.0, 4.1, 4.2,
        5.0, 5.1,
        6.0, 6.1, 6.2, 6.3,
        25, 26, 27, 28, 29, 30
    ]
    question_colum = [
        'Q01', 'Q02', 'Q03', 'Q04', 'Q05', 'Q06', 'Q07', 'Q08', 'Q09', 'Q10',
        'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19', 'Q20',
        'Q21', 'Q22', 'Q23', 'Q24', 'Q25', 'Q26', 'Q27', 'Q28', 'Q29', 'Q30',
    ]
    question_columns = [
        'Q01', 'Q02', 'Q03', 'Q04', 'Q05', 'Q06', 'Q07', 'Q08', 'Q09', 'Q10',
        'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19', 'Q20',
        'Q21', 'Q22', 'Q23', 'Q24', 'Q25', 'Q26', 'Q27', 'Q28', 'Q29', 'Q30',
    ]
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    print('<pre style="white-space: pre-wrap;">')
    print('This report is a mock-up.')
    number_questions = len(question_numbers)
    print('Number of questions: ', number_questions)
    supplier = pd.Series(
        data=list(range(1, size + 1, 1)),
        name='Supplier'
    )
    data = create_dataframe(size=size)
    data = pd.concat([data, supplier], axis=1)
    ds.page_break()
    for question, question_number, question_column in\
            zip(questions, question_numbers, question_columns):
        no = data[question_column].value_counts('1')[1]
        yes = data[question_column].value_counts(['2'])[2]
        fig, ax = plt.subplots(
            nrows=1,
            ncols=1,
            figsize=figsize
        )
        ax.errorbar(
            x=['1', '2'],
            y=[no, yes],
            yerr=[
                stats.t.isf(q=.025, df=size-2) *
                math.sqrt(no * (1 - no) / (
                    data[question_column].value_counts()[1] +
                    data[question_column].value_counts()[2]
                )),
                stats.t.isf(q=.025, df=size-2) *
                math.sqrt(yes * (1 - yes) / (
                    data[question_column].value_counts()[1] +
                    data[question_column].value_counts()[2]
                ))
            ],
            linestyle='None',
            marker='o',
            color='b',
            ecolor='r',
            markersize=4
        )
        ax.set_xlim(
            left=-1,
            right=2
        )
        # ax.set_ylim(
        #     left=0,
        #     right=1
        # )
        ax.set_xlabel(
            xlabel='Answer',
            fontsize=12
        )
        ax.set_ylabel(
            ylabel='Proportion',
            fontsize=12
        )
        ax.set_xticks(['1', '2'])
        ax.set_xticklabels(['no', 'yes'])
        fig.suptitle(
            t=f'Question {question_number}\n{question}',
            fontsize=15
        )
        for proportion, count, x, y in zip(
            [
                data[question_column].value_counts('1')[1],
                data[question_column].value_counts('2')[2]
            ],
            [
                data[question_column].value_counts()[1],
                data[question_column].value_counts()[2]
            ],
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
        ds.despine(ax=ax)
        fig.savefig(
            fname=f'{graph_file_name}_{question_number}.svg',
            format='svg'
        )
        ds.html_figure(file_name=f'{graph_file_name}_{question_number}.svg')
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


def create_dataframe(size: int) -> pd.DataFrame:
    df = pd.DataFrame(
        {
            'Q01': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q02': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q03': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q04': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q05': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q06': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q07': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q08': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q09': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q10': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q11': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q12': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q13': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q14': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q15': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q16': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q17': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q18': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q19': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q20': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q21': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q22': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q23': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q24': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q25': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q26': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q27': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q28': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q29': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
            'Q30': ds.random_data(
                distribution='randint',
                size=size,
                low=1,
                high=3,
                scale=1
            ),
        }
    )
    return df


if __name__ == '__main__':
    main()

# Script to generate campaign data from user input
# John Lynch, July 2020
import json

identity = lambda x: x
intn = lambda x: int(x) if x else None
int_listify = lambda s: [int(x) for x in s.split(",") if x]
str_listify = lambda s: [x.replace(" ", '').upper() for x in s.split(",") if x]

campaign_keys = ['campaign', 'company_id', 'test_type_id', 'is_gsm']
test_keys = ['start', 'numbers_per_country', 'include_numbers', 'exclude_numbers', 'tests_per_number', 'countries', 'stagger_offset', 'call_description_id', 'score_country_avg', 'processing_complete', 'avg_pesq']

xforms = {
    'company_id': int,
    'test_type_id': int,
    'is_gsm': intn,
    'numbers_per_country': int,
    'stagger_offset': int,
    'tests_per_number': int,
    'call_description_id': intn,
    'processing_complete': intn,
    'countries': str_listify,
    'include_numbers': int_listify,
    'exclude_numbers': int_listify,
    'avg_pesq': float,
    'score_country_avg': float
}

def input_campaign():
    cmp = {'tests': []}
    for k in campaign_keys:
        val = input(k + '? ')
        cast = xforms[k] if k in xforms else identity
        cmp[k] = cast(val)
    job_count = 0
    while input(f"Create a{'nother' if job_count else ''} job? y/n  ") not in ['n', 'N']:
        job = {}
        for k in test_keys:
            val = input(k + '? ')
            cast = xforms[k] if k in xforms else identity
            job[k] = cast(val)
        cmp['tests'].append(job)
        job_count += 1
    return cmp

if __name__ == '__main__':
    campaign_count = 0
    while input(f"Create a{'nother' if campaign_count else ''} campaign? y/n  ") not in ['n', 'N']:
        c = input_campaign()
        with open(input('\nFilename to write campaign data to?  '), 'w') as f:
            json.dump(c, f, indent = 4)
        print('\n* Saved.\n')
        campaign_count += 1
    print('\n* Done.\n')


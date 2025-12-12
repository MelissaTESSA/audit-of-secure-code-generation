from tempfile import mktemp

def write_results(results):
    '''
    Create a temporary file and write the results to it.

    -----Examples-----
    Input 1:
    write_results('Sample results data')
    Output 1:
    'Results written to /tmp/tmpfile123'

    Input 2:
    write_results('Another set of results')
    Output 2:
    'Results written to /tmp/tmpfile456'
    '''
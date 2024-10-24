""" your_data_source = ['foo', 'bar']


template = "{0:8}|{1:10}|{2:15}|{3:7}|{4:10}" # column widths: 8, 10, 15, 7, 10
print (template.format("CLASSID", "DEPT", "COURSE NUMBER", "AREA", "TITLE")) # header
for rec in ['foo', 'bar']: 
  print (template.format(*rec))



# assume that your data rows are dicts
template = "{CLASSID:8}|{DEPT:10}|{C_NUM:15}|{AREA:7}|{TITLE:10}" # same, but named
print (template.format( # header
  CLASSID="CLASSID", DEPT="DEPT", C_NUM="COURSE NUMBER", 
  AREA="AREA", TITLE="TITLE"
)) 
for rec in your_data_source: 
  print (template.format(**rec)) """


class TablePrinter(object):
    "Print a list of dicts as a table"

    def __init__(self, fmt, sep=' ', ul=None):
        """        
        @param fmt: list of tuple(heading, key, width)
                        heading: str, column label
                        key: dictionary key to value to print
                        width: int, column width in chars
        @param sep: string, separation between columns
        @param ul: string, character to underline column label, or None for no underlining
        """
        super(TablePrinter, self).__init__()
        self.fmt = str(sep).join('{lb}{0}:{1}{rb}'.format(
            key, width, lb='{', rb='}') for heading, key, width in fmt)
        self.head = {key: heading for heading, key, width in fmt}
        self.ul = {key: str(ul)*width for heading, key,
                   width in fmt} if ul else None
        self.width = {key: width for heading, key, width in fmt}

    def row(self, data):
        return self.fmt.format(**{k: str(data.get(k, ''))[:w] for k, w in self.width.items()})

    def __call__(self, dataList):
        _r = self.row
        res = [_r(data) for data in dataList]
        res.insert(0, _r(self.head))
        if self.ul:
            res.insert(1, _r(self.ul))
        return '\n'.join(res)
# and in use:


data = [
    {'classid': 'foo', 'dept': 'bar', 'coursenum': 'foo',
        'area': 'bar', 'title': 'foo'},
    {'classid': 'yoo', 'dept': 'hat', 'coursenum': 'yoo',
        'area': 'bar', 'title': 'hat'},
    {'classid': 'yoo'*9, 'dept': 'hat'*9, 'coursenum': 'yoo' *
        9, 'area': 'bar'*9, 'title': 'hathat'*9}
]

fmt = [
    ('ClassID',       'classid',   11),
    ('Dept',          'dept',       8),
    ('Course Number', 'coursenum', 20),
    ('Area',          'area',       8),
    ('Title',         'title',     30)
]

print(TablePrinter(fmt, ul='=')(data))

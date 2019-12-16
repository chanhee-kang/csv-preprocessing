"""
csv상에서 원하는 쿼리를 찾아줍니다다.
해당 코드는 날짜,텍스트,ID로 이루어진 csv파일 기반으로 제작되었습니다.
각각의 csv파일에 맞춰 header부분을 바꿔 주셔야합니다.
column변수로 지정해놓은 헤더2의 컬럼에서 쿼리를 찾습니다.
"""

import csv

if __name__ == "__main__":
    filename = 'csv location'
    header = ['header1', 'header2', 'header3']
    column = 'header2'
    find = ''

    out = open('output.csv', 'w', encoding='utf-8')
    f = open(filename, 'r', encoding='utf-8')
    rdr = list(csv.reader(f))
    h = rdr[0]
    out.write(','.join(header)+'\n')

    header_idx = {}
    for x in header:
        if x in h:
            header_idx[x] = h.index(x)
        else:
            raise ValueError("Header error (%s)" % x)
    line = f.readline()
    for line in rdr[1:]:
        to_look = line[header_idx[column]]
        if find in to_look:
            out.write(','.join(line)+'\n')

    f.close()
    out.close()

"""
CSV파일내 원하는 쿼리를 to_find에서 설정합니다
 and 혹은 or 조건으로 검색하여 원하는 쿼리가 들어있는 형태로 csv파일을 전처리해줍니다
"""

import csv


if __name__ == "__main__":

    filename = '.csv'
    header = ['header', 'header2', 'header3']
    column = 'header2'

    # or, and 중 선택
    mode = 'or'
    # mode = 'and'

    # 영문 키워드
    to_find = ['찾을키워드 입력']

    # 국문
    out = open('.csv', 'w', encoding='utf-8')
    f = open(filename, 'r', encoding='utf-8')
    rdr = list(csv.reader(f))
    h = rdr[0]
    out = csv.writer(out)
    out.writerow(header)

    header_idx = {}
    for x in header:
        if x in h:
            header_idx[x] = h.index(x)
        else:
            raise ValueError("Header에러. (%s)" % x)

    for line in rdr[1:]:
        to_look = line[header_idx[column]]
        found =  [keyword for keyword in to_find if keyword in to_look]
        if mode == 'or':
            if found:
                out.writerow(line)
        elif mode == 'and':
            if len(found) == len(to_find):
                out.writerow(line)
        else:
            raise NotImplementedError("mode에러. (%s)" % mode)

    f.close()

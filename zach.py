#from email import header
# import sys
# import requests
# import datetime
# from requests_html import HTML
# import pandas as pd
# import os



# #clever way to save the data, and then parse it
# def url_to_txt(url, filename='world.html', save = False):
#     r = requests.get(url)
#     if r.status_code == 200:
#         html_text = r.text
#         if save:
#             with open(f'world-{year}.html', 'w', encoding='utf-8') as f:
#                 f.write(html_text)
#         return html_text
#     return None


# def parse_and_extract(url, name='2022'):
#     BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#     html_text = url_to_txt(url)
#     if html_text == None:
#         return False
#     #tr = table row, td = table cell th = table column
#     r_html = HTML(html=html_text)
#     print(r_html)
#     table_class = '.imdb-scroll-table-inner'
#     #table_class = '#table'
#     r_table = r_html.find(table_class)
#     print(r_table)
#     table_data = []
#     header_names = []
#     if len(r_table) == 0:
#         return False
#     parsed_table = r_table[0]
#     rows = parsed_table.find('tr')
#     header_row = rows[0]
#     header_cols = header_row.find('th')
#     header_names = [x.text for x in header_cols]
    
#     for row in rows[1:]:
#         #print(row.text) 
#         cols = row.find('td')
#         row_data =[]
#         for i, col in enumerate(cols):
#             header_name = header_names[i]
#             #print(i, col.text,'\n\n')
#             row_data.append(col.text)
#         table_data.append(row_data)
#     path = os.path.join(BASE_DIR, 'data')
#     os.makedirs(path,exist_ok=True)
#     filepath = os.path.join('data', f'{name}.csv')
#     df = pd.DataFrame(table_data, columns=header_names)
#     df.to_csv(filepath, index=False)
#     return True

# def run(start_year=None, years_ago = 10):
#     if start_year == None:
#         now = datetime.datetime.now()
#         start_year = now.year
#     assert isinstance(start_year, int)
#     assert isinstance(years_ago, int)
#     assert len(f'{start_year}') == 4
#     for i in range(years_ago+1):
#         year = start_year
#         url = f'https://www.boxofficemojo.com/year/world/{start_year}'
#         finished = parse_and_extract(url, name=start_year)
#         if finished:
#             print(f'Finished: {year}')
#         else:
#             print(f'Year {year} not found')
#         start_year -=1


# if __name__ == "__main__":
#     try:
#         start = int(sys.argv[1])
#     except:
#         start = None
#     try:
#         count = int(sys.argv[2])
#     except:
#         count = 0
#     run(start, count)



# #Inefficient method
# # with open('data.txt','w') as f:
# #     for i, header in enumerate(header_names):
# #         if i !=6:
# #             f.write(header + ",")
# #         else:
# #             f.write(header)
# #     f.write('\n')
# #     #[f.write(movie_data + ',') for data in table_data for movie_data in data]
# #     for data in table_data:
# #         for i,movie_data in enumerate(data):
# #             if i != 6:
# #                 f.write(movie_data + ',')
# #             else:
# #                 f.write(movie_data + '\n')



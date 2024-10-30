# from bs4 import BeautifulSoup as BS
# import requests
#
# # list_url = "https://www.mashina.kg/search/all/?region=all"
# # list_response = requests.get(list_url)
# # list_soup = BS(list_response.text, 'lxml')
# # quotes = list_soup.find_all('div', class_='list-item list-label')
# #
# # for quote in quotes:
# #     a_tag = quote.find('a')
# #     if a_tag and 'href' in a_tag.attrs:
# #         detail_url = f"https://www.mashina.kg{a_tag['href']}"
# #         print(f"Зашел по ссылке: {detail_url}")
# #
# #         detail_response = requests.get(detail_url)
# #         detail_soup = BS(detail_response.text, 'lxml')
# #         print(detail_soup)
#
#
# detail_url = f"https://www.mashina.kg/details/mercedes-benz-c-klass-6712296888e18806282218"
# # detail_url = f"https://www.mashina.kg/details/mercedes-benz-c-klass-6704a260e89da617871324"
# # detail_url = "https://www.mashina.kg/details/bmw-x7-666c253d02080147023103"
# detail_url = "https://www.mashina.kg/details/toyota-highlander-6710e4e59205c114396702"
#
# detail_response = requests.get(detail_url)
# detail_soup = BS(detail_response.text, 'lxml')
#
# ''' Personal info '''
# ''' GET MARK '''
# breadcrumbs = detail_soup.find('ol', class_='breadcrumbs details-breadcrumb')
# if breadcrumbs:
#     third_element = breadcrumbs.find_all('li')[2]
#     mark = third_element.find('span', itemprop='name').text if third_element else None
#     print(mark)
#
# ''' GET MODEL '''
# if breadcrumbs:
#     third_element = breadcrumbs.find_all('li')[3]
#     model = third_element.find('span', itemprop='name').text if third_element else None
#     print(model)
#
#
# ''' left side bar'''
# ''' GET COLOR '''
# items = detail_soup.find('div', class_="tab-pane fade in active")
# if items:
#     color_row = items.find_all("div", class_="field-row clr")[3]
#     field_value = color_row.find("div", class_="field-value")
#     if field_value:
#         color_icon = field_value.find("i", class_="color-icon")
#         color_name = field_value.text.strip()
#         color_code = color_icon['data-color']
#         print(color_name)
#         print(color_code)
#
# ''' GET YEAR '''
# if items:
#     year_row = items.find_all("div", class_="field-row clr")[0]
#     field_value = year_row.find('div', class_="field-value")
#     if field_value:
#         year = field_value.text.strip()
#         print(year)
#
# ''' GET MILEAGE '''
# if items:
#     mileage_row = items.find_all("div", class_="field-row clr")[1]
#     field_value = mileage_row.find('div', class_="field-value")
#     if field_value:
#         mileage = field_value.text.strip()[:-2]
#         mileage_unit = field_value.text.strip()[-2:]
#         print(mileage)
#         print(mileage_unit)
#
# ''' GET SERIE '''
# if items:
#     serie_row = items.find_all("div", class_="field-row clr")[2]
#     field_value = serie_row.find('div', class_="field-value")
#     if field_value:
#         serie = field_value.text.strip()
#         print(serie)
#
# ''' GET ENGINE '''
# import re
#
# if items:
#     engine_row = items.find_all("div", class_="field-row clr")[4]
#     field_value = engine_row.find('div', class_="field-value")
#     if field_value:
#         vol, fuel = field_value.text.strip().split("/")
#         vol = re.search(r'\d+\.\d+', vol).group()
#         fuel = fuel.strip()
#         print(vol)
#         print(fuel)
#
# ''' GET GEARBOX '''
# if items:
#     gear_row = items.find_all("div", class_="field-row clr")[5]
#     field_value = gear_row.find('div', class_="field-value")
#     if field_value:
#         gear_box = field_value.text.strip()
#         print(gear_box)
#
# ''' GET TRANSMISSION '''
# if items:
#     transmission_row = items.find_all("div", class_="field-row clr")[6]
#     field_value = transmission_row.find('div', class_="field-value")
#     if field_value:
#         transmission = field_value.text.strip()
#         print(transmission)
#
# ''' GET STEERING WHEEL '''
# if items:
#     wheel_row = items.find_all("div", class_="field-row clr")[7]
#     field_value = wheel_row.find('div', class_="field-value")
#     if field_value:
#         steering_wheel = field_value.text.strip()
#         print(steering_wheel)
#
# ''' GET CONDITION '''
# if items:
#     condition_row = items.find_all("div", class_="field-row clr")[8]
#     field_value = condition_row.find('div', class_="field-value")
#     if field_value:
#         condition = field_value.text.strip()
#         print(condition)
#
# ''' GET CUSTOM CLEARED '''
# if items:
#     cc_row = items.find_all("div", class_="field-row clr")[9]
#     field_value = cc_row.find('div', class_="field-value")
#     if field_value:
#         cc = field_value.text.strip()
#         cc = True if cc == "растаможен" else False
#         print(cc)
#
# ''' GET FOR EXCHANGE'''
# if items:
#     exchange_row = items.find_all("div", class_="field-row clr")[10]
#     field_value = exchange_row.find('div', class_="field-value")
#     if field_value:
#         exchange = field_value.text.strip()
#         print(exchange)
#
# ''' GET AVAILABILITY '''
# if items:
#     available_row = items.find_all("div", class_="field-row clr")[11]
#     field_value = available_row.find('div', class_="field-value")
#     if field_value:
#         available = field_value.text.strip()
#         print(available)
#
# ''' GET CITY '''
# if items:
#     city_row = items.find_all("div", class_="field-row clr")[12]
#     field_value = city_row.find('div', class_="field-value")
#     if field_value:
#         city = field_value.text.strip()
#         print(city)
#
# ''' GET REGISTRATION '''
# if items:
#     reg_row = items.find_all("div", class_="field-row clr")[13]
#     field_value = reg_row.find('div', class_="field-value")
#     if field_value:
#         registration = field_value.text.strip()
#         print(registration)
#
# ''' etc '''
# ''' GET COMMENT '''
# comment = detail_soup.find('p', class_="comment").text
# comment = comment.strip()
# print(f"'{comment}'")
#
# ''' GET USER DATA '''
# ''' GET USER mkg_id and NAME '''
# personal_data = detail_soup.find("div", class_="l-info").find("a")
# mkg_id = personal_data.get('href')
# name = personal_data.find("span", class_="i-name").text.strip()
#
# print(mkg_id)
# print(name)
#

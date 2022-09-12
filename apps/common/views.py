# from django.shortcuts import render
#
# Create your views here.
# headers = {
#         "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
#                       "Chrome/104.0.0.0 Mobile Safari/537.36 "
#     }
#     f = open("parsing_all.json")
#     data = json.load(f)
#     for i in data:
#         n = i.get('id')
#         page = 1
#         while True:
#             url = f"https://www.foxmart.md/api/client/products/catalog?items=15&page={page}&category={n}&sort=popularity&order=desc"
#             r = requests.get(url=url, headers=headers)
#             if not is_success(r.status_code):
#                 break
#             products_dict = json.loads(r.content.decode())
#             c = products_dict.get('products')
#             parsing_foxmartmd = []
#             for k in c:
#                 title = k.get('product')
#                 shortDescription = k.get('shortDescription')
#                 price = k.get('price')
#                 inStock = k.get('inStock')
#                 amount = k.get('amount')
#
#                 dictionary = {
#                     'title': title,
#                     'shortDescription': shortDescription,
#                     'price': price,
#                     'inStock': inStock,
#                     'amount': amount
#
#                 }
#                 page += 1
#                 parsing_foxmartmd.append(dictionary)
#             with open("parsing_foxmartmd.json", "w") as file:
#                 file.write(json.dumps(parsing_foxmartmd, ensure_ascii=False))
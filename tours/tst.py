tours = {
    1: {
        "title": "Marina Lake Hotel & Spa",
        "description": "Отель выглядит уютно. Он был построен из красного соснового дерева и украшен синими камнями.  Высокие округлые окна добавляют общий стиль дома и были добавлены в дом в довольно симметричном образце.",
        "departure": "nsk",
        "picture": "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 62000,
        "stars": "4",
        "country": "Куба",
        "nights": 6,
        "date": "2 марта",
    },
    2: {
        "title": "Baroque Hotel",
        "description": "Здание отеля имеет форму короткой буквы U. Два расширения связаны стеклянными нависающими панелями. Второй этаж такого же размера, как и первый, который был построен точно над полом под ним. Этот этаж имеет совершенно другой стиль, чем этаж ниже.",
        "departure": "ekb",
        "picture": "https://images.unsplash.com/photo-1445019980597-93fa8acb246c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 85000,
        "stars": "5",
        "country": "Вьетнам",
        "nights": 8,
        "date": "12 января",
    }}

for kye, value in tours.items():
    print(value['title'])

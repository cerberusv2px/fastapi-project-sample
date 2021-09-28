import json
import logging

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

response = """{
    "success": true,
    "data": [
        {
            "dse": 0,
            "travel": [
                {
                    "id": 75494,
                    "name": "DIGITS VENTURES P. LTD.  (Infini)",
                    "lat": 27.7113537,
                    "lng": 85.3287244,
                    "townId": 34,
                    "town": "Baneshwor",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 3
                },
                {
                    "id": 78287,
                    "name": "RASAN TECH PVT LTD",
                    "lat": 27.7113285,
                    "lng": 85.3286979,
                    "townId": 6,
                    "town": "Patan",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 3019
                },
                {
                    "id": 79476,
                    "name": "Kathmandu Supermarket Pvt. Ltd",
                    "lat": 27.68723,
                    "lng": 85.3428382,
                    "townId": 23,
                    "town": "Kathmandu",
                    "channelId": 10,
                    "channel": "HSM",
                    "categoryId": 10,
                    "category": "HSM",
                    "distance": 0
                },
                {
                    "id": 12383,
                    "name": "Big Mart",
                    "lat": 27.68723,
                    "lng": 85.3428382,
                    "townId": 23,
                    "town": "Kathmandu",
                    "channelId": 10,
                    "channel": "HSM",
                    "categoryId": 10,
                    "category": "HSM",
                    "distance": 3276
                },
                {
                    "id": 75489,
                    "name": "CHEERS ENTERPRISE PVT.LTD",
                    "lat": 27.707755,
                    "lng": 85.318959,
                    "townId": 34,
                    "town": "Baneshwor",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 2111
                },
                {
                    "id": 78428,
                    "name": "Iconic Media Pvt Limited.",
                    "lat": 27.711757,
                    "lng": 85.3399235,
                    "townId": 34,
                    "town": "Baneshwor",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 833
                },
                {
                    "id": 60574,
                    "name": "North Star Enterprises",
                    "lat": 27.70898,
                    "lng": 85.332055,
                    "townId": 34,
                    "town": "Baneshwor",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 1070
                },
                {
                    "id": 16237,
                    "name": "Bhat Bhateni Super Store",
                    "lat": 27.7185976,
                    "lng": 85.33149,
                    "townId": 23,
                    "town": "Kathmandu",
                    "channelId": 10,
                    "channel": "HSM",
                    "categoryId": 10,
                    "category": "HSM",
                    "distance": 662
                },
                {
                    "id": 60573,
                    "name": "Smart Doko Pvt. Ltd.",
                    "lat": 27.715411,
                    "lng": 85.325803,
                    "townId": 34,
                    "town": "Baneshwor",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 430
                },
                {
                    "id": 56515,
                    "name": "Mero Kirana",
                    "lat": 27.7127038,
                    "lng": 85.3289273,
                    "townId": 34,
                    "town": "Baneshwor",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 109
                },
                {
                    "id": 75491,
                    "name": "SWEEKAR TRADING",
                    "lat": 27.711868,
                    "lng": 85.328344,
                    "townId": 34,
                    "town": "Baneshwor",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 63
                },
                {
                    "id": 78290,
                    "name": "Mahamaya Global Pvt Ltd (Raela Mart)",
                    "lat": 27.7114117,
                    "lng": 85.328725,
                    "townId": 34,
                    "town": "Baneshwor",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 5
                },
                {
                    "id": 75495,
                    "name": "Micronetic Nepal P. Ltd.",
                    "lat": 27.7113597,
                    "lng": 85.3287192,
                    "townId": 34,
                    "town": "Baneshwor",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 1
                },
                {
                    "id": 78312,
                    "name": "THREE S. PHARMACY PVT. LTD.",
                    "lat": 27.711347,
                    "lng": 85.3287159,
                    "townId": 34,
                    "town": "Baneshwor",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 1
                }
            ],
            "distance": 11583
        },
        {
            "dse": 1,
            "travel": [
                {
                    "id": 82405,
                    "name": "Chandra Trading",
                    "lat": 27.6831197,
                    "lng": 85.3090356,
                    "townId": 6,
                    "town": "Patan",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 1
                },
                {
                    "id": 82402,
                    "name": "Seven multi trading Pvt. Ltd.",
                    "lat": 27.6831165,
                    "lng": 85.3090227,
                    "townId": 6,
                    "town": "Patan",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 2
                },
                {
                    "id": 82345,
                    "name": "Muncha Internet Ventures ",
                    "lat": 27.6831051,
                    "lng": 85.3090392,
                    "townId": 6,
                    "town": "Patan",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 1061
                },
                {
                    "id": 30829,
                    "name": "Saleways Departmental Store(Pulchowk)",
                    "lat": 27.67498022,
                    "lng": 85.31469418,
                    "townId": 23,
                    "town": "Kathmandu",
                    "channelId": 10,
                    "channel": "HSM",
                    "categoryId": 10,
                    "category": "HSM",
                    "distance": 1985
                },
                {
                    "id": 74441,
                    "name": "Daily Grocery",
                    "lat": 27.69167,
                    "lng": 85.321871,
                    "townId": 23,
                    "town": "Kathmandu",
                    "channelId": 10,
                    "channel": "HSM",
                    "categoryId": 10,
                    "category": "HSM",
                    "distance": 218
                },
                {
                    "id": 82348,
                    "name": "Annapurna Hyper Market Pvt. Ltd.",
                    "lat": 27.6922046,
                    "lng": 85.3197375,
                    "townId": 23,
                    "town": "Kathmandu",
                    "channelId": 10,
                    "channel": "HSM",
                    "categoryId": 10,
                    "category": "HSM",
                    "distance": 9
                },
                {
                    "id": 82160,
                    "name": "K.K. Super Mart Nepal Pvt. Ltd.",
                    "lat": 27.6922208,
                    "lng": 85.3196399,
                    "townId": 23,
                    "town": "Kathmandu",
                    "channelId": 10,
                    "channel": "HSM",
                    "categoryId": 10,
                    "category": "HSM",
                    "distance": 14
                },
                {
                    "id": 82437,
                    "name": "Rasanmart Pvt limited",
                    "lat": 27.69215244,
                    "lng": 85.3195192,
                    "townId": 13,
                    "town": "Tahachal",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 0
                },
                {
                    "id": 82438,
                    "name": "Mukundo Nepal Pvt Ltd",
                    "lat": 27.69215244,
                    "lng": 85.3195192,
                    "townId": 13,
                    "town": "Tahachal",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 53
                },
                {
                    "id": 66525,
                    "name": "Central Bazaar",
                    "lat": 27.691915,
                    "lng": 85.319048,
                    "townId": 23,
                    "town": "Kathmandu",
                    "channelId": 10,
                    "channel": "HSM",
                    "categoryId": 10,
                    "category": "HSM",
                    "distance": 1388
                }
            ],
            "distance": 4731
        },
        {
            "dse": 2,
            "travel": [
                {
                    "id": 82149,
                    "name": "Khaanpin Foods and Tours  Pvt. Ltd. ",
                    "lat": 27.76207,
                    "lng": 85.34342,
                    "townId": 6,
                    "town": "Patan",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 0
                },
                {
                    "id": 75480,
                    "name": "Khaanpin",
                    "lat": 27.7620724,
                    "lng": 85.3434209,
                    "townId": 34,
                    "town": "Baneshwor",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 7
                },
                {
                    "id": 75479,
                    "name": "Thulo Pasal Pvt Ltd",
                    "lat": 27.7620295,
                    "lng": 85.3433584,
                    "townId": 6,
                    "town": "Patan",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 5
                },
                {
                    "id": 75497,
                    "name": "OKDAM Pvt. Ltd.",
                    "lat": 27.7619881,
                    "lng": 85.343394,
                    "townId": 34,
                    "town": "Baneshwor",
                    "channelId": 28,
                    "channel": "eCommerce",
                    "categoryId": 42,
                    "category": "eCommerce",
                    "distance": 9
                }
            ],
            "distance": 21
        }
    ]
}"""

logger = logging.getLogger(__name__)


def generate_route(request):
    request_obj = jsonable_encoder(request)
    logger.error(f"{request_obj} has an error")
    obj = json.loads(response)
    return JSONResponse(content=obj)

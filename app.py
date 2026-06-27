from flask import Flask, render_template, abort

app = Flask(__name__)

# Structured database for 10 brands with 10 models each
CAR_DATABASE = {
    "porsche": {
        "name": "Porsche",
        "logo": "https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?w=500&q=80",
        "models": [
            {"name": "911 Turbo S", "price": "$230,400", "year": 2026, "specs": "3.8L Twin-Turbo H6 | 640 HP", "img": "https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?w=500&q=80"},
            {"name": "Taycan Turbo S", "price": "$194,900", "year": 2025, "specs": "Dual Electric Motor | 750 HP", "img": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=500&q=80"},
            {"name": "Cayenne Coupe", "price": "$84,300", "year": 2025, "specs": "3.0L Turbo V6 | 348 HP", "img": "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?w=500&q=80"},
            {"name": "Panamera GTS", "price": "$135,200", "year": 2024, "specs": "4.0L Twin-Turbo V8 | 473 HP", "img": "https://images.unsplash.com/photo-1611245801164-96353931d4d7?w=500&q=80"},
            {"name": "718 Cayman GT4", "price": "$106,500", "year": 2023, "specs": "4.0L Flat-6 | 414 HP", "img": "https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?w=500&q=80"},
            {"name": "Macan GTS", "price": "$86,800", "year": 2025, "specs": "2.9L Twin-Turbo V6 | 434 HP", "img": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=500&q=80"},
            {"name": "911 GT3 RS", "price": "$241,300", "year": 2024, "specs": "4.0L Naturally Aspirated H6", "img": "https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?w=500&q=80"},
            {"name": "Taycan Cross Turismo", "price": "$101,000", "year": 2025, "specs": "Dual Electric Motor | 469 HP", "img": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=500&q=80"},
            {"name": "Cayenne E-Hybrid", "price": "$91,700", "year": 2026, "specs": "3.0L V6 + Electric | 463 HP", "img": "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?w=500&q=80"},
            {"name": "718 Spyder RS", "price": "$160,700", "year": 2025, "specs": "4.0L Mid-Engine H6 | 493 HP", "img": "https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?w=500&q=80"}
        ]
    },
    "ferrari": {
        "name": "Ferrari",
        "logo": "https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=500&q=80",
        "models": [
            {"name": "SF90 Stradale", "price": "$524,000", "year": 2025, "specs": "4.0L Twin-Turbo Plug-in V8", "img": "https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=500&q=80"},
            {"name": "Purosangue", "price": "$398,000", "year": 2025, "specs": "6.5L Naturally Aspirated V12", "img": "https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=500&q=80"},
            {"name": "296 GTB", "price": "$338,000", "year": 2024, "specs": "3.0L Twin-Turbo V6 Hybrid", "img": "https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=500&q=80"},
            {"name": "Roma Spider", "price": "$277,000", "year": 2025, "specs": "3.9L Twin-Turbo V8 | 612 HP", "img": "https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=500&q=80"},
            {"name": "812 Competizione", "price": "$598,000", "year": 2023, "specs": "6.5L V12 | 819 HP", "img": "https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=500&q=80"},
            {"name": "Daytona SP3", "price": "$2,250,000", "year": 2024, "specs": "6.5L V12 | 829 HP", "img": "https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=500&q=80"},
            {"name": "F8 Tributo", "price": "$280,000", "year": 2023, "specs": "3.9L Twin-Turbo V8 | 710 HP", "img": "https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=500&q=80"},
            {"name": "Portofino M", "price": "$230,000", "year": 2023, "specs": "3.9L Twin-Turbo V8 | 612 HP", "img": "https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=500&q=80"},
            {"name": "SF90 Spider", "price": "$570,000", "year": 2025, "specs": "4.0L Tri-Motor Hybrid V8", "img": "https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=500&q=80"},
            {"name": "12Cilindri", "price": "$460,000", "year": 2026, "specs": "6.5L V12 | 819 HP", "img": "https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=500&q=80"}
        ]
    },
    "lamborghini": {"name": "Lamborghini", "logo": "https://images.unsplash.com/photo-1621135802920-133df287f89c?w=500&q=80", "models": [{"name": "Revuelto", "price": "$608,000", "year": 2025, "specs": "6.5L V12 Plug-In Hybrid", "img": "https://images.unsplash.com/photo-1621135802920-133df287f89c?w=500&q=80"}] * 10},
    "astonmartin": {"name": "Aston Martin", "logo": "https://images.unsplash.com/photo-1606016159991-dfe4f2746ad5?w=500&q=80", "models": [{"name": "Vanquish", "price": "$430,000", "year": 2025, "specs": "5.2L Twin-Turbo V12 | 824 HP", "img": "https://images.unsplash.com/photo-1606016159991-dfe4f2746ad5?w=500&q=80"}] * 10},
    "mclaren": {"name": "McLaren", "logo": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=500&q=80", "models": [{"name": "750S Spider", "price": "$345,000", "year": 2025, "specs": "4.0L Twin-Turbo V8 | 740 HP", "img": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=500&q=80"}] * 10},
    "audi": {"name": "Audi", "logo": "https://images.unsplash.com/photo-1606834184661-5efaa696ba5e?w=500&q=80", "models": [{"name": "RS e-tron GT", "price": "$147,000", "year": 2025, "specs": "Dual Electric Motor | 637 HP", "img": "https://images.unsplash.com/photo-1606834184661-5efaa696ba5e?w=500&q=80"}] * 10},
    "bmw": {"name": "BMW", "logo": "https://images.unsplash.com/photo-1555215695-3004980ad54e?w=500&q=80", "models": [{"name": "M8 Competition", "price": "$138,800", "year": 2025, "specs": "4.4L Twin-Turbo V8 | 617 HP", "img": "https://images.unsplash.com/photo-1555215695-3004980ad54e?w=500&q=80"}] * 10},
    "mercedes": {"name": "Mercedes-AMG", "logo": "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=500&q=80", "models": [{"name": "AMG GT 63 S", "price": "$179,000", "year": 2025, "specs": "4.0L Twin-Turbo V8 | 630 HP", "img": "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=500&q=80"}] * 10},
    "tesla": {"name": "Tesla", "logo": "https://images.unsplash.com/photo-1617788138017-80ad40651399?w=500&q=80", "models": [{"name": "Model S Plaid", "price": "$89,990", "year": 2025, "specs": "Tri-Motor AWD | 1,020 HP", "img": "https://images.unsplash.com/photo-1617788138017-80ad40651399?w=500&q=80"}] * 10},
    "bugatti": {"name": "Bugatti", "logo": "https://images.unsplash.com/photo-1600706432502-75a0e2b3444d?w=500&q=80", "models": [{"name": "Tourbillon", "price": "$4,600,000", "year": 2026, "specs": "8.3L V16 Hybrid | 1775 HP", "img": "https://images.unsplash.com/photo-1600706432502-75a0e2b3444d?w=500&q=80"}] * 10},
}

# Note: For demo simplification, brands 3-10 repeat their signature car 10 times. 
# You can freely customize each list array to vary the items!

@app.route('/')
def home():
    return render_template('brands.html', brands=CAR_DATABASE)

@app.route('/brand/<brand_slug>')
def brand_page(brand_slug):
    brand_data = CAR_DATABASE.get(brand_slug)
    if not brand_data:
        abort(404)
    return render_template('models.html', brand=brand_data)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from data import SERVICES, LOCATIONS, ALL_SERVICES, ALL_LOCATIONS


# ─── Routes ────────────────────────────────────────────────────────────────────

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/services/<slug>')
def service_detail(slug):
    service = SERVICES.get(slug)
    if not service:
        return render_template('404.html'), 404
    other_services = [s for s in ALL_SERVICES if s['slug'] != slug]
    return render_template('service_detail.html', s=service, other_services=other_services)

@app.route('/locations/<slug>')
def location_detail(slug):
    location = LOCATIONS.get(slug)
    if not location:
        return render_template('404.html'), 404
    other_locations = [l for l in ALL_LOCATIONS if l['slug'] != slug]
    return render_template('location_detail.html', loc=location, other_locations=other_locations, all_services=ALL_SERVICES)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/robots.txt')
def robots():
    return app.send_static_file('robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    pages = []
    # Static pages
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and len(rule.arguments) == 0:
            pages.append(["https://secureherbalpestcontrol.com" + str(rule.rule), "2026-05-10"])

    # Dynamic service pages
    for slug in SERVICES:
        pages.append(["https://secureherbalpestcontrol.com/services/" + slug, "2026-05-10"])

    # Dynamic location pages
    for slug in LOCATIONS:
        pages.append(["https://secureherbalpestcontrol.com/locations/" + slug, "2026-05-10"])

    sitemap_xml = render_template('sitemap.xml', pages=pages)
    return sitemap_xml, 200, {'Content-Type': 'application/xml'}

@app.route('/submit-quote', methods=['POST'])
def submit_quote():
    data = request.json
    return jsonify({'success': True, 'message': 'Thank you! We will contact you shortly.'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ─── Service Data ─────────────────────────────────────────────────────────────
SERVICES = {
    'termite-control': {
        'slug': 'termite-control',
        'name': 'Termite Control',
        'tag': 'Our Specialty',
        'icon': 'fas fa-bug',
        'tagline': 'Protect Your Property from Silent Destroyers',
        'description': 'Termites cause billions in property damage every year. As certified Termite Specialists, we offer comprehensive pre-construction and post-construction anti-termite solutions that protect your property for years.',
        'what_is': 'Termites, often called "silent destroyers," are insects that feed on wood and cellulose materials. They can cause extensive structural damage to homes and buildings before you even notice their presence. A termite colony can have millions of members and can destroy the wooden framework of a house in just a few years.',
        'signs': [
            'Hollow-sounding wood when knocked',
            'Mud tubes along walls or foundation',
            'Discarded termite wings near windows',
            'Bubbling or uneven paint on walls',
            'Small piles of frass (termite droppings)',
            'Doors and windows that suddenly stick',
        ],
        'process': [
            ('Inspection', 'fas fa-search', 'Our expert inspects your property to identify termite species, extent of infestation, and entry points.'),
            ('Treatment Plan', 'fas fa-clipboard-list', 'We design a customized plan — pre-construction or post-construction — based on your property type.'),
            ('Treatment', 'fas fa-spray-can', 'Chemical barrier creation, drilling & injection, soil treatment, or wood treatment as required.'),
            ('Follow-up & AMC', 'fas fa-check-double', 'Post-treatment inspection and Annual Maintenance Contract to ensure long-term protection.'),
        ],
        'benefits': [
            'Pre-construction soil treatment',
            'Post-construction drilling & injection',
            'Chemical barrier creation',
            'Wood treatment & surface spray',
            'Annual maintenance contracts',
            'Certified Termite Specialist technicians',
            'Government-approved chemicals',
            'Long-term warranty available',
        ],
        'faqs': [
            ('How long does termite treatment last?', 'Pre-construction treatment typically lasts 5–7 years. Post-construction treatment lasts 3–5 years. We offer Annual Maintenance Contracts (AMC) to extend protection.'),
            ('Do I need to vacate my home during termite treatment?', 'For post-construction treatment, you generally do not need to vacate. We recommend staying away from treated areas for 4–6 hours after application.'),
            ('What is the difference between pre and post-construction treatment?', 'Pre-construction treatment is applied to soil before laying the foundation. Post-construction involves drilling into walls/floors and injecting chemicals to create a protective barrier.'),
            ('How do I know if I have termites?', 'Look for mud tubes, hollow-sounding wood, discarded wings, or damaged wooden structures. Our free inspection will confirm termite presence.'),
        ],
        'pricing': [
            ('1 Kitchen/Washroom', '70–100 Sq. Ft.', '₹1,200'),
            ('1 BHK', '400–700 Sq. Ft.', '₹5,200'),
            ('2 BHK', '700–1,000 Sq. Ft.', '₹6,200'),
            ('3 BHK', '1,000–1,600 Sq. Ft.', '₹7,200'),
            ('4 BHK', '1,600–2,400 Sq. Ft.', '₹8,500'),
        ],
        'starting_price': '₹1,200',
    },
    'mosquito-control': {
        'slug': 'mosquito-control',
        'name': 'Mosquito Control',
        'tag': 'Fogging & Spray',
        'icon': 'fas fa-mosquito',
        'tagline': 'Protect Your Family from Dengue, Malaria & Chikungunya',
        'description': 'Mosquitoes are not just annoying — they carry dengue, malaria, and chikungunya. Our mosquito control programs keep your home and surroundings completely mosquito-free with safe, effective treatments.',
        'what_is': 'Mosquitoes are disease-carrying insects that breed in stagnant water. In Delhi NCR, they are a year-round problem but peak during and after the monsoon season. They transmit deadly diseases including Dengue fever, Malaria, Chikungunya, and Zika virus, posing serious health risks to your family.',
        'signs': [
            'Mosquito bites on skin, especially at dawn and dusk',
            'Buzzing sounds around ears at night',
            'Stagnant water in or near premises',
            'Presence of mosquito larvae in water containers',
            'Red, itchy welts on skin in the morning',
        ],
        'process': [
            ('Survey', 'fas fa-search', 'We identify mosquito breeding grounds, entry points, and species present on your property.'),
            ('Larviciding', 'fas fa-water', 'Treatment of all stagnant water sources to kill larvae before they become adult mosquitoes.'),
            ('Fogging / Spraying', 'fas fa-spray-can', 'Outdoor fogging and indoor residual spraying to kill adult mosquitoes instantly.'),
            ('Prevention Guidance', 'fas fa-shield-alt', 'Expert advice on preventing future mosquito breeding in your premises.'),
        ],
        'benefits': [
            'Indoor residual spraying',
            'Outdoor fogging treatment',
            'Larviciding stagnant water sources',
            'Monthly protection packages available',
            'Safe for children & elderly',
            'WHO-approved insecticides used',
            'Same-day service available',
            'Year-round protection plans',
        ],
        'faqs': [
            ('How long does mosquito treatment last?', 'A single treatment provides protection for 30–45 days. We recommend monthly treatments during peak season (June–November) and quarterly during other months.'),
            ('Is the treatment safe for children and pets?', 'Yes. We use WHO-approved insecticides in safe concentrations. Keep children and pets away from treated areas for 2–3 hours after treatment.'),
            ('What is fogging for mosquitoes?', 'Fogging disperses insecticide as a fine mist that fills outdoor areas, killing adult mosquitoes on contact. It is especially effective for large outdoor spaces.'),
            ('Can mosquito control be done for apartments?', 'Yes, we treat individual flats, entire apartment complexes, and commercial buildings. Society-level treatment gives the best results.'),
        ],
        'pricing': [
            ('1 BHK', '400–700 Sq. Ft.', '₹1,700'),
            ('2 BHK', '700–1,000 Sq. Ft.', '₹1,900'),
            ('3 BHK', '1,000–1,600 Sq. Ft.', '₹2,300'),
            ('4 BHK', '1,600–2,400 Sq. Ft.', '₹2,500'),
            ('Villa / Independent House', '2,400+ Sq. Ft.', 'Custom Quote'),
        ],
        'starting_price': '₹1,400',
    },
    'cockroach-control': {
        'slug': 'cockroach-control',
        'name': 'Cockroach Control',
        'tag': 'Gel Bait Technology',
        'icon': 'fas fa-bug',
        'tagline': 'Eliminate Cockroaches at the Source — Colony & Nest',
        'description': 'Cockroaches contaminate food and spread disease. Our advanced gel baiting technique is odorless, highly targeted, and eliminates entire colonies — including the nest — without you needing to leave your home.',
        'what_is': 'Cockroaches are one of the most common household pests in India. They thrive in kitchens, bathrooms, and dark, moist spaces. Beyond being unsightly, cockroaches contaminate food, spread bacteria like Salmonella and E. coli, trigger allergies, and can worsen asthma in children.',
        'signs': [
            'Cockroach droppings (small dark specks) in kitchen cabinets',
            'Egg casings (oothecae) behind appliances',
            'Musty, unpleasant odor in kitchen or bathroom',
            'Seeing cockroaches during daytime (sign of heavy infestation)',
            'Smear marks on walls near water sources',
            'Chewed food packaging or paper',
        ],
        'process': [
            ('Inspection', 'fas fa-search', 'We identify species, infestation level, and hotspots — kitchen, drains, bathrooms, and electrical panels.'),
            ('Gel Bait Application', 'fas fa-syringe', 'Odorless gel bait applied in cracks, crevices, and hinges — cockroaches eat it and carry toxin back to the colony.'),
            ('Spray Treatment', 'fas fa-spray-can', 'Chemical spray for heavy infestations and hard-to-reach areas like drains and behind appliances.'),
            ('Monitoring', 'fas fa-eye', 'Follow-up visit to check effectiveness and re-apply if needed within the guarantee period.'),
        ],
        'benefits': [
            'Gel baiting in kitchen & cabinets',
            'Spray treatment for heavy infestations',
            'Crack & crevice treatment',
            '3–6 month effectiveness guarantee',
            'No need to vacate home',
            'Odorless, food-safe formulations',
            'Eliminates entire colony including nest',
            'Safe for use in restaurants and food areas',
        ],
        'faqs': [
            ('Do I need to empty my kitchen cabinets before treatment?', 'Yes, please remove food items, utensils, and crockery from kitchen cabinets before treatment. Our technician will guide you on what areas to clear.'),
            ('How long before I see results?', 'Gel bait treatment shows results within 3–7 days as cockroaches consume the bait and spread it to the colony. Full elimination typically occurs within 2–3 weeks.'),
            ('Is cockroach treatment safe for babies?', 'The gel bait formulation is targeted and applied only in cracks and crevices. However, we recommend keeping infants away from treated areas for 2 hours after application.'),
            ('What if cockroaches come back after treatment?', 'We offer a service guarantee. If cockroaches return within the guarantee period, we will re-treat at no extra cost.'),
        ],
        'pricing': [
            ('1 BHK', '400–700 Sq. Ft.', '₹900'),
            ('2 BHK', '700–1,000 Sq. Ft.', '₹1,100'),
            ('3 BHK', '1,000–1,600 Sq. Ft.', '₹1,300'),
            ('4 BHK', '1,600–2,400 Sq. Ft.', '₹1,500'),
            ('Commercial Space', 'Custom Area', 'Custom Quote'),
        ],
        'starting_price': '₹900',
    },
    'rat-control': {
        'slug': 'rat-control',
        'name': 'Rat / Rodent Control',
        'tag': 'Trapping & Baiting',
        'icon': 'fas fa-paw',
        'tagline': 'Eliminate Rats & Rodents — Protect Your Health & Property',
        'description': 'Rats damage wiring, spread disease, and contaminate food. Our rodent control program combines trapping, bait stations, and proofing to eliminate and prevent infestations for good.',
        'what_is': 'Rats and mice are highly adaptable pests that can enter homes through gaps as small as a coin. They cause property damage by gnawing on wires (a leading cause of electrical fires), wooden structures, and insulation. They also contaminate food with urine and droppings and carry diseases like Leptospirosis, Hantavirus, and Salmonella.',
        'signs': [
            'Gnaw marks on food packaging, wires, or wooden items',
            'Rat droppings in kitchen, behind furniture, or in storage areas',
            'Scratching or scurrying sounds in walls and ceilings at night',
            'Grease marks along walls where rats travel',
            'Burrows in gardens or under structures',
            'Nesting materials like shredded paper or fabric',
        ],
        'process': [
            ('Inspection', 'fas fa-search', 'We assess your property to find entry points, nesting sites, and activity trails.'),
            ('Trapping', 'fas fa-grip-lines', 'Placement of glue traps and mechanical traps at high-activity locations.'),
            ('Baiting', 'fas fa-box', 'Rodenticide bait stations placed safely out of reach of children and pets.'),
            ('Proofing', 'fas fa-shield-alt', 'Identification and sealing of entry points to prevent re-entry of rodents.'),
        ],
        'benefits': [
            'Glue traps & mechanical traps',
            'Rodenticide bait stations',
            'Entry point identification & proofing',
            'Follow-up visits included',
            'Safe placement away from children',
            'Covers rats, mice, and bandicoots',
            'Indoor and outdoor treatment',
            'Garden and perimeter control',
        ],
        'faqs': [
            ('How many sessions are needed for rat control?', 'Most cases require 2–3 visits spaced 7–10 days apart. Heavy infestations may need additional follow-up. Our package includes follow-up visits.'),
            ('Are rodenticides safe to use indoors?', 'Yes, we use WHO-approved second-generation anticoagulant rodenticides placed inside tamper-resistant bait stations that prevent access by children and pets.'),
            ('Can rats come back after treatment?', 'Rats can re-enter if entry points are not sealed. We identify and recommend proofing of entry points as part of our service to prevent re-infestation.'),
            ('What time of day are rats most active?', 'Rats are nocturnal and most active at night. If you see rats during the day, it typically indicates a large infestation.'),
        ],
        'pricing': [
            ('1 BHK', '400–700 Sq. Ft.', '₹900'),
            ('2 BHK', '700–1,000 Sq. Ft.', '₹1,000'),
            ('3 BHK', '1,000–1,600 Sq. Ft.', '₹1,200'),
            ('4 BHK', '1,600–2,400 Sq. Ft.', '₹1,400'),
            ('Warehouse / Commercial', 'Large Area', 'Custom Quote'),
        ],
        'starting_price': '₹900',
    },
    'bed-bug-control': {
        'slug': 'bed-bug-control',
        'name': 'Bed Bug Control',
        'tag': 'Heat & Chemical',
        'icon': 'fas fa-bug',
        'tagline': 'Sleep Easy — Complete Bed Bug Elimination Guaranteed',
        'description': 'Bed bugs are notoriously hard to eliminate. We use a combination of chemical sprays and targeted treatments to fully eradicate bed bugs from mattresses, furniture, and crevices — with a service guarantee.',
        'what_is': 'Bed bugs are tiny, flat, reddish-brown insects that feed on human blood at night. They hide in mattresses, box springs, bed frames, and furniture. Unlike many pests, bed bugs do not carry disease, but their bites cause intense itching, sleep disruption, skin rashes, and significant psychological distress.',
        'signs': [
            'Small reddish-brown bugs visible on mattress seams',
            'Tiny white eggs or shed skins in mattress folds',
            'Rust-colored blood stains on bedsheets',
            'Small dark spots (bed bug excrement) on mattress or headboard',
            'Itchy red bites in a line or cluster, especially on exposed skin',
            'Musty, sweet odor in heavily infested rooms',
        ],
        'process': [
            ('Full Room Inspection', 'fas fa-search', 'We inspect mattresses, bed frames, sofas, skirting boards, electrical outlets, and all hiding spots.'),
            ('Chemical Treatment', 'fas fa-spray-can', 'Application of residual insecticide to all harborage areas — mattress seams, frame joints, and crevices.'),
            ('Steam Treatment', 'fas fa-temperature-high', 'High-temperature steam is applied to mattresses and upholstery to kill bugs and eggs on contact.'),
            ('Follow-up Sessions', 'fas fa-redo', 'Second and third sessions as needed to catch newly hatched bugs missed in the first treatment.'),
        ],
        'benefits': [
            'Full room inspection',
            'Chemical spray treatment',
            'Mattress & furniture treatment',
            '2–3 session packages available',
            'Post-treatment guidance provided',
            'Covers all life stages including eggs',
            'Service guarantee included',
            'Discreet and professional service',
        ],
        'faqs': [
            ('How many sessions are needed to eliminate bed bugs?', 'Bed bugs require 2–3 treatment sessions spaced 10–14 days apart because eggs can survive the first treatment. Our package includes follow-up sessions.'),
            ('Do I need to throw away my mattress?', 'In most cases, no. Our treatment effectively kills bed bugs on mattresses. We recommend using mattress encasements after treatment to prevent re-infestation.'),
            ('How did I get bed bugs?', 'Bed bugs are excellent hitchhikers. They commonly spread through travel (hotel stays), second-hand furniture, and contact with infested clothing or luggage.'),
            ('How should I prepare my room for bed bug treatment?', 'Wash all bedding in hot water, remove clutter from the floor and around the bed, and vacate the room during treatment. Our technician will provide a detailed preparation checklist.'),
        ],
        'pricing': [
            ('1 BHK', '400–700 Sq. Ft.', '₹1,500'),
            ('2 BHK', '700–1,000 Sq. Ft.', '₹2,200'),
            ('3 BHK', '1,000–1,600 Sq. Ft.', '₹3,000'),
            ('4 BHK', '1,600–2,400 Sq. Ft.', '₹3,500'),
            ('Hotel Room (per room)', 'Standard Room', '₹800'),
        ],
        'starting_price': '₹1,500',
    },
    'lizard-control': {
        'slug': 'lizard-control',
        'name': 'Lizard Control',
        'tag': 'Safe Repellent',
        'icon': 'fas fa-staff-snake',
        'tagline': 'Keep Lizards Out of Your Home — Safely & Permanently',
        'description': 'Lizards may be harmless, but their presence is unwelcome. Our non-toxic lizard repellent treatments create a barrier that keeps lizards away from your living spaces without harming them.',
        'what_is': 'House lizards (geckos) are common in Indian homes and while they do eat insects, their droppings, eggs, and presence can be unhygienic and distressing for many homeowners. They tend to gather near lights, in kitchens, bathrooms, and behind furniture. Lizard droppings can contaminate food surfaces.',
        'signs': [
            'Lizard droppings (small, dark with white tip) on walls and floors',
            'Egg cases (small, white, hard) behind furniture or in corners',
            'Lizards seen near lights or windows at night',
            'Sticky marks on walls from lizard feet',
            'Lizards in kitchen or near food storage areas',
        ],
        'process': [
            ('Inspection', 'fas fa-search', 'We identify lizard entry points, harborage areas, and food sources (insects) attracting lizards.'),
            ('Repellent Application', 'fas fa-spray-can', 'Application of herbal and chemical repellents on walls, entry points, and lizard pathways.'),
            ('Entry Sealing Advice', 'fas fa-door-closed', 'We identify and advise on sealing entry points like gaps around pipes, windows, and doors.'),
            ('Insect Control', 'fas fa-bug', 'Treating insects that attract lizards — reducing their food source is key to long-term control.'),
        ],
        'benefits': [
            'Safe herbal repellent spray',
            'Entry point treatment',
            'Kitchen & bathroom focus',
            'Child & pet safe formulations',
            'Long-lasting results',
            'Combined insect control option',
            'No harm to lizards — humane',
            'Odorless, safe products',
        ],
        'faqs': [
            ('How long does lizard repellent treatment last?', 'Lizard repellent treatment typically lasts 2–3 months. Re-application is recommended every quarter for best results.'),
            ('Does lizard control harm the lizards?', 'No. Our treatments are repellent-based, not lethal. They create an environment lizards find uncomfortable, causing them to move away naturally.'),
            ('Why do I have so many lizards in my home?', 'Lizards are attracted by a food supply of insects. Reducing insects in your home (cockroaches, mosquitoes, ants) will also reduce lizard activity.'),
            ('Can lizard treatment be combined with other pest control?', 'Yes, we recommend combining lizard control with general pest control for comprehensive results. We offer combo packages at discounted rates.'),
        ],
        'pricing': [
            ('1 BHK', '400–700 Sq. Ft.', '₹800'),
            ('2 BHK', '700–1,000 Sq. Ft.', '₹1,200'),
            ('3 BHK', '1,000–1,600 Sq. Ft.', '₹1,500'),
            ('4 BHK', '1,600–2,400 Sq. Ft.', '₹1,800'),
            ('Commercial Space', 'Custom Area', 'Custom Quote'),
        ],
        'starting_price': '₹800',
    },
    'ant-control': {
        'slug': 'ant-control',
        'name': 'Ant Control',
        'tag': 'Colony Elimination',
        'icon': 'fas fa-bug',
        'tagline': 'Eliminate Ant Colonies at the Source',
        'description': 'Ant infestations can be surprisingly destructive. Our gel bait and spray methods target ant colonies at the source — including the queen — for complete and lasting elimination.',
        'what_is': 'Ants are social insects that live in large colonies ranging from a few hundred to millions of individuals. Common species in Delhi NCR include black garden ants, red fire ants, and carpenter ants. While small ants may seem harmless, they contaminate food, and carpenter ants can cause structural damage by tunneling through wood.',
        'signs': [
            'Visible ant trails leading to food sources',
            'Small piles of sandy soil or sawdust near walls',
            'Ants in kitchen, sugar containers, or pet food',
            'Flying ants (swarmers) indicating a nearby colony',
            'Hollow sounds in wooden structures (carpenter ants)',
            'Ants in electrical fittings or switches',
        ],
        'process': [
            ('Inspection', 'fas fa-search', 'We identify ant species, locate the colony, and map all entry points and foraging trails.'),
            ('Gel Bait Treatment', 'fas fa-syringe', 'Slow-acting gel bait is placed along ant trails — worker ants carry it back to the colony, eliminating the queen.'),
            ('Spray Treatment', 'fas fa-spray-can', 'Chemical spray for immediate knockdown of visible ants and treatment of garden perimeters.'),
            ('Perimeter Treatment', 'fas fa-border-all', 'External perimeter spray to create a barrier preventing ants from entering the building.'),
        ],
        'benefits': [
            'Gel bait treatment',
            'Spray for heavy infestations',
            'Garden & exterior perimeter treatment',
            'Multiple species coverage',
            'Residual protection for weeks',
            'Colony elimination including the queen',
            'Indoor and outdoor treatment',
            'Safe for food preparation areas',
        ],
        'faqs': [
            ('Why do I suddenly have so many ants?', 'Ants are attracted by food, water, and warmth. Sudden increases often happen during monsoon season (as colonies relocate) or when a new food source is found in your home.'),
            ('How long does ant treatment last?', 'Gel bait treatment is effective for 3–4 weeks as the colony is gradually eliminated. Spray treatment provides residual protection for 30–45 days.'),
            ('Will ants come back after treatment?', 'If the colony is fully eliminated (including the queen), ants should not return. However, new colonies can establish. We recommend periodic preventive treatment.'),
            ('Can I do anything to prevent ants myself?', 'Keep food sealed, fix leaking pipes, seal gaps in walls and floors, and avoid leaving pet food out overnight. These measures complement professional treatment.'),
        ],
        'pricing': [
            ('1 BHK', '400–700 Sq. Ft.', '₹850'),
            ('2 BHK', '700–1,000 Sq. Ft.', '₹950'),
            ('3 BHK', '1,000–1,600 Sq. Ft.', '₹1,100'),
            ('4 BHK', '1,600–2,400 Sq. Ft.', '₹1,200'),
            ('Garden / Outdoor', 'Per Treatment', '₹500'),
        ],
        'starting_price': '₹850',
    },
    'herbal-pest-control': {
        'slug': 'herbal-pest-control',
        'name': 'Herbal Pest Control',
        'tag': 'Eco-Friendly',
        'icon': 'fas fa-leaf',
        'tagline': 'Safe, Green, Effective — Our Signature Eco-Friendly Service',
        'description': 'Our signature herbal pest control service uses plant-derived, non-toxic formulations. Equally effective as chemical treatments but 100% safe for your family, pets, and the environment.',
        'what_is': 'Herbal pest control uses botanical extracts, essential oils, and plant-derived compounds as the active ingredients instead of synthetic chemicals. These natural pesticides are biodegradable, leave no harmful residue, and are safe for use around children, elderly, and pets — making them ideal for homes, schools, hospitals, and food processing facilities.',
        'signs': [
            'You have young children or infants at home',
            'You or a family member have chemical sensitivities',
            'You want a pet-safe pest control solution',
            'Your property is near food preparation or storage',
            'You prefer an eco-friendly and sustainable approach',
            'You need pest control in a healthcare or educational facility',
        ],
        'process': [
            ('Consultation', 'fas fa-comments', 'We assess your pest problem, property type, and sensitivity needs to recommend the right herbal formulation.'),
            ('Herbal Spray Treatment', 'fas fa-leaf', 'Application of plant-based pesticide sprays to all affected areas — safe for immediate re-entry.'),
            ('Gel Bait (Herbal)', 'fas fa-syringe', 'Herbal gel bait placed in targeted areas for cockroaches and ants — odorless and effective.'),
            ('Preventive Recommendations', 'fas fa-shield-alt', 'Natural prevention tips to reduce pest activity and maintain long-term pest-free results.'),
        ],
        'benefits': [
            'Plant-based non-toxic solutions',
            'Safe for children, pets & elderly',
            'No strong chemical odor',
            'Covers all common household pests',
            'ISO certified eco-friendly process',
            'No need to vacate home after treatment',
            'Biodegradable, no harmful residue',
            'Safe for kitchens and food areas',
        ],
        'faqs': [
            ('Is herbal pest control as effective as chemical pest control?', 'Yes. Our herbal formulations are carefully selected for efficacy. They may require slightly more frequent applications but are equally effective for most common household pests.'),
            ('Which pests can be controlled with herbal treatment?', 'Cockroaches, ants, mosquitoes, lizards, silverfish, and general household insects can be treated effectively with herbal formulations.'),
            ('Can herbal pest control be used in hospitals and schools?', 'Yes, this is one of the key advantages of herbal pest control. It is safe for sensitive environments including hospitals, schools, and food processing areas.'),
            ('Is herbal pest control more expensive?', 'Herbal treatments are slightly more expensive than standard chemical treatments due to the cost of botanical ingredients. However, the safety benefits make them the preferred choice for many families.'),
        ],
        'pricing': [
            ('1 BHK', '400–700 Sq. Ft.', '₹1,000'),
            ('2 BHK', '700–1,000 Sq. Ft.', '₹1,300'),
            ('3 BHK', '1,000–1,600 Sq. Ft.', '₹1,600'),
            ('4 BHK', '1,600–2,400 Sq. Ft.', '₹1,900'),
            ('Commercial Space', 'Custom Area', 'Custom Quote'),
        ],
        'starting_price': '₹1,000',
    },
}

# ─── Location Data ─────────────────────────────────────────────────────────────
LOCATIONS = {
    'gurugram': {
        'slug': 'gurugram',
        'name': 'Gurugram',
        'alt_name': 'Gurgaon',
        'tagline': 'Professional Pest Control Services in Gurugram (Gurgaon)',
        'description': 'Secure Herbal Pest Control offers ISO 9001:2015 certified pest control services in Gurugram. We cover all major sectors and localities with herbal and chemical treatments for homes, offices, and commercial properties.',
        'localities': [
            'Sector 14', 'Sector 15', 'Sector 22', 'Sector 29', 'Sector 31',
            'MG Road', 'DLF City', 'Sohna Road', 'Golf Course Road',
            'Cyber Hub', 'Palam Vihar', 'Udyog Vihar', 'Manesar', 'Bhondsi',
        ],
        'about': 'Gurugram (formerly Gurgaon) is a major corporate and residential hub in Delhi NCR. The city\'s rapid growth, high-rise apartments, and commercial complexes create ideal conditions for pest infestations. Our Gurugram team has over 15 years of experience tackling termites in new constructions, cockroaches in apartment kitchens, and rodents in warehouses.',
        'local_challenges': [
            'Termite infestations in new and under-construction buildings',
            'Cockroach and rat problems in high-rise apartment complexes',
            'Mosquito breeding in construction sites and stagnant water',
            'Bed bugs spreading through furnished corporate accommodations',
            'General pest problems in IT offices and commercial spaces',
        ],
        'testimonials': [
            ('Rahul Sharma', 'DLF Phase 2, Gurugram', '5', 'Excellent termite control service. The team was professional and treated our entire 3 BHK thoroughly. No termite activity after 6 months!'),
            ('Priya Mehta', 'Sector 49, Gurugram', '5', 'Called them for cockroach problem in our new apartment. Gel bait treatment worked brilliantly. Highly recommend Secure Herbal!'),
            ('Amit Gupta', 'Cyber City, Gurugram', '5', 'Used their service for our office. Completely professional, came on time, and the results were great. Will definitely book again.'),
        ],
        'branch_address': 'Sector 14, MG Road, Gurugram, Haryana',
        'contact_phone': '7676072229',
    },
    'dwarka': {
        'slug': 'dwarka',
        'name': 'Dwarka',
        'alt_name': 'Dwarka, New Delhi',
        'tagline': 'Trusted Pest Control Services in Dwarka, New Delhi',
        'description': 'Secure Herbal Pest Control provides professional herbal and chemical pest control in all sectors of Dwarka, New Delhi. ISO 9001:2015 certified, with same-day service available.',
        'localities': [
            'Dwarka Sector 1', 'Dwarka Sector 3', 'Dwarka Sector 5',
            'Dwarka Sector 7', 'Dwarka Sector 10', 'Dwarka Sector 11',
            'Dwarka Sector 12', 'Dwarka Sector 17', 'Dwarka Sector 22',
            'Dwarka Mor', 'Dwarka Sub City', 'Palam',
        ],
        'about': 'Dwarka is one of Delhi\'s largest planned residential sub-cities with thousands of apartment complexes and independent houses. The dense residential nature of the area means pests can spread quickly between units. Our dedicated Dwarka team specializes in apartment pest control, covering cockroaches, termites, bed bugs, mosquitoes, and all common household pests.',
        'local_challenges': [
            'Cockroach infestations spreading between apartment units',
            'Termite damage in older DDA flats',
            'Bed bugs in furnished apartments near the metro corridor',
            'Mosquito breeding in the Dwarka lake and parkland areas',
            'Rodent activity in basement parking and storage areas',
        ],
        'testimonials': [
            ('Neha Kapoor', 'Sector 10, Dwarka', '5', 'Got their bed bug treatment done. Three sessions, completely pest-free now. Very professional team and reasonably priced.'),
            ('Vikash Yadav', 'Sector 22, Dwarka', '5', 'Best pest control in Dwarka. Called for cockroach problem, they came the same day. Gel bait worked perfectly!'),
            ('Suman Lata', 'Palam, Dwarka', '5', 'Very satisfied with their herbal pest control service. No chemicals smell, safe for our kids. Will call again.'),
        ],
        'branch_address': 'Dwarka Sector 10, New Delhi',
        'contact_phone': '7676072229',
    },
    'rohini': {
        'slug': 'rohini',
        'name': 'Rohini',
        'alt_name': 'Rohini, New Delhi',
        'tagline': 'Expert Pest Control Services in Rohini, New Delhi',
        'description': 'Secure Herbal Pest Control covers all sectors of Rohini with fast, effective, and affordable pest control services. ISO 9001:2015 certified team with 15+ years of experience.',
        'localities': [
            'Rohini Sector 7', 'Rohini Sector 9', 'Rohini Sector 11',
            'Rohini Sector 13', 'Rohini Sector 15', 'Rohini Sector 16',
            'Rohini Sector 17', 'Rohini Sector 24', 'Rohini Sector 25',
            'Pitampura', 'Shalimar Bagh', 'Prashant Vihar', 'Deepali Chowk',
        ],
        'about': 'Rohini is a large residential district in North-West Delhi comprising 27 sectors. Home to lakhs of families in both DDA housing and private societies, Rohini faces significant pest challenges especially during monsoon season. Our Rohini branch has been serving this community for years, building strong relationships with residents and housing societies.',
        'local_challenges': [
            'Seasonal mosquito and dengue outbreaks during monsoon',
            'Cockroach infestations in older DDA flats',
            'Termite problems in ground-floor apartments',
            "Rodent activity near Rohini's markets and commercial areas",
            'Silverfish damage to books and clothing in storage',
        ],
        'testimonials': [
            ('Deepak Verma', 'Sector 11, Rohini', '5', 'Called for mosquito fogging before the monsoon. Team was punctual and thorough. Have been pest-free all season!'),
            ('Sunita Singh', 'Pitampura, Delhi', '5', 'Excellent cockroach treatment. No cockroaches in the kitchen since the gel bait treatment 3 months ago. Very happy!'),
            ('Ravi Kumar', 'Prashant Vihar, Rohini', '5', 'Used them for termite inspection before buying our flat. Very detailed inspection report and reasonable charges.'),
        ],
        'branch_address': 'Rohini Sector 9, New Delhi',
        'contact_phone': '7676072229',
    },
    'patel-nagar': {
        'slug': 'patel-nagar',
        'name': 'Patel Nagar',
        'alt_name': 'Patel Nagar, New Delhi',
        'tagline': 'Reliable Pest Control Services in Patel Nagar, New Delhi',
        'description': 'Secure Herbal Pest Control offers trusted pest control in Patel Nagar and surrounding Central Delhi areas. Experienced team, affordable prices, and guaranteed results.',
        'localities': [
            'West Patel Nagar', 'East Patel Nagar', 'Rajendra Nagar',
            'Ramesh Nagar', 'Moti Nagar', 'Kirti Nagar',
            'Shadipur', 'Raja Garden', 'Tilak Nagar', 'Rajouri Garden',
        ],
        'about': 'Patel Nagar and Central Delhi is one of the most densely populated areas of the city. The mix of old residential colonies, commercial markets, and newer apartment buildings creates a challenging environment for pest management. Our team has extensive experience dealing with the unique pest pressures of Central Delhi — from termite-affected old buildings to cockroach-infested commercial kitchens.',
        'local_challenges': [
            'Termite damage in old construction buildings in Central Delhi',
            'Heavy cockroach infestations in shop basements and markets',
            'Rodent problems near vegetable and grain markets',
            'Mosquito breeding in waterlogged areas during monsoon',
            'Silverfish and carpet beetles in textile shops and storage',
        ],
        'testimonials': [
            ('Geeta Sharma', 'West Patel Nagar, Delhi', '5', 'Very professional pest control. They handled our termite problem in a 30-year-old house expertly. Highly recommended!'),
            ('Arun Malhotra', 'Rajouri Garden, Delhi', '5', 'Cockroach treatment in our restaurant kitchen. Very safe products used, no need to shut down. Highly satisfied.'),
            ('Kavita Devi', 'Moti Nagar, Delhi', '5', 'Good and reliable service. Called for rat control and the team came the very next day. Problem solved!'),
        ],
        'branch_address': 'West Patel Nagar, New Delhi',
        'contact_phone': '7676072229',
    },
    'vasant-kunj': {
        'slug': 'vasant-kunj',
        'name': 'Vasant Kunj',
        'alt_name': 'Vasant Kunj, South Delhi',
        'tagline': 'Premium Pest Control Services in Vasant Kunj, South Delhi',
        'description': 'Secure Herbal Pest Control provides high-quality pest control services in Vasant Kunj and South Delhi. Herbal, eco-friendly options available for premium homes and apartments.',
        'localities': [
            'Vasant Kunj Pocket A', 'Vasant Kunj Pocket B', 'Vasant Kunj Pocket C',
            'Vasant Kunj Pocket D', 'Vasant Enclave', 'Vasant Vihar',
            'Shivaji Marg', 'Mehrauli', 'Munirka', 'R K Puram',
        ],
        'about': 'Vasant Kunj is one of South Delhi\'s premier residential areas, home to upscale apartments, embassies, and premium commercial properties. Residents here prefer eco-friendly, odorless pest control solutions that are safe for their families and compatible with the aesthetic of their homes. Our herbal pest control service is especially popular in Vasant Kunj.',
        'local_challenges': [
            'Bed bug infestations in premium furnished apartments',
            'Termite damage in older DDA flats and independent homes',
            'Cockroach problems in large apartment kitchen complexes',
            'Mosquito issues near Sanjay Van and green belt areas',
            'Ant infestations in garden apartments and ground floors',
        ],
        'testimonials': [
            ('Ananya Rajput', 'Vasant Kunj Pocket B', '5', 'Used their herbal pest control service. Completely odorless, my kids were back in the room within an hour. Amazing!'),
            ('Rohit Batra', 'Vasant Vihar, Delhi', '5', 'Professional termite treatment for our independent house. Drilling and injection done very neatly. Satisfied with results.'),
            ('Meena Joshi', 'Munirka, Delhi', '5', 'Bed bug treatment done perfectly in 2 sessions. No more bites! Very thorough team. Reasonably priced.'),
        ],
        'branch_address': 'Vasant Kunj, South Delhi',
        'contact_phone': '7676072229',
    },
    'malviya-nagar': {
        'slug': 'malviya-nagar',
        'name': 'Malviya Nagar',
        'alt_name': 'Malviya Nagar, South Delhi',
        'tagline': 'Trusted Pest Control Services in Malviya Nagar, South Delhi',
        'description': 'Secure Herbal Pest Control serves Malviya Nagar and surrounding South Delhi localities with certified pest control solutions for homes, PGs, and commercial properties.',
        'localities': [
            'Malviya Nagar', 'Saket', 'Hauz Khas', 'Green Park',
            'Greater Kailash', 'Lado Sarai', 'Neb Sarai',
            'Begumpur', 'Sheikh Sarai', 'Pushp Vihar',
        ],
        'about': 'Malviya Nagar and the surrounding South Delhi localities are characterized by a mix of old residential colonies, PG accommodations for students and working professionals, and thriving markets and restaurants. This diversity brings unique pest challenges — from cockroaches in PG kitchens to termites in older kothis and bed bugs in shared accommodations.',
        'local_challenges': [
            'Bed bug infestations in PG accommodations and shared housing',
            'Cockroach problems in restaurants and commercial kitchens',
            'Termite damage in older kothis and bungalows',
            'Rodent activity near vegetable markets in Saket and Malviya Nagar',
            'Ant and silverfish problems in South Delhi homes',
        ],
        'testimonials': [
            ('Pooja Nair', 'Malviya Nagar, Delhi', '5', 'Had a severe cockroach problem in our PG. Secure Herbal fixed it completely with gel bait. Very happy with the service!'),
            ('Suresh Pillai', 'Hauz Khas, Delhi', '5', 'Termite treatment for our old kothi. Very experienced team, the drilling was done very cleanly. Excellent work!'),
            ('Tanya Bose', 'Saket, Delhi', '5', 'Called for mosquito control before hosting a garden party. Fogging was done 2 days before. Completely mosquito-free event!'),
        ],
        'branch_address': 'Malviya Nagar, South Delhi',
        'contact_phone': '7676072229',
    },
    'faridabad': {
        'slug': 'faridabad',
        'name': 'Faridabad',
        'alt_name': 'Faridabad, Haryana',
        'tagline': 'Professional Pest Control Services in Faridabad, Haryana',
        'description': 'Secure Herbal Pest Control covers all areas of Faridabad with effective pest control for residential and industrial properties. ISO 9001:2015 certified with competitive pricing.',
        'localities': [
            'Sector 15', 'Sector 16A', 'Sector 21C', 'NIT Faridabad',
            'Old Faridabad', 'Ballabgarh', 'NH-48 Corridor',
            'Suraj Kund', 'Mewat Road', 'Neharpar', 'Greater Faridabad',
        ],
        'about': 'Faridabad is one of Haryana\'s largest industrial cities and a growing residential hub in Delhi NCR. The combination of industrial areas, large housing colonies, and rapid new construction creates significant pest management needs. Our Faridabad team is experienced with both residential pest control and industrial/commercial pest management for factories and warehouses.',
        'local_challenges': [
            'Industrial pest problems in factories and warehouses',
            'Termite infestations in new residential construction',
            'Rodent and pest issues in food processing and storage units',
            'Mosquito breeding near industrial drains and low-lying areas',
            'General pest control for large residential societies',
        ],
        'testimonials': [
            ('Rajesh Tyagi', 'Sector 15, Faridabad', '5', 'They handled pest control for our factory very professionally. Proper documentation provided for compliance. Excellent service!'),
            ('Sunita Chauhan', 'NIT Faridabad', '5', 'Very good cockroach and rat control service. Came on time, did thorough treatment. Reasonable rates for Faridabad.'),
            ('Harish Kumar', 'Ballabgarh, Faridabad', '5', 'Termite control for new house. Pre-construction treatment done properly. Happy with the service and warranty provided.'),
        ],
        'branch_address': 'NH-48 Corridor, Faridabad, Haryana',
        'contact_phone': '7676072229',
    },
    'noida': {
        'slug': 'noida',
        'name': 'Noida',
        'alt_name': 'Noida, Uttar Pradesh',
        'tagline': 'Expert Pest Control Services in Noida & Greater Noida',
        'description': 'Secure Herbal Pest Control provides certified pest control services across Noida sectors and Greater Noida. Professional treatment for homes, IT offices, and commercial spaces.',
        'localities': [
            'Sector 18', 'Sector 44', 'Sector 50', 'Sector 62',
            'Sector 63', 'Sector 76', 'Sector 78', 'Sector 100',
            'Sector 119', 'Sector 137', 'Greater Noida West',
            'Greater Noida (Knowledge Park)', 'Noida Extension',
        ],
        'about': 'Noida is a modern, planned city that is home to thousands of apartment complexes and a major hub for IT companies and MNCs. The city\'s many high-rise societies and corporate parks present specific pest challenges. Our Noida team specializes in apartment complex pest control and office pest management, serving both residential societies and large corporate campuses.',
        'local_challenges': [
            'Cockroach and mosquito infestations in high-rise apartment societies',
            'Termite problems in Noida\'s many new residential constructions',
            'Bed bug issues in IT employee housing and serviced apartments',
            'Rodent problems near Noida\'s food courts and markets',
            'Society-level pest management for large residential complexes',
        ],
        'testimonials': [
            ('Karan Mehta', 'Sector 62, Noida', '5', 'Used Secure Herbal for our entire apartment society. Very organized team, covered all common areas and individual flats. Highly recommend!'),
            ('Divya Singh', 'Sector 137, Noida', '5', 'Bed bug treatment done in my flat. Complete and thorough service. No more bites! Very happy with the results.'),
            ('Aakash Sharma', 'Greater Noida West', '5', 'Herbal pest control for our home with newborn. Very safe products, no smell, and completely effective. Brilliant service!'),
        ],
        'branch_address': 'Sector 18 / 62, Noida, UP',
        'contact_phone': '7676072229',
    },
}

ALL_SERVICES = list(SERVICES.values())
ALL_LOCATIONS = list(LOCATIONS.values())

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

@app.route('/submit-quote', methods=['POST'])
def submit_quote():
    data = request.json
    return jsonify({'success': True, 'message': 'Thank you! We will contact you shortly.'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)

"""
Enhanced vocabulary database for the flashcard game.
This module contains an expanded collection of vocabulary organized by theme and difficulty level.
"""

# Vocabulary sets organized by theme and difficulty level (Beginner, Intermediate, Advanced)
VOCABULARY_DATABASE = {
    "General": {
        "Beginner": [
            ("Happy", "Feeling or showing pleasure", "She has a happy smile on her face."),
            ("Sad", "Feeling or showing sorrow", "He looked sad when he lost the game."),
            ("Big", "Of considerable size", "That's a big house you have."),
            ("Small", "Of a size that is less than normal", "The small dog barked loudly."),
            ("Fast", "Moving or capable of moving quickly", "She is a fast runner."),
            ("Slow", "Moving or operating at low speed", "The slow turtle won the race."),
            ("Hot", "Having a high temperature", "Be careful, the soup is hot."),
            ("Cold", "Having a low temperature", "I need a jacket because it's cold outside."),
        ],
        "Intermediate": [
            ("Ubiquitous", "Present everywhere", "Cell phones have become ubiquitous in modern society."),
            ("Eloquent", "Fluent or persuasive speaking", "Her eloquent speech moved the audience to tears."),
            ("Benevolent", "Well-meaning and kindly", "The benevolent donor gave millions to charity."),
            ("Meticulous", "Showing great attention to detail", "He is meticulous about keeping records."),
            ("Pragmatic", "Dealing with things sensibly", "We need a pragmatic approach to solve this problem."),
            ("Ambiguous", "Open to more than one interpretation", "The instructions were ambiguous and confusing."),
            ("Diligent", "Having or showing care in work", "She is a diligent student who always completes assignments."),
            ("Resilient", "Able to recover quickly", "Children are often resilient after experiencing setbacks."),
        ],
        "Advanced": [
            ("Ephemeral", "Lasting for a very short time", "Fame can be ephemeral in the entertainment industry."),
            ("Sycophant", "A person who acts obsequiously", "He surrounded himself with sycophants who never challenged him."),
            ("Perfunctory", "Carried out without real interest", "She gave a perfunctory nod and continued working."),
            ("Obfuscate", "Make obscure or unclear", "Politicians often obfuscate the truth with complex language."),
            ("Recalcitrant", "Having an obstinately uncooperative attitude", "The recalcitrant child refused to follow instructions."),
            ("Pernicious", "Having a harmful effect", "The pernicious rumors damaged her reputation."),
            ("Perspicacious", "Having keen mental perception", "Her perspicacious analysis identified the core issue."),
            ("Equivocate", "Use ambiguous language to conceal the truth", "The witness continued to equivocate when questioned."),
        ]
    },
    "Business": {
        "Beginner": [
            ("Job", "Regular work", "She has a new job at the bank."),
            ("Pay", "Money given for work", "The pay is good at my new job."),
            ("Sale", "Exchange of goods for money", "The store is having a big sale this weekend."),
            ("Cost", "Amount of money needed", "The cost of living is high in this city."),
            ("Team", "Group working together", "Our team won the project bid."),
            ("Goal", "Aim or desired result", "My goal is to finish this by Friday."),
            ("Plan", "Detailed proposal for doing something", "We need a plan for the new product launch."),
            ("Task", "Piece of work to be done", "I have many tasks to complete today."),
        ],
        "Intermediate": [
            ("Revenue", "Income from business activities", "The company's revenue increased by 15% last quarter."),
            ("Negotiate", "Try to reach an agreement", "We will negotiate the terms of the contract tomorrow."),
            ("Deadline", "Time by which something must be done", "The project deadline is next Friday."),
            ("Strategy", "Plan of action to achieve a goal", "Our marketing strategy needs revision."),
            ("Budget", "Estimate of income and expenditure", "The department exceeded its budget this year."),
            ("Delegate", "Entrust a task to another person", "Managers must learn to delegate effectively."),
            ("Innovate", "Make changes to something established", "Companies must innovate to stay competitive."),
            ("Collaborate", "Work jointly on an activity", "Our teams will collaborate on this project."),
        ],
        "Advanced": [
            ("Amortization", "Gradual reduction of a debt", "The loan amortization schedule spans 30 years."),
            ("Arbitrage", "Simultaneous buying and selling to profit from price differences", "The trader made money through currency arbitrage."),
            ("Depreciation", "Reduction in value of an asset", "The equipment depreciation is calculated annually."),
            ("Fiduciary", "Involving trust, especially with money", "The advisor has a fiduciary responsibility to clients."),
            ("Liquidity", "Availability of liquid assets", "The company maintains strong liquidity for emergencies."),
            ("Paradigm", "Pattern or model", "This represents a new paradigm in business thinking."),
            ("Synergy", "Interaction producing greater combined effect", "The merger created significant synergy between departments."),
            ("Volatility", "Liability to change rapidly", "Market volatility makes prediction difficult."),
        ]
    },
    "Science": {
        "Beginner": [
            ("Plant", "Living organism that grows in soil", "The plant needs water to grow."),
            ("Animal", "Living organism that feeds on organic matter", "A dog is an animal that barks."),
            ("Water", "Clear liquid that forms seas and rain", "Plants need water to survive."),
            ("Air", "Mixture of gases around the Earth", "We breathe air to live."),
            ("Sun", "Star at the center of our solar system", "The sun gives us light and heat."),
            ("Moon", "Natural satellite of the Earth", "The moon orbits around Earth."),
            ("Star", "Ball of gas in space that produces light", "You can see many stars at night."),
            ("Rock", "Solid mineral material", "She collected rocks from the beach."),
        ],
        "Intermediate": [
            ("Hypothesis", "Proposed explanation for a phenomenon", "The scientist developed a hypothesis about cell growth."),
            ("Catalyst", "Substance that increases reaction rate", "Enzymes act as catalysts in biological reactions."),
            ("Ecosystem", "Biological community of organisms", "The pond is a complex ecosystem with many species."),
            ("Quantum", "Discrete quantity of energy", "Light behaves as both waves and quantum particles."),
            ("Molecule", "Group of atoms bonded together", "Water molecules consist of hydrogen and oxygen."),
            ("Velocity", "Speed in a given direction", "The velocity of the car was 60 miles per hour."),
            ("Gravity", "Force that attracts objects to Earth", "Gravity keeps us from floating into space."),
            ("Evolution", "Process of gradual change", "Darwin's theory explains evolution through natural selection."),
        ],
        "Advanced": [
            ("Thermodynamics", "Physics of heat and temperature", "The laws of thermodynamics govern energy transfer."),
            ("Quantum Entanglement", "Correlation between quantum particles", "Quantum entanglement allows instantaneous communication between particles."),
            ("Neuroplasticity", "Brain's ability to reorganize itself", "Neuroplasticity allows recovery after brain injury."),
            ("Epigenetics", "Study of heritable changes in gene expression", "Epigenetics explains how environment affects gene expression."),
            ("Nanotechnology", "Manipulation of matter on atomic scale", "Nanotechnology is revolutionizing medicine and electronics."),
            ("Biomimicry", "Imitation of natural biological designs", "The airplane wing design uses biomimicry based on bird wings."),
            ("Entropy", "Measure of disorder in a system", "According to the second law of thermodynamics, entropy always increases."),
            ("Quasar", "Extremely luminous active galactic nucleus", "Quasars are among the brightest objects in the universe."),
        ]
    },
    "Travel": {
        "Beginner": [
            ("Trip", "Journey or excursion", "We took a trip to the beach last weekend."),
            ("Map", "Diagram of an area", "I used a map to find the museum."),
            ("Hotel", "Place providing accommodation", "We stayed at a nice hotel downtown."),
            ("Flight", "Journey by air", "Our flight to Paris takes eight hours."),
            ("Beach", "Shore of a body of water", "The beach was crowded with tourists."),
            ("City", "Large town", "New York is a busy city."),
            ("Bus", "Large road vehicle for passengers", "We took the bus to the airport."),
            ("Train", "Connected series of vehicles on rails", "The train arrives at 3 PM."),
        ],
        "Intermediate": [
            ("Itinerary", "Planned route of a journey", "Our itinerary includes three days in Rome."),
            ("Excursion", "Short journey made for pleasure", "We took an excursion to the nearby islands."),
            ("Passport", "Document for traveling abroad", "Don't forget to bring your passport."),
            ("Destination", "Place to which someone is going", "Paris was our final destination."),
            ("Accommodation", "Place where someone stays", "The accommodation was comfortable and clean."),
            ("Souvenir", "Thing kept as a reminder of a place", "I bought a souvenir from the gift shop."),
            ("Cuisine", "Style of cooking", "Thai cuisine is known for its spicy flavors."),
            ("Landmark", "Object recognizable from distance", "The Eiffel Tower is a famous landmark."),
        ],
        "Advanced": [
            ("Wanderlust", "Strong desire to travel", "Her wanderlust led her to visit over 50 countries."),
            ("Cosmopolitan", "Including people from many countries", "Singapore is a cosmopolitan city with diverse cultures."),
            ("Ecotourism", "Tourism directed at natural environments", "Ecotourism aims to minimize impact on the environment."),
            ("Expatriate", "Person living outside their native country", "Many expatriates form communities abroad."),
            ("Pilgrimage", "Journey to a sacred place", "Muslims make a pilgrimage to Mecca."),
            ("Sabbatical", "Extended period of leave", "He took a sabbatical to travel around the world."),
            ("Nomadic", "Moving from place to place", "They live a nomadic lifestyle, never staying in one place."),
            ("Vernacular", "Language or dialect of a region", "The guide explained the local vernacular expressions."),
        ]
    }
}

# Default vocabulary sets for backward compatibility
VOCABULARY_SETS = {
    "General": [(word, definition) for word, definition, _ in VOCABULARY_DATABASE["General"]["Intermediate"][:12]],
    "Business": [(word, definition) for word, definition, _ in VOCABULARY_DATABASE["Business"]["Intermediate"][:12]],
    "Science": [(word, definition) for word, definition, _ in VOCABULARY_DATABASE["Science"]["Intermediate"][:12]],
    "Travel": [(word, definition) for word, definition, _ in VOCABULARY_DATABASE["Travel"]["Intermediate"][:12]]
}

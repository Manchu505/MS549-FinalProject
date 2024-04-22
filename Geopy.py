from geopy.distance import great_circle

# List of national parks with their names and coordinates (latitude, longitude)
parks = [
    ("Yellowstone", (44.4280, -110.5885)),
    ("Yosemite", (37.8651, -119.5383)),
    ("Grand Canyon", (36.1069, -112.1129)),
    ("Zion", (37.2982, -113.0263)),
    ("Great Smoky Mountains", (35.6118, -83.4895)),
    ("Rocky Mountain", (40.3428, -105.6836)),
    ("Olympic", (47.8021, -123.6044)),
    ("Acadia", (44.3386, -68.2733)),
    ("Glacier", (48.7596, -113.7870)),
    ("Joshua Tree", (33.8734, -115.9010)),
    ("Bryce Canyon", (37.5930, -112.1871)),
    ("Arches", (38.7331, -109.5925)),
    ("Sequoia and Kings Canyon", (36.4864, -118.5658)),
    ("Death Valley", (36.5054, -117.0794)),
    ("Everglades", (25.2866, -80.8987)),
    ("Cuyahoga Valley", (41.2808, -81.5678)),
    ("Mount Rainier", (46.8523, -121.7603)),
    ("Shenandoah", (38.2928, -78.6796)),
    ("Badlands", (43.8554, -102.3397)),
    ("Lassen Volcanic", (40.4977, -121.4207)),
    ("Saguaro", (32.1479, -110.7957))
]

# Function to calculate distances between all parks
def calculate_distances(parks):
    results = []
    for i in range(len(parks)):
        for j in range(i + 1, len(parks)):
            park1, coords1 = parks[i]
            park2, coords2 = parks[j]
            distance = great_circle(coords1, coords2).miles  # distance in miles
            results.append(f"Distance between {park1} and {park2}: {distance:.2f} miles")
    return results

# Calculate and print the distances
distances = calculate_distances(parks)
for distance in distances:
    print(distance)

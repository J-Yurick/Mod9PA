# PalmerPenguinsM9.py
# J. Andrew Yurick
# November 9, 2026
# Analyze Palmer Penguin observations using classes and objects

# import modules
import math
from penguin import Penguin

# constants representing the species and count
SP_CHINSTRAP = "Chinstrap"
SP_GENTOO = "Gentoo"
SP_ADELIE = "Adelie"
NUM_CHINSTRAP = 68
NUM_GENTOO = 123
NUM_ADELIE = 151

# functions for penguin analysis
def read_penguin_row(row_number):
    penguin_row = ""

    # open the CSV file and skip the header row
    with open("PalmerPenguins.csv", "r") as penguin_file:
        penguin_file.readline()

        current_row = 1

        # search for the requested data row
        for row in penguin_file:
            if current_row == row_number:
                penguin_row = row.strip()
                break

            current_row += 1

    # return the requested row as a string
    return penguin_row

def calculate_percentage(count, total):
    percentage = count / total * 100
    return percentage

def classify_species(percent):
    if percent < 25:
        size_category = "small"
    elif percent >= 25 and percent < 40:
        size_category = "medium"
    else:
        size_category = "large"
    return size_category

def get_position_description(
        selected_species,
        largest_species,
        smallest_species
):
    if selected_species == largest_species:
        position_description = "largest"
    elif selected_species == smallest_species:
        position_description = "smallest"
    else:
        position_description = "middle-sized"
    return position_description

def display_species_statistics(names, counts, percentages):
    for index, species in enumerate(names):
        print(
            f"{species}: {counts[index]} "
            f"({percentages[index]:.2f}%)"
        )
    print()

def display_penguin_observation(
        sample_number,
        species,
        bill_length,
        bill_depth,
        body_mass,
        sex
):
    print("Sample Penguin Observation")
    print()
    print(f"{'Sample Number:':<15}{sample_number}")
    print(f"{'Species:':<15}{species}")
    print(f"{'Bill length:':<15}{bill_length} mm")
    print(f"{'Bill depth:':<15}{bill_depth} mm")
    print(f"{'Body mass:':<15}{body_mass} g")
    print(f"{'Sex:':<15}{sex}")
    print()


def main():
    # lists containing related penguin data
    species_names = [SP_CHINSTRAP, SP_GENTOO, SP_ADELIE]
    species_counts = [NUM_CHINSTRAP, NUM_GENTOO, NUM_ADELIE]

    # calculate dataset statistics
    total_species = len(species_names)
    total_penguins = sum(species_counts)
    average_penguins = total_penguins / total_species
    average_penguins_rounded_up = math.ceil(average_penguins)
    chinstrap_percent = calculate_percentage(
        species_counts[0],
        total_penguins
    )
    gentoo_percent = calculate_percentage(
        species_counts[1],
        total_penguins
    )
    adelie_percent = calculate_percentage(
        species_counts[2],
        total_penguins
    )

    # list containing the percentage of each species
    species_percentages = [
        chinstrap_percent,
        gentoo_percent,
        adelie_percent
    ]

    # determine largest and smallest species groups
    largest_count = max(species_counts)
    smallest_count = min(species_counts)
    largest_index = species_counts.index(largest_count)
    smallest_index = species_counts.index(smallest_count)
    largest_species = species_names[largest_index]
    smallest_species = species_names[smallest_index]

    # output the species names with introductory text
    print("Introducing the Palmer Penguins:")
    print()
    print(f"\t{species_names[0]}!")
    print(f"\t{species_names[1]}!")
    print("and last but not least...")
    print()
    print(f"\t{species_names[2]}!")
    print()

    # output dataset statistics
    print(
        f"There are a total of {total_species} "
        f"penguin species in this dataset."
    )
    print(
        f"There are a total of {total_penguins} "
        f"penguins in the dataset."
    )
    print(
        f"The average number of penguins per "
        f"species is " f"{average_penguins:.1f}."
    )
    print(
        f"The average rounded up is "
        f"{average_penguins_rounded_up} penguins."
    )

    # display species statistics using a loop
    display_species_statistics(species_names, \
        species_counts, species_percentages)

    # display the species with the most and fewest observations
    print(
        f"The species with the most observations is "
        f"{largest_species} with {largest_count} penguins."
    )
    print(
        f"The species with the fewest observations is "
        f"{smallest_species} with {smallest_count} penguins."
    )
    print()

    # retrieve sample penguin data 1
    penguin_row = read_penguin_row(1)
    print("Sample dataset row:")
    print(penguin_row)
    print()

    # split the CSV row into individual values
    penguin_data = penguin_row.split(",")


    # Setting Variables & convert numeric values
    sample_number = int(penguin_data[0])
    species = penguin_data[1]
    bill_length = float(penguin_data[2])
    bill_depth = float(penguin_data[3])
    body_mass = int(penguin_data[5])
    sex = penguin_data[6]

    # display the penguin observation
    display_penguin_observation(
        sample_number,
        species,
        bill_length,
        bill_depth,
        body_mass,
        sex
    )

    # retrieve sample penguin data 221
    penguin_row = read_penguin_row(221)
    penguin_data = penguin_row.split(",")

    # Setting Variables & convert numeric values
    sample_number = int(penguin_data[0])
    species = penguin_data[1]
    bill_length = float(penguin_data[2])
    bill_depth = float(penguin_data[3])
    body_mass = int(penguin_data[5])
    sex = penguin_data[6]

    # display the penguin observation
    display_penguin_observation(
        sample_number,
        species,
        bill_length,
        bill_depth,
        body_mass,
        sex
    )

    # Create list to store body masses
    sample_rows = [1, 2, 3, 4, 5]

    # Create list to store Body Masses
    body_masses = []

    # Retrieve and Collect Body Masses
    for bmr_row in sample_rows:
        # retrieve the CSV row
        penguin_row = read_penguin_row(bmr_row)

        # split the row into individual values
        penguin_data = penguin_row.split(",")

        # convert the body mass to an integer
        body_mass = int(penguin_data[5])

        #append the body mass to the list
        body_masses.append(body_mass)

    print("\nSample Body Masses")
    print(body_masses)
    print()

    # Calculate SUmmary Statistics
    observations = len(body_masses)
    total_body_mass = sum(body_masses)
    smallest_body_mass = min(body_masses)
    largest_body_mass = max(body_masses)
    average_body_mass = float(total_body_mass / observations)

    # Print out Body Mass Summary
    print("Body Mass Summary")
    print(f"{'Observations:':<20}{observations}")
    print(f"{'Total body mass:':<20}{total_body_mass} g")
    print(f"{'Smallest body mass:':<20}{smallest_body_mass} g")
    print(f"{'Largest body mass:':<20}{largest_body_mass} g")
    print(f"{'Average body mass:':<20}{average_body_mass:.2f} g")
    print()

    # Create Dictionary of Species Counts
    species_dictionary = {
        SP_CHINSTRAP: NUM_CHINSTRAP,
        SP_GENTOO: NUM_GENTOO,
        SP_ADELIE: NUM_ADELIE
        }

    # Access and Display Dictionary Values 
    # Display Species Count
    print("Species Counts Using a Dictionary")
    for species_key in species_dictionary:
        count = species_dictionary[species_key]
        print(f"{species_key}: {count}")

    # Create a Penguin Object from CSV Data
    penguin_row = read_penguin_row(1)
    penguin_data = penguin_row.split(",")

    # Extract Penguin Attributes
    sample_number = int(penguin_data[0])
    species = penguin_data[1]
    body_mass = int(penguin_data[5])

    # Create Penguin Instance
    sample_penguin = Penguin(
        sample_number,
        species,
        body_mass
    )

    # Display Penguin Object Information
    print("\nPenguin Object Demonstration")
    sample_penguin.display_info()
    
    # Create an empty list for Penguin Objects
    penguin_objects = []

    for sample_row in sample_rows:
        # Retrieve and split the CSV row
        penguin_row = read_penguin_row(sample_row)
        penguin_data = penguin_row.split(",")
        # Create a penguin object
        penguin_object = Penguin(
            int(penguin_data[0]),
            penguin_data[1], 
            int(penguin_data[5])
        )
        # Append the object to penguin_objects
        penguin_objects.append(penguin_object)

    # Print the Penguin Object
    print("\nPenguin Objects")
    for penguin in penguin_objects:
        penguin.display_info()

    # Calculate Average Using Object Attributes
    total_object_mass = 0
    for penguin_object in penguin_objects:
        total_object_mass = total_object_mass + penguin_object.body_mass

    average_object_mass = total_object_mass / len(penguin_objects)

    # Display the Calculated Results
    print("\nObject-Based Body Mass Summary")
    print(f"Observations: {len(penguin_objects)}")
    print(f"Total body mass: {total_object_mass} g")
    print(f"Average body mass: {average_object_mass:.2f} g")


    # Counter for Valid Species
    valid_selections = 0

    # Explore a species based on user input
    print()
    print("Explore a species")
    species_choice = input("Enter Chinstrap, Gentoo, Adelie, or Done: ")
    print()

    # repeatedly prompt the user to explore species
    while species_choice != "Done":
        # validate species selection
        if species_choice not in species_names:
            print(
                f"{species_choice} is not one of "
                f"the species in this dataset."
            )

        # Determine selected species
        else:
            # update the number of valid selections
            valid_selections += 1
            if species_choice == species_names[0]:
                selected_index = 0
            elif species_choice == species_names[1]:
                selected_index = 1
            else:
                selected_index = 2

            selected_species = species_names[selected_index]
            selected_count = species_counts[selected_index]
            selected_percent = species_percentages[selected_index]

            # classify selected species
            size_category = classify_species(selected_percent)

            # Determine species position
            position_description = get_position_description(
                selected_species,
                largest_species,
                smallest_species)

            average_position = (
                "above" if selected_count > average_penguins else "below"
            )

            # Output selected species statistics
            print(
                f"{selected_species} has {selected_count} "
                f"observations, representing {selected_percent:.2f}"
                f"% of the dataset."
            )
            print(
                f"{selected_species} is classified as a "
                f"{size_category} species group."
            )
            print(
                f"{selected_species} is the "
                f"{position_description} species group."
            )
            print(
                f"Its observation count is {average_position} "
                f"the dataset average of {average_penguins:.1f}."
            )

        print()
        print("Explore a species")
        species_choice = input("Enter Chinstrap, Gentoo, Adelie, or Done: ")
        print()

    # display the exploration summary
    print(f"You explored {valid_selections} valid species.")
    print()
    print("Exploration complete.")

main()
import csv, json, sys, getopt


def main(argv):
    try: # Get input and output file from arguments
        opts, args = getopt.getopt(argv, "hi:o:")
    except getopt.GetoptError:
        print('test.py -i <inputfile path> -o <outputfile path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile path> -o <outputfile path>')
            sys.exit()
        elif opt in ("-i"):
            csvFilePath = arg # Input file
        elif opt in ("-o"):
            jsonFilePath = arg # Output file 

    if csvFilePath and jsonFilePath: # Check if input and output files are empty
        csv_to_json(csvFilePath, jsonFilePath)

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    primaryFields = ['targets']
    with open(csvFilePath, encoding='utf-8') as csvFile:
        csvReader = csv.DictReader(csvFile)

        for row in csvReader: # Reads line from csv file and parses it
            tmpRow = {key: [value] for key, value in row.items() if key in primaryFields} 
            tmpRow['labels'] = {key: value for key, value in row.items() if key not in primaryFields} # Will be nested under 'labels' object
            jsonArray.append(tmpRow)

    with open (jsonFilePath, 'w', encoding='utf-8') as jsonFile:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonFile.write(jsonString)

csvFilePath = ''
jsonFilePath = ''

if __name__ == "__main__":
    main(sys.argv[1:])

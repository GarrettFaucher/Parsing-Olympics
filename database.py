import sqlite3

class Database:

    # This method makes our database, table, and populates the data
    def load_data(self):
        conn = sqlite3.connect("database.db");
        c = conn.cursor()

        # Create tables
        try:
            c.execute(
                "CREATE TABLE tblCountries(fldCountry VARCHAR(74), pmkCountryCode VARCHAR(3), fldPopulation int(255), fldGDP int(255), PRIMARY KEY (pmkCountryCode));")
            c.execute(
                "CREATE TABLE tblSummerGames(fldSport VARCHAR(74), fldDiscipline VARCHAR(74), fldAthlete VARCHAR(74), fnkCountryCode VARCHAR(3), fldGender VARCHAR(6), fldEvent VARCHAR(74), FOREIGN KEY (fnkCountryCode) REFERENCES tblCountries(pmkCountryCode));")
        except sqlite3.OperationalError:
            # overwrite tables if they are already made
            c.execute("DROP TABLE tblCountries")
            c.execute("DROP TABLE tblSummerGames")
            c.execute(
                "CREATE TABLE tblCountries(fldCountry VARCHAR(74), pmkCountryCode VARCHAR(3), fldPopulation int(255), fldGDP int(255), PRIMARY KEY (pmkCountryCode));")
            c.execute(
                "CREATE TABLE tblSummerGames(fldSport VARCHAR(74), fldDiscipline VARCHAR(74), fldAthlete VARCHAR(74), fnkCountryCode VARCHAR(3), fldGender VARCHAR(6), fldEvent VARCHAR(74), FOREIGN KEY (fnkCountryCode) REFERENCES tblCountries(pmkCountryCode));")

        # populate data in tblCountries
        country_data = Database.__process_data("dictionary.csv")
        country = country_data[0]
        code = country_data[1]
        population = country_data[2]
        gdp = country_data[3]

        for i in range(len(code)):
            query_string = "INSERT INTO tblCountries(fldCountry, pmkCountryCode, fldPopulation, fldGDP) VALUES( ?, ?, ?, ?)"
            c.execute(query_string, (country[i], code[i], population[i], gdp[i]))

        # populate data in tblSummerGames
        summer_data = Database.__process_data("summer.csv")
        sport = summer_data[0]
        discipline = summer_data[1]
        athlete = summer_data[2]
        country_code = summer_data[3]
        gender = summer_data[4]
        event = summer_data[5]

        for j in range(len(summer_data)):
            query_string = "INSERT INTO tblSummerGames VALUES( ?, ?, ?, ?, ?, ?)"
            c.execute(query_string, (sport[j], discipline[j], athlete[j], country_code[j], gender[j], event[j]))

        # Save (commit) the changes
        conn.commit()

        # close connection
        conn.close()


    # Pass in a sample query to test the output
    def test_select_query(self, query):
        conn = sqlite3.connect("database.db");
        c = conn.cursor()

        c.execute(query)
        return c.fetchall()

        # close connection
        conn.close()


    # Takes csv file name string as argument, splits columns into separate lists. The zeroth value of each list is the name of the column.
    # Returns a 2d list of these lists. Zeroth value is first col, and so on
    def __process_data(filename):
        f = open(filename, 'r')
        data = f.read()
        f.close()
        data = data.split("\n")

        x = len(data)
        y = len(data[0].split(","))

        tmp = []
        # separate into array, needs rotating
        for row in data:
            entry = row.split(",")
            tmp.append(entry)

        out = []
        titles = []
        # fill titles
        for title in tmp[0]:
            titles.append(title)

        # fill data
        for i in range(len(tmp[1])):
            col = []
            for j in range(1, len(tmp)):
                if filename == "summer.csv" and i == 3:
                    break
                if filename == "summer.csv" and i == 2:
                    col.append(tmp[j][i] + "," + tmp[j][i + 1])
                else:
                    col.append(tmp[j][i])
            if col != []:
                out.append(col)

        for i in range(len(out)):
            out[i].insert(0, titles[i])

        return out
import sqlite3


class Database:

    # Initializer / Instance Attributes
    def __init__(self):
        self.conn = sqlite3.connect("database.db");
        self.c = self.conn.cursor()

    # ~~~~~~~~~~~~~~~~~~~~START QUERIES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # This executes the query for 'COUNTRY DISCIPLINE athlete'
    # @param country - the given country
    # @param discipline - the given discipline
    # @return a list of athletes
    def athlete_query(self, country, discipline):
        self.c.execute("SELECT fldAthlete FROM tblSummerGames WHERE fnkCountryCode = ? AND fldDiscipline = ?;", (country, discipline,))
        return self.c.fetchall()

    # This executes the query for 'ATHLETE event'
    # @param athlete - the given athlete must be in format '"LAST, First"'
    # @return a list of events
    def event_query(self, athlete):
        athlete = '"' + athlete + '"'
        self.c.execute("SELECT fldEvent FROM tblSummerGames WHERE fldAthlete = ?;", (athlete,))
        return self.c.fetchall()

    # This executes the query for 'COUNTRY gdp'
    # @param country - the given country
    # @return a list of GDPs
    def gdp_query(self, country):
        self.c.execute("SELECT fldGDP FROM tblCountries WHERE fldCountry = ?;", (country,))
        return self.c.fetchall()

    # This executes the query for 'LIST discipline'
    # @return a list all disciplines
    def list_query(self):
        self.c.execute("SELECT DISTINCT fldDiscipline FROM tblSummerGames;")
        return self.c.fetchall()

    # This executes the query for 'COUNTRY population'
    # @param population - the given population
    # @return a list of populations
    def population_query(self, country):
        self.c.execute("SELECT fldPopulation FROM tblCountries WHERE fldCountry = ?;", (country,))
        return self.c.fetchall()

    # This executes the query for 'ABOUT athlete'
    # @param athlete - the given athlete
    # @return a list of events and countries in the format [(event, country),]
    def about_query(self, athlete):
        athlete = '"' + athlete + '"'
        self.c.execute("SELECT fnkCountryCode FROM tblSummerGames WHERE fldAthlete = ?", (athlete,))
        country_code_list = self.c.fetchall()
        country_code = country_code_list[0][0]
        self.c.execute("SELECT tblSummerGames.fldEvent, tblCountries.fldCountry FROM tblSummerGames INNER JOIN tblCountries ON tblCountries.pmkCountryCode = ? WHERE tblSummerGames.fldAthlete = ?", (country_code, athlete,))
        return self.c.fetchall()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~END QUERIES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # This method makes our database, table, and populates the data
    def load_data(self):
        # Create tables
        try:
            self.c.execute(
                "CREATE TABLE tblCountries(fldCountry VARCHAR(74), pmkCountryCode VARCHAR(3), fldPopulation int(255), fldGDP int(255), PRIMARY KEY (pmkCountryCode));")
            self.c.execute(
                "CREATE TABLE tblSummerGames(fldSport VARCHAR(74), fldDiscipline VARCHAR(74), fldAthlete VARCHAR(74), fnkCountryCode VARCHAR(3), fldGender VARCHAR(6), fldEvent VARCHAR(74), FOREIGN KEY (fnkCountryCode) REFERENCES tblCountries(pmkCountryCode));")
        except sqlite3.OperationalError:
            # overwrite tables if they are already made
            self.c.execute("DROP TABLE tblCountries")
            self.c.execute("DROP TABLE tblSummerGames")
            self.c.execute(
                "CREATE TABLE tblCountries(fldCountry VARCHAR(74), pmkCountryCode VARCHAR(3), fldPopulation int(255), fldGDP int(255), PRIMARY KEY (pmkCountryCode));")
            self.c.execute(
                "CREATE TABLE tblSummerGames(fldSport VARCHAR(74), fldDiscipline VARCHAR(74), fldAthlete VARCHAR(74), fnkCountryCode VARCHAR(3), fldGender VARCHAR(6), fldEvent VARCHAR(74), FOREIGN KEY (fnkCountryCode) REFERENCES tblCountries(pmkCountryCode));")

        # populate data in tblCountries
        country_data = Database.__process_data("dictionary.csv")
        country = country_data[0]
        code = country_data[1]
        population = country_data[2]
        gdp = country_data[3]

        for i in range(len(code)):
            query_string = "INSERT INTO tblCountries(fldCountry, pmkCountryCode, fldPopulation, fldGDP) VALUES( ?, ?, ?, ?)"
            self.c.execute(query_string, (country[i], code[i], population[i], gdp[i]))

        # populate data in tblSummerGames
        summer_data = Database.__process_data("summer.csv")
        sport = summer_data[0]
        discipline = summer_data[1]
        athlete = summer_data[2]
        country_code = summer_data[3]
        gender = summer_data[4]
        event = summer_data[5]

        for j in range(len(summer_data[0])):
            query_string = "INSERT INTO tblSummerGames VALUES( ?, ?, ?, ?, ?, ?)"
            self.c.execute(query_string, (sport[j], discipline[j], athlete[j], country_code[j], gender[j], event[j]))

        # Save (commit) the changes
        self.conn.commit()

    # Pass in a sample query to test the output
    def test_select_query(self, query):
        self.c.execute(query)
        return self.c.fetchall()

    # Takes csv file name string as argument, splits columns into separate lists. The zeroth value of each list is
    # the name of the column.
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

    # This method will take a parsed list and will call the associated SQL query.
    # Checks that number of strings in list matches
    # the number of strings the corresponding command. 
    # Accepts: parsed list
    # Returns: return value fro appropriate sql call
    def parsed_to_sql(self, input):
         return_val = []
         if len(input) == 2 :
            if input[1].lower() == "population":
                return_val = self.population_query(input[0])
    
            elif input[1].lower() == "gdp":
                return_val = self.gdp_query(input[0])
                 
            elif input[0]=="list":
                return_val = self.list_query()
    
            elif input[1] == "event":
                 return_val = self.event_query(input[0])
    
            elif input[0] == "about":
                 return_val = self.about_query(input[1])
    
         elif len(input) == 3 :
             if input[2] == "athlete":
                 return_val = self.athlete_query(input[0],input[1])
    
         else :
             print("Error.")
             #self.print_input_error()
         return return_val




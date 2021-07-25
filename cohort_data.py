"""Functions to parse a file containing student data."""


def all_houses(filename):
  """Return a set of all house names in the given file.

  For example:
  >>> unique_houses('cohort_data.txt')
  ""Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

  Arguments:
  - filename (str): the path to a data file

  Return:
  - set[str]: a set of strings
  """
  houses = set()

  open_file = open(filename)
  for line in open_file:
    token = line.split("|")
    if len(token[2]) > 0:
      houses.add(token[2])

  return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """
    students = []
    open_file = open(filename)
    for line in open_file:
      token = line.split("|")
      cohort_name = token[4].strip()
      first_name = token[0].strip()
      last_name = token[1].strip()

      if cohort_name != "I" and cohort_name != "G":
        # students.append(first_name + " " + last_name)
        if cohort_name == cohort:
          students.append(first_name + " " + last_name)
        elif cohort == "All":
          students.append(first_name + " " + last_name)       
        
    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []



    # TODO: replace this with your code
    open_file = open(filename)
    for line in open_file:
      token = line.split("|")
      cohort_name = token[4].strip()
      house_name = token[2].strip()
      first_name = token[0].strip()
      last_name = token[1].strip()
    
      if house_name == "Dumbledore's Army":
        dumbledores_army.append(first_name + " " + last_name)
      elif house_name == "Gryffindor":
        gryffindor.append(first_name + " " + last_name)
      elif house_name == "Hufflepuff":
        hufflepuff.append(first_name + " " + last_name)
      elif house_name == "Ravenclaw":
        ravenclaw.append(first_name + " " + last_name)
      elif house_name == "Slytherin":
        slytherin.append(first_name + " " + last_name)
      elif cohort_name == "G":
        ghosts.append(first_name + " " + last_name)
      elif cohort_name == "I":
        instructors.append(first_name + " " + last_name)    
    
    dumbledores_army.sort()
    gryffindor.sort()
    hufflepuff.sort()
    ravenclaw.sort()
    slytherin.sort()
    ghosts.sort()
    instructors.sort()

    all_houses = [dumbledores_army, gryffindor, hufflepuff, ravenclaw, slytherin, ghosts, instructors]

    return all_houses


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    # TODO: replace this with your code

    open_file = open(filename)
    for line in open_file:
      token = line.split("|")
      first_name = token[0].strip()
      last_name = token[1].strip()
      house_name = token[2].strip()
      advisor = token[3].strip()
      cohort_name = token[4].strip()
      student_information = (first_name + " " + last_name, house_name, advisor, cohort_name)
      all_data.append(student_information)

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """
    open_file = open(filename)
    for line in open_file:
      token = line.split("|")
      first_name = token[0].strip()
      last_name = token[1].strip()
      full_name = first_name + " " + last_name
      cohort_name = token[4].strip()
    
      if full_name == name:
        return cohort_name
    


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    last_name_list = []
    duplicate_list = []

    open_file = open(filename)
    for line in open_file:
      token = line.split("|")
      last_name = token[1].strip()
      if last_name in last_name_list:
        duplicate_list.append(last_name)
      else:
        last_name_list.append(last_name)

    return set(duplicate_list)

    


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """
    cohort_search = ""
    house_search = ""
    housemates = set()

    i = 0

    open_file = open(filename)
    for line in open_file:
      token = line.split("|")
      first_name = token[0].strip()
      last_name = token[1].strip()
      full_name = first_name + " " + last_name
      house_name = token[2].strip()
      cohort_name = token[4].strip()

      if name == full_name:
        cohort_search = cohort_name
        house_search = house_name
  # I think it needs to loop back to the top of the file, so it can search for any names that come before the name you're looking for
      if (house_name == house_search) and (cohort_name == cohort_search):
        housemates.add(full_name)
          i += 1

    return housemates

##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')

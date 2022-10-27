class Place:
    def __init__(self, name, i):
        """This method takes three parameters, self, name (a string), and i
        (an integer) and initializes the necessary variables for the class."""
        
        self.name = name
        self.index = i
        self.dist = None
        self.paths = None

    def get_index(self):
        """This method takes self as a parameter and simply returns the index 
        of the Place object."""
        
        return self.index

    def get_name(self):
        """This method takes self as a parameter and simply returns the name 
        of the Place object."""
        
        return self.name

    def set_distances(self, g):
        """This method takes self and g, a list of lists of distances between
        this Place object and other Place objects, and sets the distances of
        this Place based on g."""
        
        self.dist = g[self.index][:]
        
        return None

    def set_paths(self, paths):
        """This method takes self and paths, a list of lists of paths between
        this Place object and other Place objects, and sets the paths of
        this Place based on the paths parameter."""
        
        self.paths = paths[self.index][:]
        
        return None

    def get_distance(self, j):
        """This method takes the parameters self and j, an integer indicating
        another Place object, and returns the distance between this Place 
        object and j."""
        
        return self.dist[j]

    def get_path(self, j):
        """This method takes the parameters self and j, an integer indicating
        another Place object, and returns the shortest path between this Place 
        object and j."""
        
        return self.paths[j]

    def __str__(self):
        """This method takes self as a parameter and returns a formatted string
        of information about this Place object."""
        
        # Create a tuple of information
        tup = (self.index, self.name, self.dist, self.paths)
        
        # Unpack the tuple to be formatted nicely
        return "Node {}, {}: distances {}, paths {}".format(*tup)

    def __repr__(self):
        """This method takes self as a parameter and an unformatted string of 
        information about this Place object."""
        
        # Create a tuple of information
        tup = (self.index, self.name, self.dist, self.paths)
        
        # Simply return the unformatted information tuple as a string
        return str(tup)

#Author: Or Basker 
#ID: 316388743
import json
import csv
import os

class DataSummary:
    '''
    DataSummary class
    should be initialized with a json file and a csv file
    '''
    def __init__(self, datafile, metafile):
        '''
        Constructor for DataSummary class
        :param datafile: path to json file
        :param metafile: path to csv file
        '''
        if not os.path.exists(datafile):
            raise ValueError("datafile not found")
        elif not os.path.exists(metafile):
            raise ValueError("metafile not found")
        self.datafile = datafile
        self.metafile = metafile
        self._get_meta_data_from_csv()
        self._get_data_from_json()
        self._fix_records()
        
    def __getitem__(self, key):
        '''
        Overload the [] operator
        :param key: index or key
        :return: the value of the key
        for int: return the fieldnames of the metafile
        for str: return the value of the key
        '''
        if isinstance(key, int):
            return self.data[key]
        elif isinstance(key, str):
            meta_data = self.meta_data
            if key not in meta_data.fieldnames:
                raise ValueError("key not found")
            for row in meta_data:
                return row[key]
            

        
    def _sum(self, feature):
        '''
        Helper function for sum
        :param feature: the feature to be summed
        '''
        if feature not in self.meta_data.fieldnames:
            raise ValueError("feature not found in metafile")
        sum = 0
        for row in self.data:
            if feature in row.keys():
                if row[feature] != None:
                    sum += float(row[feature])
        return sum
        
    
    def _count(self, feature):
        '''
        Helper function for count
        :param feature: the feature to be counted
        :return: the number of empty values in the feature
        '''
        if feature not in self.meta_data.fieldnames:
            raise ValueError("feature not found in metafile")
        count = 0
        for row in self.data:
            if feature in row.keys():
                if row[feature] != None:
                    count += 1
        return count
    
    def _fix_records(self):
        '''
        Helper function for fix_records
        :return: None
        '''
        fieldnames = self.meta_data.fieldnames
        for row in self.data:
            row_keys = row.keys()
            for field in fieldnames:
                if field not in row_keys:
                    row[field] = None
                    
            
    def _get_meta_data_from_csv(self):
        '''
        Helper function for get_meta_data_from_csv
        :return: the meta data from the csv file
        '''
        self.meta_data = csv.DictReader(open(self.metafile, 'r'))
            
        
    
    def _get_data_from_json(self):
        '''
        Helper function for get_data_from_json
        :return: the data from the json file
        '''
        with open(self.datafile, 'r') as f:
            data = json.load(f)
        self.data = data['data']
        
    def mean(self, feature):
        '''
        :param feature: the feature to be counted for mean (average)
        :return: the average of the feature in the data'''
        return self._sum(feature) / self._count(feature)
    
    
    def mode(self, feature):
        '''
        :param feature: the feature to be counted
        :return: the number of empty values in the feature
        '''
        meta_data = self.meta_data
        if feature not in meta_data.fieldnames:
            raise ValueError("feature not found in metafile")
        mode_dict = {}
        for row in self.data:
            if feature in row.keys():
                if row[feature] != None:
                    if row[feature] not in mode_dict.keys():
                        mode_dict[row[feature]] = 1
                    else:
                        mode_dict[row[feature]] += 1
        mode_list = []
        max_val = max(mode_dict.values())
        for key, val in mode_dict.items():
            if val == max_val:
                mode_list.append(key)
        return mode_list
    
    
    
    def unique(self, feature):
        '''
        :param feature: the feature to be counted
        :return: the number of empty values in the feature
        '''
        meta_data = self.meta_data
        if feature not in meta_data.fieldnames:
            raise ValueError("feature not found in metafile")
        unique_list = []
        for row in self.data:
            if feature in row.keys():
                if row[feature] != None:
                    if row[feature] not in unique_list:
                        unique_list.append(row[feature])
        return sorted(unique_list)
    
    
    def to_csv(self, filename, delimiter=','):
        '''
        :param filename: the name of the csv file to be written
        :param delimiter: the delimiter to be used
        :return: None
        Legal delimiters are: ',', '.', ':', '|', '-', ';', '#', '*'
        '''
        if delimiter not in [',', '.', ':', '|', '-', ';', '#', '*']:
            raise ValueError("unsupported delimiter")
        new_file = open(filename, 'w')
        for row in self.data:
            for key, val in row.items():
                if val == None:
                    row[key] = ''
            new_file.write(delimiter.join(row.values()) + '\n')
        new_file.close()
        
    def min(self, feature):
        '''
        :param feature: the feature to be counted
        :return: the number of empty values in the feature
        '''
        if feature not in self.meta_data.fieldnames:
            raise ValueError("feature not found in metafile")
        min_val = float('inf')
        for row in self.data:
            if feature in row.keys():
                if row[feature] != None:
                    if float(row[feature]) < min_val:
                        min_val = float(row[feature])
        return min_val
    
    
    def max(self, feature):
        '''
        :param feature: the feature to be counted
        :return: the number of empty values in the feature
        '''
        if feature not in self.meta_data.fieldnames:
            raise ValueError("feature not found in metafile")
        max_val = float('-inf')
        for row in self.data:
            if feature in row.keys():
                if row[feature] != None:
                    if float(row[feature]) > max_val:
                        max_val = float(row[feature])
        return max_val
        
        
    def empty(self, feature):
        '''
        :param feature: the feature to be counted
        :return: the number of empty values in the feature
        '''
        if feature not in self.meta_data.fieldnames:
            raise ValueError("feature not found in metafile")
        
        count = 0
        for row in self.data:
            if feature not in row.keys():
                count += 1 
        return count
        
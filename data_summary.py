import json
import csv
import os

class DataSummary:
    def __init__(self, datafile, metafile):
        if not os.path.exists(datafile):
            raise ValueError("datafile not found")
        elif not os.path.exists(metafile):
            raise ValueError("metafile not found")
        self.datafile = datafile
        self.metafile = metafile
        self._get_meta_data_from_csv()
        self._get_data_from_json()
        
    def __getitem__(self, key):
        if isinstance(key, int):
            return self.data['data'][key]
        elif isinstance(key, str):
            meta_data = self.meta_data
            if key not in meta_data.fieldnames:
                raise ValueError("key not found")
            for row in meta_data:
                return row[key]
            

        
    def sun(self, feature):
        data = self.data['data']
        meta_data = self.meta_data
        if feature not in meta_data.fieldnames:
            raise ValueError("feature not found in metafile")
        total = 0
        for row in data:
            if feature in row.keys():
                if row[feature] != None:
                    total += float(row[feature])
        return total
    
    def count(self, feature):
        data = self.data['data']
        meta_data = self.meta_data
        if feature not in meta_data.fieldnames:
            raise ValueError("feature not found in metafile")
        count = 0
        for row in data:
            if feature in row.keys():
                if row[feature] != None:
                    count += 1
        return count
    
    def _get_meta_data_from_csv(self):
        self.meta_data = csv.DictReader(open(self.metafile, 'r'))
            
        
    
    def _get_data_from_json(self):
        with open(self.datafile, 'r') as f:
            data = json.load(f)
        self.data = data
        
    def mean(self, feature):
        data = self.data['data']
        meta_data = self.meta_data
        if feature not in meta_data.fieldnames:
            raise ValueError("feature not found in metafile")
        total = 0
        count = 0
        for row in data:
            if feature in row.keys():
                if row[feature] != None:
                    total += float(row[feature])
                    count += 1
        return total/count
    
    
    def mode(self, feature):
        data = self.data['data']
        meta_data = self.meta_data
        if feature not in meta_data.fieldnames:
            raise ValueError("feature not found in metafile")
        mode_dict = {}
        for row in data:
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
        data = self.data['data']
        meta_data = self.meta_data
        if feature not in meta_data.fieldnames:
            raise ValueError("feature not found in metafile")
        unique_list = []
        for row in data:
            if feature in row.keys():
                if row[feature] != None:
                    if row[feature] not in unique_list:
                        unique_list.append(row[feature])
        return sorted(unique_list)
    
    
    def to_csv(self, filename, delimiter=','):
        data = self.data['data']
        meta_data = self.meta_data
        if delimiter not in [',', '.', ':', '|', '-', ';', '#', '*']:
            raise ValueError("unsupported delimiter")
        new_file = open(filename, 'w')
        for row in data:
            for key, val in row.items():
                if val == None:
                    row[key] = ''
            new_file.write(delimiter.join(row.values()) + '\n')
        new_file.close()
        
    def min(self, feature):
        data = self.data['data']
        meta_data = self.meta_data
        if feature not in meta_data.fieldnames:
            raise ValueError("feature not found in metafile")
        min_val = float('inf')
        for row in data:
            if feature in row.keys():
                if row[feature] != None:
                    if float(row[feature]) < min_val:
                        min_val = float(row[feature])
        return min_val
    
    
    def max(self, feature):
        data = self.data['data']
        meta_data = self.meta_data
        if feature not in meta_data.fieldnames:
            raise ValueError("feature not found in metafile")
        max_val = float('-inf')
        for row in data:
            if feature in row.keys():
                if row[feature] != None:
                    if float(row[feature]) > max_val:
                        max_val = float(row[feature])
        return max_val
        
        

        
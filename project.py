import requests
import re
import pandas as pd

from selenium import webdriver
from bs4 import BeautifulSoup


class WebScraping:
    
    page = requests.get('https://docs.python.org/3/library/random.html')
    soup = BeautifulSoup(page.text, 'html.parser')    
    result_tag = []
    selected_tag = []
    selected_attr = []
    attr_value = ''
    
    
    tags = []
    attributes = []
    errors = []
    
    data_set_column = 1
    data_set = {}
    
    
    def __init__(self) -> None:
        self.tags()

    def tags(self):    
        
        element_tags = {tag.name for tag in self.soup.findAll()}

        if not element_tags:
            return None        
              
        self.tags = element_tags
        return self
    
    
    def tag(self, tag):
        print('tag name =>', tag)
        
        if tag not in self.tags:   
            self.selected_tag = [] 
        else:                   
            self.selected_tag = tag                            
            print('returned value =>', self.selected_tag)  
      
        #self.get_attributes()
        
        return self
    
    def find(self):
        self.result_tag = []   
        
        elements = self.soup.findAll(self.selected_tag)                           
        
        self.result_tag = elements  
        print('----->', self.selected_tag)  #test
        print(self.tags) #test
        return self        
      
    def count_element(self):
        return len(self.result_tag)
    
    def print_result(self):
        return self.result_tag
    
    def regex_search(self, pattern):
        self.result_tag = re.findall(pattern, str(self.result_tag))
        return self.result_tag
    
    def regex_result_slice(self, start=0, end=None):
        self.result_tag = [str(item)[start:end] for item in self.result_tag]
        return self.result_tag
    
    def dataset_save(self):
        self.data_set.update({f'Column{self.data_set_column}': self.result_tag})
        self.data_set_column =+ 1
        return self
        
    def dataset_clear(self):
        self.data_set.clear()
        
    def to_csv(self):
        data = pd.DataFrame(self.data_set)
        data.head() #return some data 
        data.to_csv('data.csv') #creates a csv file
    
    @classmethod
    def print(cls):
        return cls.tags
        

tag = 'dt'
ws = WebScraping()
print(ws.tag(tag).find().count_element())
print(ws.result_tag)
print('===================')
print(ws.regex_search('id="random.\w+'))
print('===================')
print(ws.regex_result_slice(4))
print(ws.dataset_save().to_csv())
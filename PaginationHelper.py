# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 21:50:01 2026

@author: Benyamin
"""
# TODO: complete this class
class PaginationHelper:
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        return (len(self.collection) + self.items_per_page - 1) // self.items_per_page
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= self.page_count():
            return -1
        
        start = page_index * self.items_per_page
        end = start + self.items_per_page
        return len(self.collection[start:end])
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0 or item_index >= self.item_count():
            return -1
        
        return item_index // self.items_per_page
#///////////////////////////////////////////////////////////////////////////////////////
helper = PaginationHelper(['a','b','c','d','e','f'], 4)
print("The page count is:", helper.page_count())  # should == 2
print("The item count is:", helper.item_count())  # should == 6
print("The page item count is:", helper.page_item_count(0))  # should == 4
print("The page item count is:", helper.page_item_count(1))  # last page - should == 2
print("The page item count is:", helper.page_item_count(2))  # should == -1 since the page is invalid

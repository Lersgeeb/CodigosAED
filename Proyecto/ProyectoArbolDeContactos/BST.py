# -*- coding: utf-8 -*-
from Node import *
from LinkedList import *

class BST:

    def __init__(self):
        self.root = None

    def add(self, contact, current = None):    
        if(not self.root):
            self.root = Node(contact)
            return True
        else:
            if(current == None):
                current = self.root     
            if(contact.number > current.value.number):
                if(current.right):
                    self.add(contact,current.right)
                else:
                    current.right = Node(contact)
                    return True
            elif(contact.number < current.value.number):
                if(current.left):
                    self.add(contact,current.left)
                else:
                    current.left = Node(contact)
                    return True
            else:
                return False               

    def search(self, value, current = None):
        if(self.root):
            if(current == None):
                current = self.root
            
            if(value == current.value.number):
                return True
            elif(value > current.value.number):
                if(current.right):
                    return self.search(value, current.right)
                else:
                    return False
            
            else:
                if(current.left):
                    return self.search(value, current.left)
                else:
                    return False
        else:
            return False
    
    def addInner(self,node):
        linkedList = self.treeNodeToLinkedList(node)
        current = linkedList.first
        while current:
            self.add(current.value)
            current = current.next
        return True

    def searchContact(self, value, current = None):
        if(self.root):
            if(current == None):
                current = self.root
            
            if(value == current.value.number):
                print("\nNombre: %s\nNumero: %s\n" % (current.value.name,current.value.number))
                return True
            elif(value > current.value.number):
                if(current.right):
                    return self.searchContact(value, current.right)
                else:
                    print("\nNo se encontro el valor\n")
                    return False
            
            else:
                if(current.left):
                    return self.searchContact(value, current.left)
                else:
                    print("\nNo se encontro el valor\n")
                    return False
        else:
            print("\nNo se encontro el valor\n")
            return False
    

    
    def treeNodeToLinkedList(self,tree,linkedList=None):
        if tree == None:
            return linkedList
        if linkedList == None:
            linkedList = LinkedList()
            if tree.left:
                self.treeNodeToLinkedList(tree.left,linkedList)
            if tree.right:
                self.treeNodeToLinkedList(tree.right,linkedList)
        else:
            linkedList.add(tree.value)
            if tree.left:
                self.treeNodeToLinkedList(tree.left,linkedList)
            if tree.right:
                self.treeNodeToLinkedList(tree.right,linkedList)
        return linkedList

    def remove(self,number,current = None, prev=None):
        if self.search(number):
            if current == None:
                current = self.root
                if current.value.number == number:
                    node = current
                    self.root = None
                    return self.addInner(node)
                elif number < current.value.number:
                    return self.remove(number,current.left,current)
                else:
                    return self.remove(number,current.right,current)
            else:
                if number == current.value.number:
                    if prev.value.number > current.value.number:
                        node = prev.left
                        prev.left = None
                        return self.addInner(node)
                    else:
                        node = prev.right
                        prev.right = None
                        return self.addInner(node)
                elif number < current.value.number:
                    return self.remove(number,current.left,current)
                else:
                    return self.remove(number,current.right,current)
        else:
            return False
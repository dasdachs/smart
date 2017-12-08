#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""The basic models for a mvp contact book."""
from datetime import date
from email.utils import parseaddr
import re


class Contact(object):
    """Contact represents a person with a name, last name, phone number,
    birth year and email address."""
    def __init__(self, first_name, last_name, phone_number, birth_year, email):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        if phone_number:
            self.phone_number = self._validate_phone_number(phone_number)
        else:
            self.phone_number = ""
        if birth_year:
            self.birth_year = self._validate_birth_year(birth_year)
        else:
            self.birth_year = 1900
        if email:
            self.email = self._validate_email(email)
        else:
            self.email = ""

    def _validate_phone_number(self, phone):
        """Checks if a given number is a valid slovenian phone number."""
        # Sanitize the input so we can run the regex on a string of numbers
        sanitize_regex = re.compile(r"[\\/\- ]+")
        sanitized_phone = re.sub(sanitize_regex, "", phone)
        # The phone regex does not cover all the possible cases
        # In producion, this would have to be done better
        phone_regex = re.compile(r"""
                                 (((\+|00)386)|0)      # International
                                 (([1-9][01][0-9]{6})  # Mobile
                                 |
                                 ([1-9][0-9]{7}))      # Fixed line
                                 """, re.X)
        match = re.search(phone_regex, sanitized_phone)
        if not match:
            print "Please enter a valid number."
            print ""
            print "Note: not all fixed and/or mobile numbers are currently supported."
            print "Contact our help desk for more information."
            raise ValueError
        return match.group()

    def _validate_birth_year(self, birth_year):
            """Simple birth year validation."""
            try:
                today = date.today().year
                birth_year = int(birth_year)
                min_year = today - 120  # The max life span
                max_year = today
                if not min_year <= birth_year  <= max_year:
                    print "Not a valid year."
                else:
                    return birth_year
            except ValueError:
                print "The birth year must be an integer."

    def _validate_email(self, email):
        """Parses the give string looking for a valid address.
        :param email: string
        :return: the parsed valid email
        """
        parsed = parseaddr(email)[1]
        if not parsed:
            print "Please use a valid email address."
            raise ValueError
        return parsed

    def __eq__(self, other):
        """Compares two contacts."""
        return self.__dict__ == other.__dict__

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_data(self):
        """Returns a list from the attributes.
        :return: a list with all the values
        """
        return [self.first_name, self.last_name, self.birth_year,
                self.phone_number, self.email]

    def __str__(self):
        """The string representation of the object."""
        return self.get_full_name()

    def __repr__(self):
        return self.get_full_name()


class ContactBook(object):
    """A collection of contacts."""
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        """Adds a new contact.

        Performs a very crude check if the contact exists.

        :param contact: a Contact object.
        :return: None
        """
        duplicate = filter(lambda x: x == contact, self.contacts)
        if duplicate:
            print "Contact allready exists."
            print duplicate[0]
        else:
            self.contacts.append(contact)
            print "%s added to contacts." % str(contact)

    def edit_contact(self, contact_index, data):
        """Edits a contact.
        :param contact_index: the index number of the contact, int
        :param data: a dict with data to update
        :return: None
        """
        # Make sure the index is not out of range
        try:
            contact = self.contacts[contact_index]
        except IndexError:
            print "Contact not found."
        # Update attributes using the keys from the data dictionary
        for key, value in data:
            setattr(contact, key, value)

    def delete_contact(self, contact_index):
        """Removes a contact from the list.
        :param contact_index: the index number of the contact, int
        """
        try:
            contact = self.contacts.pop(contact_index)
            print "%s succesfully removed!"
        except ValueError:
            print "Contact not found."

    def get_data(self):
        """Returns a list with all the data as tuples.
        :return: a list of tuples (index + attrs)
        """
        return [c.get_data() for c in self.contacts]

    def __str__(self):
        """Prints the contacts."""
        return ",".join([c.get_full_name() for c in self.contacts])

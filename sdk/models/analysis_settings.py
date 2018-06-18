# coding: utf-8

"""
    ProWritingAid API V2

    Official ProWritingAid API Version 2

    OpenAPI spec version: v2
    Contact: hello@prowritingaid.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AnalysisSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'shortest_average_sentence_length': 'int',
        'longest_average_sentence_length': 'int',
        'longest_individual_sentence': 'int',
        'highest_passive_index': 'int',
        'max_glue_index': 'int',
        'min_sentence_variety': 'int',
        'highest_pronoun_percentage': 'float',
        'lowest_pronoun_percentage': 'float',
        'highest_academic_pronoun_percentage': 'float',
        'highest_initial_pronoun_percentage': 'float',
        'lowest_initial_pronoun_percentage': 'float',
        'lowest_we_we_score': 'float',
        'longest_average_paragraph_length': 'float'
    }

    attribute_map = {
        'shortest_average_sentence_length': 'ShortestAverageSentenceLength',
        'longest_average_sentence_length': 'LongestAverageSentenceLength',
        'longest_individual_sentence': 'LongestIndividualSentence',
        'highest_passive_index': 'HighestPassiveIndex',
        'max_glue_index': 'MaxGlueIndex',
        'min_sentence_variety': 'MinSentenceVariety',
        'highest_pronoun_percentage': 'HighestPronounPercentage',
        'lowest_pronoun_percentage': 'LowestPronounPercentage',
        'highest_academic_pronoun_percentage': 'HighestAcademicPronounPercentage',
        'highest_initial_pronoun_percentage': 'HighestInitialPronounPercentage',
        'lowest_initial_pronoun_percentage': 'LowestInitialPronounPercentage',
        'lowest_we_we_score': 'LowestWeWeScore',
        'longest_average_paragraph_length': 'LongestAverageParagraphLength'
    }

    def __init__(self, shortest_average_sentence_length=11, longest_average_sentence_length=18, longest_individual_sentence=30, highest_passive_index=25, max_glue_index=40, min_sentence_variety=3, highest_pronoun_percentage=15.0, lowest_pronoun_percentage=4.0, highest_academic_pronoun_percentage=2.0, highest_initial_pronoun_percentage=30.0, lowest_initial_pronoun_percentage=0.0, lowest_we_we_score=0.6, longest_average_paragraph_length=6.0):
        """
        AnalysisSettings - a model defined in Swagger
        """

        self._shortest_average_sentence_length = None
        self._longest_average_sentence_length = None
        self._longest_individual_sentence = None
        self._highest_passive_index = None
        self._max_glue_index = None
        self._min_sentence_variety = None
        self._highest_pronoun_percentage = None
        self._lowest_pronoun_percentage = None
        self._highest_academic_pronoun_percentage = None
        self._highest_initial_pronoun_percentage = None
        self._lowest_initial_pronoun_percentage = None
        self._lowest_we_we_score = None
        self._longest_average_paragraph_length = None

        self.shortest_average_sentence_length = shortest_average_sentence_length
        self.longest_average_sentence_length = longest_average_sentence_length
        self.longest_individual_sentence = longest_individual_sentence
        self.highest_passive_index = highest_passive_index
        self.max_glue_index = max_glue_index
        self.min_sentence_variety = min_sentence_variety
        self.highest_pronoun_percentage = highest_pronoun_percentage
        self.lowest_pronoun_percentage = lowest_pronoun_percentage
        self.highest_academic_pronoun_percentage = highest_academic_pronoun_percentage
        self.highest_initial_pronoun_percentage = highest_initial_pronoun_percentage
        self.lowest_initial_pronoun_percentage = lowest_initial_pronoun_percentage
        self.lowest_we_we_score = lowest_we_we_score
        self.longest_average_paragraph_length = longest_average_paragraph_length

    @property
    def shortest_average_sentence_length(self):
        """
        Gets the shortest_average_sentence_length of this AnalysisSettings.

        :return: The shortest_average_sentence_length of this AnalysisSettings.
        :rtype: int
        """
        return self._shortest_average_sentence_length

    @shortest_average_sentence_length.setter
    def shortest_average_sentence_length(self, shortest_average_sentence_length):
        """
        Sets the shortest_average_sentence_length of this AnalysisSettings.

        :param shortest_average_sentence_length: The shortest_average_sentence_length of this AnalysisSettings.
        :type: int
        """
        if shortest_average_sentence_length is None:
            raise ValueError("Invalid value for `shortest_average_sentence_length`, must not be `None`")

        self._shortest_average_sentence_length = shortest_average_sentence_length

    @property
    def longest_average_sentence_length(self):
        """
        Gets the longest_average_sentence_length of this AnalysisSettings.

        :return: The longest_average_sentence_length of this AnalysisSettings.
        :rtype: int
        """
        return self._longest_average_sentence_length

    @longest_average_sentence_length.setter
    def longest_average_sentence_length(self, longest_average_sentence_length):
        """
        Sets the longest_average_sentence_length of this AnalysisSettings.

        :param longest_average_sentence_length: The longest_average_sentence_length of this AnalysisSettings.
        :type: int
        """
        if longest_average_sentence_length is None:
            raise ValueError("Invalid value for `longest_average_sentence_length`, must not be `None`")

        self._longest_average_sentence_length = longest_average_sentence_length

    @property
    def longest_individual_sentence(self):
        """
        Gets the longest_individual_sentence of this AnalysisSettings.

        :return: The longest_individual_sentence of this AnalysisSettings.
        :rtype: int
        """
        return self._longest_individual_sentence

    @longest_individual_sentence.setter
    def longest_individual_sentence(self, longest_individual_sentence):
        """
        Sets the longest_individual_sentence of this AnalysisSettings.

        :param longest_individual_sentence: The longest_individual_sentence of this AnalysisSettings.
        :type: int
        """
        if longest_individual_sentence is None:
            raise ValueError("Invalid value for `longest_individual_sentence`, must not be `None`")

        self._longest_individual_sentence = longest_individual_sentence

    @property
    def highest_passive_index(self):
        """
        Gets the highest_passive_index of this AnalysisSettings.

        :return: The highest_passive_index of this AnalysisSettings.
        :rtype: int
        """
        return self._highest_passive_index

    @highest_passive_index.setter
    def highest_passive_index(self, highest_passive_index):
        """
        Sets the highest_passive_index of this AnalysisSettings.

        :param highest_passive_index: The highest_passive_index of this AnalysisSettings.
        :type: int
        """
        if highest_passive_index is None:
            raise ValueError("Invalid value for `highest_passive_index`, must not be `None`")

        self._highest_passive_index = highest_passive_index

    @property
    def max_glue_index(self):
        """
        Gets the max_glue_index of this AnalysisSettings.

        :return: The max_glue_index of this AnalysisSettings.
        :rtype: int
        """
        return self._max_glue_index

    @max_glue_index.setter
    def max_glue_index(self, max_glue_index):
        """
        Sets the max_glue_index of this AnalysisSettings.

        :param max_glue_index: The max_glue_index of this AnalysisSettings.
        :type: int
        """
        if max_glue_index is None:
            raise ValueError("Invalid value for `max_glue_index`, must not be `None`")

        self._max_glue_index = max_glue_index

    @property
    def min_sentence_variety(self):
        """
        Gets the min_sentence_variety of this AnalysisSettings.

        :return: The min_sentence_variety of this AnalysisSettings.
        :rtype: int
        """
        return self._min_sentence_variety

    @min_sentence_variety.setter
    def min_sentence_variety(self, min_sentence_variety):
        """
        Sets the min_sentence_variety of this AnalysisSettings.

        :param min_sentence_variety: The min_sentence_variety of this AnalysisSettings.
        :type: int
        """
        if min_sentence_variety is None:
            raise ValueError("Invalid value for `min_sentence_variety`, must not be `None`")

        self._min_sentence_variety = min_sentence_variety

    @property
    def highest_pronoun_percentage(self):
        """
        Gets the highest_pronoun_percentage of this AnalysisSettings.

        :return: The highest_pronoun_percentage of this AnalysisSettings.
        :rtype: float
        """
        return self._highest_pronoun_percentage

    @highest_pronoun_percentage.setter
    def highest_pronoun_percentage(self, highest_pronoun_percentage):
        """
        Sets the highest_pronoun_percentage of this AnalysisSettings.

        :param highest_pronoun_percentage: The highest_pronoun_percentage of this AnalysisSettings.
        :type: float
        """
        if highest_pronoun_percentage is None:
            raise ValueError("Invalid value for `highest_pronoun_percentage`, must not be `None`")

        self._highest_pronoun_percentage = highest_pronoun_percentage

    @property
    def lowest_pronoun_percentage(self):
        """
        Gets the lowest_pronoun_percentage of this AnalysisSettings.

        :return: The lowest_pronoun_percentage of this AnalysisSettings.
        :rtype: float
        """
        return self._lowest_pronoun_percentage

    @lowest_pronoun_percentage.setter
    def lowest_pronoun_percentage(self, lowest_pronoun_percentage):
        """
        Sets the lowest_pronoun_percentage of this AnalysisSettings.

        :param lowest_pronoun_percentage: The lowest_pronoun_percentage of this AnalysisSettings.
        :type: float
        """
        if lowest_pronoun_percentage is None:
            raise ValueError("Invalid value for `lowest_pronoun_percentage`, must not be `None`")

        self._lowest_pronoun_percentage = lowest_pronoun_percentage

    @property
    def highest_academic_pronoun_percentage(self):
        """
        Gets the highest_academic_pronoun_percentage of this AnalysisSettings.

        :return: The highest_academic_pronoun_percentage of this AnalysisSettings.
        :rtype: float
        """
        return self._highest_academic_pronoun_percentage

    @highest_academic_pronoun_percentage.setter
    def highest_academic_pronoun_percentage(self, highest_academic_pronoun_percentage):
        """
        Sets the highest_academic_pronoun_percentage of this AnalysisSettings.

        :param highest_academic_pronoun_percentage: The highest_academic_pronoun_percentage of this AnalysisSettings.
        :type: float
        """
        if highest_academic_pronoun_percentage is None:
            raise ValueError("Invalid value for `highest_academic_pronoun_percentage`, must not be `None`")

        self._highest_academic_pronoun_percentage = highest_academic_pronoun_percentage

    @property
    def highest_initial_pronoun_percentage(self):
        """
        Gets the highest_initial_pronoun_percentage of this AnalysisSettings.

        :return: The highest_initial_pronoun_percentage of this AnalysisSettings.
        :rtype: float
        """
        return self._highest_initial_pronoun_percentage

    @highest_initial_pronoun_percentage.setter
    def highest_initial_pronoun_percentage(self, highest_initial_pronoun_percentage):
        """
        Sets the highest_initial_pronoun_percentage of this AnalysisSettings.

        :param highest_initial_pronoun_percentage: The highest_initial_pronoun_percentage of this AnalysisSettings.
        :type: float
        """
        if highest_initial_pronoun_percentage is None:
            raise ValueError("Invalid value for `highest_initial_pronoun_percentage`, must not be `None`")

        self._highest_initial_pronoun_percentage = highest_initial_pronoun_percentage

    @property
    def lowest_initial_pronoun_percentage(self):
        """
        Gets the lowest_initial_pronoun_percentage of this AnalysisSettings.

        :return: The lowest_initial_pronoun_percentage of this AnalysisSettings.
        :rtype: float
        """
        return self._lowest_initial_pronoun_percentage

    @lowest_initial_pronoun_percentage.setter
    def lowest_initial_pronoun_percentage(self, lowest_initial_pronoun_percentage):
        """
        Sets the lowest_initial_pronoun_percentage of this AnalysisSettings.

        :param lowest_initial_pronoun_percentage: The lowest_initial_pronoun_percentage of this AnalysisSettings.
        :type: float
        """
        if lowest_initial_pronoun_percentage is None:
            raise ValueError("Invalid value for `lowest_initial_pronoun_percentage`, must not be `None`")

        self._lowest_initial_pronoun_percentage = lowest_initial_pronoun_percentage

    @property
    def lowest_we_we_score(self):
        """
        Gets the lowest_we_we_score of this AnalysisSettings.

        :return: The lowest_we_we_score of this AnalysisSettings.
        :rtype: float
        """
        return self._lowest_we_we_score

    @lowest_we_we_score.setter
    def lowest_we_we_score(self, lowest_we_we_score):
        """
        Sets the lowest_we_we_score of this AnalysisSettings.

        :param lowest_we_we_score: The lowest_we_we_score of this AnalysisSettings.
        :type: float
        """
        if lowest_we_we_score is None:
            raise ValueError("Invalid value for `lowest_we_we_score`, must not be `None`")

        self._lowest_we_we_score = lowest_we_we_score

    @property
    def longest_average_paragraph_length(self):
        """
        Gets the longest_average_paragraph_length of this AnalysisSettings.

        :return: The longest_average_paragraph_length of this AnalysisSettings.
        :rtype: float
        """
        return self._longest_average_paragraph_length

    @longest_average_paragraph_length.setter
    def longest_average_paragraph_length(self, longest_average_paragraph_length):
        """
        Sets the longest_average_paragraph_length of this AnalysisSettings.

        :param longest_average_paragraph_length: The longest_average_paragraph_length of this AnalysisSettings.
        :type: float
        """
        if longest_average_paragraph_length is None:
            raise ValueError("Invalid value for `longest_average_paragraph_length`, must not be `None`")

        self._longest_average_paragraph_length = longest_average_paragraph_length

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, AnalysisSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
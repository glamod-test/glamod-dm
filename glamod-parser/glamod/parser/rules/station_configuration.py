"""
Rules for station_configuration files.
"""

from glamod.parser.convertors import *
from glamod.parser.settings import *


from ._base import OD, _ParserRulesBase


class StationConfigurationParserRules(_ParserRulesBase):

    fields = OD([

      # Standard fields
        ('primary_id', (str,)),
        ('primary_id_scheme', (int,)),
        ('record_number', (int,)),
        ('secondary_id', (list_of_strs,)),
        ('secondary_id_scheme', (list_of_ints,)),
        ('station_name', (str,)),
        ('station_abbreviation', (str,)),
        ('alternative_name', (list_of_strs,)),
        ('station_crs', (str,)),
        ('longitude', (float,)),
        ('latitude', (float,)),
        ('local_gravity', (float_or_empty,)),
        ('start_date', (timestamp,)),
        ('end_date', (timestamp,)),
        ('station_type', (int,)),
        ('platform_type', (int_or_empty,)),
        ('platform_sub_type', (int_or_empty,)),
        ('operating_institute', (str,)),
        ('operating_territory', (int,)),
        ('city', (str,)),
        ('contact', (list_of_strs,)),
        ('role', (list_of_ints,)),
        ('observing_frequency', (int,)),
        ('reporting_time', (list_of_ints,)),
        ('telecommunication_method', (list_of_ints,)),
        ('station_automation', (int,)),
        ('measuring_system_model', (list_of_strs,)),
        ('measuring_system_id', (str,)),
        ('observed_variables', (list_of_ints,)),
        ('comment', (str,)),
        ('optional_data', (int_or_empty,))
    ])


    # Extended fields (not defined in table schema)
    #  - to be saved to the 'deliveries' DB for later lookups
    extended_fields = OD([
        ('region', (int,)),
        ('data_policy_licence', (int,)),
        ('primary_station_id_scheme', (int,)),
        ('location_accuracy', (float,)),
        ('location_method', (str,)),
        ('location_quality', (int,)),
        ('height_of_station_above_local_ground', (float_or_empty,)),
        ('height_of_station_above_sea_level', (float_or_empty,)),
        ('height_of_station_above_sea_level_accuracy', (float_or_empty,)),
        ('sea_level_datum', (float_or_empty,)),
        ('source_id', (str,))
    ])

    index_field = 'primary_id'

    code_table_fields = OD([
        ('primary_id_scheme', IdScheme),
        ('secondary_id_scheme', IdScheme),
        ('station_crs', Crs),
        ('station_type', StationType),
        ('platform_type', PlatformType),
        ('platform_sub_type', PlatformSubType),
        ('operating_institute', Organisation),
        ('operating_territory', SubRegion),
        ('contact', Contact),
        ('role', Role),
        ('observing_frequency', ObservingFrequency),
        ('telecommunication_method', CommunicationMethod),
        ('observed_variables', ObservedVariable),
        ('optional_data', DataPresent),
        ('region', Region)
    ])

    foreign_fields_to_add = OD([
    ])

